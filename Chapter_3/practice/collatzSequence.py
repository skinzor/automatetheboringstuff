# Practice: The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 1 == 0:
        result = 3 * number + 1
        print(result)
        return result


print('Please type a number:')

try:
    n = int(input())
    while n != 1:
        n = collatz(n)

except ValueError:
    print('You must type an integer. Letters are not allowed...')
