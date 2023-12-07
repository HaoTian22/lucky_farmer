import flet as ft
import random


# 定义植物
class Plant:
    name = ""
    temperature = (0, 0)
    light = (0, 0)
    water = (0, 0)

    def __init__(self, name, temperature, light, water) -> None:
        self.name = name
        self.temperature = temperature
        self.light = light
        self.water = water


plants = [
    Plant(name="Corn", temperature=(20, 30), light=(60, 999), water=(70, 999)),
    Plant(name="Wheat", temperature=(20, 30), light=(70, 999), water=(50, 999)),
    Plant(name="Banana", temperature=(25, 30), light=(40, 999), water=(50, 999)),
    Plant(name="Carrot", temperature=(20, 30), light=(40, 999), water=(60, 999)),
    Plant(name="Potato", temperature=(10, 20), light=(70, 999), water=(20, 999)),
    Plant(name="Apple", temperature=(12, 24), light=(70, 999), water=(10, 999)),
    Plant(name="Sugar Cane", temperature=(20, 30), light=(80, 999), water=(80, 999)),
    Plant(name="Mushroom", temperature=(15, 25), light=(10, 30), water=(80, 999)),
]


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


class Land:
    plant = None
    plant_points = 0
    plant_status = 0
    display = None

    # 更改所有作物数值的值都在这里，只能改数值，不能重新创建组件
    def __init__(self, plant) -> None:
        self.plant = plant
        self.plant_points = 0
        if plant != None:
            self.display = ft.Row(
                [ft.Text(self.plant.name),ft.Text(self.plant_points), ft.ProgressBar(width=100, value=0)]
            )
        else:
            self.display = ft.Row(
                [ft.Text("❌ Empty"), ft.ProgressBar(width=100, value=0)]
            )

    # 种植作物
    def grow_crops(self,plant):
        self.plant=plant
        self.display.controls[0].value = self.plant.name

    # 收获
    def harvest(self):
        self.plant_status = 1
        self.display.controls[0].value = "✅" + self.plant.name
        print("✅Harvest")

    # 清除
    def clear(self):
        self.plant = None
        self.plant_points = 0
        self.plant_status = 0
        self.display.controls[0].value = "❌ Empty"
        self.display.controls[2].value = 0

    # 成长
    def grow(self, temperature, water, light, player):
        # 计算玩家道具效果
        for buff in player.buff:
            if buff.name == "Grow light":
                light += 20
                buff.use(player)
            if buff.name == "Water Pump":
                water += 20
                buff.use(player)
            if buff.name == "Greenhouse":
                temperature += 5
                buff.use(player)
            if buff.name == "Cold wave":
                temperature -= 5
                buff.use(player)
            if buff.name == "Drought":
                water -= 10
                buff.use(player)
            if buff.name == "Cloudy":
                water -= 10
                buff.use(player)

        self.plant_points += calc_grow(self.plant, temperature, water, light)
        self.display.controls[1].value = self.plant_points
        self.display.controls[2].value = self.plant_points / 10


def calc_grow(plant, temperature, water, light):
    point = 0
    if temperature in range(plant.temperature[0], plant.temperature[1] + 1):
        point += 1
    if water in range(plant.water[0], plant.water[1] + 1):
        point += 1
    if light in range(plant.light[0], plant.light[1] + 1):
        point += 1
    return point


def main(page: ft.Page):
    def new_day(*e):
        global season, weather, temperature, water, light, day
        day += 1
        season = seasons[(day - 1) // 10 % 4]
        weather = random.choice(list(season.weathers))
        temperature = random.randint(season.temperature[0], season.temperature[1])
        water = random.randint(weather.water[0], weather.water[1])
        light = random.randint(weather.light[0], weather.light[1])

        # 输出数值
        #       card      container column
        info_card.content.content.controls = [
            ft.Text("📅Day: {}".format(day),size=30),
            ft.Text("🌏Season: {}".format(season.name)),
            ft.Text("📆Date: {}".format(10 if day % 10 == 0 else day % 10)),
            ft.Text("🌈Weather: {}".format(weather.name)),
            ft.Text("🌡️Temperature: {}".format(temperature)),
            ft.Text("💡Light: {}".format(light)),
            ft.Text("💧Water: {}".format(water)),
            ft.Divider(),
        ]

        # 植物计算与输出
        for plant in plants:
            point = calc_grow(plant, temperature, water, light)
            info_card.content.content.controls.append(
                ft.Text("{}: {} points".format(plant.name, point))
            )
            print("  {}: {} points".format(plant.name, point))

        # 下一天按钮
        info_card.content.content.controls.append(
            ft.ElevatedButton(
                text="Next Day", on_click=new_day, icon=ft.icons.BEDTIME_ROUNDED
            ),
        )

        # 计算玩家土地生长情况
        for player in players:
            for land in player.lands:
                if land.plant == None:
                    continue
                # 生长
                if land.plant_status == 0:
                    land.grow(temperature, water, light, player)
                # 收获
                if land.plant_status == 1:
                    land.clear()
                # 更改植物状态
                if land.plant_points >= 10:
                    land.harvest()
                page.update()

        page.update()
        print(day)

    # 场景信息卡
    info_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ElevatedButton(
                        text="Start", on_click=new_day, icon=ft.icons.PLAY_ARROW_ROUNDED
                    ),
                ],
            ),
            width=400,
            height=600,
            padding=15,
        )
    )

    # 玩家界面
    class Player:
        playername = ""
        lands = []
        buff = []
        player_card = None
        land_display = ft.Column([])

        def __init__(self, playername, land) -> None:
            self.playername = playername
            self.lands = [land]
            self.buff = []
            for l in self.lands:
                self.land_display = l.display
            self.player_card = ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(playername),
                                    ft.Text("Lands: "),
                                    self.land_display,
                                    ft.Text("Buffs: "),
                                ],
                                width=300,
                            ),
                            ft.Column(
                                [
                                    ft.OutlinedButton(
                                        "Plant", on_click=self.menuitem_plant
                                    ),
                                    ft.OutlinedButton("Use prop"),
                                    ft.OutlinedButton("Buy land"),
                                ],
                            ),
                        ],
                    ),
                    padding=10,
                ),
                width=500,
                height=140,
            )

        def menuitem_plant(self, e):
            land_num = int(input("Input land number: (1-{}): ".format(len(self.lands))))
            if self.lands[land_num - 1].plant == None:
                plant_num = int(input("Input plant: (1-{}): ".format(len(plants))))
                # self.lands[land_num - 1].plant = plants[plant_num - 1]
                self.lands[land_num - 1].grow_crops(plants[plant_num - 1])
                page.update()
            else:
                print("🚫 Land is not empty!")
                return

    players = []
    players.append(Player("Player 1", Land(plants[1])))
    players.append(Player("Player 2", Land(None)))
    players.append(Player("Player 3", Land(None)))
    players.append(Player("Player 4", Land(None)))

    players_card = ft.Column([])
    for player in players:
        players_card.controls.append(player.player_card)

    # page.add(color_dropdown, submit_btn, output_text)
    # 主界面布局
    page.title = "Lucky Farmer"
    page.add(
        ft.Row(
            [
                info_card,
                ft.VerticalDivider(),
                players_card,
            ]
        )
    )
    page.update()


ft.app(target=main)
