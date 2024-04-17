def compiler(standard: str, warnings: list[str], ignore: list[str]) -> list[str]:
    return [
        f"-std={standard}",
        *[f"-W{i}" for i in warnings],
        *[f"-Wno-{i}" for i in ignore],
    ]
