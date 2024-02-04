#Function for Question 1
def sum_checker():
    list = [2, 7, 4, 1, 3, 6]
    length=len(list)
    count = 0
    #loop to find the pairs whose sum is equal to 10
    for i in range(length):
        for j in range(i+1,length):
            #condition checking if sum is equal to 10 and incrementing the count
            if list[i]+list[j] == 10:
                count += 1
    print("The no. of pairs whose sum is equal to 10 are: ",count)
#Function for Question 2
def range_determiner():
    length=int(input("Enter the no. of elements in list"))#Accepting length of the list
    #condition for checking if range determination is possible
    if length<3:
        print("Range determination not possible")
    else:
        list=[]
        minimum=float('inf')#variable storing the greatest value
        maximum=float('-inf')#variable storing the least value
        #loop for accepting elements for the list
        for _ in range(length):
            a=int(input("Enter a no."))
            list.append(a)
        #loop for finding the greatest and least value
        for i in list:
            #condition checking if current value greater than maximum and updating
            if i>maximum:
                maximum=i
            # condition checking if current value lesser than minimum and updating
            if i<minimum:
                minimum=i
        difference=maximum-minimum#variable storing the range
        print("The range is ",difference)

#Function for Question 3
def matrix_power():
    MatrixA = []
    size = int(input("Enter the size of the matrix"))#Accepting size of matrix
    #loop for accepting elements of the matrix
    for i in range(size):
        row_list = []#stores values of each row
        for j in range(size):
            number = int(input(f"Enter number of row {i} column {j}"))
            row_list.append(number)
        MatrixA.append(row_list)

    power = int(input("Enter the power to which you want the matrix: "))#Accepting the power to which the matrix is wanted
    #Checking if power is a positive integer
    if power > 0:
        for _ in range(power - 1):
            MatrixA = matrix_multiply(MatrixA, size)#loop which multiplies matrix by itself again and again and stores the matrix
        #loop for printing final matrix
        print("The final matrix is:")
        for i in range(size):
            for j in range(size):
                print(MatrixA[i][j], end=" ")
            print("\n")
    else:
        print("Power is not a positive integer")

#function for matrix multiplication
def matrix_multiply(matA, size):
    matB = [row.copy() for row in matA]#copying matrix row by row
    result = [[0 for _ in range(size)] for _ in range(size)]#initializing a matrix of same size with all values set to 0
    #loop for matrix multiplication
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matA[i][k] * matB[k][j]

    return result#sending the multiplied matrix back

#Function for Question 4
def highest_occurence():
    character_count={}#initializing dictionary to store new letters and their count
    sentence=input("Enter the sentence")#accepting the input string
    #looping through all characters in sentence
    for i in sentence:
        #checking if character is an alphabet
        if i.isalpha():
            """checking if the alphabet is already there in dictionary,
             if it is increases count by 1, 
             else adds it to dictionary and sets it's value to 1"""
            if i in character_count:
                character_count[i]+=1
            else:
                character_count[i]=1

    max=float('-inf')
    maxchar=''
    #loop for finding character with highest count
    for i in character_count:
        if character_count[i]>max:
            max=character_count[i]
            maxchar=i
        elif character_count[i]==max:
            maxchar+=", "+i

    print("The highest occuring character is ",maxchar," and the no. of times it occured is ",max)
#calling all functions
sum_checker()#Q1
range_determiner()#Q2
matrix_power()#Q3
highest_occurence()#Q4
