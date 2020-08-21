def get_number():
    number = int(input("Choose a number between 1-255: "))
    return(number)

def divide(number, base):
    return((number // base , number % base))

def translate(number, base):
    result = []
    input = number
    while input != 0:
        answer_tuple = divide(input, base)
        result.append(answer_tuple[1])
        input = answer_tuple[0]
    return(result[::-1])

def to_bin_string(number_list):
    str_list = [str(number) for number in number_list]
    result = "".join(str_list)
    return(result)


def bin_to_hex(number_list):
    result = 0
    power = 1
    while len(number_list) > 0:
        result = result + number_list.pop(-1) * power
        power = power * 2
    return(translate(result, 16))

def to_hex_string(number_list):
    look_up = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    str_list = [look_up[number] for number in number_list]
    result = "".join(str_list)
    return(result)

def hex_to_dec(number_list):
    result = 0
    power = 1
    while len(number_list) > 0:
        result = result + number_list.pop(-1) * power
        power = power * 16
    return(result)

def hex_string_to_num_list(hex_str):
    look_up = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    result = [look_up.index(char) for char in hex_str]
    return(result)


def get_hex():
    hex_str = input("Put a hex number in: ")
    return(hex_str)




def main():
    decimal = get_number()
    bin_num_list = translate(decimal, 2)
    bin_str = to_bin_string(bin_num_list)
    print(f"Binary is {bin_str}")
    hex_str = to_hex_string(bin_to_hex(bin_num_list))
    print(f"The hex of this is {hex_str}")
    hex_num_list = hex_string_to_num_list(get_hex())
    decimal = hex_to_dec(hex_num_list)
    print(f"The decimal of the hex is {decimal}")

main()
