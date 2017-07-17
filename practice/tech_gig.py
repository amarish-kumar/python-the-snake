def alternateSorting(input1):
    sorted_list = sorted(input1)
    length = len(input1)
    new_list = []
    i = 0
    j = length - 1
    while i < (length/2):
        new_list.append(sorted_list[j])
        new_list.append(sorted_list[i])
        j -= 1
        i += 1
        
    if length%2 != 0:
        new_list.append(sorted_list[i])  
        
    return new_list


ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = alternateSorting(ip1)
for output_cur in output:
    print( str(output_cur))
