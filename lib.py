def average(values: list) -> float:
    if not values:
        raise ValueError("La liste ne doit pas être vide.")
    return sum(values) / len(values)