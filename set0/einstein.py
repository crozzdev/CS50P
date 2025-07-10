C = 300000000


def calculate_energy(mass: int) -> int:
    "This function calculates the energy using Einstein's formula E=mc2"
    return mass * (C * C)


def main():
    mass = int(input("m: "))
    print(f"E: {calculate_energy(mass)}")


main()
