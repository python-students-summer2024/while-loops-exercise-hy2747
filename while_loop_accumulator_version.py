def get_starting_number():
    number = 0
    while number < 1:
        input_number = input("Enter your bottle of water to start with: ")
        if input_number.isdigit():
            number = int(input_number)
        else:
            number = 0
    return number

def sing(num_bottles):
    if num_bottles < 1:
        return
    i = 0
    while i < num_bottles - 1:
        print(f"{num_bottles - i} bottles of beer on the wall, {num_bottles - i} bottles of beer.")
        if num_bottles - i - 1 > 1:
            print(f"Take one down, pass it around, {num_bottles - i - 1} bottles of beer on the wall.\n")
        else:
            print(f"Take one down, pass it around, {num_bottles - i - 1} bottle of beer on the wall.\n")
        i += 1
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take it down, pass it around, no more bottles of beer on the wall!")