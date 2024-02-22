from dataclasses import dataclass, field


@dataclass(frozen=True)
class Book:
    title: str = field(hash=True)
    author: str = field(hash=True)
    quantity: int = field(hash=True)
    id: str = field(hash=True)
