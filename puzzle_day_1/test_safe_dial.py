from .safe_dial import Rotation, count_zero_positions


def test_example_password_is_3() -> None:
    rotations = [
        Rotation("L", 68),
        Rotation("L", 30),
        Rotation("R", 48),
        Rotation("L", 5),
        Rotation("R", 60),
        Rotation("L", 55),
        Rotation("L", 1),
        Rotation("L", 99),
        Rotation("R", 14),
        Rotation("L", 82),
    ]

    assert count_zero_positions(rotations) == 3


