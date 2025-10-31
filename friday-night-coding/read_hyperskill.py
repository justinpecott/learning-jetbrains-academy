import math
from collections import deque


def read_hyperskill_file():
    """Read and print the contents of the hyperskill dataset file."""
    # Day 1 hyperskill-dataset-117283190.txt
    # Day 2 hyperskill-dataset-117316244.txt
    # Day 3 hyperskill-dataset-117316666.txt
    # Day 4 hyperskill-dataset-117363050.txt
    # Day 5 hyperskill-dataset-117388870.txt
    # Day 6 hyperskill-dataset-117397278.txt
    # Day 7 hyperskill-reply-144295977.txt
    # Day 8 hyperskill-dataset-117485786.txt
    # Day 9 hyperskill-dataset-117488223.txt
    # Day 10 hyperskill-dataset-117517182.txt
    filename = "hyperskill-dataset-117517182.txt"

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
    filename = "hyperskill-dataset-117517182.txt"

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


def convert_phone_to_binary(phone_number):
    """
    Convert a decimal phone number to 32-bit binary with overflow handling.

    Args:
        phone_number: integer phone number to convert

    Returns: string in format "overflows,binary_number"
    """
    # Maximum value for a 32-bit unsigned integer
    max_32bit = 2**32 - 1  # 4294967295
    overflow_value = 2**32  # 4294967296 (the value to subtract on overflow)

    # Count overflows
    overflows = 0

    # Reduce the number until it fits in 32 bits
    while phone_number > max_32bit:
        overflows += 1
        phone_number -= overflow_value
        print(
            f"Overflow occurred! New phone number: {phone_number}. Overflows: {overflows}"
        )

    # Convert to binary and remove leading zeros
    binary = bin(phone_number)[2:]  # Remove '0b' prefix

    # Return the result
    return f"{overflows},{binary}"


