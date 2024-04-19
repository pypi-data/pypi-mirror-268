import os
from dataclasses import dataclass, field
from SCons.Environment import Environment


@dataclass
class Build:
    name: str

    files: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    output: str = "dist"

    def __repr__(self) -> str:
        return self.name

    @property
    def target(self) -> str:
        return os.path.join(self.output, self.name)

    def register(self, env: Environment) -> None:
        env.Program(self.target, source=self.files, CXXFLAGS=self.flags)
        env.Alias(self.name, self.target)
