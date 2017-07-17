# Chef Code Probelm - CHEFSIGN 
def get_possible_p():
    n = int(raw_input().strip())

    counter = 1
    while counter <= n:
        s = raw_input().strip()
        prev_code = -1
        p = 0
        min_p = 0

        index = 0 
        for ch in s:
            if prev_code == -1:
                if ch == "<":
                    if len(s) - 1 == index:
                        p = 2
                    else:
                        p = 1
                    prev_code = 1
                elif ch == "=":
                    prev_code = 2
                    p = 1
                else:
                    prev_code = 3
                    p = 2
            else:
                if prev_code == 1:
                    if ch == "<" :
                        if len(s) - 1 == index: 
                            p += 2 
                        else:
                            p += 1
                        prev_code = 1
                    elif ch == "=":
                        p += 1
                        prev_code = 2
                    else:   
                        p += 1 
                        prev_code = 3
                elif prev_code == 2:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            p += 1
                        else:
                            pass
                        prev_code = 1
                    elif ch == "=":
                        prev_code = 2
                    else:
                        if len(s) - 1 == index:
                            p -= 1
                            if p == 0:
                                min_p += 1
                        else:
                            pass
                        prev_code = 3
                else:     
                    if ch == "<":
                        p -= 1
                        if p == 0:
                            p += 1
                            min_p += 1
                        prev_code = 1
                    elif ch == "=":
                        p -= 1
                        if p == 0:
                            p += 1
                            min_p += 1
                        prev_code = 2
                    else:
                        if index == len(s) - 1:
                            min_p += 2
                        else:
                            p -= 1
                            if p == 0:
                                p += 1
                                min_p += 1
                        prev_code = 3

            if p > min_p:
                min_p = p
            # print "MinP ", min_p
            index += 1  # index increment
        counter += 1    # testcases increment
        print min_p

if __name__ == "__main__":
    get_possible_p()

