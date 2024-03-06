import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('FridayProj5.db')
cursor = conn.cursor()

# Get the names of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Assuming there's only one table, extract its name
if tables:
    table_name = tables[0][0]

    # Fetch questions and answers from the table
    cursor.execute(f"SELECT question, answer FROM {table_name}")
    trivia_questions = dict(cursor.fetchall())

    # Display and check answers using a for loop
    for question, correct_answer in trivia_questions.items():
        # Display the question to the user
        print(question)

        # Prompt the user to input their answer
        user_answer = input("Your answer: ")

        # Check if the user's answer matches the correct answer
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.\n")

    # End of the trivia questions
    print("You've completed the trivia questions. Great job!")

else:
    print("No tables found in the database.")

# Close the database connection
conn.close()
