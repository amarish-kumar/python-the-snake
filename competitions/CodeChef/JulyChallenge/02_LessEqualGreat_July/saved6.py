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
            else:
                if prev_code == 1:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            print "Fish"    
                            p += 2 
                        else:
                            print "E1"
                            p += 1
                        prev_code = 1
                    elif ch == "=":
                        print "H2"
                        p += 1
                        prev_code = 2
                    else:   
                        print "R4"
                        p += 1 
                        prev_code = 3
                elif prev_code == 2:
                    if ch == "<" :
                        if len(s) - 1 == index:
                            print "Got"
                            p += 1
                        else:
                            pass
                        prev_code = 1
                    elif ch == "=":
                        print "Great2", min_p
                        prev_code = 2
                    else:
                        if len(s) - 1 == index:
                            print "Got"
                            p -= 1
                            if p == 0:
                                min_p += 1
                                # p += 1
                        else:
                            print "Great"
                        prev_code = 3
                else:
                    p -= 1
                    print "B", p 
                    if p == 0:
                        print "D"
                        min_p = min_p + 1
                        p += 1
                    if ch == "<":
                        prev_code = 1
                    elif ch == "=":
                        prev_code = 2

            if p > min_p:
                min_p = p
            print "MIN ", min_p
            index += 1  # index increment
            print ch, ": prevcode", prev_code,", p" ,p  
        counter += 1    # testcases increment
    print min_p

if __name__ == "__main__":
    get_possible_p()

