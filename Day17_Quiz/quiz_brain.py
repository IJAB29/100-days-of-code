class QuizBrain:
    def __init__(self, bank):
        self.number = 0
        self.bank = bank
        self.score = 0

    def stillHasQuestions(self):
        return self.number < len(self.bank)

    def nextQuestion(self):
        question = self.bank[self.number]
        self.number += 1
        userAnswer = input(f"Q.{self.number}: {question.text} (True or False)?: ")
        self.checkAnswer(userAnswer, question.answer)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{self.number}")
        print("\n==============================================================================")
