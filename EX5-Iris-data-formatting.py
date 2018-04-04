# Ger O'Mahony

# Exercise 5 Requirements:
#
# Write a Python script that reads the Iris data set in 
# and prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, 
# petal width, sepal length and sepal width, and these values should 
# have the decimal places aligned, with a space between the columns.

# read file in IrisData folder which is relative to this
# file in repo (./)
with open('./IrisData/iris.data.txt', 'r') as data_in:
    for line in data_in:
        print(line)

