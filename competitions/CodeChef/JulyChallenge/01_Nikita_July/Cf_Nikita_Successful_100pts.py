#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	{
		"problem_link": "https://www.codechef.com/JULY17/problems/NITIKA",
		"coded_on": "7 July 2017",
		"coded_by": "Rihsikesh Agrawani",
	}
"""

import re


def get_short_name():
    n = int(raw_input().strip())

    i = 1
    while i <= n:
        name = raw_input().strip()
        parts = re.compile("\s+").split(name)
        l = len(parts)

        if l == 1:
            print name.title()
        elif l == 2:
            print parts[0][0].upper() + '.' + ' ' + parts[1].title()
        elif l == 3:
            print parts[0][0].upper() + '.' + ' ' + parts[1][0].upper() \
                + '.' + ' ' + parts[2].title()
        else:

            def short_name(name):
                return name[0].upper() + '.'

            print ' '.join(map(short_name, parts[:l - 1])) + ' ' \
                + parts[l - 1].title()

        i += 1


if __name__ == '__main__':
    get_short_name()
		
# 10
# rishikesh 
# Rishikesh
# rishikesh agrawani
# R. Agrawani
# sandeep kumar eswar
# S. K. Eswar
# shwetabh kumar soni chhattisgarh
# S. K. S. Chhattisgarh
# mukesh   kumar    jakHAR
# M. K. Jakhar
# tiger     anderson belly
# T. A. Belly
# FinaLL Offline trenD
# F. O. Trend
# gablin d bishell
# G. D. Bishell
# finesh don     FihKD
# F. D. Fihkd
# Ohlin Jell     Shfgfggf
# O. J. Shfgfggf