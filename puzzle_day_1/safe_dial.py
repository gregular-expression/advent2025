from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Rotation:
    direction: str  # "L" or "R"
    distance: int


DIAL_SIZE = 100
START_POSITION = 50


def parse_rotations(lines: Iterable[str]) -> List[Rotation]:
    """Parse raw input lines into Rotation objects."""
    rotations: List[Rotation] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        direction = line[0]
        if direction not in ("L", "R"):
            raise ValueError(f"Invalid direction {direction!r} in line {line!r}")
        distance = int(line[1:])
        rotations.append(Rotation(direction=direction, distance=distance))
    return rotations


def apply_rotation(position: int, rotation: Rotation) -> int:
    """Return the new position after applying a single rotation."""
    if rotation.direction == "L":
        delta = -rotation.distance
    else:
        delta = rotation.distance
    return (position + delta) % DIAL_SIZE


def count_zero_positions(rotations: Iterable[Rotation]) -> int:
    """
    Count how many times the dial is pointing at 0 immediately after a rotation.
    """
    position = START_POSITION
    zeros = 0
    for rotation in rotations:
        position = apply_rotation(position, rotation)
        if position == 0:
            zeros += 1
    return zeros


