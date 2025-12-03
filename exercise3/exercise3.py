#def find_max_battery(batteries):
#    max_battery = batteries[0]
#    for battery in batteries:
#        if battery[0] > max_battery[0]:
#            max_battery = battery
#    batteries.remove(max_battery)
#    return max_battery, batteries

def arrange(digit1, digit2):
    return int(str(digit1) + str(digit2))

#def find_second(batteries, max):
#    if max[1] == len(batteries):
#        max_comb = arrange(batteries[0], max)
#        for battery in batteries:
#            if max_comb < arrange(battery, max):
#                max_comb = arrange(battery, max)
#        return max_comb
#    else:
#        max_comb =0
#        for battery in batteries:
#            if max_comb < arrange(max, battery) and max[1] < battery[1]:
#                max_comb = arrange(max, battery)
#        return max_comb

def part1(batteries):
    remove_count = len(batteries) - 2
    result_stack=[]
    for battery in batteries:
        while remove_count > 0 and result_stack and result_stack[-1] < battery:
            result_stack.pop()
            remove_count -= 1
        result_stack.append(battery)
    result_stack = result_stack[:2]
    first = arrange(int(result_stack[0]), int(result_stack[1]))
    return first

def part2(batteries):
    remove_count = len(batteries) - 12
    result_stack=[]
    for battery in batteries:
        while remove_count > 0 and result_stack and result_stack[-1] < battery:
            result_stack.pop()
            remove_count -= 1
        result_stack.append(battery)
    result_stack = result_stack[:12]
    first = arrange(int(result_stack[0]), int(result_stack[1]))
    for result in result_stack[2:]:
        first = arrange(first, int(result))
    return first

if __name__ == "__main__":
    f = open("input3.txt", "r")
    sum=0
    for line in f:
        index =0
        banks = line.strip()
        batteries = []
        for c in banks:
            batteries.append(int(c))
            #index += 1
        #max, batteries = find_max_battery(batteries)
        #sum += find_second(batteries, max)
        sum +=part1(batteries)
        #sum +=part2(batteries)
        print(sum)

    f.close()