#coding: UTF-8
#1-100までの数列
#3と5で割れる->FizzBuzz
#3の倍数or3がつく ->Fizz
#5 ->Buzz



for i in range(1,101):
    if i%15 == 0:
        print 'FizzBuzz'",",
    elif i%5 == 0 or "5" in str(i):
        print 'Buzz'",",
	
    elif i%3 == 0 or "3" in str(i):
        print 'Fizz'",",
    else:
        print i,",",
		
		
str(i).rstrip(',')


#最後の,を消したかったけど上手くいきませんでした