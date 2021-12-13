from typing import List


def list_max(values: List) -> int:
    max: int = values[0]

    for value in values[1::]:
        if value > max:
            max = value

    return max


def list_min(values: List) -> int:
    min: int = values[0]

    for value in values[1::]:
        if value < min:
            min = value

    return min


def main():
    list_a = [1, 2, 3, 4, 5, 6]

    max_value = list_max(list_a)
    print(max_value)

    min_value = list_min(list_a)
    print(min_value)


if __name__ == "__main__":
    main()
