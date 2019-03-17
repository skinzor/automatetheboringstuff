# Practice: Comma code
#
# I know that this may not be the best code, but i'm noob and it works xD
# Also, the practice didn't mention to add any debugging mode, but i've
# used prints functions to understand how it works / what i have to do
# and since they helped me, i ended up adding the debugging mode xD


def spam(value):
    debug = 0 # debugging mode
    nItems = len(value) # get the number of the items which the list value has
    result = ('')
    for i in range(nItems):
        result = result + value[i]

        if debug == 1:
            print(result)
            print(value.index(value[i]))

        # if it's the last item of the list, then add ', and ' before it, else add ;, ;
        if value.index(value[i]) == nItems - 2:
            result = result + ', and '
        elif not value.index(value[i]) == nItems - 1:
            result = result + ', '
    print('Result: ' + result)
    return result



list = ['apples', 'bananas', 'tofu', 'cats']
spam(list)
