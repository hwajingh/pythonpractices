# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
# ..... 

def hello_name(user_name):
    print(f"hello {user_name}")

hello_name("tiger")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
# ..... 
def first_odds():
    for x in range(1,100):
        if x % 2 != 0:
            print(x)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
# ..... 
def max_num_in_list(a_list):
    max_value = max(a_list) 
    return (max_value)

listss = [10, 2, 3, 4, 5, 6, 7, 8]

print(max_num_in_list(listss))



# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
# ..... 

def leapyear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

print(leapyear(2024))


# Question 5

# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    for x in range(1, len(a_list)):
        if (a_list[x]+1) == a_list[x+1]:
            return True
        else:
            return False

lists2 = [10, 2, 3, 4, 5, 6, 7, 8]

lists1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(is_consecutive(lists2))
print(is_consecutive(lists1))


