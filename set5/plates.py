def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate: str) -> bool:
    """Check if a license plate meets all validation requirements."""
    MIN_LENGTH, MAX_LENGTH = 2, 6

    return (
        MIN_LENGTH <= len(plate) <= MAX_LENGTH
        and plate[:2].isalpha()
        and plate.isalnum()
        and _has_valid_number_placement(plate)
    )


def _has_valid_number_placement(plate: str) -> bool:
    """Check if the license plate has numbers in valid positions."""
    # If there are no digits, the plate is valid
    if not any(char.isdigit() for char in plate):
        return True

    for index in range(len(plate) - 1):
        if plate[index].isalpha() and plate[index + 1] == "0":
            return False
        if plate[index].isdigit() and plate[index + 1].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
