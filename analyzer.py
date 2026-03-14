import re

def analyze_code(code: str):
    issues = []

    # Rule 1: Detect debug print statements
    if "print(" in code:
        issues.append("Debug print statement detected")

    # Rule 2: Detect TODO comments
    if "TODO" in code:
        issues.append("TODO comment found in code")

    # Rule 3: Detect long lines (> 80 characters)
    lines = code.split("\n")
    for i, line in enumerate(lines, start=1):
        if len(line) > 80:
            issues.append(f"Line {i} exceeds recommended length (80 characters)")

    # Rule 4: Detect unused imports (basic check)
    imports = re.findall(r'import (\w+)', code)
    for imp in imports:
        if imp not in code.replace(f"import {imp}", ""):
            issues.append(f"Potential unused import: {imp}")

    return issues
