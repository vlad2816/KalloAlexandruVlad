
questions = ('How many elements are in the periodic table?: ',
             'What is the most abundant gas in Earth atmosphere: ',
             'How many bons are in the human body?: ')

options = (('A. 116', 'B. 117', 'C. 118', 'D. 119'),
           ('A. Nitrogen', 'B. Oxygen', 'C. CO2', 'D. Hydrogen'),
           ('A. 206', 'B. 207', 'C. 208', 'D. 209'))

answers = ('C', 'B', 'D')
guesses = []
score = 0
question_num = 0


for question in questions:
    print('-'*40)
    print(question)
    print('-'*40)
    for option in options[question_num]:
        print(option)

    guess = input('Enter: (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('Correct!')
    else:
        print('Incorrect!')
        print(f'The correct answer is: {answers[question_num]}')
    question_num += 1


print('-'*40)
print('Results')
print('-'*40)

print('answers:', end=' ')

for answer in answers:
    print(answer, end=' ')
print()

print('guesses:', end=' ')

for guess in guesses:
    print(guess, end=' ')
print()

score = int(score / len(questions) * 100)
print(f'Your score is: {score}%')
