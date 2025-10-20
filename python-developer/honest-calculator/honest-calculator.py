messages = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move...",
    4: "Do you want to store the result? (y / n):",
    5: "Do you want to continue calculations? (y / n):",
    6: " ... lazy",
    7: " ... very lazy",
    8: " ... very, very lazy",
    9: "You are",
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
}

PLUS = "+"
MINUS = "-"
MULT = "*"
DIV = "/"
OPERS = [PLUS, MINUS, MULT, DIV]


def is_a_number(j):
    """Check if input is a number"""
    numb = True
    parts = j.split(".")
    if len(parts) > 2:
        numb = False
    else:
        for part in parts:
            if not part.isnumeric():
                numb = False
                break
    return numb


def get_calculation():
    """Get calculation from user, return parts"""
    calc = input(messages[0] + "\n")
    calc_parts = calc.split()
    return calc_parts[0], calc_parts[1], calc_parts[2]


def get_yes_no_input(prompt):
    """Keep asking until valid y/n response"""
    while True:
        response = input(prompt + "\n")
        if response in ["y", "n"]:
            return response


def calculate(x, oper, y):
    """Perform calculation, return None if error"""
    if oper == PLUS:
        return float(x) + float(y)
    if oper == MINUS:
        return float(x) - float(y)
    if oper == MULT:
        return float(x) * float(y)
    if oper == DIV:
        if float(y) == 0.0:
            print(messages[3])
            return None
        return float(x) / float(y)


def is_one_digit(v):
    """Check if value is a one-digit integer"""
    if float(v).is_integer():
        if -10 < float(v) < 10:
            return True
    return False


def check_laziness(x, oper, y):
    """Check for lazy operations and print messages"""
    msg = ""

    if is_one_digit(x) and is_one_digit(y):
        msg += messages[6]
    if (float(x) == 1 or float(y) == 1) and oper == MULT:
        msg += messages[7]
    if (float(x) == 0 or float(y) == 0) and oper in [MULT, PLUS, MINUS]:
        msg += messages[8]
    if msg != "":
        print(messages[9] + msg)


# Initializations
memory = 0.0

while True:
    # Get the calculation
    x, oper, y = get_calculation()

    # Check for memory usage
    if x == "M":
        x = str(memory)
    if y == "M":
        y = str(memory)

    #print("CURRENT STATE: x =", x, ", oper =", oper, ", y =", y)

    # Check for valid numbers
    all_numbers = is_a_number(x) and is_a_number(y)
    if not all_numbers:
        print(messages[1])
        continue

    # Check for valid oper
    valid_oper = oper in OPERS
    if not valid_oper:
        print(messages[2])
        continue

    # Check for laziness
    check_laziness(x, oper, y)

    # Perform calculation
    result = calculate(x, oper, y)
    if result is None:  # Division by zero
        continue

    # Show result
    print(str(result))

    # Store result
    if get_yes_no_input(messages[4]) == "y":
        if is_one_digit(result):
            msg_index = 10
            while msg_index <= 12:
                if get_yes_no_input(messages[msg_index]) == "y":
                    msg_index += 1
                    if msg_index > 12:
                        memory = result
                else:
                    break
        else:
            memory = result

    # Continue?
    if get_yes_no_input(messages[5]) == "n":
        break
