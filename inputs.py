def input_int(prompt: str) -> int | None:
    while True:
        raw = input(prompt).strip()

        if raw == "":
               return None

        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")

def input_float(prompt: str) -> float | None:
    while True:
        raw = input(prompt).strip()

        if raw == "":
               return None

        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")

def input_str(prompt: str) -> str | None:
    while True:
        value = input(prompt).strip()

        if value == "":
            return None

        return value