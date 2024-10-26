def evaluate_rule(ast, data):
    if ast is None:
        print("Error: AST is None. Cannot evaluate rule.")
        return False  # Return a sensible default if AST is None

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
            return field_value > ast.value["threshold"]
        else:
            print(f"Error: Unknown AST type '{ast.type}'.")
            return False
    except KeyError as e:
        print(f"Missing key in data: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
