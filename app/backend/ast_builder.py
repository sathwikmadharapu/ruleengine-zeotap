class Node:
    def __init__(self, type_, left=None, right=None, value=None):
        self.type = type_
        self.left = left
        self.right = right
        self.value = value

    def serialize(self):
        # Convert the node and its children to a dictionary
        return {
            "type": self.type,
            "left": self.left.serialize() if self.left else None,
            "right": self.right.serialize() if self.right else None,
            "value": self.value
        }

ALLOWED_ATTRIBUTES = ["age", "department", "salary", "experience"]
COMPARISON_OPERATORS = [">", "<", ">=", "<=", "==", "!="]

def validate_rule(rule_string):
    tokens = rule_string.split()
    if len(tokens) != 3:
        raise ValueError("Rule must be in the format 'attribute operator value'.")

    attribute, operator, value = tokens
    if attribute not in ALLOWED_ATTRIBUTES:
        raise ValueError(f"Invalid attribute: {attribute}.")
    if operator not in COMPARISON_OPERATORS:
        raise ValueError(f"Invalid operator: {operator}.")
    try:
        float(value)  # Validate that value is a number
    except ValueError:
        raise ValueError(f"Invalid value: {value}. Must be a number.")

def create_rule(rule_string):
    try:
        validate_rule(rule_string)
        return Node("operand", value={"field": rule_string.split()[0], "threshold": float(rule_string.split()[2])})
    except ValueError as e:
        print(f"Error in create_rule: {e}")
        return None



def modify_rule(ast, modification):
    if ast is None:
        print("Error: AST is None. Cannot modify rule.")
        return None

    try:
        if modification["action"] == "change_operator":
            ast.type = modification["new_operator"]
        elif modification["action"] == "change_operand":
            ast.value = modification["new_value"]
        elif modification["action"] == "add_expression":
            new_node = Node(modification["type"], value=modification["value"])
            if not ast.left:
                ast.left = new_node
            else:
                ast.right = new_node
        return ast
    except Exception as e:
        print(f"Error modifying rule: {e}")
        return None
    
def evaluate_rule(ast, data):
    if ast is None:
        print("Error: AST is None. Cannot evaluate rule.")
        return False

    try:
        if ast.type == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.type == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
        elif ast.type == "operand":
            field_value = data.get(ast.value["field"])
            if field_value is None:
                print(f"Error: Field '{ast.value['field']}' not found in data.")
                return False
            
            # Evaluate based on operator
            operator = ast.value.get("operator")
            threshold = ast.value["threshold"]
            if operator == ">":
                return field_value > threshold
            elif operator == "<":
                return field_value < threshold
            elif operator == ">=":
                return field_value >= threshold
            elif operator == "<=":
                return field_value <= threshold
            elif operator == "==":
                return field_value == threshold
            elif operator == "!=":
                return field_value != threshold
            else:
                print(f"Error: Unknown operator '{operator}'.")
                return False
        else:
            print(f"Error: Unknown AST type '{ast.type}'. Expected 'AND', 'OR', or 'operand'.")
            return False
    except KeyError as e:
        print(f"Missing key in data: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error during evaluation: {e}")
        return False
