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
    "specifications": "spec_id,source_id,status,component_id,build_applicability",
    "service_tasks": "task_id,status,component_id",
    "observations": "observation_id,vehicle_id,source_id",
    "parts": "part_record_id,component_id,source_id,verification_status",
    "repairs": "repair_id,vehicle_id,component_id",
    "claims": "claim_id,vehicle_id,source_id",
    "upgrade_candidates": "upgrade_id,fitment_status,research_status",
    "upgrade_value_matrix": "upgrade_id,source_ids,source_research_id,source_fitment_status,purchase_ready,decision",
    "upgrade_research": "research_id,upgrade_id,fitment_status,source_ids,reviewed_on,verified_facts,production_applicability,fitment_rationale,benefit_basis,measured_vehicle_benefit,engineering_hypothesis,disadvantages,diy_level,diy_requirements,cost_usd,cost_basis,next_validation,review_state",
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
        self.append("specifications", "s1,no-such-source,factory_reference,,manual_scope_oct_2003_onward")
        self.assertTrue(any("missing sources reference" in e for e in validate(self.root)))

    def test_bad_spec_component_is_rejected(self):
        self.append("sources", "src")
        self.append("specifications", "s1,src,factory_reference,not_a_component,manual_scope_oct_2003_onward")
        self.assertTrue(any("missing components reference" in e for e in validate(self.root)))

    def test_unknown_spec_build_scope_is_rejected(self):
        self.append("sources", "src")
        self.append("components", "engine,reference,")
        self.append("specifications", "s1,src,factory_reference,engine,unverified_scope")
        self.assertTrue(any("invalid build_applicability" in e for e in validate(self.root)))

    def test_specification_requires_component(self):
        self.append("sources", "src")
        self.append("specifications", "s1,src,factory_reference,,manual_scope_oct_2003_onward")
        self.assertTrue(any("blank required reference component_id" in e for e in validate(self.root)))

    def test_service_task_requires_component(self):
        self.append("service_tasks", "t1,pending,")
        self.assertTrue(any("blank required reference component_id" in e for e in validate(self.root)))

    def test_claim_requires_source(self):
        self.append("vehicle", "v1,")
        self.append("claims", "c1,v1,")
        self.assertTrue(any("blank required reference source_id" in e for e in validate(self.root)))

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

    def test_reviewed_candidate_needs_evidence(self):
        self.append("upgrade_candidates", "UPG-001,candidate,literature_reviewed")
        self.assertTrue(any("without research evidence" in e for e in validate(self.root)))

    def research(self, **changes):
        row = dict.fromkeys(HEADERS["upgrade_research"].split(","), "documented")
        row.update(research_id="UR-001", upgrade_id="UPG-001", fitment_status="candidate",
                   source_ids="src", reviewed_on="2026-10-25", benefit_basis="hypothesis",
                   diy_level="basic", cost_usd="", review_state="open")
        row.update(changes)
        self.append("sources", "src")
        self.append("upgrade_candidates", "UPG-001,candidate,literature_reviewed")
        with (self.root / "database/upgrade_research.csv").open("a", newline="") as f:
            csv.DictWriter(f, fieldnames=row.keys()).writerow(row)

    def test_research_record_valid(self):
        self.research()
        self.assertEqual([], validate(self.root))

    def test_unknown_research_source_rejected(self):
        self.research(source_ids="src|missing")
        self.assertTrue(any("missing sources reference" in e for e in validate(self.root)))

    def test_unsubstantiated_confirmed_fitment_rejected(self):
        self.research(fitment_status="confirmed")
        self.assertTrue(any("requires confirmation_evidence" in e for e in validate(self.root)))

    def test_research_cost_and_date_rejected(self):
        self.research(cost_usd="cheap", reviewed_on="yesterday")
        errors = validate(self.root)
        self.assertTrue(any("invalid cost_usd" in e for e in errors))
        self.assertTrue(any("invalid reviewed_on" in e for e in errors))

    def test_blank_upgrade_reference_rejected(self):
        self.research(upgrade_id="")
        self.assertTrue(any("blank required reference upgrade_id" in e for e in validate(self.root)))

    def test_full_coverage_requires_every_original_candidate(self):
        self.research()
        self.assertTrue(any("148 stable IDs" in e for e in validate(self.root, True)))

    def test_full_coverage_rejects_missing_review(self):
        self.append("upgrade_candidates", "UPG-002,candidate,research_hypothesis")
        self.assertTrue(any("no research record for UPG-002" in e for e in validate(self.root, True)))

    def test_catalog_fitment_disagreement_rejected(self):
        self.research(fitment_status="probable")
        self.assertTrue(any("fitment differs from catalog" in e for e in validate(self.root)))

    def matrix(self, **changes):
        row = dict(upgrade_id="UPG-001", source_ids="src", source_research_id="UR-001",
                   source_fitment_status="candidate", purchase_ready="no", decision="promising_but_unverified")
        row.update(changes)
        with (self.root / "database/upgrade_value_matrix.csv").open("a", newline="") as f:
            csv.DictWriter(f, fieldnames=row.keys()).writerow(row)

    def test_valid_matrix_references(self):
        self.research()
        self.matrix()
        self.assertEqual([], validate(self.root))

    def test_matrix_cross_candidate_link_rejected(self):
        self.research()
        self.matrix(upgrade_id="UPG-002")
        errors = validate(self.root)
        self.assertTrue(any("different candidate" in e for e in errors))

    def test_matrix_missing_source_rejected(self):
        self.research()
        self.matrix(source_ids="missing")
        self.assertTrue(any("missing source" in e for e in validate(self.root)))

    def test_purchase_ready_requires_review_details(self):
        self.research()
        self.matrix(purchase_ready="yes")
        errors = validate(self.root)
        self.assertTrue(any("purchase-ready missing" in e for e in errors))
        self.assertTrue(any("decision conflicts" in e for e in errors))

    def test_matrix_fitment_drift_rejected(self):
        self.research()
        self.matrix(source_fitment_status="confirmed")
        self.assertTrue(any("fitment differs from linked research" in e for e in validate(self.root)))

if __name__ == "__main__":
    unittest.main()
