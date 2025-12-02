def find_invalid_ids(id_list):
    invalid_ids = []
    for i in range(len(id_list)):
        #print("Checking range:", id_list[i][0], "to", id_list[i][1])
        for number in range(id_list[i][0], id_list[i][1]+1):
            str_num = str(number)
            if str_num[:len(str_num)//2] == str_num[len(str_num)//2:]:
                invalid_ids.append(number)
                #print("Invalid ID found:", number)
    return invalid_ids

def sum_invalid_ids(invalid_ids):
    return sum(invalid_ids)


if __name__ == "__main__":  
    f = open("input2.txt", "r")
    id_list = []
    invalid_ids = []
    for line in f:
        input_data = line.strip().split(',')
        for item in input_data:
            data = item.split("-")
            id_list.append((int(data[0]),int(data[1])))
    f.close()
    invalid_ids = find_invalid_ids(id_list)
    sum = sum_invalid_ids(invalid_ids)
    print("Sum of invalid IDs:", sum)