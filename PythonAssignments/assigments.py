# Ex. 1 Random number
# Create a program that creates a list of 10 random numbers and sums all the numbers.  The result is printed to the console.  The numbers in the list range from 0 - 100.  The program must use an f-string to display the output.

# Example list: `[1, 34, 2, 33, 45, 67, 24, 87, 32, 38]`

# Example Output:
# ```
# The sum is: 363
import random
def sum_num():
    sum_list = []
    sum = 0
    for i in range(0,10):
        # print(i)
        num = random.randint(0,100)
        sum_list.append(num)
        sum += num
    print(f'Example list: {sum_list}')
    print(f'The sum is: {sum}')

# if __name__ == "__main__":
#     sum_num()

# Ex. 2 Python in a Box
# Create a program that uses the `input()` function to obtain the width, height and length of a box.  The program computes the volume of the box (width * height * length) and writes it to the console:

# Example input:
# ```
# Enter width: 1.1 
# Enter height: 1.2
# Enter length: 1.3
# ```

# Example output:
# ```
# Volume is: 1.72.

def volume():
    vol = 0
    width = input("Enter width: ")
    height = input("Enter height: ")
    length = input("Enter length: ")

    vol = float(width) * float(height) * float(length)
    print(f"Volume is: {round(vol,2)}")

# # if __name__ == "__main__":
# #     volume()


# # Ex. 3 First and Last
# Create a program that accepts a list of numbers using the `input()` function and writes `True` if the first and last numbers are the same, otherwise write `False` to the console.

# Example input:
# ```
# Enter list of numbers: 1,2,3
# ```

# Example output:
# ```
# False
# ```
def first_last():
    input_list = [int (i) for i in (input("Enter list of numbers: ").split(","))]
    if input_list[0] == input_list[-1]:
        print("True")
    else:
        print("False")
        

# first_last()

# Ex. 4 Word Count
# Create a program that counts the number of times the word `Python` appears in the text below and writes the result to the console. Do not use the `string.count()` method.

# ```
# "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
# ```
#  Example output:
# ```
# 3
# ```

def word_count():
    ex_string = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    new_list = ex_string.strip(",.").split()
    count = 0
    for i in range(len(new_list)-1):
        if (new_list[i] == 'Python'):
            count += 1
    print(count)
    
# word_count()

# # Ex. 5 Bigger Set
# Create a program that adds the following List of numbers to the Set and writes the final Set to the console:
# ```
# myList = [1,2,3]
# mySet = {3,4,5}
# ```
# Example output:
# ```
# {1,2,3,4,5}

def bigger_set():
    myList = set([1,2,3])
    mySet = {3,4,5}
    print(myList | mySet)
# bigger_set()

# Ex. 6 Reverse Me
# Create a program that writes the following list of numbers in reverse order to the console:
# ```
# [11, 100, 101, 999, 1001]
# ```
# Example output:
# ```
# [1001, 999, 101, 100, 11]
# ```
def reverse_list():
    myList = [11, 100, 101, 999, 1001]
    reverseList = []
    for i in myList[::-1]:
        reverseList.append(i)
    print(reverseList)

# reverse_list()

# Ex. 7 Winner Winner
# Create a program that generates a randon number between 1 and 100.  If the number is less than 10 the program prints the value of the number and `You lose.` on the console.  If the number is greater than 10 and less than 50 the program prints the value of the number and `Try again.` on the console.  If the number is greater than 50 the program prints the value of the number and `You win!` on the console.

# Example output:
# ```
# 9: You lose.
# 17: Try again.
# 86: You win!
# ```
def winner():
    num = random.randint(1,100)
    if num <= 10:
        print(f"{num} You lose.")
    elif num > 10 and num <= 50:
        print(f"{num} Try again")
        winner()
    else:
        print(f"{num} You win!")

# winner()
# Ex. 8 Shortest Straw
# Create a program that finds the smallest number in this list and writes the result to the console.  Do not use the `min()` or `sort()` functions.
# ```
# myList = [6,2,7,3,77,7,1]
# ```
# Example output:
# ```
# 1
# ```
def shortest_straw():
    myList = [6,2,7,3,77,7,1]
    min = myList[0]
    if len(myList) > 1:
        for i in range(1,len(myList)):
            if myList[i] < min:
                min = myList[i]
    print(f"{min}")

# shortest_straw()    
# Ex. 9 Uppers or Lowers
# Create a program that writes `True` to the console if a string is upper case, `False` if a string is not.

# Example input:
# ```
# Enter string: "HELLO"
# ```

# Example output:
# ```
# True
# ```

def upper_lower():
    word = input("Enter String: ")
    if word == word.upper():
        print("true")
    else:
        print("false")

        
# upper_lower()

# Ex. 10 Vs and Cs
# Create a program that counts all the vowels and consonants in a word and writes the count to the console:

# Example input:
# ```
# Enter string: Apple
# ```

# Example output:
# ```
# Vowels: 2
# Consonants: 3
# ```

def v_and_c():
    vowels = {'a','e','i','u','o'}    
    v_count = 0
    c_count = 0
    word = input("Enter String: ")
    for i in word.lower():
        if i in vowels:
            v_count += 1
        else:
            c_count += 1
    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")

# v_and_c()

# Ex. 11 Write Today's Date
# Create a program that writes the current date to a file named: `output.txt`.  The program must use an f-string when writing to a file.

# File Contents:
# ```
# Today's date is: 08/17/2021.
# ```]
import datetime
def curr_date():
    with open("output.txt", "w") as my_file:
        my_file.write("File Contents: \n")
        my_file.write(f"Today's date is: {datetime.date.today().strftime('%m/%d/%Y')}")
    with open("output.txt") as my_file:
        for line in my_file:
            print(line)
# curr_date()

# # Ex. 12 Negative to Positive / Positive to Negative
# Create a program that prompts the user to enter an integer value.  The program converts a positive integer to a negative integer, and converts a negative integer to a positive integer.  The result is written to the console. The program returns an error if the user enters a float value.  Do not use the `abs()` function.

# Examples:
# ```
# Enter integer: 12
# -12
# ```

# ```
# Enter integer: -133
# 133
# ```

# ```
# Enter integer: 123232.1
# ERROR: 123232.1 is not an integer.
# ```

# def neg_pos():
#     while True:
#         integer = int(input("Enter integer: "))
#         try:
#             if integer > 0:
#                 integer *= -1
#                 print(integer)
#                 break
#             elif integer < 0:
#                 integer *= -1
#                 print(integer)
#                 break
#             else:
#                 print("0")
#                 break
#         except ValueError:
#             print(f"ERROR: {integer} not an integer")
#             break
# neg_pos()

def ng_ps():
    val = input("Enter integer:")
    if '-' in val:
        val = val.strip('-')
        print(val)
    elif '.' in val:
        print(f"ERROR: {val} not an integer")
    else:
        print(f"-{val}")
    
# ng_ps()


# Ex. 13 Add Only Calculator
# Create a program that prompts the user for two integers and adds them.  The program runs indefinitely until `exit` is typed.

# Example:
# ```
# Enter first integer: 1
# Enter second integer: 3
# Answer: 4.
# Enter first integer: 5
# Enter second integer: 5
# Answer: 10.
# Enter first integer: exit

def addOnly():
    flag = True
    while (flag):
        num1 = input("Enter first integer: ")
        if (num1 != "exit"):
            num2 = input("Enter second integer: ")
            sum = int(num1) + int(num2)
            print(f"Answer: {sum}.")
        else:
            flag = False

# addOnly()
