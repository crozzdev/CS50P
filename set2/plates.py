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

    if not plate[-1].isdigit():
        return False

    for index in range(len(plate) - 1):

        if plate[index].isdigit() and plate[index] == "0":
            return False

        if plate[index].isdigit() and not plate[index + 1].isdigit():
            return False

    return True


main()