if __name__ == "__main__":
    # Read and display the entire file
    print("Reading hyperskill dataset file...\n")
    print("=" * 50)
    content = read_hyperskill_file_lines()
    print(content)

    if content:
        print("\n" + "=" * 50)
        print(f"File read successfully! Total characters: {len(content)}")

    # Day 10 solution
    for line in content:
        for char in line:
            if line.count(char) == 1:
                print(f"non-repeat: {char}")

    # # Day 9 solution
    # maze = content

    # # Find start (P) and goal (G) positions
    # start = None
    # goal = None

    # for row in range(len(maze)):
    #     for col in range(len(maze[row])):
    #         if maze[row][col] == "P":
    #             start = (row, col)
    #         elif maze[row][col] == "G":
    #             goal = (row, col)

    # print(f"Start: {start}, Goal: {goal}")

    # # BFS to find shortest path
    # queue = deque([(start, "")])  # (position, path)
    # visited = {start}

    # # Direction mappings: (row_delta, col_delta, direction_letter)
    # directions = [
    #     (-1, 0, "U"),  # Up
    #     (1, 0, "D"),  # Down
    #     (0, -1, "L"),  # Left
    #     (0, 1, "R"),  # Right
    # ]

    # while queue:
    #     (row, col), path = queue.popleft()

    #     # Check if we reached the goal
    #     if (row, col) == goal:
    #         print(f"Shortest path: {path}")
    #         print(f"Path length: {len(path)}")
    #         break

    #     # Try all four directions
    #     for dr, dc, direction in directions:
    #         new_row, new_col = row + dr, col + dc

    #         # Check if the new position is valid
    #         if (
    #             0 <= new_row < len(maze)
    #             and 0 <= new_col < len(maze[new_row])
    #             and maze[new_row][new_col] != "#"
    #             and (new_row, new_col) not in visited
    #         ):
    #             visited.add((new_row, new_col))
    #             queue.append(((new_row, new_col), path + direction))

    # # Day 8 solution
    # names = content.strip().split(" ")
    # for i in range(len(names)):
    #     ana = False
    #     for j in range(len(names)):
    #         if names[i] != names[j] and len(names[i]) == len(names[j]):
    #             # Check if they're anagrams by comparing sorted characters
    #             if sorted(names[i].lower()) == sorted(names[j].lower()):
    #                 # print(f"Anagram found: {names[i]} and {names[j]}")
    #                 ana = True
    #                 break
    #     if not ana:
    #         print(f"No anagram for: {names[i]}")

    # for name in names:
    #     if len(name) > 0:
    #         first_letter = name[0].upper()
    #         last_letter = name[-1].upper()
    #         print(f"{first_letter}{last_letter}")

    # Day 7 solution
    # answer = convert_phone_to_binary(int(content.strip()))
    # print(answer)

    # # Day 6 solution - 4D Vector distances
    # vectors = []

    # # Parse each line as a 4D vector
    # for line in content:
    #     # Split by comma and convert to integers
    #     coords = [int(x.strip()) for x in line.split(',')]
    #     vectors.append(coords)

    # total_distance = 0

    # # Calculate distance between consecutive vectors
    # for i in range(len(vectors) - 1):
    #     v1 = vectors[i]
    #     v2 = vectors[i + 1]

    #     # Euclidean distance in 4D: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)² + (w2-w1)²)
    #     distance_squared = sum((v2[j] - v1[j]) ** 2 for j in range(4))
    #     distance = math.sqrt(distance_squared)

    #     # Round up to nearest integer
    #     rounded_distance = math.ceil(distance)

    #     print(f"Vector {i} to {i+1}: {v1} -> {v2}, distance = {distance:.2f}, rounded up = {rounded_distance}")

    #     total_distance += rounded_distance

    # print(f"\nTotal distance: {total_distance}")

    # # Day 5 solution
    # notes = 'ABCDEFG'
    # shortest_length = 999999
    # for i in range(0, 1000):
    #     j = i + 6
    #     for j in range(i + 6, 1000):
    #         if j - i < shortest_length:
    #             k = content[i:j]
    #             if set(notes).issubset(set(k)):
    #                 shortest_length = j - i
    #                 print(f"Found: {k} with length {shortest_length}")
    #                 break

    # # Day 4 solution

    # # Define the keypad as a 2D grid
    # keypad = [
    #     ['A', 'B', 'C', 'D'],
    #     ['E', 'F', 'G', 'H'],
    #     ['I', 'J', 'K', 'L'],
    #     ['M', 'N', 'O', 'P']
    # ]

    # # Split content by newlines to get each instruction sequence
    # instruction_lines = content.strip().split('\n')

    # code = []

    # for line in instruction_lines:
    #     print("---")
    #     print(line)
    #     # Start at A (row 0, col 0)
    #     row, col = 0, 0

    #     # Split by comma to get individual moves
    #     moves = line.split(',')

    #     for move in moves:
    #         move = move.strip()
    #         if move == 'UP':
    #             row = max(0, row - 1)
    #         elif move == 'DOWN':
    #             row = min(3, row + 1)
    #         elif move == 'LEFT':
    #             col = max(0, col - 1)
    #         elif move == 'RIGHT':
    #             col = min(3, col + 1)

    #     # Record the final letter
    #     print(keypad[row][col])
    #     code.append(keypad[row][col])
    #     print("---")

    # # Join all letters to get the final code
    # final_code = ''.join(code)
    # print(final_code)

    # # Day 3 solution
    # # Create dictionary to count each letter
    # letter_count = {}

    # for char in content.lower():
    #     if char.isalpha():  # Only count letters
    #         if char in letter_count:
    #             letter_count[char] += 1
    #         else:
    #             letter_count[char] = 1

    # letters_once = [letter for letter, count in letter_count.items() if count == 1]

    # print(f"Letters that appear once: {letters_once}")
    # print(f"Total unique letters appearing once: {len(letters_once)}")

    # print(letter_count)

    # Day 2 solution
    # angles = content.split(",")

    # # Convert strings to integers and normalize each angle to 0-359 range
    # normalized_angles = []
    # for angle in angles:
    #     angle_int = int(angle.strip())  # Convert to int and remove whitespace
    #     normalized = angle_int % 360
    #     normalized_angles.append(normalized)

    # # Sum all the normalized angles
    # total = sum(normalized_angles)

    # # Get final position (0-359)
    # final_position = total % 360

    # print(final_position)

    # Day 1 solution
    #
    # digit_dict = {}
    # for d in range(10):
    #     digit_dict[str(d)] = 0

    # for char in content:
    #     print(char)
    #     digit_dict[char] += 1

    # sorted_dict = dict(
    #     sorted(digit_dict.items(), key=lambda item: item[1], reverse=True)
    # )
    # print(sorted_dict)

# EGMBJKMCJPDAHIFCMIFLLMOKACGEAJAPEEPCNBNLMHFAKCBIIKBHPEHBKKDFNKFE
# EGMBJKMCJPDAHIFCMIFLLMOKACGEAJAPEEPCNBNLMHFAKCBIIKBHPEHBKKDFNKFE
# DLCOCHPDAADCMPJIELLKCIGFBIIEFEJEHGCMGCFNKNIAMNEDLGIEHPKFAANFFCFH
# AEIBHAAAJEINDIBNIAIBHEIODFDLACJEHHBAGEAIKGIDAIFHFBCKBJCBBOHKNGAM
# AEIBHAAAJEINDIBNIAIBHEIODFDLACJEHHBAGEAIKGIDAIFHFBCKBJCBBOHKNGAM
