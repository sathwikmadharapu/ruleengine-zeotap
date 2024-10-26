import unittest
from app.backend import rule_evaluator
from app.backend.ast_builder import Node

class TestRuleEvaluator(unittest.TestCase):
    def test_evaluate_valid_and_condition(self):
        ast = Node("AND", left=Node("operand", value={"field": "age", "threshold": 30}), right=Node("operand", value={"field": "salary", "threshold": 50000}))
        data = {"age": 35, "salary": 60000}
        result = rule_evaluator.evaluate_rule(ast, data)
        self.assertTrue(result)  # Should evaluate to True

    def test_evaluate_missing_field(self):
        ast = Node("operand", value={"field": "age", "threshold": 30})
        data = {}  # Missing data
        result = rule_evaluator.evaluate_rule(ast, data)
        self.assertFalse(result)  # Should evaluate to False

    def test_evaluate_invalid_ast_type(self):
        ast = Node("INVALID_TYPE")
        data = {}
        result = rule_evaluator.evaluate_rule(ast, data)
        self.assertFalse(result)  # Should evaluate to False
