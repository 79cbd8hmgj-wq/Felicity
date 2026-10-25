#!/usr/bin/env python3
"""Validate the current Felicity CSV repository without editing vehicle data."""
import csv
import re
import sys
from pathlib import Path

FILES = {
    "vehicle": ("vehicle_id", ["source_id"]),
    "components": ("component_id", ["parent_id"]),
    "sources": ("source_id", []),
    "specifications": ("spec_id", ["source_id"]),
    "service_tasks": ("task_id", ["component_id"]),
    "observations": ("observation_id", ["vehicle_id", "source_id"]),
    "parts": ("part_record_id", ["component_id", "source_id"]),
    "repairs": ("repair_id", ["vehicle_id", "component_id"]),
    "claims": ("claim_id", ["vehicle_id", "source_id"]),
}
TARGETS = {"vehicle_id": "vehicle", "component_id": "components", "source_id": "sources", "parent_id": "components"}
STATUS = {
    "components": ("verification_status", {"reference", "research_pending", "label_verified", "equipment_unknown", "partially_observed", "not_inspected"}),
    "specifications": ("status", {"factory_reference", "observed", "owner_confirmed", "pending"}),
    "service_tasks": ("status", {"pending", "history_unknown", "not_inspected", "done"}),
    "parts": ("verification_status", {"candidate", "probable", "verified"}),
}
PRIVACY_HEADERS = {"vin", "full_vin", "license_plate", "license_number", "insurance_number"}

def validate(root: Path):
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
    # Existing service_tasks system column is legacy free text, not a foreign key.
    # Enforce structured component references once a migration is approved.
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
    return errors

def main():
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Felicity CSV integrity checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
