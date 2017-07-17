def nochange_bits(input1, input2, input3):
    length = len(input1)
    saved = input1
    if ((input2 < 0) or (input2 > length)) or (
            (input2 < 0) or (input2 > length)):
        return -1

    for inp in [input2, input3]:
        for index in xrange(inp - 1, length, inp):
            # print index, input1[index]
            if input1[index] == "0":
                input1 = input1[0:index] + "1" + input1[index + 1:]
            else:
                input1 = input1[0:index] + "0" + input1[index + 1:]
        # print input1
    count = 0
    for item in zip(saved, input1):
        if item[0] == item[1]:
            count += 1
    return count

try:
    ip1 = raw_input()
except BaseException:
    ip1 = None
ip2 = int(raw_input())
ip3 = int(raw_input())
output = nochange_bits(ip1, ip2, ip3)
print(str(output))

# 10110101101
# 3
# 4
# 2 1
# 5 1
# 8 1
# 10010001001
# 3 1
# 7 1
# 10000000001
# 5