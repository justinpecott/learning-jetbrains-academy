msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

PLUS = "+"
MINUS = "-"
MULT = "*"
DIV = "/"
OPERS = [PLUS, MINUS, MULT, DIV]


def is_a_number(j):
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


x = 0
oper = ""
y = 0
while True:
    print(msg_0)
    calc = input()

    # Split the calc to variable
    calc_parts = calc.split()
    x = calc_parts[0]
    oper = calc_parts[1]
    y = calc_parts[2]

    # Check for valid numbers
    all_numbers = is_a_number(x) and is_a_number(y)
    if not all_numbers:
        print(msg_1)
        continue

    # Check for valid oper
    valid_oper = oper in OPERS
    if not valid_oper:
        print(msg_2)
        continue

    result = 0
    if oper == PLUS:
        result = float(x) + float(y)
    if oper == MINUS:
        result = float(x) - float(y)
    if oper == MULT:
        result = float(x) * float(y)
    if oper == DIV:
        if float(y) == 0.0:
            print(msg_3)
            continue
        result = float(x) / float(y)

    print(str(result))
    break
