import math
from collections import deque

# filename = "hyperskill-dataset-119002108.txt" # Day 2
# filename = "hyperskill-dataset-119020066.txt"  # Day 3
# filename = "hyperskill-dataset-119046295.txt"  # Day 4
filename = "hyperskill-dataset-119049171.txt"  # Day 5


def read_hyperskill_file():
    """Read and print the contents of the hyperskill dataset file."""
    filename = "hyperskill-dataset-119002108.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in the current directory.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def read_hyperskill_file_lines():
    """Read the file line by line and return as a list."""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Strip newlines from each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in the current directory.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


if __name__ == "__main__":
    # Read and display the entire file
    print("Reading hyperskill dataset file...\n")
    print("=" * 50)
    content = read_hyperskill_file_lines()
    print(content)

    # Day 5 solution
    coordinates = []
    for coordinate in content:
        print(f"Coordinate: {coordinate}")
        x, y = coordinate.split(",")
        x = float(x)
        y = float(y)
        coordinates.append((x, y))
        print(f" X: {x}, Y: {y}")

    # Apply Shoelace formula
    n = len(coordinates)
    area = 0

    for i in range(n):
        j = (i + 1) % n  # Next vertex (wraps around to 0 at the end)
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]

    area = abs(area) / 2

    print(f"\nArea of polygon: {area}")
    # Day 4 solution
    # fork_status = {}
    # picks = 0
    # contention = 0
    # for log in content:
    #     parts = log.split(",")
    #     elf = parts[0]
    #     action = parts[1]
    #     fork = parts[2]

    #     # print(f"Elf: {elf}, Action: {action}, Fork: {fork}")

    #     if action == "pick":
    #         picks += 1
    #         if fork in fork_status and fork_status[fork] is not None:
    #             # print(
    #             #     f" Error: {elf} picked Fork {fork} but that is already already picked by {fork_status[fork]}"
    #             # )
    #             contention += 1
    #         else:
    #             fork_status[fork] = elf
    #     else:
    #         fork_status[fork] = None

    #     # print(f" Current fork status: {fork_status}")

    # print(f"\nTotal picks: {picks}")
    # print(f"\nTotal contentions: {contention}")

    # Day 3 solution
    # best_score = 0
    # best_password = ""

    # for password in content:
    #     print(f"Password: {password}")
    #     score = len(password)

    #     # Check Requirements
    #     has_lowercase = any(c.islower() for c in password)
    #     has_uppercase = any(c.isupper() for c in password)
    #     has_digit = any(c.isdigit() for c in password)
    #     has_special = any(c in "!@#$%^&*" for c in password)

    #     if not (has_lowercase and has_uppercase and has_digit and has_special):
    #         print(" Missing character types")
    #         score = score * 0.75

    #     # Check for repeated characters
    #     char_counts = {}
    #     for char in password:
    #         char_counts[char] = char_counts.get(char, 0) + 1

    #     # Find most frequent character
    #     max_count = max(char_counts.values())
    #     if max_count / len(password) >= 0.3:
    #         print(f"  Repeated character penalty: -{max_count}")
    #         score -= max_count

    #     if score > best_score:
    #         best_score = score
    #         best_password = password

    # print(f"\nBest password: {best_password} with score {best_score}")

    # Day 2 solution
    # target_sweetness = int(content[0])
    # deviation = 999999999
    # cocoas = [int(x) for x in content[1].split(",")]

    # print("Trying to an average of ", str(target_sweetness))
    # print(" We have " + str(len(cocoas)) + " cocoas")

    # best_pair = None
    # min_deviation = float("inf")

    # for i in range(len(cocoas)):
    #     for j in range(i + 1, len(cocoas)):
    #         average = (cocoas[i] + cocoas[j]) / 2
    #         current_deviation = abs(average - target_sweetness)

    #         if current_deviation < min_deviation:
    #             min_deviation = current_deviation
    #             best_pair = (cocoas[i], cocoas[j])

    # print(f"Best pair: {best_pair}")
    # print(f"Average: {sum(best_pair) / 2}")
    # print(f"Deviation from target: {min_deviation}")
