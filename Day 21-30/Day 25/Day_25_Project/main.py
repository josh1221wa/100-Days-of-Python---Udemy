import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"Day 25\Day_25_Project\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.up()

state_df = pandas.read_csv(r"Day 25\Day_25_Project\50_states.csv")

count = 0
guessed_states = []

while count <= 50:
    user_answer = str(screen.textinput(title=f"{count}/50 States Correct", prompt = "What's another state name?"))
    user_answer = user_answer.title()

    if user_answer == "Exit":
        break

    if user_answer in state_df.values:
        x = int(state_df[state_df.state == user_answer].x)  # type: ignore
        y = int(state_df[state_df.state == user_answer].y)  # type: ignore
        writing_turtle.goto(x=x, y=y)
        writing_turtle.write(user_answer, align="center")
        count += 1
        guessed_states.append(user_answer)

with open(r"Day 25\Day_25_Project\states_to_learn.csv", "w") as f:
    csv_writer = csv.writer(f)
    count = 1
    for i in state_df.state:
        if i not in guessed_states:
            csv_writer.writerow([count, i])
            count += 1

