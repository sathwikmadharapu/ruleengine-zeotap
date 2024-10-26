import unittest
from app.backend import rule_combiner

class TestRuleCombiner(unittest.TestCase):
    def test_combine_rules_with_invalid_rule(self):
        rules = ["age > 30", "invalid_attr > 40"]
        combined_ast = rule_combiner.combine_rules(rules)
        self.assertIsNone(combined_ast)  # Ensure None is returned for invalid rules

    def test_combine_rules_with_all_valid_rules(self):
        rules = ["age > 30", "salary < 50000"]
        combined_ast = rule_combiner.combine_rules(rules)
        self.assertIsNotNone(combined_ast)  # Ensure we get a non-None AST

    def test_combine_rules_with_some_invalid_rules(self):
        rules = ["age > 30", "invalid_attr > 40"]
        combined_ast = rule_combiner.combine_rules(rules)
        self.assertIsNotNone(combined_ast)  # We should still get an AST for valid rules
    
