#!/usr/bin/env python3
"""Validate the current Felicity CSV repository without editing vehicle data."""
import csv
from datetime import date
import re
import sys
from pathlib import Path

FILES = {
    "vehicle": ("vehicle_id", ["source_id"]),
    "components": ("component_id", ["parent_id"]),
    "sources": ("source_id", []),
    "specifications": ("spec_id", ["source_id", "component_id"]),
    "service_tasks": ("task_id", ["component_id"]),
    "observations": ("observation_id", ["vehicle_id", "source_id"]),
    "parts": ("part_record_id", ["component_id", "source_id"]),
    "repairs": ("repair_id", ["vehicle_id", "component_id"]),
    "claims": ("claim_id", ["vehicle_id", "source_id"]),
    "upgrade_candidates": ("upgrade_id", []),
    "upgrade_research": ("research_id", ["upgrade_id"]),
    "upgrade_value_matrix": ("upgrade_id", ["source_research_id"]),
}
TARGETS = {"vehicle_id": "vehicle", "component_id": "components", "source_id": "sources", "parent_id": "components", "upgrade_id": "upgrade_candidates", "source_research_id": "upgrade_research"}
STATUS = {
    "components": ("verification_status", {"reference", "research_pending", "label_verified", "equipment_unknown", "partially_observed", "not_inspected"}),
    "specifications": ("status", {"factory_reference", "observed", "owner_confirmed", "pending"}),
    "service_tasks": ("status", {"pending", "history_unknown", "not_inspected", "done"}),
    "parts": ("verification_status", {"candidate", "probable", "verified"}),
    "upgrade_candidates": ("fitment_status", {"candidate_unverified", "candidate", "probable", "confirmed", "vehicle-validated"}),
    "upgrade_research": ("fitment_status", {"candidate", "probable", "confirmed", "vehicle-validated"}),
}
PRIVACY_HEADERS = {"vin", "full_vin", "license_plate", "license_number", "insurance_number"}

