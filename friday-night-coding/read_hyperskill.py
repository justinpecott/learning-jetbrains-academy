# Script to read the hyperskill dataset text file


def read_hyperskill_file():
    """Read and print the contents of the hyperskill dataset file."""
    # Day 1 hyperskill-dataset-117283190.txt
    # Day 2 hyperskill-dataset-117316244.txt
    # Day 3 hyperskill-dataset-117316666.txt
    filename = "hyperskill-dataset-117316666.txt"

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
    filename = "hyperskill-dataset-117283190.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
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
    content = read_hyperskill_file().strip()
    print(content)

    if content:
        print("\n" + "=" * 50)
        print(f"File read successfully! Total characters: {len(content)}")


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
