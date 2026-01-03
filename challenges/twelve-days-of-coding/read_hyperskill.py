import math
from collections import deque
import heapq

# filename = "hyperskill-dataset-119002108.txt" # Day 2
# filename = "hyperskill-dataset-119020066.txt"  # Day 3
# filename = "hyperskill-dataset-119046295.txt"  # Day 4
# filename = "hyperskill-dataset-119049171.txt"  # Day 5
# filename = "hyperskill-dataset-119095940.txt"  # Day 6
# filename = "hyperskill-dataset-119118740.txt"  # Day 7
# filename = "hyperskill-dataset-119140575.txt"  # Day 8
# filename = "hyperskill-dataset-119143157.txt"  # Day 9
filename = "hyperskill-dataset-119170557.txt"  # Day 10


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

    # Day 10 solution - Find longest common rhythm pattern
    # Parse each drummer's rhythm pattern
    rhythms = []
    for line in content:
        rhythm = [int(x) for x in line.split(",")]
        rhythms.append(rhythm)

    print(f"\nNumber of drummers: {len(rhythms)}")
    print(f"First drummer's pattern length: {len(rhythms[0])}")

    # Helper function to check if a subsequence appears in a sequence
    def contains_subsequence(sequence, subseq):
        """Check if subseq appears as a contiguous subsequence in sequence"""
        subseq_len = len(subseq)
        seq_len = len(sequence)

        if subseq_len > seq_len:
            return False

        for i in range(seq_len - subseq_len + 1):
            if sequence[i : i + subseq_len] == subseq:
                return True
        return False

    # Find longest common substring
    # Start with the first drummer's pattern as reference
    reference = rhythms[0]
    max_length = 0

    # Try all possible contiguous subsequences from longest to shortest
    for length in range(len(reference), 0, -1):
        found = False

        # Try all starting positions for this length
        for start in range(len(reference) - length + 1):
            candidate = reference[start : start + length]

            # Check if this candidate appears in all other rhythms
            if all(contains_subsequence(rhythm, candidate) for rhythm in rhythms[1:]):
                max_length = length
                found = True
                print(f"\nFound common pattern of length {length}: {candidate[:10]}...")
                break

        if found:
            break

    print(f"\nLongest common rhythm pattern length: {max_length}")

    # Day 8 solution
#     queens = []
#     for line in content:
#         row, col = line.split(",")
#         queens.append((int(row), int(col)))

#     # Count attacking pairs
#     attacking_pairs = 0

#     for i in range(len(queens)):
#         for j in range(i + 1, len(queens)):
#             row1, col1 = queens[i]
#             row2, col2 = queens[j]

#             # Check if queens attack each other
#             # Same row
#             if row1 == row2:
#                 attacking_pairs += 1
#             # Same column
#             elif col1 == col2:
#                 attacking_pairs += 1
#             # Same diagonal (difference in rows equals difference in cols)
#             elif abs(row1 - row2) == abs(col1 - col2):
#                 attacking_pairs += 1

# print(f"\nNumber of attacking queen pairs: {attacking_pairs}")

# Day 7 solution
# # Build graph and count degrees
# degree = {}

# for line in content:
#     land1, land2 = line.split(",")

#     # Count degree (number of bridges) for each landmass
#     degree[land1] = degree.get(land1, 0) + 1
#     degree[land2] = degree.get(land2, 0) + 1

# # Count landmasses with odd degree
# odd_degree_count = sum(1 for d in degree.values() if d % 2 == 1)

# # Eulerian path rules:
# # - 0 odd vertices: Eulerian circuit exists (can traverse all edges once)
# # - 2 odd vertices: Eulerian path exists (can traverse all edges once)
# # - More than 2 odd vertices: Need additional crossings

# if odd_degree_count == 0 or odd_degree_count == 2:
#     additional_crossings = 0
# else:
#     # Need to pair up odd degree vertices
#     # Formula: (odd_degree_count / 2) - 1
#     additional_crossings = (odd_degree_count // 2) - 1

# print(f"\nLandmasses with odd degree: {odd_degree_count}")
# print(f"Additional bridge crossings required: {additional_crossings}")
# Day 6 solution
# starting_being = content[0]
# print(f"Starting being: {starting_being}")

# # Build adjacency list for the graph
# graph = {}
# for line in content[1:]:
#     name1, name2 = line.split(",")

#     # Add bidirectional relationships
#     if name1 not in graph:
#         graph[name1] = []
#     if name2 not in graph:
#         graph[name2] = []

#     graph[name1].append(name2)
#     graph[name2].append(name1)

# # BFS to find furthest being
# queue = deque([(starting_being, 0)])  # (being, distance)
# visited = {starting_being}
# max_distance = 0
# furthest_beings = []

# while queue:
#     current, distance = queue.popleft()

#     # Track beings at maximum distance
#     if distance > max_distance:
#         max_distance = distance
#         furthest_beings = [current]
#     elif distance == max_distance:
#         furthest_beings.append(current)

#     # Explore neighbors
#     if current in graph:
#         for neighbor in graph[current]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append((neighbor, distance + 1))

# # Sort alphabetically and get first
# furthest_beings.sort()
# result = furthest_beings[0]

# print(f"\nFurthest being: {result}")
# print(f"Distance: {max_distance}")

# Day 5 solution
# coordinates = []
# for coordinate in content:
#     print(f"Coordinate: {coordinate}")
#     x, y = coordinate.split(",")
#     x = float(x)
#     y = float(y)
#     coordinates.append((x, y))
#     print(f" X: {x}, Y: {y}")

# # Apply Shoelace formula
# n = len(coordinates)
# area = 0

# for i in range(n):
#     j = (i + 1) % n  # Next vertex (wraps around to 0 at the end)
#     area += coordinates[i][0] * coordinates[j][1]
#     area -= coordinates[j][0] * coordinates[i][1]

# area = abs(area) / 2

# print(f"\nArea of polygon: {area}")
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
