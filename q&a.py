from Brain import Brain

print('\n#####################\n')
print('Welcome to the jungle\n')
print('#####################\n')
print('Choose your battle mode:\n')
print('1) Advanced Vision\n')
print('2) Probabilistic Modelling and Reasoning\n')
print('3) Too late, I\'m going to sleep!\n')

selection = input()
if selection == '3':
    exit('\nGood night. And if there\'s an apocalypse, good luck!\n')

current_courses = {'1': 'av', '2': 'pmr'}
course = current_courses[selection]

brain = Brain(course)

brain.display_latest_results()
brain.choose_topic()

in_ = input('Ready?\n')

if in_ == '':
    question_counter = 0
    while not brain.ran_out_of_questions():
        question, answer, topic, idx = brain.get_next_question()
        next = input('\nQ{} '.format(question_counter) + question + ' [' +
                     topic + ']' + '\n')
        question_counter += 1
        if next == '':
            print('Answer\n' + '------')
            result = input(answer + ' \n\n...Correct?\n')
            if result == '1':
                brain.add_correct(idx)
            elif result == 'end':
                break
            else:
                brain.add_wrong(idx)
        elif next == 'end':
            break
        else:
            print('Not sure what to do now...\n')
    print(
        f'\nAnswered all questions, result: {len(brain.correct)}/{len(brain.correct) + len(brain.wrong)}\n'
    )

brain.save_results()
