from data import *
from question_model import *
from quiz_brain import *


questionBank = []
for question in question_data:
    questionText = question["question"]
    questionAnswer = question["correct_answer"]
    questionBank.append(Question(questionText, questionAnswer))


quizBrain = QuizBrain(questionBank)
while quizBrain.stillHasQuestions():
    quizBrain.nextQuestion()

print("Congratulations, you have completed the quiz.")
print(f"Your final score was: {quizBrain.score}/{quizBrain.number}")
