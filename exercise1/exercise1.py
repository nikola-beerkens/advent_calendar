import re

def dial_number_2(prev_location,direction, number, count):

    for _ in range(number):
        if direction == "L":
            prev_location = (prev_location - 1+100) % 100
        else:
            prev_location = (prev_location + 1) % 100
        if prev_location == 0:
            count += 1
    return prev_location, count    
    #repeat = number // 100
    #if direction == "R":
        #new_location = prev_location + number
        #if new_location >= 100 and new_location != 100:
            #count += 1 * repeat
    #elif direction == "L":
    #    new_location = prev_location - number
    #    if new_location < 0 and prev_location > 0:
    #        count += 1 * repeat
    #print(count, direction, number, prev_location,new_location)
    #new_location = new_location % 100
    #if new_location == 0:
    #    count += 1
    #return new_location, count

def dial_number_1(prev_location,direction, number, count):
    for _ in range(number):
        if direction == "L":
            prev_location = (prev_location - 1+100) % 100
        else:
            prev_location = (prev_location + 1) % 100
    if prev_location == 0:
        count += 1
    return prev_location, count    

def give_direction(chars):
    return chars[0]

def give_number(chars):
    number_str = ""
    for c in chars[1:]:
        number_str += c
    return int(number_str)

if __name__ == "__main__":
    f = open("input1.txt", "r")
    location = 50
    count = 0
    for line in f:
        input_data = line.strip()
        chars = []
        for c in input_data:
            chars.append(c)
        direction = give_direction(chars)
        number = give_number(chars)
        location, count = dial_number_2(location, direction, number, count)
    print(count)   
    f.close()