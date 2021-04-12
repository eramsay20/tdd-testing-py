"XVI"
"XC"

def parse(roman_num):
    mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    shortcuts = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    index = 0
    total = 0
    while index < len(roman_num):
        curr_num = roman_num[index]
        if index + 1 == len(roman_num):
            total += mappings[curr_num]
            index += 1
        else:
            next_num = roman_num[index + 1]
            potential_shortcut = curr_num + next_num
            if potential_shortcut in shortcuts:
                total += shortcuts[potential_shortcut]
                index += 2
            else: 
                total += mappings[curr_num]
                index += 1
    return total