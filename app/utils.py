from dataclasses import dataclass
from typing import Iterator

# Simple generator example used for teaching about generators

def id_generator(start: int = 1) -> Iterator[int]:
    """Yield incrementing IDs starting from `start`.

    Example usage:
        gen = id_generator(10)
        next(gen)  # 10
        next(gen)  # 11
    """
    current = start
    while True:
        yield current
        current += 1


# Simple dataclass example to demonstrate the dataclass pattern
@dataclass
class SimpleData:
    id: int
    name: str

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name}
