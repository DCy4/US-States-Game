import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read csv and look for user guess in it
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    #read and store user guess and convert to title case (using .title())
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's Name?").title()
    if answer_state == "Exit":
        # new list to track all states user did not guess
        missing_states = [state for state in all_states if (state not in guessed_states)]
        break
    #check answer to list the states in all the states in 50_states.csv >>>in keyword only works if data converted to_list()<<<
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

df = pandas.DataFrame(missing_states)
print(df)
screen.exitonclick()