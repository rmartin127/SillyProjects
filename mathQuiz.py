# Write your code here :-)
import pyinputplus as pyip
import random, time

#Let's play a math game
numberOfQuestions = 10
correctAnswers = 0

def test():
    global correctAnswers
    global numberOfQuestions
    correctAnswers = 0
    for questionNumber in range(numberOfQuestions): #to the max question limit
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        prompt = '\n#%s: %s x %s = ' % (questionNumber + 1, num1, num2) #display how many were correct
        try:
            pyip.inputStr(prompt, #display the prompt
            allowRegexes=['^%s$' % (num1 * num2)], #check for correct answer
            blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3) #check for incorrect answer

        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of Tries!')
        else:
            print('Correct!')
            correctAnswers += 1
        time.sleep(1)
test()
print('Score: %s / %s' % (correctAnswers, numberOfQuestions)) #Print score

#This is to check the correct percentages

if correctAnswers == 0:
    print('SMH my head')
elif correctAnswers <= 6:
    print('Try again later')
elif correctAnswers <= 9:
    print('Congrats you passed!')
else:
    print('PERFECT!')
#TODO: Make it dynamic
#TODO: :D
