import pandas
import turtle
from name_state import NameState
from score_board import ScoreBoard

data = pandas.read_csv("50_states.csv")
stateNames = data.state.tolist()
guessedStates = []

pic = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("STATES GEM")
screen.addshape(pic)
screen.bgcolor("black")
screen.setup(height=500, width=730)
turtle.shape(pic)
screen.tracer(0)

scoreBoard = ScoreBoard()

isPlaying = True
while isPlaying:

    if scoreBoard.score == 50:
        isPlaying = False
        scoreBoard.youWin()

    userGuess = screen.textinput(f"{scoreBoard.score}/50 States Correct", "Name another state")
    userGuess = userGuess.title()

    if userGuess == "X":
        isPlaying = False
        missedStates = [s for s in stateNames if s not in guessedStates]
        missedStates = {"Unguessed States": missedStates}
        missedStatesDF = pandas.DataFrame(missedStates)
        missedStatesDF.to_csv("missed_states.csv")
        turtle.bye()

    elif userGuess in guessedStates:
        print(f"You already guessed {userGuess}.")
    elif userGuess in stateNames:
        currentState = data[data.state == userGuess]
        state = NameState(userGuess, int(currentState.x), int(currentState.y))
        guessedStates.append(userGuess)
        scoreBoard.increaseScore()
    else:
        print(f"{userGuess} is not a state of America.")
    screen.update()


turtle.mainloop()
