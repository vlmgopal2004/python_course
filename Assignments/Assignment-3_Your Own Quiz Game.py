questions = {1:{'question':'''What is the effect of break in a loop with multiple iterations remaining? 
A: It skips the remaining iterations
B: It executes the remaining iterations
C: It pauses the loop
D: It restarts the loop''',
                'answer':'A'},
             2:{'question':'''In a nested loop, what happens when a break is executed in the inner loop? 
A: Both loops terminate
B: Only the inner loop terminates
C: The outer loop skips an iteration
D: The program crashes''',
                'answer':'B'},
             3:{'question':'''If a while loop condition is False from the start, what happens to break inside it? 
A: Break executes immediately
B: Break is never reached
C: An error occurs
D: The loop runs once''',
                'answer':'B'},
             4:{'question':'''What happens if break is inside an infinite loop? 
A: The loop continues forever
B: The loop exits when break is reached
C: Break does not work
D: It crashes the program''',
                'answer':'B'},
             5:{'question':'''How do you pass parameters to a function?
A: Using return
B: Using class
C: Using parentheses
D: Using square brackets''',
                'answer':'C'},
             6:{'question':'''Does a break statement affect outer loops?
A: Yes, it exits all loops
B: No, it only affects the current loop
C: Yes, if nested deeply
D: It causes an error''',
                'answer':'B'},
             7:{'question':'''Can built-in functions be redefined by user? 
A: Yes
B: No
C: Only in main()
D: Only using class''',
                'answer':'A'},
             8:{'question':'''Recursive solutions are often more
A: Code-readable
B: Faster
C: Compiled
D: Easier to debug''',
                'answer':'A'},
             9:{'question':'''What does input("Input: ").strip("x") return if the user types "xxhelloxx"?
A: helloxx
B: xxhelloxx
C: hello
D: Error''',
                'answer':'C'},
             10:{'question':'''Which argument must come first in function definition? 
A: *args
B: Default
C: **kwargs
D: Positional''',
                'answer':'D'},
            11:{'question':'''What type of data structure does *args store its values in? 
A: List
B: Dictionary
C: Tuple
D: Set''',
                'answer':'C'},
            12:{'question':'''Which function is used to take input from the user in Python?
A: get_input()
B: input()
C: scan()
D: read()''',
                'answer':'B'},
            13:{'question':'''Where is procedural programming commonly applied? 
A: Complex GUI applications
B: Operating Systems and embedded systems
C: Large scale enterprise applications
D: Modern web frameworks''',
                'answer':'B'},
            14: {'question': '''What is the use of the 'pass' statement in Python?
A: Terminates the program
B: Does nothing, acts as a placeholder
C: Repeats a loop
D: Skips a function''',
                'answer': 'B'},
            15: {'question': '''Which of the following is **not** a Python data type?
A: set
B: map
C: list
D: tuple''',
                'answer': 'B'},
            16: {'question': '''What is the output of: len("Hello\\nWorld")?
A: 10
B: 11
C: 12
D: Error''',
                'answer': 'B'},
            17: {'question': '''What does the enumerate() function return?
A: A sorted list
B: An index-value pair iterator
C: A string
D: A list of keys''',
                'answer': 'B'},
            18: {'question': '''Which of the following is used for single-line comments in Python?
A: //
B: --
C: #
D: /**/''',
                'answer': 'C'},
            19: {'question': '''What will be the output of bool([]) in Python?
A: True
B: False
C: None
D: Error''',
                'answer': 'B'},
            20: {'question': '''Which built-in function returns the unique identifier for an object?
A: id()
B: hash()
C: type()
D: uid()''',
                'answer': 'A'}}

print("🧪 Welcome to the Python Quiz Game!")
def quiz_game(questions):
    score = 0
    for qus in questions.keys():
        print(f"Question {qus}:{questions[qus]['question']}")
        ans = input("Your answer (A/B/C/D):").upper()
        while ans not in ['A','B','C','D']:
            ans = input(f"❗ Invalid choice {ans}. Please enter A, B, C, or D: ").upper()
        if ans == questions[qus]['answer']:
            score += 1
            print(f"✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer is {questions[qus]['answer']}")
    print(f"🎯 Your Final Score: {score}/{len(questions)}")
    print("🎉 Great job! Keep practicing!")

quiz_game(questions)