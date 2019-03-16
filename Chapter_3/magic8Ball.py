import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)


# Note that since you can pass return values as an argument
# to another function call, you could shorten the last three lines
# to a single equivalent line:

# print(getAnswer(random.randint(1, 9)))
# OR print(getAnswer(r))

# Remember, expressions are composed of values and operators.
# A function call can be used in an expression because it
# evaluates to its return value.
