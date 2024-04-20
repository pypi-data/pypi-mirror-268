import os


def inherit() -> dict[str, str]:
    return {"PATH": os.getenv("PATH", "")}
