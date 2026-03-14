from analyzer import analyze_code

def main():
    sample_code = """
print("Hello World")
"""

    issues = analyze_code(sample_code)

    print("Detected Issues:")
    for issue in issues:
        print("-", issue)

if __name__ == "__main__":
    main()
