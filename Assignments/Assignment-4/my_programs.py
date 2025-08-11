def gcd_program():
    print("🧠 Program: Find the GCD of Two Numbers\n")

    print("📄 Code:")
    print('''\
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD is", find_gcd(a, b))
''')

    print("🧪 Test Cases:")
    print("Input: 60, 48 → Output: GCD is 12")
    print("Input: 81, 27 → Output: GCD is 27")

    print("\n📝 Explanation:")
    print("This program uses the Euclidean algorithm. It repeatedly replaces a with b and b with a % b until b becomes 0. The remaining value in a is the GCD.")


def perfect_number_check():
    print("🧠 Program: Check if a Number is a Perfect Number")

    print("📄 Code:")
    print('''\
def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
          sum += i
    if sum == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")
''')

    print("🧪 Test Cases:")
    print("Input: 28 → Output: 28 is a Perfect number")
    print("Input: 12 → Output: 12 is not a Perfect number")

    print("\n📝 Explanation:")
    print("A perfect number is one where the sum of all its proper divisors (excluding itself) equals the number itself. "
          "This program adds such divisors and checks if their sum matches the original number.")


def anagram_check():
    print("🧠 Program: Check if Two Strings are Anagrams")

    print("📄 Code:")
    print('''\
def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if are_anagrams(str1, str2):
    print("Anagrams")
else:
    print("Not Anagrams")
''')

    print("🧪 Test Cases:")
    print('''\
Test Case 1:
Input: "listen", "silent"
Output: Anagrams

Test Case 2:
Input: "hello", "world"
Output: Not Anagrams
''')

    print("📝 Explanation:")
    print("This program checks if two strings are anagrams by sorting both and comparing the result. "
          "If the sorted versions are equal, the strings contain the same characters in a different order.")


