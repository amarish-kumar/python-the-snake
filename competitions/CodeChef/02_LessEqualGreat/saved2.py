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
                print "oh"
                if ch == "<":
                    if len(s) - 1 == index:
                        p = 2
                    else:
                        prev_code = 1
                        p = 1
                elif ch == "=":
                    prev_code = 2
                    p = 1
                else:
                    prev_code = 3
                    p = 2
                # p = prev_code
                if p > min_p:
                    min_p = p
            else:
                if prev_code == 1:
                    print "go1"
                    if ch == "<" :
                        if len(s) - 1 == index:
                            print "going"
                            min_p += 2
                        else:
                            print "going2"
                            p += 1
                            prev_code = 1
                    elif ch == "=":
                        prev_code = 2
                        p += 1
                    else:
                        p += 1
                        prev_code = 3
                elif prev_code == 2:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            min_p += 1
                        else:
                            pass
                    elif ch == "=":
                        prev_code = 2
                    else:
                        min_p -= 1
                        prev_code = 3
                else:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            # min_p += 2
                            pass
                        else:
                            p -= 1
                            prev_code = 1
                    elif ch == "=":
                        prev_code = 2
                    else:
                        p -= 1
                        prev_code = 3

                if p > min_p:
                    min_p = p
            index += 1
        # Incrementing counter    
        counter += 1
    print min_p

if __name__ == "__main__":
    get_possible_p()