class Jar:
    def __init__(self, capacity: int = 12) -> None:
        # private attributes
        self._size = 0

        # public attributes
        self.capacity = capacity

    def __str__(self) -> str:
        return "🍪" * self._size

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if value < 0 or value < self._size:
            raise ValueError(
                "Capacity must be non-negative and greater than or equal to size."
            )
        self._capacity = value

    def deposit(self, n: int):
        if n + self._size > self._capacity:
            raise ValueError
        self._size = self._size + n

    def withdraw(self, n: int):
        if n > self._size:
            raise ValueError
        self._size = self._size - n


def main():
    jar = Jar()
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(1)
    print(jar)
    jar.deposit(2)
    print(jar)


if __name__ == "__main__":
    main()
