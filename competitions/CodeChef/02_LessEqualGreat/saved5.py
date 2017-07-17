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
                    print "A",
                    prev_code = 3
                    p = 2
                if p > min_p:
                    min_p = p
                print min_p
            else:
                if prev_code == 1:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            # min_p += 2
                            # p += 2. 
                            print "Fish"    #Corrected (from Sandeep's test case)
                            p += 2 #Fixed issuse based on test case 
                        else:
                            print "E1"
                            p += 1
                        prev_code = 1
                    elif ch == "=":
                        print "gone"
                        prev_code = 2
                        p += 1
                    else:
                        print "H2"
                        p += 1
                        prev_code = 3
                elif prev_code == 2:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            print "Got"
                            p += 1
                            min_p += 1
                        # else:
                        #     print "Great"
                        #     p += 1
                        prev_code = 1
                    elif ch == "=":
                        print "Great2", min_p
                        prev_code = 2
                    else:
                        # p -= 1
                        # if p == 0:
                        #         p += 1
                        #         min_p = min_p + 1
                        # print "Great3", min_p
                        # prev_code = 3
                        if len(s) - 1 == index:
                            print "Got"
                            p -= 1
                            if p == 0:
                                min_p += 1
                        else:
                            print "Great"
                        prev_code = 3
                else:
                    if ch == "<" :
                        p -= 1
                        print "B", p 
                        if len(s) - 1 == index:
                            #pass      # <><   => 2
                            if p == 0:
                                p += 1
                                min_p = min_p + 1
                        else:
                            print "C"
                            if p == 0:
                                print "D"
                                min_p = min_p + 1
                                p += 1

                        prev_code = 1
                    elif ch == "=":
                        print "G"
                        p -= 1
                        if p == 0:
                            print "ZEROED"
                            min_p = min_p + 1
                            p += 1
                        prev_code = 2
                    else:
                        # print " >"
                        p -= 1
                        if p == 0:
                            print "ZERO"
                            min_p += 1
                            p += 1
                        prev_code = 3
                        print "MIN",min_p
                if p > min_p:
                    min_p = p
            index += 1 
            print ch, ": prevcode", prev_code,", p" ,p  
        counter += 1
    print min_p

if __name__ == "__main__":
    get_possible_p()

