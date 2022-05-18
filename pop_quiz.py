'''This module represents a multiplication pop-quiz. Using Python's
PyInputPlus and Time libraries, the script will prompt a user to
answer a series of 10 questions. They will have 3 chances and 10
seconds to answer each question. The questions will be randomly
generated for the quiz each time from 1-12 inclusive. Afterward,
the user's name, the generated questions, and the user's score
will be exported to a txt file as a souvenir.'''

import pyinputplus as pyip
import time, random

def main():

    results = []
    quiz_questions = 10
    correct_answers = 0

    for question in range(quiz_questions):

        num1 = random.randint(1, 12) #inclusive range
        num2 = random.randint(1, 12)

        answer = pyip.inpu







#file = open('certificate.txt', 'w')
