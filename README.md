# Number to Words Converter

A Python utility that converts integers (0-999,999,999,999) to their English word representations.

## Description

This project provides a command-line tool that allows users to input a number and receive its English textual representation. For example, the number `123` would be converted to `One Hundred Twenty Three`.

The converter supports numbers from 0 to 999,999,999,999 (nearly one trillion), covering:
- Single digits (0-9)  
- Teens (10-19)
- Tens (20-90)
- Hundreds
- Thousands
- Millions
- Billions

## Files

- `main.py`: Contains the core conversion logic and command-line interface
- `constans.py`: Stores the constant word mappings used in the conversion process

## Installation

No external dependencies are required. The project runs with standard Python 3.

```bash
# Clone the repository (if applicable)
git clone https://github.com/Yousefrahimi96/Number-to-Word.git

# Navigate to the project directory
cd number-to-words
```

## Usage

Run the script from the command line:

```bash
python main.py
```

The program will prompt you to enter a number. After entering a valid integer in the supported range, it will output the English word representation.

### Example

```
Please enter a number: 42
Forty Two
```

## Function Documentation

The main function that performs the conversion is:

```python
def num_to_word(num: int) -> str:
    """
    Convert an integer to its English textual representation.

    :param num: An integer between 0 and 999,999,999,999 inclusive.
    :return: A string containing the English words for `num`.
    """
```

## Error Handling

The program handles:
- Invalid inputs (non-integer values)
- Numbers outside the supported range (0-999,999,999,999)

## License

MIT

## Contributing

yousefrahimi96@yahoo.com
