Copy code
# Code Smell 1: Inconsistent Naming
Var1 = 10
Var2 = 20

def calculate_SUM(Var1, Var2):
    return Var1 + Var2

# Code Smell 2: Magic Numbers
def calculate_area(radius):
    return 3.14159 * radius * radius

# Code Smell 3: Long Functions
def process_data(data):
    result = []
    for item in data:
        # A long and complex process here
        intermediate_result = item * 2
        # More complex calculations
        final_result = intermediate_result + 5
        result.append(final_result)
    return result

# Code Smell 4: Lack of Comments/Documentation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
