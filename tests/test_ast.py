import unittest
from app.backend import ast_builder

class TestASTBuilder(unittest.TestCase):
    def test_create_rule_with_invalid_attribute(self):
        rule_string = "invalid_attr > 30"
        ast = ast_builder.create_rule(rule_string)
        self.assertIsNone(ast)
