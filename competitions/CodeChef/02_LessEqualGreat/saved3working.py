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
                        print "A"
                        p = 2
                    else:
                        print "B"
                        # prev_code = 1
                        p = 1
                    prev_code = 1
                elif ch == "=":
                    print "C"
                    prev_code = 2
                    p = 1
                else:
                    print "D"
                    prev_code = 3
                    p = 2
                # p = prev_code
                if p > min_p:
                    print "E"
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
                        print "F"
                        prev_code = 2
                        p += 1
                    else:
                        print "G"
                        p += 1
                        prev_code = 3
                elif prev_code == 2:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            print "H"
                            min_p += 1
                        else:
                            print "I"
                            # p += 1
                            pass
                        prev_code = 1
                    elif ch == "=":
                        print "J"
                        # p += 1
                        prev_code = 2
                    else:
                        # p -= 1
                        # if p == 0:
                        #     print "fish"
                        #     p += 1
                        #     print "==> ", p
                        print "K"
                        prev_code = 3
                else:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            print "L"
                            p += 1
                            # pass
                        else:
                            p -= 1
                            print "M"
                            if p == 0:
                                print "N"
                                p += 1
                        prev_code = 1
                    elif ch == "=":
                        p -= 1
                        print "O"
                        if p == 0:
                            print "P"
                            p += 1
                        prev_code = 2
                    else:
                        p -= 1
                        print "Q"
                        if p == 0:
                            print "R"
                            p += 1
                        prev_code = 3

                if p > min_p:
                    print "S"
                    min_p = p
            index += 1
        # Incrementing counter    
        counter += 1
    print min_p

if __name__ == "__main__":
    get_possible_p()
