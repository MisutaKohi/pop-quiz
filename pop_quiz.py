'''This module represents a multiplication pop-quiz. Using Python's
PyInputPlus and Time libraries, the script will prompt a user to
answer a series of 10 questions. They will have 3 chances and 10
seconds to answer each question. The questions will be randomly
generated for the quiz each time from 1-12 inclusive. Afterward,
the user's name, the generated questions, and the user's score
will be exported to a txt file as a souvenir.'''

import pyinputplus as pyip
import random, time

def main():

    results = []
    quiz_questions = 10
    correct_answers = 0

    for question in range(quiz_questions):

        num1 = random.randint(1, 12) #inclusive range
        num2 = random.randint(1, 12)

        prompt = f'{num1} x {num2} = '
        answer = ''

        try:
            answer = pyip.inputStr(prompt, allowRegexes=[f'^{str(num1 * num2)}$'],
                                   blockRegexes=[('.*', 'Incorrect!')], timeout=10, limit=3)
            correct_answers += 1
        except pyip.TimeoutException:
            answer = 'Out of time!'
            print(answer)
        except pyip.RetryLimitException:
            answer = 'Out of tries!'
            print(answer)

        results.append(prompt + answer + '\n')

    print('Done!\n')

    time.sleep(1)
    print(f'Your score: {correct_answers} out of 10')
    prompt = 'Would you like to download your certificate? '
    response = pyip.inputYesNo(prompt, caseSensitive=False)
    print() #formatting

    if response.lower() == 'yes':
        file = open('certificate.txt', 'w')

        prompt = 'What is your name? '
        name = pyip.inputStr(prompt, allowRegexes=['^[A-Z]{1}[a-z]{1,}$'], blockRegexes=['.*'])

        results.insert(0, 'Name: ' + name + '\n')
        results.insert(1, f'Score: {correct_answers} out of 10\n' )
        results.insert(2, '\n')
        results.insert(3, 'Quiz questions:\n')

        file.writelines(results)
        file.close()

    else:
        print('Thank you for completing this pop quiz.')

if __name__ == '__main__':
    main()







