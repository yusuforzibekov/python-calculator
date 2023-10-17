# Simple Calculator
This Python program is a simple calculator that allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, and division) with two integer numbers. Here's a description of the program and how to use it:

# Description:
1) It prompts the user to enter two integer values, 'a' and 'b', using the input function and converts them into integer data types using int(). <br>
2) It then prompts the user to choose an operation by entering 'add,' 'sub,' 'mul,' or 'div' using the input function. The user's choice is stored in the 'amal' variable. <br>
3) The program uses a series of conditional statements (if-elif-else) to determine which operation to perform based on the 'amal' variable:
+   If 'amal' is 'add,' it calculates the sum of 'a' and 'b' and stores the result in the 'c' variable.
+   If 'amal' is 'sub,' it calculates the difference of 'a' and 'b' and stores the result in 'c.'
+   If 'amal' is 'mul,' it calculates the product of 'a' and 'b' and stores the result in 'c.'
+   If 'amal' is 'div,' it calculates the division of 'a' by 'b' and stores the result in 'c.'
+   If 'amal' doesn't match any of these operations, it sets 'c' to 'Error.'
4) Finally, the program prints the result 'c' along with the label "Result =".
# How to Use:
<ul><li>Run the program. Typing: </li></ul><br>
    python test.py
2) Enter an integer value for 'a' when prompted. <br>
3) Enter another integer value for 'b' when prompted. <br>
4) Choose one of the four operations ('add,' 'sub,' 'mul,' or 'div') by entering the corresponding operation as 'amal.' <br>
5) The program will calculate the result based on your input and display it as "Result = [value]." <br>

For example, if you enter 'a' as 5, 'b' as 3, and 'amal' as 'add,' the program will display "Result = 8" because it performs the addition operation (5 + 3).
