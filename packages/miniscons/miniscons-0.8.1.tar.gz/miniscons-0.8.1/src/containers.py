def flatten(ignore: list[str | list[str]]) -> list[str]:
    return list(sum(map(lambda x: x if isinstance(x, list) else [x], ignore), []))
