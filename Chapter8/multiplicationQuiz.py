# Multiplication Quiz
# multiplicationQuiz.py - Timed multiplication quiz using PyInputPlus

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    # Prompt user to answer question
    prompt = '%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1*num2)],
                            blockRegexes=[('.*' 'Incorrect!')],
                            timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else: 
        # This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1
    
    time.sleep(1)  # Brief pause to let the user read the result
    print('Score: %s / %s' % (correctAnswers/numberOfQuestions))