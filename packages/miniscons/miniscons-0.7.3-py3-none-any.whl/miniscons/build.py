import os
from dataclasses import dataclass, field
from SCons.Environment import Environment


@dataclass
class Build:
    name: str

    files: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    output: str = "dist"
    shared: bool = False

    def __repr__(self) -> str:
        return self.name

    @property
    def target(self) -> str:
        return os.path.join(self.output, self.name)

    def nodes(self, env: Environment) -> list[str]:
        return [
            env.Object(
                f"{file.replace('.', '-')}-{self.name}", file, CXXFLAGS=self.flags
            )
            for file in self.files
        ]

    def register(self, env: Environment) -> None:
        if self.shared:
            env.Library(self.target, self.nodes(env))
        else:
            env.Program(self.target, self.nodes(env))
            env.Alias(self.name, self.target)
