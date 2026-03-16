import json

def calculate_revenue(price: float, quantity: int, discount_pct: float = 0) -> float:
    """
    Returns the final revenue after applying discount.
    Formula: price * quantity * (1 - discount_pct / 100)
    Default discount is 0%.
    """
    return price * quantity * (1 - discount_pct / 100)

def classify_customer(age: float | None) -> str:
    """
    Returns customer segment as a string:
    - age < 25     → "Youth"
    - 25 <= age < 45 → "Adult"
    - age >= 45    → "Senior"
    - age is None  → "Unknown"
    """
    if age is None:
        return "Unknown"
    elif age < 25:
        return "Youth"
    elif age < 45:
        return "Adult"
    else:
        return "Senior"

def is_valid_email(email: str) -> bool:
    """
    Returns True if email contains '@' and '.', else False.
    """
    return '@' in email and '.' in email

def load_config(filepath: str) -> dict:
    """
    Reads a JSON file and returns it as a Python dictionary.
    Use a context manager (with block).
    """
    with open(filepath, 'r') as f:
        return json.load(f)

def write_summary_report(stats: dict, output_path: str) -> None:
    """
    Writes a plain-text summary report to the given file path.
    Each key-value pair in stats should be on its own line.
    Format: "Key: Value"
    Use a context manager (with block).
    """
    with open(output_path, 'w') as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    # Test config loading
    config = load_config("config.json")
    print(f"Project: {config['project_name']}, Tax Rate: {config['tax_rate']}%")
    
    # Test revenue calculation
    revenue = calculate_revenue(1200, 3, 10)
    print(f"Revenue (1200, 3, 10%): {revenue}")
    
    # Test customer classification
    segment = classify_customer(None)
    print(f"Customer segment (None): {segment}")
