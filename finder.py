n = int(input("Enter your roll number: "))
questions = [1, 2, 3, 4, 5, 6, 7]  
index = (n - 1) % len(questions)
selected_question = questions[index]

print(f"The question assigned for roll number {n} is: Question {selected_question}")
