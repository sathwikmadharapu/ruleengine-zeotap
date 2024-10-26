# Rule Engine Project

## Project Overview
A rule engine to dynamically create, modify, and evaluate conditional rules on user attributes using an Abstract Syntax Tree (AST).

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone <repo_url>
    cd RuleEngineProject
    ```

2. **Setup virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize database**:
    ```bash
    python -c "from app.data.database import initialize_db; initialize_db()"
    ```

5. **Run the API**:
    ```bash
    python app/api/rule_api.py
    ```

## API Endpoints
- **POST /create_rule**: Creates an AST from a rule string.
- **POST /combine_rules**: Combines multiple rules.
- **POST /evaluate_rule**: Evaluates an AST against data.
- **POST /modify_rule**: Modifies existing AST.

## Testing
Run unit tests:
```bash
python -m unittest discover -s tests
