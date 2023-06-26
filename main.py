import turtle
import pandas

screen = turtle.Screen()
screen.title("Viet Nam Provinces Game")
screen.setup(width=400, height=783)

image = "Vietnam_location_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("63_provinces_vn.csv")
all_provinces = data.province.to_list()
guessed_provinces = []

while len(guessed_provinces) < 63:
    answer_province = screen.textinput(title=f"{len(guessed_provinces)}/63 Provinces Correct",
                                    prompt="What's another province's name?").title()
    if answer_province == "Exit":
        missing_provinces = []
        for province in all_provinces:
            if province not in guessed_provinces:
                missing_provinces.append(province)
        new_data = pandas.DataFrame(missing_provinces)
        new_data.to_csv("provinces_to_learn.csv")
        break
    if answer_province in all_provinces:
        guessed_provinces.append(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer_province, align="center", font=("Arial", 6, "normal"))
