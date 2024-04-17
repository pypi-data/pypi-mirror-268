import os
from dataclasses import dataclass
from SCons.Environment import Environment


@dataclass
class Build:
    name: str
    files: list[str]

    shared: bool = False
    output: str = "dist"

    def __repr__(self) -> str:
        return self.name

    @property
    def target(self) -> str:
        return os.path.join(self.output, self.name)

    def register(self, env: Environment) -> None:
        env.Program(self.target, source=self.files)
        env.Alias(self.name, self.target)