"""
MacBook-Pro:Cf admin$ python Cf_Less_Equal_Great.py 
1
<<<<<<>=>=>=<=>=>=<<<<<<=>=<=>
MIN  1
< : prevcode 1 , p 1
E1
MIN  2
< : prevcode 1 , p 2
E1
MIN  3
< : prevcode 1 , p 3
E1
MIN  4
< : prevcode 1 , p 4
E1
MIN  5
< : prevcode 1 , p 5
E1
MIN  6
< : prevcode 1 , p 6
R4
MIN  7
> : prevcode 3 , p 7
B 6
MIN  7
= : prevcode 2 , p 6
Great
MIN  7
> : prevcode 3 , p 6
B 5
MIN  7
= : prevcode 2 , p 5
Great
MIN  7
> : prevcode 3 , p 5
B 4
MIN  7
= : prevcode 2 , p 4
MIN  7
< : prevcode 1 , p 4
H2
MIN  7
= : prevcode 2 , p 5
Great
MIN  7
> : prevcode 3 , p 5
B 4
MIN  7
= : prevcode 2 , p 4
Great
MIN  7
> : prevcode 3 , p 4
B 3
MIN  7
= : prevcode 2 , p 3
MIN  7
< : prevcode 1 , p 3
E1
MIN  7
< : prevcode 1 , p 4
E1
MIN  7
< : prevcode 1 , p 5
E1
MIN  7
< : prevcode 1 , p 6
E1
MIN  7
< : prevcode 1 , p 7
E1
MIN  8
< : prevcode 1 , p 8
H2
MIN  9
= : prevcode 2 , p 9
Great
MIN  9
> : prevcode 3 , p 9
B 8
MIN  9
= : prevcode 2 , p 8
MIN  9
< : prevcode 1 , p 8
H2
MIN  9
= : prevcode 2 , p 9
Got
MIN  9
> : prevcode 3 , p 8
9
MacBook-Pro:Cf admin$ python Cf_Less_Equal_Great.py 
1
>>>>><=<=>>>>>>=<=><<<<<<<<<<
A MIN  2
> : prevcode 3 , p 2
B 1
MIN  2
> : prevcode 3 , p 1
B 0
D
MIN  3
> : prevcode 3 , p 1
B 0
D
MIN  4
> : prevcode 3 , p 1
B 0
D
MIN  5
> : prevcode 3 , p 1
B 0
D
MIN  6
< : prevcode 1 , p 1
H2
MIN  6
= : prevcode 2 , p 2
MIN  6
< : prevcode 1 , p 2
H2
MIN  6
= : prevcode 2 , p 3
Great
MIN  6
> : prevcode 3 , p 3
B 2
MIN  6
> : prevcode 3 , p 2
B 1
MIN  6
> : prevcode 3 , p 1
B 0
D
MIN  7
> : prevcode 3 , p 1
B 0
D
MIN  8
> : prevcode 3 , p 1
B 0
D
MIN  9
> : prevcode 3 , p 1
B 0
D
MIN  10
= : prevcode 2 , p 1
MIN  10
< : prevcode 1 , p 1
H2
MIN  10
= : prevcode 2 , p 2
Great
MIN  10
> : prevcode 3 , p 2
B 1
MIN  10
< : prevcode 1 , p 1
E1
MIN  10
< : prevcode 1 , p 2
E1
MIN  10
< : prevcode 1 , p 3
E1
MIN  10
< : prevcode 1 , p 4
E1
MIN  10
< : prevcode 1 , p 5
E1
MIN  10
< : prevcode 1 , p 6
E1
MIN  10
< : prevcode 1 , p 7
E1
MIN  10
< : prevcode 1 , p 8
E1
MIN  10
< : prevcode 1 , p 9
Fish
MIN  11
< : prevcode 1 , p 11
11
MacBook-Pro:Cf admin$ python Cf_Less_Equal_Great.py 
1
<<<<<><><<><>==>=<=><<<<<=>>>
MIN  1
< : prevcode 1 , p 1
E1
MIN  2
< : prevcode 1 , p 2
E1
MIN  3
< : prevcode 1 , p 3
E1
MIN  4
< : prevcode 1 , p 4
E1
MIN  5
< : prevcode 1 , p 5
R4
MIN  6
> : prevcode 3 , p 6
B 5
MIN  6
< : prevcode 1 , p 5
R4
MIN  6
> : prevcode 3 , p 6
B 5
MIN  6
< : prevcode 1 , p 5
E1
MIN  6
< : prevcode 1 , p 6
R4
MIN  7
> : prevcode 3 , p 7
B 6
MIN  7
< : prevcode 1 , p 6
R4
MIN  7
> : prevcode 3 , p 7
B 6
MIN  7
= : prevcode 2 , p 6
Great2 7
MIN  7
= : prevcode 2 , p 6
Great
MIN  7
> : prevcode 3 , p 6
B 5
MIN  7
= : prevcode 2 , p 5
MIN  7
< : prevcode 1 , p 5
H2
MIN  7
= : prevcode 2 , p 6
Great
MIN  7
> : prevcode 3 , p 6
B 5
MIN  7
< : prevcode 1 , p 5
E1
MIN  7
< : prevcode 1 , p 6
E1
MIN  7
< : prevcode 1 , p 7
E1
MIN  8
< : prevcode 1 , p 8
E1
MIN  9
< : prevcode 1 , p 9
H2
MIN  10
= : prevcode 2 , p 10
Great
MIN  10
> : prevcode 3 , p 10
B 9
MIN  10
> : prevcode 3 , p 9
B 8
MIN  10
> : prevcode 3 , p 8
10
MacBook-Pro:Cf admin$ python Cf_Less_Equal_Great.py 
1
><>>><>>>><=><=>=>=<=>=<>>>><<><
A MIN  2
> : prevcode 3 , p 2
B 1
MIN  2
< : prevcode 1 , p 1
R4
MIN  2
> : prevcode 3 , p 2
B 1
MIN  2
> : prevcode 3 , p 1
B 0
D
MIN  3
> : prevcode 3 , p 1
B 0
D
MIN  4
< : prevcode 1 , p 1
R4
MIN  4
> : prevcode 3 , p 2
B 1
MIN  4
> : prevcode 3 , p 1
B 0
D
MIN  5
> : prevcode 3 , p 1
B 0
D
MIN  6
> : prevcode 3 , p 1
B 0
D
MIN  7
< : prevcode 1 , p 1
H2
MIN  7
= : prevcode 2 , p 2
Great
MIN  7
> : prevcode 3 , p 2
B 1
MIN  7
< : prevcode 1 , p 1
H2
MIN  7
= : prevcode 2 , p 2
Great
MIN  7
> : prevcode 3 , p 2
B 1
MIN  7
= : prevcode 2 , p 1
Great
MIN  7
> : prevcode 3 , p 1
B 0
D
MIN  8
= : prevcode 2 , p 1
MIN  8
< : prevcode 1 , p 1
H2
MIN  8
= : prevcode 2 , p 2
Great
MIN  8
> : prevcode 3 , p 2
B 1
MIN  8
= : prevcode 2 , p 1
MIN  8
< : prevcode 1 , p 1
R4
MIN  8
> : prevcode 3 , p 2
B 1
MIN  8
> : prevcode 3 , p 1
B 0
D
MIN  9
> : prevcode 3 , p 1
B 0
D
MIN  10
> : prevcode 3 , p 1
B 0
D
MIN  11
< : prevcode 1 , p 1
E1
MIN  11
< : prevcode 1 , p 2
R4
MIN  11
> : prevcode 3 , p 3
B 2
MIN  11
< : prevcode 1 , p 2
11
MacBook-Pro:Cf admin$ 

"""