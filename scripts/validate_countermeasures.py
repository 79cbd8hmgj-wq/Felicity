#!/usr/bin/env python3
"""Check supplemental research links and prevent evidence/status conflation."""
import csv
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path


def validate(root):
    errors = []
    db = root / 'database'
    try:
        data = json.loads((db / 'factory_countermeasures.json').read_text())
        sources = {r['source_id']: r for r in csv.DictReader((db / 'sources.csv').open())}
        catalog = {r['upgrade_id'] for r in csv.DictReader((db / 'upgrade_candidates.csv').open())}
        outcomes = list(csv.DictReader((db / 'consumer_outcomes.csv').open()))
    except (OSError, ValueError, KeyError) as exc:
        return [str(exc)]
    seen = set()
    outcome_map = {}
    for row in outcomes:
        oid = row['outcome_id']
        if not oid or oid in outcome_map:
            errors.append(f'duplicate/empty outcome: {oid}')
        outcome_map[oid] = row
        if row['source_id'] not in sources or row['upgrade_id'] not in catalog:
            errors.append(f'{oid}: missing source/candidate')
        if row['qualifies_level_b'] not in {'yes', 'no'}:
            errors.append(f'{oid}: invalid Level B qualification')
        if row['reference'] != sources.get(row['source_id'], {}).get('reference'):
            errors.append(f'{oid}: outcome URL differs from source registry')
        if not all(row.values()):
            errors.append(f'{oid}: empty outcome field')

    def links(label, ids):
        if not ids or len(ids) != len(set(ids)):
            errors.append(f'{label}: absent/duplicate source IDs')
        for sid in ids:
            if sid not in sources:
                errors.append(f'{label}: missing source {sid}')

    for row in data.get('records', []):
        rid = row['research_id']
        if not re.fullmatch(r'FCM-\d{3}', rid) or rid in seen:
            errors.append(f'duplicate/invalid research ID: {rid}')
        seen.add(rid)
        if row['upgrade_id'] not in catalog:
            errors.append(f'{rid}: missing candidate')
        try:
            date.fromisoformat(row['reviewed_on'])
        except ValueError:
            errors.append(f'{rid}: invalid review date')
        level = row['evidence_level']
        if level not in {'A', 'B', 'C', 'D', 'E'}:
            errors.append(f'{rid}: invalid evidence level')
        if row['intervention_category'] not in {
            'maintenance', 'restoration', 'restoration_serviceability',
            'factory_equivalent_replacement', 'engineering_improvement', 'diagnostic_reference'
        }:
            errors.append(f'{rid}: invalid intervention category')
        evidence, verification, practical = row['evidence'], row['verification'], row['practical_assessment']
        links(rid, evidence['source_ids'])
        for oid in evidence['independent_outcome_ids']:
            if oid not in outcome_map or outcome_map[oid]['upgrade_id'] != row['upgrade_id']:
                errors.append(f'{rid}: outcome missing or belongs to another candidate: {oid}')
        for field in ['model_year_application', 'june_2003_application', 'actual_installed_vehicle', 'installed_and_tested']:
            if field not in verification:
                errors.append(f'{rid}: missing separate verification status {field}')
        if verification.get('installed_and_tested') and not verification.get('installation_evidence'):
            errors.append(f'{rid}: claimed installation lacks evidence')
        if verification.get('actual_installed_vehicle') != 'not_verified' and not verification.get('vehicle_evidence'):
            errors.append(f'{rid}: actual-vehicle verification lacks evidence')
        if level in {'A', 'B'} and not any(sources.get(s, {}).get('kind') == 'factory_bulletin' for s in evidence['source_ids']):
            errors.append(f'{rid}: factory grade lacks Toyota document')
        if level == 'B' and not any(outcome_map.get(o, {}).get('qualifies_level_b') == 'yes' for o in evidence['independent_outcome_ids']):
            errors.append(f'{rid}: Level B requires matching successful outcome')
        if level == 'C' and not any(sources.get(s, {}).get('kind') in {'manufacturer_catalog', 'manufacturer_documentation'} for s in evidence['source_ids']):
            errors.append(f'{rid}: Level C lacks manufacturer engineering/application source')
        cost = practical['estimated_us_parts_cost']
        if cost is not None:
            if not isinstance(cost.get('amount_usd'), (int, float)) or cost['amount_usd'] <= 0 or not cost.get('basis') or not cost.get('as_of'):
                errors.append(f'{rid}: invalid priced estimate; unknown must be null')
        for price in practical['price_observations']:
            if price['source_id'] not in sources:
                errors.append(f'{rid}: unknown price source')
        if practical['purchase_ready'] and level in {'D', 'E'}:
            errors.append(f'{rid}: unresolved lead marked purchase ready')
        if not verification.get('next_action') or not verification.get('missing_research'):
            errors.append(f'{rid}: missing research gate')
    for section, key in [('exclusions', 'exclusion_id'), ('service_practices', 'practice_id')]:
        ids = set()
        for row in data.get(section, []):
            if not row[key] or row[key] in ids:
                errors.append(f'{section}: duplicate/empty ID')
            ids.add(row[key])
            links(row[key], row['source_ids'])
    return errors


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    records = json.loads((root / 'database/factory_countermeasures.json').read_text())['records']
    print(f'Countermeasure integrity passed: {len(records)} studies; grades {dict(Counter(r["evidence_level"] for r in records))}.')
