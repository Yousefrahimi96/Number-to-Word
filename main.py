#!/usr/bin/env python3
"""
num_to_word module

Provides a function to convert integers in the range
0-999,999,999,999 to their English word representations.
"""

from constans import UNDER_20, TENS, ABOVE_100


def num_to_word(num: int) -> str:
    """
    Convert an integer to its English textual representation.

    :param num: An integer between 0 and 999,999,999,999 inclusive.
    :return: A string containing the English words for `num`.
    """
    if num < 20:
        return UNDER_20[num]

    if num < 100:
        ten, rem = divmod(num, 10)
        if rem == 0:
            return TENS[ten - 2]
        return f"{TENS[ten - 2]} {UNDER_20[rem]}"

    pivot = max(key for key in ABOVE_100 if key <= num)
    count, rem = divmod(num, pivot)
    prefix = num_to_word(count)
    word = ABOVE_100[pivot]

    if rem == 0:
        return f"{prefix} {word}"
    return f"{prefix} {word} {num_to_word(rem)}"


def main():
    """
    Prompt the user for a number and print its English word form.
    Handles invalid input and range errors.
    """
    try:
        user_input = input("Please enter a number: ")
        num = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if 0 <= num <= 999_999_999_999:
        print(num_to_word(num))
    else:
        print("Number is out of the supported range.")


if __name__ == "__main__":
    main()
