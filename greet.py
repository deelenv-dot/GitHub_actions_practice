def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
   
    x, y = 2, 3
    print(f"{x} + {y} = {multiply(x, y)}")
    print(greet("GitHub Workflows"))
