# This program adds up all the numbers from 0 to 100 and prints the total

# As another for loop example, consider this story about the
# mathematician Karl Friedrich Gauss. When Gauss was a boy,
# a teacher wanted to give the class some busywork. The teacher
# told them to add up all the numbers from 0 to 100. Young Gauss
# came up with a clever trick to figure out the answer in a few
# seconds, but you can write a Python program with a for loop to
# do this calculation for you.
#
#                                   -automatetheboringstuff



total = 0
for num in range(101):
    total = total + num
print(total)




# Young Gauss figured out that there were 50 pairs of numbers
# that added up to 101: 1 + 100, 2 + 99, 3 + 98, 4 + 97, and
# so on, until 50 + 51. Since 50 × 101 is 5,050, the sum of
# all the numbers from 0 to 100 is 5,050. Clever kid!)
#
#                                   -automatetheboringstuff
