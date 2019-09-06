# Generates random quizzes on the US states and capitols.

import random, os
os.makedirs('C:\\Users\\ljuskelis\\Desktop\\LaurenJuskelis\\Cursos\\IDLE\\Quizzes')     # Make a folder to hold the quizzes.
os.chdir('C:\\Users\\ljuskelis\\Desktop\\LaurenJuskelis\\Cursos\\IDLE\\Quizzes')

number_of_quizzes = 35          # Specify how many quizzes to make.
questions = []

sc = [{'state': 'Alabama', 'capital': 'Montgomery'},
      {'state': 'Alaska', 'capital': 'Juneau'},
      {'state': 'Arizona', 'capital': 'Phoenix'},
      {'state': 'Arkansas', 'capital': 'Little Rock'},
      {'state': 'California', 'capital': 'Sacramento'},
      {'state': 'Colorado', 'capital': 'Denver'},
      {'state': 'Connecticut', 'capital': 'Hartford'},
      {'state': 'Delaware', 'capital': 'Dover'},
      {'state': 'Florida', 'capital': 'Tallahassee'},
      {'state': 'Georgia', 'capital': 'Atlanta'},
      {'state': 'Hawaii', 'capital': 'Honolulu'},
      {'state': 'Idaho', 'capital': 'Boise'},
      {'state': 'Illinois', 'capital': 'Springfield'},
      {'state': 'Indiana', 'capital': 'Indianapolis'},
      {'state': 'Iowa', 'capital': 'Des Moines'},
      {'state': 'Kansas', 'capital': 'Topeka'},
      {'state': 'Kentucky', 'capital': 'Frankfurt'},
      {'state': 'Louisiana', 'capital': 'Baton Rouge'},
      {'state': 'Maine', 'capital': 'Augusta'},
      {'state': 'Maryland', 'capital': 'Annapolis'},
      {'state': 'Massachusetts', 'capital': 'Boston'},
      {'state': 'Michigan', 'capital': 'Lansing'},
      {'state': 'Minnesota', 'capital': 'Saint Paul'},
      {'state': 'Mississippi', 'capital': 'Jackson'},
      {'state': 'Missouri', 'capital': 'Jefferson City'},
      {'state': 'Montana', 'capital': 'Helena'},
      {'state': 'Nebraska', 'capital': 'Lincoln'},
      {'state': 'Nevada', 'capital': 'Carson City'},
      {'state': 'New Hampshire', 'capital': 'Concord'},
      {'state': 'New Jersey', 'capital': 'Trenton'},
      {'state': 'New Mexico', 'capital': 'Santa Fe'},
      {'state': 'New York', 'capital': 'Albany'},
      {'state': 'North Carolina', 'capital': 'Raleigh'},
      {'state': 'North Dakota', 'capital': 'Bismarck'},
      {'state': 'Ohio', 'capital': 'Columbus'},
      {'state': 'Oklahoma', 'capital': 'Oklahoma City'},
      {'state': 'Oregon', 'capital': 'Salem'},
      {'state': 'Pennsylvania', 'capital': 'Harrisburg'},
      {'state': 'Rhode Island', 'capital': 'Providence'},
      {'state': 'South Carolina', 'capital': 'Columbia'},
      {'state': 'South Dakota', 'capital': 'Pierre'},
      {'state': 'Tennessee', 'capital': 'Nashville'},
      {'state': 'Texas', 'capital': 'Austin'},
      {'state': 'Utah', 'capital': 'Salt Lake City'},
      {'state': 'Vermont', 'capital': 'Montpelier'},
      {'state': 'Virginia', 'capital': 'Richmond'},
      {'state': 'Washington', 'capital': 'Olympia'},
      {'state': 'West Virginia', 'capital': 'Charleston'},
      {'state': 'Wisconsin', 'capital': 'Madison'},
      {'state': 'Wyoming', 'capital': 'Cheyenne'}]

for i in range(50):                                             # Fill the master list 'questions' with the questions and answer keys.
    x = random.randrange(2,6)
    listy = ['', '', '', '', '', '', '']                        # Create an empty list for the ith question.
    listy[0] = sc[i]['state']                                   # Define state; store in 0th index of listy.
    listy[1] = sc[i]['capital']                                 # Define capital; store in 1st index of listy.
    listy[x] = listy[1]                                         # Store the correct answer at a random index in listy between index 2 and 5.
    for y in range(2,6):                                        # Store random wrong answers in the empty indeces in listy from index 2 to 5. 
        while listy[y] == '':
            z = random.randrange(35)
            if sc[z]['capital'] != listy[1]:
                listy[y] = sc[z]['capital']
    if x == 2:                                                  # Define the answer key in index 6 of listy.
        listy[6] = 'A'
    elif x == 3:
        listy[6] = 'B'
    elif x == 4:
        listy[6] = 'C'
    elif x == 5:
        listy[6] = 'D'
    questions.append(listy)                                     # Add the 'listy' list to the 'questions' master list.

print(questions)

for i in range(number_of_quizzes):
    qs = []
    answers = []
    for a in range(50):                                         # Create two lists, each with '' fifty times.
        qs.append('')
        answers.append('')
    for b in range(50):                                         # Fill the questions and answers lists.
        while True:
            c = random.randrange(50)
            if qs[c] == '':
                qs[c] = str(c + 1) + '. What is the capital of ' + questions[b][0] + '?\n\tA. ' + questions[b][2] + '\n\tB. ' + questions[b][3] + '\n\tC. ' + questions[b][4] + '\n\tD. ' + questions[b][5] + '\n\n'
                answers[c] = str(c + 1) + '. ' + questions[b][6] + '\n'
                break
    with open('Quiz ' + str(i + 1) + '.txt', 'w') as quiz:      # Save the quizzes to text files.
        for d in range(50):
            quiz.write(qs[d])
    with open('Answer key ' + str(i + 1) + '.txt', 'w') as answer_key:      # Save the answer keys to text files.
        for e in range(50):
            answer_key.write(answers[e])
    
os.chdir('C:\\Users\\ljuskelis\\Desktop\\LaurenJuskelis\\Cursos\\IDLE')
