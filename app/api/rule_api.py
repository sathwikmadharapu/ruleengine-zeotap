from flask import Flask, request, jsonify
from app.backend import ast_builder, rule_combiner, rule_evaluator

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get("rule")
    if not rule_string:
        return jsonify({"error": "Missing rule string"}), 400

    ast = ast_builder.create_rule(rule_string)
    if ast:
        return jsonify({"ast": ast.serialize()})  # Assuming you implement a serialize method
    else:
        return jsonify({"error": "Invalid rule"}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json.get("rules")
    if not rules:
        return jsonify({"error": "Missing rules list"}), 400

    combined_ast = rule_combiner.combine_rules(rules)
    if combined_ast:
        return jsonify({"combined_ast": combined_ast.serialize()})  # Assuming serialize method
    else:
        return jsonify({"error": "Combination failed"}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast_data = request.json.get("ast")
    data = request.json.get("data")
    ast = ast_builder.deserialize_ast(ast_data)  # Assuming this method exists
    result = rule_evaluator.evaluate_rule(ast, data)
    return jsonify({"result": result})

# Ensure you return error responses for invalid inputs across all routes.


@app.route('/modify_rule', methods=['POST'])
def modify_rule():
    ast_data = request.json.get("ast")
    modification = request.json.get("modification")
    if ast_data is None or modification is None:
        return jsonify({"error": "Missing AST or modification data"}), 400

    ast = ast_builder.deserialize_ast(ast_data)
    modified_ast = ast_builder.modify_rule(ast, modification)
    if modified_ast:
        return jsonify({"modified_ast": modified_ast.serialize()})  # Assuming serialize method
    else:
        return jsonify({"error": "Modification failed"}), 400

if __name__ == "__main__":
    app.run(debug=True)
