def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()



#  Traceback (most recent call last):
#   File "C:/test3784.py", line 6, in <module>
#     spam()
#   File "C:/test3784.py", line 2, in spam
#     print(eggs) # ERROR!
# UnboundLocalError: local variable 'eggs' referenced before assignment


# This error happens because Python sees that there is an
# assignment statement for eggs in the spam() function
# and therefore considers eggs to be local. But because
# print(eggs) is executed before eggs is assigned anything,
# the local variable eggs doesn’t exist. Python will not fall
# back to using the global eggs variable.
