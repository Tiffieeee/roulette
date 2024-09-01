import turtle
import pandas
import random

#ScreenRoulette
screen = turtle.Screen()
screen.title("Tiffie's Roulette")
screen.addshape("roulettetafel.gif")
screen.bgcolor("black")
t = turtle.Turtle()
t.shape("roulettetafel.gif")

#Ask User
player_bet = screen.textinput(title="Place your bet", prompt="Your bet: ").title()



#Data coordinates
data = pandas.read_csv("roulettecoordinates.csv")
all_numbers = data["number"].to_list()
player_score = 0
game_on = True

def show_number():
    global player_score

    global winning_number
    winning_number = random.choice(all_numbers)
    print(f"The winning number is: {winning_number}")


    wn = turtle.Turtle()
    wn.penup()
    wn.hideturtle()
    wn.color("white")
    screen.addshape("pearl3.gif")
    wn.shape("pearl3.gif")


    number_data = data[data["number"] == winning_number]
    if not number_data.empty:
        x_coord = int(number_data["x"].values[0])
        y_coord = int(number_data["y"].values[0])
        wn.goto(x_coord, y_coord)
        wn.stamp()


    if player_bet == winning_number:
        player_score += 1
        update_score()


#Show Score
def update_score():
    score.clear()
    # score.write(f"Player points:{player_score}", False, align="left", font=("Courier", 22, "normal"))

score = turtle.Turtle()
score.penup()
score.goto(0, 250)
score.color("white")
score.hideturtle()
score.write(f"Player points:{player_score}", False, align="left", font=("Courier", 22, "normal"))


#Show Bet
def update_bet():
    bet = ""
    bet.clear()
    # bet.write(f"Player bet is:{player_bet}", False, align="right", font=("Courier", 22, "normal"))


bet = turtle.Turtle()
bet.penup()
bet.goto(0, 250)
bet.color("white")
bet.hideturtle()
bet.write(f"Player bet is:{player_bet}", False, align="right", font=("Courier", 22, "normal"))




show_number()

# #
# while game_on:
#     result = show_number()
#     if result is False:
#         game_on = False
#         print("Game over!")
#         break

screen.exitonclick()