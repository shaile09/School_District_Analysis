# %%
# Define the function "say_hello" so it prints "Hello!" when called.
def say_hello():
    print("Hello!")



# %%
# Call the function.
say_hello()

# %%
# Define the function "say_something" so it prints whatever is passed as the variable when called.
def say_something(something):
    print(something)

# %%
# Call the function.
say_something("Hello World")

# %%
Jane_says = "Hi, my name is Jane. I'm learning Python!"
say_something(Jane_says)

# %%
# Define a function that calculates the percentage of students that passed both # math and reading and prints the passing percentage to the output when the
# function is called.
def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100

# %%
passing_math_count = 29370
total_student_count = 39170

# %%
# Call the function.
passing_math_percent(passing_math_count, total_student_count)

# %%
# A basic function that squares a number.
1 def sqr(x):
2    return x**2
3
4 sqr(2)

# %%
# Example of the map function.
1 numbers = [1, 2, 3, 4, 5]
2
3 def sqr(x):
4    return x**2
5
6 list(map(sqr, numbers))