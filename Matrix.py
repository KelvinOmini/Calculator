# Matrix calculator:
import numpy as np
class Matrix: # Define a Matrix class to handle matrix operations.
    
    def __init__(self, matrix1, matrix2, operation):  # Initialize the Matrix object with two matrices and an operation.
        self.matrix1 = matrix1 # store the first matrix
        self.matrix2 = matrix2 # store the second matrix
        self.operation = operation # Store the specific operation
    def compute(self): # A function to check for valid operations and calling corresponding methods 
        if self.operation == "+":
            result = self.add()
        elif self.operation == "-":
            result = self.subtract()
        elif self.operation == "*":
            result = self.multiply()
        elif self.operation == "/":
            result = self.divide()
        else:
            raise ValueError("Unsupported operation. Valid operations are '+', '-', '*', '/'.")

        return result

    def add(self):
        if len(self.matrix1) != len(self.matrix2) or len(self.matrix1[0]) != len(self.matrix2[0]): # A guardian to check if the matrix have compatible dimentions for addition.
            raise ValueError("Matrices must have the same dimensions for addition.") 
        
        result = [] # Initialize an empty list to store the result matrix
        
        for i in range(len(self.matrix1)): # Iterate over the rows of the first matrix (self.matrix1).
            row = [] # Initialize an empty list to store a row result matrix 
            for j in range(len(self.matrix1[0])): # Iterate over the columns of the first matrix (self.matrix1[0]).
                row.append(self.matrix1[i][j] + self.matrix2[i][j]) # Add the elements from both matrices.
            result.append(row) # append to the result row.
        
        return result

    def subtract(self):
        if len(self.matrix1) != len(self.matrix2) or len(self.matrix1[0]) != len(self.matrix2[0]):  # A guardian to check if the matrix have compatible dimentions for subtraction.
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result = []  # Initialize an empty list to store the result matrix
        
        for i in range(len(self.matrix1)): # Iterate over the rows of the first matrix (self.matrix1).
            row = [] # Initialize an empty list to store a row result matrix 
            for j in range(len(self.matrix1[0])): # Iterate over the columns of the first matrix (self.matrix1[0]).
                row.append(self.matrix1[i][j] - self.matrix2[i][j]) # subtract the elements from both matrices.
            result.append(row) # append to the result row
        
        return result

    def multiply(self): # A function to perform matrix multiplication
        if len(self.matrix1[0]) != len(self.matrix2):  # A guardian to check if the matrix have compatible dimentions for multiplication.
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        
        result = [] # Initialize an empty list to store the result matrix 
        
        for i in range(len(self.matrix1)): # Iterate over the rows of the first matrix (self.matrix1).
            row = [] # Initialize an empty list to store a row result matrix 
            for j in range(len(self.matrix2[0])): # Iterate over the columns of the first matrix (self.matrix1[0]).
                product = sum(self.matrix1[i][k] * self.matrix2[k][j] for k in range(len(self.matrix2))) # Calculate the dot product of corresponding rows and columns of the two matrices.
                row.append(product) # Add the calculated product to the current row of the result matrix.
            result.append(row) # Append to the result row 
        
        return result

    def divide(self): # A funnction that performs matrix division by a scalar
        if len(self.matrix1[0]) != len(self.matrix2):  # A guardian to check if the matrix have compatible dimentions for multiplication.
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for division.")
        
        # Calculate the inverse of matrix2
        matrix2_inv = np.linalg.inv(self.matrix2)
        # Perform matrix division by multiplying matrix1 with matrix2_inv
        result = np.dot(self.matrix1, matrix2_inv)        
        return result

    def __str__(self): # Define a string representation method for the Matrix object.
        '''For every element in the row of self.matrix1 convert it to a string using the .map() seperated by a space character using the .join() to create a space-separated element,
            and finally using a new line character '\n'  to combine all the rows of the matrix using .
            join() into a new string with each row separated by a new line. '''
        matrix1_string = '\n'.join([' '.join(map(str, row)) for row in self.matrix1]) # A variable that convert the first matrix (self.matrix2) to a formatted string representation.
        matrix2_string = '\n'.join([' '.join(map(str, row)) for row in self.matrix2]) # A variable that convert the second matrix (self.matrix2) to a formatted string representation.
        result_matrix = self.compute() # A variable that Compute the result matrix based on the specified operation.
        result_string = '\n'.join([' '.join(map(lambda x: str(round(x,2)), row)) for row in result_matrix]) 
        # Using a Lamda function to process each element of the function that rounds the elements x to 2 decimal places using round(),
        # then converts it to a string and joins the processed elements with a space charaacter sperator

    # Combine all representations into a final formatted string, including the operation.
        return f"[{matrix1_string}] \n{self.operation} \n[{matrix2_string}]\n = \n[{result_string}]"



# Create the first matrix:
matrix1 = []
Range = int(input("What is the dimention of this matix? "))
for i in range(Range):
    row = []  # Create an empty row for each iteration
    for j in range(Range):
        value = int(input(f'Enter a value for position ({i+1}, {j+1}): '))
        row.append(value)  # Append the value to the current row
    matrix1.append(row)  # Append the row to the matrix
print(f"Your {Range} by {Range} matrix:")
for row in matrix1:
    print(row)

# To do what you said, after creating an empty list to store the first matrix,
# I made a varible calld 'Range' to get the size of the dimention of the first matrix as an integer from the user,
# then made a for loop to iterate my variable that create each row of the first matrix,
# created a row variable to store the iteration
# now nested another loop for the columns still iterating it with my variablle 'Range'
# but to get positions from the user I created a value to promt the user to enter positions of rows and column starting from 1.
# Repeted the same code for the second matrix. 
# Now under a while loop that is True, my matirix calculater gets an operator from the user and check for default operators such as ( +-*/), if true 
# create an instance else print an invalid operator statement

# Create the second matrix:
matrix2 = []
Range = int(input("Enter type of marix2: "))
for i in range(Range):
    row = []  # Create an empty row for each iteration
    for j in range(Range):
        value = int(input(f'Enter a value for position ({i+1}, {j+1}): '))
        row.append(value)  # Append the value to the current row
    matrix2.append(row)  # Append the row to the matrix
print(f"Your {Range} by {Range} matrix:")
for row in matrix2:
    print(row)


while True:
    operation = input('Enter an operation: ')  # Change this to the desired operation: "+", "-", "*", "/"
    if operation in ("+", "-", "*", "/"):
        Result = Matrix(matrix1, matrix2, operation)
        print(Result)
    else: print('"Invalid operation. Please enter '+', '-', '*', or '/'."')
    choice = input("Would you like to continue, yes/no? ")
    if choice == 'yes': continue
    elif choice == 'no': break
    else: print('Invalid responds')
    break

