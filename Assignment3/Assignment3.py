import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_category_recorded(category_name):
    for name in categories.keys():
        if name == category_name:
            return categories[name]
    return None

def create_category(category_info):
    category_info = category_info.split(' ')

    if is_category_recorded(category_info[0]) is not None:
        print(f"Warning: Cannot create the category for the second time. The stadium has already {category_info[0]}")
        w_file.write(f"Warning: Cannot create the category for the second time. The stadium has already "
                     f"{category_info[0]}.\n")

    else:
        num_of_rows, num_of_columns = category_info[1].split('x')
        num_of_rows, num_of_columns = int(num_of_rows), int(num_of_columns)
        category = [['X' for _ in range(num_of_columns)] for _ in range(num_of_rows)]
        categories[category_info[0]] = category

        print(f"The category '{category_info[0]}' having {num_of_rows * num_of_columns} seats has been created")
        w_file.write(f"The category '{category_info[0]}' having {num_of_rows * num_of_columns} "
                     f"seats has been created\n")

def sell_ticket(ticket_info):
    ticket_info = ticket_info.split(' ')
    i = 3
    while i < len(ticket_info):
        seat = ticket_info[i].split('-')
        row = alphabet.index(seat[0][0].lower())
        seat[0] = seat[0][1:]
        is_empty = True
        category = categories[ticket_info[2]]

        if row >= len(category):
            print(f"Error: The category '{ticket_info[2]}' has less row than the specified index {ticket_info[i]}!")
            w_file.write(f"Error: The category '{ticket_info[2]}' has less row than the specified index {ticket_info[i]}!\n")
            i = i + 1
            continue
        if int(seat[-1]) >= len(category[row]):
            print(f"Error: The category '{ticket_info[2]}' has less column than the specified index {ticket_info[i]}!")
            w_file.write(f"Error: The category '{ticket_info[2]}' has less column than the specified index {ticket_info[i]}!\n")
            i = i + 1
            continue

        for seat_number in range(int(seat[0]), int(seat[-1])):
            if category[row][seat_number] != 'X':
                is_empty = False
                break
        if is_empty:
            seat_type = "S" if ticket_info[1] == 'student' else "F" if ticket_info[1] == 'full' else "T"
            category[row][int(seat[0]):int(seat[-1]) + 1] = [seat_type] * (int(seat[-1]) - int(seat[0]) + 1)
            categories[ticket_info[2]] = category
            print(f"Success: {ticket_info[0]} has bought {ticket_info[i]} at {ticket_info[2]}")
            w_file.write(f"Success: {ticket_info[0]} has bought {ticket_info[i]} at {ticket_info[2]}\n")
        else:
            if len(seat) == 1:
                print(f"Warning: The seat {ticket_info[i]} cannot be sold to {ticket_info[0]} since it was already sold!")
                w_file.write(f"Warning: The seat {ticket_info[i]} cannot be sold to {ticket_info[0]} since it was already sold!\n")
            else:
                print(f"Warning: The seats {ticket_info[i]} cannot be sold to {ticket_info[0]} due some of them have already been sold!")
                w_file.write(f"Warning: The seats {ticket_info[i]} cannot be sold to {ticket_info[0]} due some of them have already been sold!\n")

        i = i + 1

