#Method 1
try:
    int1=int(input("Please enter your integer 1: "))
    int2=int(input("Please enter your integer 2: "))
    sum_result = int1 + int2
    print(sum_result)

except ValueError:
    print("please enter a valid integer")    



# Method 2
try:
    # Get input from the user
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Calculate the sum
    sum_result = num1 + num2

    # Display the result
    print(f"The sum of {num1} and {num2} is: {sum_result}")

except ValueError:
    print("Invalid input! Please enter valid integers.")





