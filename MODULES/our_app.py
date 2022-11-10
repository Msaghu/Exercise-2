#Using modules
#1
import module

print(module.name)

print(module.age)

module.hello()

#2
from module import *

print(name)

print(age)

hello()

#3: Insert modules as aliases
import module as superman

print(superman.name)
print(superman.age)

superman.hello()

#4: Selective import
from module import age, hello, name

print(name)
print(age)
hello()

# 5:
from module import hello as x

x()
