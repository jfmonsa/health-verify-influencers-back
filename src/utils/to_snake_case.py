import re


def to_snake_case(string: str) -> str:
    """Convert given string to snake case."""
    # Replace spaces with underscores
    string = re.sub(r"\s+", "_", string)
    # Convert CamelCase to snake_case
    string = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", string)
    # Convert any remaining CamelCase to snake_case
    string = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", string)
    # Convert the string to lowercase
    return string.lower()
