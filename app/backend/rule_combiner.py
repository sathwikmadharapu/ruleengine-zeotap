from app.backend.ast_builder import Node, create_rule
from app.backend.ast_builder import create_rule


def combine_rules(rules):
    ast = None
    for rule in rules:
        sub_tree = create_rule(rule)
        if sub_tree is None:
            return None  # Return None if any rule is invalid
        if ast is None:
            ast = sub_tree  # Set AST if it's the first valid rule
        else:
             ast = combine_ast(ast, sub_tree)
            # Logic to combine ASTs if needed
    return ast  # Return combined AST if all valid
