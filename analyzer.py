def analyze_code(code):
    issues = []

    if "print(" in code:
        issues.append("Debug print statement detected")

    if len(code) > 1000:
        issues.append("File length too large")

    return issues
