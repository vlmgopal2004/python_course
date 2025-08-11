import my_programs as mp

function_map = {
    1: mp.gcd_program,
    2: mp.perfect_number_check,
    3: mp.anagram_check,
    4: mp.transpose_matrix,
    5: mp.prime_in_range,
    6: mp.convert_number_bases,
    7: mp.list_palindrome_check,
    8: mp.calculate_pow,
    9: mp.duplicate_elements,
    10: mp.todo_list
}
while True:
    print('''
------ FUNCTION MENU ------
1. Find the GCD of two numbers
2. Check if a number is a perfect number
3. Check if two strings are anagrams
4. Transpose a matrix
5. Find all prime numbers in a given range
6. Convert decimal to binary, octal, and hexadecimal
7. Check if a list is a palindrome
8. Calculate power of a number without using ** or pow()
9. Find duplicate elements in a list
10. Implement a basic todo list (CLI-based)
0. Exit
---------------------------''')
    
    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        break
    else:
        ("Invalid choice")