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

    def node(self, file: str, env: Environment) -> str:
        return env.Object(
            f"{file.replace('.', '-')}-{self.name}", file, CXXFLAGS=self.flags
        )

    def register(self, env: Environment) -> None:
        env.Program(self.target, [self.node(file, env) for file in self.files])
        env.Alias(self.name, self.target)
