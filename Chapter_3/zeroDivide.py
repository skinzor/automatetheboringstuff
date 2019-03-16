def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))




# 21.0
# 3.5
# Traceback (most recent call last):
#   File "C:/zeroDivide.py", line 6, in <module>
#     print(spam(0))
#   File "C:/zeroDivide.py", line 2, in spam
#     return 42 / divideBy
# ZeroDivisionError: division by zero



# 21.0
# 3.5
# Error: Invalid argument.
# None
# 42.0
