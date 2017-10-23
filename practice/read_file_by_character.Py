"""
	{
		"aimOfScript": "Reading file character by character",
		"codedOn": "23 Oct 2017, Mon",
		"codedBy": "Rishikesh Agrawani"
	}
"""

with open("intro.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			break
		print c, ord(c)

"""
MacBook-Pro-2:practice admin$ python read_file_by_character.Py 
M 77
y 121
  32
n 110
a 97
m 109
e 101
  32
i 105
s 115
  32
R 82
i 105
s 115
h 104
i 105
k 107
e 101
s 115
h 104
  32
A 65
g 103
r 114
a 97
w 119
a 97
n 110
i 105
. 46

10

10
I 73
  32
a 97
m 109
  32
2 50
5 53
  32
y 121
e 101
a 97
r 114
s 115
  32
o 111
l 108
d 100
. 46

10
	9
1 49
  32
t 116
a 97
b 98
  32
b 98
e 101
f 102
o 111
r 114
e 101
. 46

10
	9
	9
2 50
  32
t 116
a 97
b 98
s 115
  32
b 98
e 101
f 102
o 111
r 114
e 101
. 46

10
1 49
  32
n 110
e 101
w 119
  32
l 108
i 105
n 110
e 101
  32
a 97
f 102
t 116
e 101
r 114
  32
t 116
h 104
i 105
s 115
  32
l 108
i 105
n 110
e 101
. 46

10

10
"""
