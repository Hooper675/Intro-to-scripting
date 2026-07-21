#input a char
# input the heigh in integer form
# set triangle to a place holder
# for each row of the outer loop in triangle height from range 1 to triangle_heigh plus 1 ( move row by row and grid by grid)
        # for each column of the inner loop( move side to side) in range of row
                  #output triangle_char each row and column on each line.

triangle_char = input("Enter a character:\n")
triangle_height = int(input("Enter triangle height:\n"))
triangle = " "

for row in range(1, triangle_height +1):
    for col in range(row):
        print( f"{triangle_char}", end =" ")
    print()
