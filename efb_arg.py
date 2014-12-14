#coding: UTF-8


import sys 
argv = sys.argv

x = int(argv[1]) 
y = int(argv[2])

for i in range(1,101):
    if i%(x*y) == 0:
        print 'FizzBuzz'",",
    elif i%y == 0 or "y" in str(i):
        print 'Buzz'",",
	
    elif i%x == 0 or "x" in str(i):
        print 'Fizz'",",
    else:
        print i,",",
 
 
 