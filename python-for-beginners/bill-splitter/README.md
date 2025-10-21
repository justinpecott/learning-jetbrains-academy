# Bill Splitter

A simple command-line script that splits a dinner bill evenly among friends, with an optional “Who is lucky?” feature that picks one person who doesn’t pay.

This is a small learning project aimed at practicing user input handling, basic data structures, and simple control flow in Python.

## Features

- Prompt for the number of friends (including you)
- Collect each friend’s name
- Ask for the total bill amount and split it evenly to two decimal places
- Optional: select a random “lucky” friend who pays nothing, and re-split the bill among the rest
- Print the final amounts as a Python dictionary mapping each friend’s name to their share

## How it works (high level)

1. Ask for the number of participants.
2. If the number isn’t a positive integer, exit with a friendly message.
3. Read each friend’s name and initialize their share to 0.
4. Prompt until a valid positive bill value is entered.
5. Split the bill equally among all friends.
6. Ask if you want to use the “Who is lucky?” feature:
   - If Yes: randomly pick one person and set their share to 0, then re-split the bill among the remaining participants.
   - If No: keep the equal split.
7. Print the final result as a dictionary like:
   ```
   {'Alice': 40.0, 'Bob': 40.0, 'Charlie': 40.0}
   ```

## Requirements

- Python 3.8+ (any recent Python 3 should work)
- Standard library only (no external dependencies)

## Getting started

From the `bill-splitter` directory, run:

```
python bill-splitter.py
```

or, depending on your environment:

```
python3 bill-splitter.py
```

## Examples

### Example (without lucky feature)

```
Enter the number of friends joining (including you): 3
Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie

Enter the total bill value:
120
Do you want to use the "Who is lucky?" feature? Write Yes/No:
No
No one is going to be lucky
{'Alice': 40.0, 'Bob': 40.0, 'Charlie': 40.0}
```

### Example (with lucky feature)

```
Enter the number of friends joining (including you): 3
Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie

Enter the total bill value:
120
Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes
Bob is the lucky one!
{'Alice': 60.0, 'Bob': 0.0, 'Charlie': 60.0}
```

## Input details and validation

- Number of friends:
  - If it’s not a positive integer, the program prints “No one is joining for the party” and exits.
- Friend names:
  - Enter exactly as many names as the number of friends.
- Total bill:
  - Must be a positive number (float allowed). The program will reprompt until a valid positive number is entered.
- Lucky feature:
  - Must be exactly “Yes” or “No” (case-sensitive in this version).

## Rounding behavior

- Shares are rounded to two decimal places using standard rounding.
- Because of rounding, the sum of individual shares may differ slightly from the total bill (for example, by a cent). This is expected in this simple version.
- If you need exact cent-equality, a common approach is:
  1. Convert the total to cents (integer arithmetic).
  2. Divide evenly to get a base share in cents.
  3. Distribute any remaining cents to some participants (e.g., the first N participants).

## Known limitations

- Single participant + “Yes” to lucky:
  - With only one person, choosing “Who is lucky?” attempts to divide by zero. This version will raise a division-by-zero error in that edge case.
- Yes/No strictness:
  - The prompt requires exactly “Yes” or “No” with matching case. Typing “yes” or “no” won’t be accepted in this version.

## Possible improvements

- Make “Yes/No” input case-insensitive and whitespace-tolerant.
- Ensure the sum of shares always equals the total bill by distributing remainder cents.
- Handle the single-person “lucky” edge case gracefully (e.g., keep the single person’s share at 0.00).
- Print the result in a formatted table for easier reading.
- Add automated tests for input handling and rounding logic.

## Project structure

- `bill-splitter.py` — the main script
- `README.md` — this file

## Troubleshooting

- “Command not found” or “No such file” when running:
  - Ensure you’re in the `bill-splitter` directory and that `bill-splitter.py` exists.
- Python version issues:
  - Try `python3` instead of `python`, or set up a virtual environment with a recent Python 3.
- Input rejected repeatedly:
  - Check the prompts carefully. The number of friends must be a positive integer, the bill must be a positive number, and the lucky prompt expects exactly `Yes` or `No`.

Enjoy splitting bills fairly!
