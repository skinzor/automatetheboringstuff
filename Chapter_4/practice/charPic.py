# Practice: Character Picture Grid
#
#
# I was stuck with this because it was printing:
#
#       ......
#       .OO...
#       OOOO..
#       OOOOO.
#       .OOOOO
#       OOOOO.
#       OOOO..
#       .OO...
#       ......
#
# My code for the above print is here: https://gist.github.com/skinzor/395de1cb0f5b3e2ae781464e81b05af2#file-charpic-py
#
# After checking the solutions of other people on stackoverflow,
# it looks like i just had to swap the for loops. I mean, firstly
# the for y and then the for x inside the for y, not vice versa
# (like i was doing). As of typing now, i still don't know why
# the y (cols) for loop has to be the first one.
#
# Also, it was wrong ; unnecessary to print(grid[x][y] in y (x)
# loop too.


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rows = len(grid)
cols = len(grid[0])

for y in range(cols):
    print()
    for x in range(rows):
        print(grid[x][y], end='')
