import math

def read_hyperskill_file():
    """Read and print the contents of the hyperskill dataset file."""
    # Day 1 hyperskill-dataset-117283190.txt
    # Day 2 hyperskill-dataset-117316244.txt
    # Day 3 hyperskill-dataset-117316666.txt
    # Day 4 hyperskill-dataset-117363050.txt
    # Day 5 hyperskill-dataset-117388870.txt
    # Day 6 hyperskill-dataset-117397278.txt
    filename = "hyperskill-dataset-117397278.txt"

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
    filename = "hyperskill-dataset-117397278.txt"

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

    if content:
        print("\n" + "=" * 50)
        print(f"File read successfully! Total characters: {len(content)}")

    # Day 6 solution
    # Day 7 solution - 4D Vector distances
    vectors = []
    
    # Parse each line as a 4D vector
    for line in content:
        # Split by comma and convert to integers
        coords = [int(x.strip()) for x in line.split(',')]
        vectors.append(coords)
    
    total_distance = 0
    
    # Calculate distance between consecutive vectors
    for i in range(len(vectors) - 1):
        v1 = vectors[i]
        v2 = vectors[i + 1]
        
        # Euclidean distance in 4D: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)² + (w2-w1)²)
        distance_squared = sum((v2[j] - v1[j]) ** 2 for j in range(4))
        distance = math.sqrt(distance_squared)
        
        # Round up to nearest integer
        rounded_distance = math.ceil(distance)
        
        print(f"Vector {i} to {i+1}: {v1} -> {v2}, distance = {distance:.2f}, rounded up = {rounded_distance}")
        
        total_distance += rounded_distance
    
    print(f"\nTotal distance: {total_distance}")

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