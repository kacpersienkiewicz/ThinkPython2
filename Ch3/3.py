'''
Exercise 3.3. Note: This exercise should be done using only the statements and other features we
have learned so far.
1. Write a function that draws a grid like the following:

Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. The output from the next print
statement would begin on the next line.
2. Write a function that draws a similar grid with four rows and four columns.
'''

def simple_2_by_2_grid():
    # This implementation is a really simply way to create the 2 by 2 grid without any shortcuts
    print('+', '- ' * 4, '+', '- ' * 4, '+')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('+', '- ' * 4, '+', '- ' * 4, '+')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|')
    print('+', '- ' * 4, '+', '- ' * 4, '+')

def concatenation_2_by_2_grid():
    # This implementation tries to use concatenation and set strings to make it easier. It classifies the lines into two types: outside (uses + and -), and inner (| and spaces)
    outside_line = '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+\n'
    inner_line = '| ' + '  ' * 4 + '| ' +  '  ' * 4 + '|\n'
    print(outside_line + inner_line * 4 + outside_line + inner_line * 4 + outside_line)

def simple_4_by_4_grid():
    # This implementation is a really simply way to create the 4 by 4 grid without any shortcuts
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('|', '  ' * 4,'|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')


def m_by_n_grid(rows: int, columns: int):
    # Creates an n x m grid made up of two types of lines: outer (contains +. -) and inner (| and spaces)
    # It also uses the illegal for loop, which wasn't introduced at this point in the book
    
    repeated_outer_segment = '- ' * 4 + '+ '
    outer_line = '+ ' + repeated_outer_segment * columns
    repeated_inner_segment =  '  ' * 4 + '| '
    inner_line = '| ' + repeated_inner_segment * columns + '\n'

    for i in range(rows):
        print(outer_line)
        print(inner_line * 4, end='')
    
    print(outer_line)

simple_2_by_2_grid()
concatenation_2_by_2_grid()
simple_4_by_4_grid()
m_by_n_grid(6, 5)
