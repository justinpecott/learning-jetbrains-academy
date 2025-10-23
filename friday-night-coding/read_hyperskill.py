# Script to read the hyperskill dataset text file


def read_hyperskill_file():
    """Read and print the contents of the hyperskill dataset file."""
    filename = "hyperskill-dataset-117283190.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
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

    if content:
        print("\n" + "=" * 50)
        print(f"File read successfully! Total characters: {len(content)}")

    digit_dict = {}
    for d in range(10):
        digit_dict[str(d)] = 0

    for char in content:
        print(char)
        digit_dict[char] += 1

    sorted_dict = dict(
        sorted(digit_dict.items(), key=lambda item: item[1], reverse=True)
    )
    print(sorted_dict)
