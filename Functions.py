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
def sqr(x):
    return x**2
sqr(2)

# %%
# Example of the map function.
numbers = [1, 2, 3, 4, 5]

def sqr(x):
    return x**2
list(map(sqr, numbers))

# %%
# A for loop that squares a number.
numbers = [1, 2, 3, 4, 5]
numbers_sqr = []

for number in numbers:
    numbers_sqr.append(number**2)

print(numbers_sqr)

# %%
# Using the format() function.
my_grades = [92.34, 84.56, 86.78, 98.32]

for grade in my_grades:
    print("{:.0f}".format(grade))

# %%
# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]

# %%
# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]

# %%
