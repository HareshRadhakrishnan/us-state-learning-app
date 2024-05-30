import turtle
import pandas
from writer import Writer
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pandas.read_csv("50_states.csv")
SCORE = 0
game_over = False
TITLE = "Guess the State"
all_states = state_data['state'].to_list
answered_list =[]
while not game_over:
    answer_state = screen.textinput(title=TITLE, prompt="What's another state's name?").title()
    state_list = state_data["state"].to_list
    if answer_state =="Exit":
        missing_answers =[State for State in state_data['state'] if State not in answered_list]
        new_data = pandas.DataFrame(missing_answers)
        new_data.to_csv("You_missed_out.csv")
        break

    for state in state_data.state:
        if state == answer_state:
            answered_list.append(answer_state)
            SCORE += 1
            state_row = state_data[state_data.state == answer_state]
            x_pos = int(state_row.x)
            y_pos = int(state_row.y)
            text = Writer()
            text.write_text(x_cod=x_pos, y_cod=y_pos, text=answer_state)
            TITLE = f"{SCORE}/50 States Correct"