def validate(root: Path, require_upgrade_coverage=False):
    """Return a list of actionable errors. Empty data tables are valid."""
    errors, tables = [], {}
    for name, (key, _references) in FILES.items():
        path = root / "database" / (name + ".csv")
        if not path.is_file():
            errors.append(f"{path}: missing")
            continue
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            headers = reader.fieldnames or []
            if not headers or key not in headers or len(set(headers)) != len(headers):
                errors.append(f"{path}: missing {key}, duplicate or empty headers")
                continue
            unsafe = PRIVACY_HEADERS.intersection(h.lower() for h in headers)
            if unsafe:
                errors.append(f"{path}: private identifier column(s): {sorted(unsafe)}")
            rows, ids = [], set()
            for number, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    errors.append(f"{path}:{number}: malformed number of columns")
                    continue
                identifier = row[key].strip()
                if not identifier or identifier in ids:
                    errors.append(f"{path}:{number}: blank or duplicate {key}: {identifier!r}")
                ids.add(identifier)
                rows.append((number, row))
            tables[name] = (headers, rows, ids)
    for name, (_key, references) in FILES.items():
        if name not in tables:
            continue
        headers, rows, _ = tables[name]
        for field in references:
            if field not in headers:
                errors.append(f"{name}: missing foreign key column {field}")
                continue
            target = TARGETS[field]
            if target not in tables:
                continue
            target_ids = tables[target][2]
            for number, row in rows:
                value = row[field].strip()
                if not value and (name, field) in {
                    ("upgrade_research", "upgrade_id"),
                    ("specifications", "source_id"),
                    ("specifications", "component_id"),
                    ("service_tasks", "component_id"),
                    ("claims", "vehicle_id"),
                    ("claims", "source_id"),
                    ("observations", "vehicle_id"),
                    ("observations", "source_id"),
                    ("parts", "component_id"),
                    ("parts", "source_id"),
                    ("repairs", "vehicle_id"),
                    ("repairs", "component_id"),
                }:
                    errors.append(f"{name}:{number}: blank required reference {field}")
                if value and value not in target_ids:
                    errors.append(f"{name}:{number}: missing {target} reference {field}={value!r}")
        if name in STATUS:
            column, valid = STATUS[name]
            if column not in headers:
                errors.append(f"{name}: missing status column {column}")
            else:
                for number, row in rows:
                    if row[column] not in valid:
                        errors.append(f"{name}:{number}: invalid {column}={row[column]!r}")
    if "components" in tables:
        headers, rows, _ = tables["components"]
        if "parent_id" in headers:
            parents = {row["component_id"]: row["parent_id"] for _, row in rows}
            for start in parents:
                seen = set()
                current = start
                while current:
                    if current in seen:
                        errors.append(f"components: cyclic parent chain for {start}")
                        break
                    seen.add(current)
                    current = parents.get(current, "")
    if "specifications" in tables:
        headers, rows, _ = tables["specifications"]
        if "build_applicability" not in headers:
            errors.append("specifications: missing build_applicability column")
        else:
            allowed = {"manual_scope_oct_2003_onward", "individual_vehicle_observed"}
            for number, row in rows:
                if row["build_applicability"] not in allowed:
                    errors.append(f"specifications:{number}: invalid build_applicability")
    if "upgrade_research" in tables:
        headers, rows, _ = tables["upgrade_research"]
        required = {"source_ids", "reviewed_on", "verified_facts", "production_applicability",
                    "fitment_rationale", "benefit_basis", "measured_vehicle_benefit",
                    "engineering_hypothesis", "disadvantages", "diy_level", "diy_requirements",
                    "cost_usd", "cost_basis", "next_validation", "review_state"}
        missing = required - set(headers)
        if missing:
            errors.append(f"upgrade_research: missing required columns {sorted(missing)}")
        else:
            source_ids = tables.get("sources", ([], [], set()))[2]
            for number, row in rows:
                for field in required - {"cost_usd"}:
                    if not row[field].strip():
                        errors.append(f"upgrade_research:{number}: blank required {field}")
                for source in row["source_ids"].split("|"):
                    if source not in source_ids:
                        errors.append(f"upgrade_research:{number}: missing sources reference {source!r}")
                try:
                    date.fromisoformat(row["reviewed_on"])
                except ValueError:
                    errors.append(f"upgrade_research:{number}: invalid reviewed_on")
                if row["diy_level"] not in {"basic", "intermediate", "advanced", "professional"}:
                    errors.append(f"upgrade_research:{number}: invalid diy_level")
                if row["benefit_basis"] not in {"hypothesis", "manufacturer_claim", "factory_reference", "oem_corrective_action", "independent_test", "vehicle_measurement"}:
                    errors.append(f"upgrade_research:{number}: invalid benefit_basis")
                if row["review_state"] not in {"open", "documented", "independently_reviewed"}:
                    errors.append(f"upgrade_research:{number}: invalid review_state")
                if row["cost_usd"] and not re.fullmatch(r"\d+(\.\d{1,2})?", row["cost_usd"]):
                    errors.append(f"upgrade_research:{number}: invalid cost_usd")
                if row["fitment_status"] in {"confirmed", "vehicle-validated"}:
                    if not row.get("confirmation_evidence", "").strip():
                        errors.append(f"upgrade_research:{number}: promoted fitment requires confirmation_evidence")
    if "upgrade_candidates" in tables and "upgrade_research" in tables:
        researched = {r["upgrade_id"] for _, r in tables["upgrade_research"][1]}
        candidates = tables["upgrade_candidates"][2]
        for number, row in tables["upgrade_candidates"][1]:
            if row.get("research_status") == "literature_reviewed" and row["upgrade_id"] not in researched:
                errors.append(f"upgrade_candidates:{number}: literature_reviewed without research evidence")
        if require_upgrade_coverage:
            for identifier in sorted(candidates - researched):
                errors.append(f"upgrade_candidates: no research record for {identifier}")
            expected = {f"UPG-{n:03}" for n in range(1, 149)}
            if not expected.issubset(candidates):
                errors.append("upgrade_candidates: original 148 stable IDs must be preserved")
        catalog_rows = {r["upgrade_id"]: r for _, r in tables["upgrade_candidates"][1]}
        for number, row in tables["upgrade_research"][1]:
            catalog = catalog_rows.get(row["upgrade_id"])
            if catalog and catalog.get("research_status") == "literature_reviewed":
                if catalog["fitment_status"] != row["fitment_status"]:
                    errors.append(f"upgrade_research:{number}: fitment differs from catalog")
    if "upgrade_value_matrix" in tables:
        headers, rows, matrix_ids = tables["upgrade_value_matrix"]
        required = {"source_ids", "source_research_id", "source_fitment_status", "purchase_ready", "decision"}
        missing = required - set(headers)
        if missing:
            errors.append(f"upgrade_value_matrix: missing required columns {sorted(missing)}")
        else:
            research_rows = {r["research_id"]: r for _, r in tables.get("upgrade_research", ([], [], set()))[1]}
            source_ids = tables.get("sources", ([], [], set()))[2]
            catalog_ids = tables.get("upgrade_candidates", ([], [], set()))[2]
            for number, row in rows:
                if row["upgrade_id"] not in catalog_ids:
                    errors.append(f"upgrade_value_matrix:{number}: missing candidate {row['upgrade_id']}")
                linked = research_rows.get(row["source_research_id"])
                if linked and linked["upgrade_id"] != row["upgrade_id"]:
                    errors.append(f"upgrade_value_matrix:{number}: research belongs to different candidate")
                if linked and linked["fitment_status"] != row["source_fitment_status"]:
                    errors.append(f"upgrade_value_matrix:{number}: fitment differs from linked research")
                for source in row["source_ids"].split("|"):
                    if source not in source_ids:
                        errors.append(f"upgrade_value_matrix:{number}: missing source {source!r}")
                for source in filter(None, row.get("procedure_source_ids", "").split("|")):
                    if source not in source_ids:
                        errors.append(f"upgrade_value_matrix:{number}: missing procedure source {source!r}")
                if row["purchase_ready"] not in {"yes", "no"}:
                    errors.append(f"upgrade_value_matrix:{number}: invalid purchase_ready")
                if row["decision"] not in {"not_reassessed", "worth_buying", "worth_buying_for_specific_purpose", "promising_but_unverified", "poor_value", "not_an_improvement_over_healthy_oem", "outside_current_diy_scope"}:
                    errors.append(f"upgrade_value_matrix:{number}: invalid decision")
                if row["purchase_ready"] == "yes":
                    for field in {"healthy_oem_baseline", "incremental_function_over_healthy_oem", "observed_product_cost_usd", "price_basis", "procedure_source_ids", "installation_requirements", "benefit_confidence", "buying_scope", "lifting_required", "fabrication_required", "wiring_required", "calibration_required"}:
                        if not row.get(field, "").strip():
                            errors.append(f"upgrade_value_matrix:{number}: purchase-ready missing {field}")
                    if row["decision"] not in {"worth_buying", "worth_buying_for_specific_purpose"}:
                        errors.append(f"upgrade_value_matrix:{number}: purchase-ready decision conflicts")
                for field in {"observed_product_cost_usd", "shipping_usd", "supporting_cost_usd", "annual_fuel_savings_usd", "payback_years"}:
                    value = row.get(field, "")
                    if value and not re.fullmatch(r"\d+(\.\d+)?", value):
                        errors.append(f"upgrade_value_matrix:{number}: invalid numeric {field}")
            if require_upgrade_coverage and catalog_ids != matrix_ids:
                errors.append("upgrade_value_matrix: candidate coverage differs from catalog")
    return errors

def main():
    root = Path(__file__).resolve().parents[1]
    errors = validate(root, require_upgrade_coverage="--require-upgrade-coverage" in sys.argv)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Felicity CSV integrity checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
