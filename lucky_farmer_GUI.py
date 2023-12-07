import flet as ft
import random


# 定义场景
class Season:
    name = ""
    temperature = (0, 0)
    weathers = {}

    def __init__(self, name, temperature, weathers) -> None:
        self.name = name
        self.temperature = temperature
        self.weathers = weathers


day = 0


class Weather:
    name = ""
    light = (0, 0)
    water = (0, 0)

    def __init__(self, name, light, water) -> None:
        self.name = name
        self.light = light
        self.water = water


seasons = [
    Season(
        name="spring",
        temperature=(10, 25),
        weathers={
            Weather(name="Sunny", light=(80, 80), water=(10, 10)),
            Weather(name="Cloudy", light=(50, 50), water=(20, 20)),
            Weather(name="Light Rain", light=(40, 40), water=(40, 40)),
            Weather(name="Heavy Rain", light=(40, 40), water=(70, 70)),
        },
    ),
    Season(
        name="summer",
        temperature=(25, 40),
        weathers={
            Weather(name="Sunny", light=(100, 100), water=(0, 0)),
            Weather(name="Cloudy", light=(70, 70), water=(10, 10)),
            Weather(name="Light Rain", light=(50, 50), water=(30, 30)),
            Weather(name="Heavy Rain", light=(50, 50), water=(90, 90)),
        },
    ),
    Season(
        name="autumn",
        temperature=(10, 25),
        weathers={
            Weather(name="Sunny", light=(70, 70), water=(10, 10)),
            Weather(name="Cloudy", light=(40, 40), water=(10, 10)),
            Weather(name="Light Rain", light=(30, 30), water=(30, 30)),
            Weather(name="Heavy Rain", light=(30, 30), water=(60, 60)),
        },
    ),
    Season(
        name="winter",
        temperature=(-10, 10),
        weathers={
            Weather(name="Sunny", light=(50, 50), water=(0, 0)),
            Weather(name="Cloudy", light=(40, 40), water=(20, 20)),
            Weather(name="Light Rain", light=(20, 20), water=(40, 40)),
            Weather(name="Heavy Rain", light=(20, 20), water=(50, 50)),
        },
    ),
]


def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )

    def new_day(*e):
        global season, weather, temperature, water, light, day
        day += 1
        season = seasons[0]
        weather = random.choice(list(season.weathers))
        temperature = random.randint(season.temperature[0], season.temperature[1])
        water = random.randint(weather.water[0], weather.water[1])
        light = random.randint(weather.light[0], weather.light[1])

        info_card.content.content.controls=(
                    ft.Text("Day:{}".format(day)),
                    ft.Text("Season:{}".format(season.name)),
                    ft.Text("Date:{}".format(day)),
                    ft.Text("Weather:{}".format(weather.name)),
                    ft.Text("Temperature:{}".format(temperature)),
                    ft.Text("Light:{}".format(light)),
                    ft.Text("Water:{}".format(water)),
                    ft.Divider(),
                    ft.ElevatedButton(text="New Day", on_click=new_day),
        )
    
        page.update()
        print(day)

    info_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ElevatedButton(text="New Day", on_click=new_day),
                ],
            ),
            width=400,
            height=600,
            padding=15,
        )
    )

    # new_day()

    # page.add(color_dropdown, submit_btn, output_text)
    page.title = "Lucky Farmer"
    page.add(info_card)
    page.update()


ft.app(target=main)
