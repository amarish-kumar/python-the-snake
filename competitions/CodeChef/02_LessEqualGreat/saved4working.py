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
                            min_p += 2
                        else:
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
                            print "Got"
                            p += 1
                        else:
                            print "Great"
                            pass
                        prev_code = 1
                    elif ch == "=":
                        print "Great2", min_p
                        prev_code = 2
                    else:
                        print "Great3", min_p
                        prev_code = 3
                else:
                    if ch == "<" :
                        p -= 1
                        if len(s) - 1 == index:
                            #pass      # <><   => 2
                            if p == 0:
                                min_p = min_p + 1
                        else:
                            if p == 0:
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
        counter += 1
    print min_p

if __name__ == "__main__":
    get_possible_p()


"""
1
<<<
1
4
"""

"""
1
<><
1
2
"""

"""
1
>>>==><
A 2
MIN 2
ZERO
MIN 3
G
ZEROED
Great2 4
Great3 4
5
"""

"""
1
<=>
1
Great3 2
2
"""

"""
1
<=<
1
Got
3
"""

"""
1
=====<><><><<>====>
1
Great2 1
Great2 1
Great2 1
Great2 1
Great
G
Great2 3
Great2 3
Great2 3
Great3 3
3
"""