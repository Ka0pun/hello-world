import typing

s = "moon child  "
def count_letters(s: str) -> int:
    
    """
    Count the number of alphabet letters in the string

    Paremeters
    s: Input string
    return
    int: the number of alphabet

    """
    number = 0
    for letter in s:
        if letter.isalpha() or letter.isspace():
            number +=1
    return number
    

print(count_letters(s))




def calculate_mean(a: int | float, b: int | float , c: int | float, d: int | float, e: int | float) -> int | float :

    """
    Calculate the mean of 5 numbers

    Parameter
    a(float): 1st number
    b(float): 2nd number 
    c(float): 3rd number
    d(float): 4th number
    e(float): 5th number

    Return:
    float: the mean of the five input numbers.

    """
    return(a+b+c+d+e) / 5

answer = calculate_mean(0,9,0,-1,3.14)
print(answer)



def smallest(a: float,b: float ,c: float) -> float:

    """
    Find the smallest number among the 3 inout numbers

    Parameters:
    a (float): 1st number.
    b (float): 2nd number.
    c (float): 3rd number.

    Returns:
    float: The smallest value among the three input numbers.

    """

    return min(a,b,c)
result = smallest(0,-9,3.14)
print(result)