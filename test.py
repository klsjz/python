#!/usr/bin/python
print "hello.python";
i=5;
print i;
s='hey, man'
print s;
print'the number need you to guess is 23'
number=23;
running=True;
while running:
	guess=int(raw_input('please input a integer:'))
	if guess==number:
		print'congratulations,you guess it.'
		running=False;
	else:
		print'oh shit.'
else:
	print'Done';
while True:
	s=raw_input('enter something:')
	if s=='quit':
		break;
	print'the length is',len(s)	
print 'over'
