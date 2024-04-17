import sys
from .builds.build import Build
from .scripts.flag import Flag
from .scripts.routine import Routine
from .scripts.script import Script
from .builds.target import Target
from dataclasses import dataclass, field
from SCons.Environment import Environment


@dataclass
class Tasks:
    builds: list[Build]

    targets: list[Target] = field(default_factory=list)
    scripts: list[Script] = field(default_factory=list)
    routines: list[Routine] = field(default_factory=list)
    flags: list[Flag] = field(default_factory=list)

    def __str__(self) -> str:
        fields = "\n\n".join(
            [
                ":".join(
                    [k, "".join([f"\n  {i}" for i in v] if len(v) > 0 else "\n  -")]
                )
                for k, v in self.__dict__.items()
            ]
        )

        return f"\n{fields}\n"

    def dump(self) -> None:
        sys.stdout.write(f"{self}\n")

    def register(self, env: Environment) -> None:
        for group in self.__dict__.values():
            for task in group:
                task.register(env)
