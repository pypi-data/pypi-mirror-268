import os
import psutil
from functools import reduce
from SCons.Environment import Environment
from SCons.Script import SConscript


def conan(libs: list[str], path: str = "SConscript_conandeps") -> Environment:
    exports = SConscript(path)
    conandeps = exports["conandeps"]

    environment = reduce(
        lambda acc, x: {k: v + x[k] for k, v in acc.items()},
        [v for k, v in exports.items() if k in libs],
        conandeps,
    )

    return Environment(
        **environment,
        ENV={"PATH": os.getenv("PATH", "")},
        num_jobs=psutil.cpu_count(),
    )
