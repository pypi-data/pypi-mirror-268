from dataclasses import dataclass, field
from SCons.Environment import Environment
from typing import Optional


@dataclass
class Script:
    name: str

    args: list[str] = field(default_factory=list)
    prefix: Optional[str] = None

    def __repr__(self) -> str:
        return self.name

    @property
    def action(self) -> str:
        segments = [self.name, *self.args]

        if self.prefix:
            segments.insert(0, self.prefix)

        return " ".join(segments)

    def register(self, env: Environment) -> None:
        alias = env.Alias(self.name, [], self.action)
        env.AlwaysBuild(alias)