def transpose_matrix():
    print("🧠 Program: Transpose a Matrix")

    print("📄 Code:")
    print('''\
def get_transpose(matrix):
    transpose = []
    for i in range(cols):
        row = []
        for j in range(rows):
          row.append(matrix[j][i])
        transpose.append(row)
    print(transpose)

matrix = [
    [1, 2, 3],
    [5, 6, 7]
]

print("Transpose Matrix")
get_transpose(matrix)
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input: [[1, 2, 3], [5, 6, 7]]")
    print("Output: [[1, 5], [2, 6], [3, 7]]\n")

    print("Test Case 2:")
    print("Input: [[9, 8], [7, 6], [5, 4]]")
    print("Output: [[9, 7, 5], [8, 6, 4]]")

    print("\n📝 Explanation:")
    print("We loop over columns first and then rows to swap rows with columns,")
    print("building a new matrix where each row becomes a column from the original.")


def prime_in_range():
    print("🧠 Program: Find All Prime Numbers in a Given Range")

    print("📄 Code:")
    print('''\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter the upper limit: "))
for n in range(2, num + 1):
    if is_prime(n):
        print(n, end=" ")
print()
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input: 10")
    print("Output: 2 3 5 7\n")

    print("Test Case 2:")
    print("Input: 20")
    print("Output: 2 3 5 7 11 13 17 19")

    print("\n📝 Explanation:")
    print("We check each number from 2 to the upper limit.")
    print("For each number, we check divisibility up to its square root.")
    print("If it has no divisors other than 1 and itself, it is printed as a prime.")


def convert_number_bases():
    print("🧠 Program: Convert Decimal to Binary, Octal, and Hexadecimal")

    print("📄 Code:")
    print('''\
def convert(decimal):
    return bin(decimal)[2:], oct(decimal)[2:], hex(decimal)[2:]

decimal = int(input("Enter a decimal number: "))
binary, octal, hexa = convert(decimal)
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexa)
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input: 25")
    print("Output: Binary: 11001 | Octal: 31 | Hexadecimal: 19")

    print("Test Case 2:")
    print("Input: 100")
    print("Output: Binary: 1100100 | Octal: 144 | Hexadecimal: 64")

    print("\n📝 Explanation:")
    print("This program takes a decimal number and uses built-in functions `bin()`, `oct()`, and `hex()`")
    print("to convert it into binary, octal, and hexadecimal respectively. Slicing removes the prefix (like 0b).")


def list_palindrome_check():
    print("🧠 Program: Check if a List is a Palindrome")

    print("📄 Code:")
    print('''\
def is_palindrome(lis):
    return lis == lis[::-1]

lis = list(map(int, input("Enter a list of numbers: ").split()))
if is_palindrome(lis):
    print(f"{lis} is a palindrome.")
else:
    print(f"{lis} is not a palindrome.")
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input: 1 2 3 2 1")
    print("Output: [1, 2, 3, 2, 1] is a palindrome.")

    print("Test Case 2:")
    print("Input: 1 2 3 4")
    print("Output: [1, 2, 3, 4] is not a palindrome.")

    print("\n📝 Explanation:")
    print("A list is a palindrome if it reads the same forward and backward. This is checked using slicing `lis[::-1]`.")


def calculate_pow():
    print("🧠 Program: Calculate Power of a Number Without Using ** or pow()")

    print("📄 Code:")
    print('''\
def manual_pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input("Enter a base value: "))
exponent = int(input("Enter an exponent value: "))
result = manual_pow(base, exponent)
print(f"{base} power {exponent} is {result}")
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input: base = 2, exponent = 5")
    print("Output: 2 power 5 is 32")

    print("Test Case 2:")
    print("Input: base = 3, exponent = 3")
    print("Output: 3 power 3 is 27")

    print("\n📝 Explanation:")
    print("This program multiplies the base repeatedly in a loop equal to the exponent value to calculate power manually without using ** or pow().")


def duplicate_elements():
    print("🧠 Program: Find Duplicate Elements in a List")

    print("📄 Code:")
    print('''\
def find_duplicates(lis):
    seen = set()
    duplicates = []
    for num in lis:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    return duplicates

lis = list(map(int, input("Enter list elements separated by space: ").split()))
print("Duplicate elements:", find_duplicates(lis))
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input: 1 2 3 2 4 1")
    print("Output: Duplicate elements: [2, 1]")

    print("Test Case 2:")
    print("Input: 5 6 7 8 9")
    print("Output: Duplicate elements: []")

    print("\n📝 Explanation:")
    print("This program uses a set to track seen elements and appends duplicates only once in a new list.")


def todo_list():
    print("🧠 Program: CLI-Based To-Do List")

    print("📄 Code:")
    print('''\
todo = []

while True:
    print("\\n1. Add Task\\n2. View Tasks\\n3. Delete Task\\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")  
        todo.append(task)

    elif choice == 2:
        if not todo:
            print("No tasks to display.")
        else:
            for i in range(len(todo)):
                print(f"{i+1}: {todo[i]}")

    elif choice == 3:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(todo):
            del todo[index-1]
        else:
            print("Invalid task number")

    elif choice == 4:
        break

    else:
        print("Invalid choice")
''')

    print("🧪 Test Cases:")
    print("Test Case 1:")
    print("Input:")
    print("1 (Add Task) → 'Buy milk'")
    print("2 (View Tasks) → Shows '1: Buy milk'")
    print("4 (Exit)")
    print("Output: Task list displays correctly")

    print("Test Case 2:")
    print("Input:")
    print("1 (Add Task) → 'Study Python'")
    print("1 (Add Task) → 'Exercise'")
    print("3 (Delete Task) → 1")
    print("2 (View Tasks)")
    print("4 (Exit)")
    print("Output: Remaining tasks → '1: Exercise'")

    print("\n📝 Explanation:")
    print("This program allows users to manage a task list using a menu. It supports adding, viewing, and deleting tasks using basic list operations.")
