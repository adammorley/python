#!/usr/bin/python3

print("hello world")
x = 1
if x == 1:
    print("x is 1")

myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring="don't worry be happy"
print(mystring)
one = 1
two = 2
three = one + two
print(three)
hello="hello"
world="world"
helloworld=hello+world
print(helloworld)
a,b=3,4
print(a,b)
one=1
two=2
hello="hello"
print(str(one)+str(two)+hello)

mystring = 'hello'
myfloat = float(10)
myint=20
print(mystring+str(myfloat)+str(myint))

mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for i in mylist:
    print(i)
try:
    print(mylist[10])
except IndexError:
    print('oopsie daisy!')

number = []
string = []
names = ['john', 'eric', 'jessica']
secondname = names[1]
print(number)
print(string)
print('second name is: %s' % secondname)

number = 1+2+3/4.0
print(number)

remainder = 11%3
print(remainder)

squared = 7**2
cubed = 2**3
print(squared)
print(cubed)

helloworld = 'hello' + ' ' + world
print(helloworld)
lotsH = 'hello' * 10
print(lotsH)
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
print([1,2,3]*4)

x = 5
y = 6
x_list = [x] * 10
y_list = [y] * 10
both = x_list + y_list
print(both)

name = 'bobo'
print('hi {}'.format(name))

fruits = ['apple', 'orange']
fruitsC = ''
for f in fruits:
    fruitsC += f + ' '
print(fruitsC)

print('my fruits: {}'.format(fruits))

bobo = (1,2,3)
mobo = [4,5,6]
print(bobo)
print(mobo)

x = True
y = False
if x or y:
    print('at least one is true')
if x and y:
    print('both are true')
else:
    print('both are not true')
if not y:
    print('y is not true')

data = ('john', 'doe', 53.44)
format_string = 'hello'
print('{}, {} {}.  Your balance is ${}'.format(format_string, data[0], data[1], data[2]))

try:
    data[0] = 'booboo'
except TypeError:
    print('no changing tuples')

string = 'foo' ' bobo'
print(string)
print(len(string))

astring='hello'
print(astring.index('o'))
thing = []
for i in range(0,5):
    thing.append(i)
i = 1
e = 2
print('slice of the list: {} from {} to {} is {}'.format(thing, i, e, thing[i:e]))
print('min value {} of list: {}'.format(min(thing), thing))

astring = 'hello world'
print(astring.count('l'))
print('stuff {}'.format(astring[1:7:2]))
print('{} reversed is {}'.format(astring, astring[::-1]))
print(astring.upper())
print(astring.lower())

x = 2
print(x == 2)
print(x == 3)

name='john'
age=23
if name == 'john' and age==23:
    print('your name is john and you are 23')

name = 'john'
if name in ['john', 'rick']:
    print('your name is either john or rick')

statement = False
another = True
if statement is True:
    print('the statement is true')
if another is True:
    print('the other statement is true')

print('new')
x = [1,2,3]
y = [1,2,3]
print(x==y)
print(x is y)
if []:
    print('list')

primes = [2,3,5,7,11]
for prime in primes:
    print(prime)

print('foo')
for x in range(0,5):
    print(x)
for x in range(3):
    print(x)
for x in range(3, 8, 2):
    print(x)

print('foo')
print('')

count = 0
while count < 5:
    print(count)
    count += 1
print('')

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print('')

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
print('')

count=0
while(count<5):
    print(count)
    count+=1
else:
    print("count value reached {}".format(count))

for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print('this is not printed because of break')

def myfunc():
    print('in a function')

myfunc()

def myfuncArgs(name, age):
    print('name is {} and age is {}'.format(name, age))

myfuncArgs(name, age)

def sumNums(a, b):
    return a+b

print(sumNums(1,2))

class MyClass:
    variable = "blah"
    def function(self):
        print('this is inside class')
        print('variable is {}'.format(self.variable))

o = MyClass()
o.function()
print(o.variable)
p = MyClass()
p.variable = 'foo'
p.function()

phonebook = {}
phonebook['john'] = 945
phonebook['bob'] = 323
phonebook['cat'] = 765
print(phonebook)

phonebook2 = {
    'john': 453,
    'jack': 237,
    'jill': 123,
}
print(phonebook2)
print('')

for name, number in phonebook.items():
    print('phone number of {} is {}'.format(name, number))

del phonebook['john']
print(phonebook)

phonebook = dict()
phonebook['bill'] = 333
print(phonebook)

import requests

r = requests.get('http://google.com')
print(r.status_code)
print(r.headers['content-type'])

a = set(['bob', 'sue', 'sally'])
b = set(['joe', 'sue'])
print(a.intersection(b))

print(a.symmetric_difference(b))
print(a.difference(b))
