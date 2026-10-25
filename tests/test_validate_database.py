"""Regression coverage for repository schema validation."""
import csv
import tempfile
import unittest
from pathlib import Path
from scripts.validate_database import validate, FILES

HEADERS = {
    "vehicle": "vehicle_id,source_id",
    "components": "component_id,verification_status,parent_id",
    "sources": "source_id",
    "specifications": "spec_id,source_id,status",
    "service_tasks": "task_id,status,component_id",
    "observations": "observation_id,vehicle_id,source_id",
    "parts": "part_record_id,component_id,source_id,verification_status",
    "repairs": "repair_id,vehicle_id,component_id",
    "claims": "claim_id,vehicle_id,source_id",
}

class DatabaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        db = self.root / "database"
        db.mkdir()
        for name in FILES:
            (db / f"{name}.csv").write_text(HEADERS[name] + "\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def append(self, table, line):
        with (self.root / "database" / f"{table}.csv").open("a") as f:
            f.write(line + "\n")

    def test_empty_ledgers_are_valid(self):
        self.assertEqual([], validate(self.root))

    def test_duplicate_primary_key_is_rejected(self):
        self.append("sources", "src-1")
        self.append("sources", "src-1")
        self.assertTrue(any("duplicate" in e for e in validate(self.root)))

    def test_missing_foreign_key_is_rejected(self):
        self.append("specifications", "s1,no-such-source,factory_reference")
        self.assertTrue(any("missing sources reference" in e for e in validate(self.root)))

    def test_invalid_status_is_rejected(self):
        self.append("components", "engine,totally_done,")
        self.assertTrue(any("invalid verification_status" in e for e in validate(self.root)))

    def test_unknown_parent_is_rejected(self):
        self.append("components", "engine,reference,no_such_parent")
        self.assertTrue(any("missing components reference" in e for e in validate(self.root)))

    def test_unknown_task_component_is_rejected(self):
        self.append("service_tasks", "t1,pending,no_such_component")
        self.assertTrue(any("missing components reference" in e for e in validate(self.root)))

    def test_claim_requires_valid_source(self):
        self.append("claims", "c1,missing-vehicle,missing-source")
        self.assertTrue(any("missing vehicle reference" in e for e in validate(self.root)))

    def test_component_parent_cycle_is_rejected(self):
        self.append("components", "a,reference,b")
        self.append("components", "b,reference,a")
        self.assertTrue(any("cyclic parent chain" in e for e in validate(self.root)))

    def test_malformed_row_is_rejected(self):
        self.append("sources", "s1,unexpected_extra_column")
        self.assertTrue(any("malformed" in e for e in validate(self.root)))

    def test_private_identifier_column_is_rejected(self):
        (self.root / "database/vehicle.csv").write_text("vehicle_id,source_id,full_vin\n")
        self.assertTrue(any("private identifier" in e for e in validate(self.root)))

if __name__ == "__main__":
    unittest.main()
