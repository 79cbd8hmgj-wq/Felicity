#!/usr/bin/env python3
"""Validate Phase 2 evidence joins and quote/stock scope without certifying fit."""
import csv
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SUFFIX = '2026-10-29'


def validate(root=ROOT):
    errors = []

    def table(name, key):
        with (root / 'database' / (name + '.csv')).open(newline='') as stream:
            reader = csv.DictReader(stream)
            data = list(reader)
        if not data or any(None in row or any(v is None for v in row.values()) for row in data):
            raise ValueError(f'{name}: empty or malformed rows')
        identifiers = [row[key] for row in data]
        if len(identifiers) != len(set(identifiers)) or any(not k for k in identifiers):
            raise ValueError(f'{name}: duplicate/blank {key}')
        return {row[key]: row for row in data}

    discoveries = table('external_product_discoveries_' + SUFFIX, 'discovery_id')
    products = {k: v for k, v in discoveries.items() if k.startswith('DSC-P2-')}
    details = table('phase2_product_details_' + SUFFIX, 'discovery_id')
    evidence = table('phase2_evidence_links_' + SUFFIX, 'link_id')
    stock = table('phase2_local_stock_' + SUFFIX, 'observation_id')
    coverage = table('phase2_supplier_category_coverage_' + SUFFIX, 'coverage_id')
    sources = table('sources', 'source_id')
    suppliers = table('local_parts_supplier_candidates', 'supplier_id')
    if set(products) != set(details):
        errors.append('Phase 2 discovery/detail coverage mismatch')
    for key, row in details.items():
        for field in ('evidence_stage', 'price_unit', 'price_evidence', 'complete_job_cost_status', 'comparison_notes', 'supplier_evidence_scope', 'independent_vehicle_result'):
            if not row[field].strip():
                errors.append(f'{key}: blank {field}')
        if row['complete_job_cost_status'] != 'unquoted':
            errors.append(f'{key}: complete job cost needs a separately documented quote')
    linked = set()
    for key, row in evidence.items():
        if row['discovery_id'] not in products:
            errors.append(f'{key}: missing Phase 2 discovery')
        if row['source_id'] not in sources:
            errors.append(f'{key}: missing source')
        if not row['role'] or not row['scope']:
            errors.append(f'{key}: blank evidence scope')
        linked.add(row['discovery_id'])
    if linked != set(products):
        errors.append('Phase 2 evidence coverage mismatch')
    for key, row in coverage.items():
        for identifier in filter(None, row['discovery_ids'].split('|')):
            if identifier not in products:
                errors.append(f'{key}: missing coverage discovery')
        for identifier in filter(None, row['source_ids'].split('|')):
            if identifier not in sources:
                errors.append(f'{key}: missing coverage source')
        if not row['evidence_level'] or not row['remaining_work']:
            errors.append(f'{key}: missing coverage limitation')
        if row['branch_stock_claim'] != 'none_from_this_coverage_row':
            errors.append(f'{key}: category coverage cannot establish branch stock')
    allowed = {'in_stock', 'out_of_stock', 'call_for_pricing_no_stock_result', 'site_bot_restriction_before_store_selection', 'store_selection_not_persisted_no_target_stock'}
    for key, row in stock.items():
        if row['discovery_id'] not in products:
            errors.append(f'{key}: missing discovery')
        if row['supplier_id'] and row['supplier_id'] not in suppliers:
            errors.append(f'{key}: missing supplier')
        if row['result'] not in allowed:
            errors.append(f'{key}: unknown stock result')
        date.fromisoformat(row['observed_on'])
        if not row['limitations'] or not row['source_url'] or not row['branch_address']:
            errors.append(f'{key}: missing scope/provenance')
        if row['result'] in {'in_stock', 'out_of_stock'}:
            if row['method'] not in {'live_browser_Check_Other_Stores_with_individual_branch_rows', 'live_browser_selected_product_fulfillment'}:
                errors.append(f'{key}: shelf result lacks individual live branch evidence')
        if row['selected_store_price_usd']:
            if not re.fullmatch(r'\d+\.\d{2}', row['selected_store_price_usd']):
                errors.append(f'{key}: invalid item price')
            if row['price_scope'] not in {'1390_Central_selected_item_display_only_not_each_branch_checkout', '517_Delaware_selected_item_display_not_checkout'}:
                errors.append(f'{key}: selected item price promoted to other branch quote')
        elif row['price_scope'] != 'no_quote':
            errors.append(f'{key}: empty price has quote scope')
    return errors


if __name__ == '__main__':
    try:
        problems = validate()
    except (OSError, ValueError, KeyError) as exc:
        problems = [str(exc)]
    if problems:
        print('\n'.join(problems), file=sys.stderr)
        raise SystemExit(1)
    print('Phase 2 integrity passed: product/detail/source joins and branch-price scope.')
