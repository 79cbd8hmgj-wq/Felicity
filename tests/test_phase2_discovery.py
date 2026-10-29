"""Regression checks for evidence becoming stronger than its observed scope."""
import csv
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_phase2_discovery import ROOT, validate


class Phase2EvidenceScopeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'database', self.root / 'database')

    def tearDown(self):
        self.tmp.cleanup()

    def edit(self, filename, change):
        path = self.root / 'database' / (filename + '_2026-10-29.csv')
        with path.open(newline='') as stream:
            reader = csv.DictReader(stream)
            headers, rows = reader.fieldnames, list(reader)
        change(rows)
        with path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def test_current_evidence_integrity(self):
        self.assertEqual(validate(self.root), [])

    def test_selected_price_cannot_become_other_branch_quote(self):
        self.edit('phase2_local_stock', lambda rows: rows[1].update(price_scope='verified_local_checkout'))
        self.assertTrue(any('promoted' in e for e in validate(self.root)))

    def test_indexed_result_cannot_become_shelf_stock(self):
        self.edit('phase2_local_stock', lambda rows: rows[0].update(method='search_index_excerpt', result='in_stock'))
        self.assertTrue(any('lacks individual live branch evidence' in e for e in validate(self.root)))

    def test_source_relationship_cannot_dangle(self):
        self.edit('phase2_evidence_links', lambda rows: rows[0].update(source_id='src-missing'))
        self.assertTrue(any('missing source' in e for e in validate(self.root)))

    def test_missing_detail_row_is_detected(self):
        self.edit('phase2_product_details', lambda rows: rows.pop())
        self.assertTrue(any('coverage mismatch' in e for e in validate(self.root)))


if __name__ == '__main__':
    unittest.main()
