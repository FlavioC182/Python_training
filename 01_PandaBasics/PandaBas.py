# In this lecture we are going to cover the basics of Pandas.

# Pandas is an external library you can download from http://pandas.pydata.org/
# and which allows you to perform efficient data analysis

# After having installed pandas, we need to import it

import pandas

# Pandas introduces DataFrames: special objects which hold data

# DataFrames hold tables, so we need to insert a list of lists (rows) into it:
df1 = pandas.DataFrame([[2,4,6], [10,20,30]])
df2 = pandas.DataFrame([[40,32,20], [200,410,40]])
print (df1)
print
print

# As you can see from the output, we get:
# First row: 2 4 6
# Second row: 10 20 30

# We can specify the names of the columns:

df1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns = ["Price", "Age", "Value"])

print (df1)
print
print

# The same stands for indexes (rows):

df1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns = ["Price", "Age", "Value"], index = ["First", "Second"])

print (df1)
print
print

# The index name is not so used, because datasets can have millions of lines
# and giving name to each line is not possible.

# Now we create a DataFrame of dictionaries
df2 = pandas.DataFrame ([{"Name":"John", "Surname":"Smith"},{"Name":"Jack", "Surname":"Marshal"}])

print (df2)
print
print

# In real life you won't create DataFrames this way, because you will be going
# to create them from existing files (csv, txt etc...)

# Now we are going to do some basics operations on DataFrames
# For example, let's assume we want to extract the average of the values present
# in the df1
#A VALUE FOR EACH COLUMN

df3 = df1.mean()

print (df3)
print
print
# The type of these structure is a Pandas Series

# If we want the mean of the entire DataFrame:
#A SINGLE TOTAL VALUE
df3 = df1.mean().mean()

print (df3)
print
print
# With pandas we can access to single columns too:

print (df1.Price)
print
print (df1.Age)
print
print
# The type of these structure is a Pandas Series

# Other methods:
# For each column it is given the max or min value.
print (df1.max())
print
print (df1.min())
