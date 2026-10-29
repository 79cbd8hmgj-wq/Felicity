#!/usr/bin/env python3
"""Check supplier coverage, discovery references and branch-stock evidence."""
import csv
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SUFFIX = "2026-10-29"


def rows(name, key):
    with (ROOT / "database" / f"{name}.csv").open(newline="") as stream:
        reader = csv.DictReader(stream)
        result = list(reader)
    if not result or any(None in row or any(v is None for v in row.values()) for row in result):
        raise ValueError(f"{name}: empty or malformed rows")
    identifiers = [row[key] for row in result]
    if any(not value for value in identifiers) or len(set(identifiers)) != len(identifiers):
        raise ValueError(f"{name}: duplicate/blank {key}")
    return result


def validate():
    errors = []
    suppliers = rows("local_parts_supplier_candidates", "supplier_id")
    audit = rows(f"local_supplier_coverage_audit_{SUFFIX}", "supplier_id")
    products = rows(f"external_product_discoveries_{SUFFIX}", "discovery_id")
    offers = rows(f"external_product_offers_{SUFFIX}", "offer_id")
    stock = rows(f"local_stock_observations_{SUFFIX}", "observation_id")
    extras = rows(f"additional_supplier_discoveries_{SUFFIX}", "extra_supplier_id")
    sources = {row["source_id"] for row in rows("sources", "source_id")}
    upgrades = {row["upgrade_id"] for row in rows("upgrade_candidates", "upgrade_id")}
    original = {f"LOC-{number:03}" for number in range(1, 41)}
    supplier_ids = {row["supplier_id"] for row in suppliers}
    audit_ids = {row["supplier_id"] for row in audit}
    product_ids = {row["discovery_id"] for row in products}
    if not original.issubset(supplier_ids) or audit_ids != original:
        errors.append("Audit must contain exactly the original LOC-001 through LOC-040")

    def refs(value, valid, description):
        for identifier in filter(None, value.split("|")):
            if identifier not in valid:
                errors.append(f"{description}: missing {identifier}")

    for row in audit:
        for field in ("location_source_url", "business_status", "customer_access", "completion_level", "remaining_questions", "product_research_scope"):
            if not row[field].strip():
                errors.append(f"{row['supplier_id']}: blank {field}")
        date.fromisoformat(row["verification_date"])
        refs(row["source_ids"], sources, row["supplier_id"])
        if row["product_findings"] != "no_branch_SKUs_authenticated":
            refs(row["product_findings"], product_ids, row["supplier_id"])
        if row["straight_line_miles"]:
            if not row["coordinate_source_url"] or not row["distance_method"]:
                errors.append(f"{row['supplier_id']}: distance without coordinate provenance")
            if float(row["straight_line_miles"]) < 0:
                errors.append(f"{row['supplier_id']}: negative distance")
    for row in products:
        if row["classification"] not in set("ABCDE"):
            errors.append(f"{row['discovery_id']}: invalid classification")
        if row["purchase_ready"] != "no":
            errors.append(f"{row['discovery_id']}: this research checkpoint has no purchase-ready approval")
        refs(row["existing_upgrade_ids"], upgrades, row["discovery_id"])
        refs(row["source_ids"], sources, row["discovery_id"])
        for field in ("manufacturer", "part_number", "discovery_url", "benefit_evidence", "june2003_applicability", "required_interfaces", "remaining_questions", "complete_cost_basis"):
            if not row[field].strip():
                errors.append(f"{row['discovery_id']}: blank {field}")
        for field in ("advertised_price_usd", "local_price_usd", "complete_diy_cost_usd"):
            if row[field] and not re.fullmatch(r"\d+(\.\d{1,2})?", row[field]):
                errors.append(f"{row['discovery_id']}: invalid {field}")
        # National web prices must never silently become branch quotes.
        if row["local_price_usd"] and not row["local_stock_status"].startswith("verified_branch_checkout"):
            errors.append(f"{row['discovery_id']}: local price lacks branch checkout evidence")
    for row in offers:
        refs(row["discovery_id"], product_ids, row["offer_id"])
        if row["supplier_id"]:
            refs(row["supplier_id"], supplier_ids, row["offer_id"])
        if not re.fullmatch(r"\d+(\.\d{1,2})?", row["price_usd"]):
            errors.append(f"{row['offer_id']}: invalid price")
        if not row["quote_scope"] or not row["source_url"]:
            errors.append(f"{row['offer_id']}: missing price provenance")
    for row in stock:
        refs(row["supplier_id"], audit_ids, row["observation_id"])
        refs(row["discovery_id"], product_ids, row["observation_id"])
        if not row["method"] or not row["limitations"]:
            errors.append(f"{row['observation_id']}: missing observation scope")
    for row in extras:
        refs(row["discovery_ids"], product_ids, row["extra_supplier_id"])
    return errors


if __name__ == "__main__":
    try:
        problems = validate()
    except (ValueError, KeyError, OSError) as exc:
        problems = [str(exc)]
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("Supplier discovery integrity passed: 40 original locations, linked products/offers/stock evidence.")
