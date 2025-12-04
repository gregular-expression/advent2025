from pathlib import Path

from .safe_dial import count_zero_positions, parse_rotations


def main() -> None:
    # Input for this puzzle day is colocated with the code.
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "input.txt"

    with input_path.open("r", encoding="utf-8") as f:
        rotations = parse_rotations(f)
    password = count_zero_positions(rotations)
    print(password)


if __name__ == "__main__":
    main()