def cancel_ticket(ticket_info):
    ticket_info = ticket_info.split(' ')
    i = 1
    while i < len(ticket_info):
        seat = ticket_info[i].split('-')
        row = alphabet.index(seat[0][0].lower())
        seat[0] = seat[0][1:]

        is_taken = True
        category = categories[ticket_info[0]]

        if row >= len(category):
            print(f"Error: The category '{ticket_info[0]}' has less row than the specified index {ticket_info[i]}!")
            w_file.write(
                f"Error: The category '{ticket_info[0]}' has less row than the specified index {ticket_info[i]}!\n")
            i = i + 1
            continue
        if int(seat[-1]) >= len(category[row]):
            print(f"Error: The category '{ticket_info[0]}' has less column than the specified index {ticket_info[i]}!")
            w_file.write(
                f"Error: The category '{ticket_info[0]}' has less column than the specified index {ticket_info[i]}!\n")
            i = i + 1
            continue

        for seat_number in range(int(seat[0]), int(seat[-1]) + 1):
            if category[row][seat_number] == 'X':
                is_taken = False
                break

        if is_taken:
            category[row][int(seat[0]):int(seat[-1]) + 1] = ['X'] * (int(seat[-1]) - int(seat[0]) + 1)
            categories[ticket_info[0]] = category
            if len(seat) == 1:
                print(f"Success: The seat {ticket_info[i]} at '{ticket_info[0]}' has been canceled and now ready to sell again")
                w_file.write(f"Success: The seat {ticket_info[i]} at '{ticket_info[0]}' has been canceled and now ready to sell again\n")
            else:
                print(f"Success: The seats {ticket_info[i]} at '{ticket_info[0]}' has been canceled and now ready to sell again")
                w_file.write(f"Success: The seats {ticket_info[i]} at '{ticket_info[0]}' has been canceled and now ready to sell again\n")

        else:
            if len(seat) == 1:
                print(f"Error: The seat {ticket_info[i]} at {ticket_info[0]} has already been free! Nothing to cancel")
                w_file.write(f"Error: The seat {ticket_info[i]} at {ticket_info[0]} has already been free! Nothing to cancel\n")
            else:
                print(f"Error: Some of the seats {ticket_info[i]} at {ticket_info[0]} have already been free! Cannot cancel")
                w_file.write(f"Error: Some of the seats {ticket_info[i]} at {ticket_info[0]} have already been free! Cannot cancel\n")
        i = i+1

def balance(category_name):
    if is_category_recorded(category_name) is None:
        print("Error: The category '{category_name}' has not been recorded!")
        w_file.write(f"Error: The category '{category_name}' has not been recorded!\n")

    category = categories[category_name]
    s, f, t = 0, 0, 0
    for row in category:
        for seat in row:
            if seat == 'S':
                s += 1
            elif seat == 'F':
                f += 1
            elif seat == 'T':
                t += 1
    text = f"category report of '{category_name}'"
    print(text + "\n" + (len(text) * "-") + f"\nSum of students = {s}, Sum of full pay = {f}, "
                                          f"Sum of season ticket = {t}, "
                                          f"and Revenues = {s*10 + f*20 + t*250} Dollars")
    w_file.write(text + "\n" + (len(text) * "-") + f"\nSum of students = {s}, Sum of full pay = {f}, "
                                          f"Sum of season ticket = {t}, "
                                          f"and Revenues = {s*10 + f*20 + t*250} Dollars\n")

def show_category(category_name):
    if is_category_recorded(category_name) is None:
        print(f"Error: The category '{category_name}' has not been recorded!")
        w_file.write(f"Error: The category '{category_name}' has not been recorded!\n")
        return 0

    category = categories[category_name]
    print(f"Printing category layout of {category_name}\n")
    w_file.write(f"Printing category layout of {category_name}\n\n")
    for row in range(len(category) - 1, -1, -1):
        text = alphabet[row].upper() + " "
        for seat in category[row]:
            text += seat + "  "
        print(text[:-2])
        w_file.write(text[:-2] + "\n")
    col_num = ""
    for i in range(len(category[0])):
        col_num = col_num + (" " * (2 if len(str(i)) == 1 else 1)) + str(i)

    print(col_num)
    w_file.write(col_num + "\n")
    return 0

if __name__ == '__main__':
    file_name = sys.argv[1]
    r_file = open(file_name, 'r')
    w_file = open('output.txt', 'w')
    lines = r_file.read()
    lines = lines.split("\n")

    categories = {}

    for line in lines:
        line_list = line.split(' ', 1)

        if line_list[0] == "CREATECATEGORY":
            create_category(line_list[1])

        elif line_list[0] == "SELLTICKET":
            sell_ticket(line_list[1])

        elif line_list[0] == "CANCELTICKET":
            cancel_ticket(line_list[1])

        elif line_list[0] == "BALANCE":
            balance(line_list[1])

        elif line_list[0] == "SHOWCATEGORY":
            show_category(line_list[1])