from .containers import flatten


def flags(
    standard: str,
    warnings: list[str] | None = None,
    ignore: list[str] | None = None,
    shared: bool = False,
) -> list[str]:
    if warnings is None:
        warnings = []

    if ignore is None:
        ignore = []

    return flatten(
        [
            f"-std={standard}",
            ["-shared"] if shared else [],
            [f"-W{warning}" for warning in warnings],
            [f"-Wno-{warning}" for warning in ignore],
        ]
    )
