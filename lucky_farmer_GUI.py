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
                [
                    ft.Text(self.plant.name),
                    ft.Text(self.plant_points),
                    ft.ProgressBar(width=100, value=0),
                ]
            )
        else:
            self.display = ft.Row(
                [
                    ft.Text("❌ Empty"),
                    ft.Text(self.plant_points),
                    ft.ProgressBar(width=100, value=0),
                ]
            )

    # 种植作物
    def grow_crops(self, plant):
        self.plant = plant
        self.display.controls[0].value = self.plant.name

    # 收获
    def harvest(self):
        self.plant_status = 1
        self.display.controls[0].value = "✅ " + self.plant.name
        print("✅Harvest")

    # 清除
    def clear(self):
        self.plant = None
        self.plant_points = 0
        self.plant_status = 0
        self.display.controls[1].value = 0
        self.display.controls[0].value = "❌ Empty"
        self.display.controls[2].value = 0

    # 成长
    def grow(self, temperature, water, light, player):
        # 计算玩家道具效果
        for buff in player.buffs:
            if buff.name == "Grow light":
                light += 20
            if buff.name == "Water Pump":
                water += 20
            if buff.name == "Greenhouse":
                temperature += 5
            if buff.name == "Cold wave":
                temperature -= 5
            if buff.name == "Drought":
                water -= 10
            if buff.name == "Cloudy":
                water -= 10

        self.plant_points += calc_grow(self.plant, temperature, water, light)
        self.display.controls[1].value = self.plant_points
        self.display.controls[2].value = self.plant_points / 10

# 定义道具
class Prop:
    name = ""
    duration = 0

    def __init__(self, name, duration) -> None:
        self.name = name
        self.duration = duration
        self.display = ft.Row(
                [
                    ft.Text(self.name),
                    ft.Text(self.duration),
                ]
            )

    def use(self, player):
        self.duration -= 1
        self.display.controls[1].value = self.duration
        print(self.name, self.duration)
        # 结束清除道具
        if self.duration == 0:
            player.buffs.remove(self)
            player.buffs_column.controls.remove(self.display)
    
    def apply(self, player):
        player.buffs.append(self)
        self.display.controls[1].value = self.duration
    @classmethod
    def create_copy(cls, original_prop):
        # Create a new instance of Prop with the same attributes
        return cls(name=original_prop.name, duration=original_prop.duration)


props = [
    Prop(
        name="Greenhouse",
        duration=20,
    ),
    Prop(
        name="Water Pump",
        duration=20,
    ),
    Prop(
        name="Grow light",
        duration=20,
    ),
    Prop(
        name="Cold wave",
        duration=10,
    ),
    Prop(
        name="Drought",
        duration=10,
    ),
    Prop(
        name="Cloudy",
        duration=10,
    ),
]


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
    # 主要的计算逻辑(需要与全部事情关联)
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
            ft.Text("📅Day: {}".format(day) ,size=30),
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

        # 道具计算与输出

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

            for buff in player.buffs:
                buff.use(player)
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

    # 定义玩家
    # 基本上全部操作都在这里
    # 函数有: 打开种子弹窗、使用种子、购买土地
    class Player:
        playername = ""
        lands = []
        buffs = []
        player_card = None

        def __init__(self, playername, land) -> None:
            self.playername = playername
            self.lands = [land]
            self.buffs = []

            # 定义地皮展示
            self.lands_column = ft.Column(spacing=0)
            for l in self.lands:
                self.lands_column.controls.append(l.display)
            
            # 定义道具显示
            self.buffs_column = ft.Column(spacing=0,wrap=True,height=60)
            for b in self.buffs:
                self.buffs_column.controls.append(b.display)

            # 玩家界面展示(静态)
            self.player_card = ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(playername),
                                    # 显示土地
                                    ft.Row([ft.Text("Lands: "),self.lands_column,]),
                                    # 显示道具
                                    ft.Row([ft.Text("Buffs: "),self.buffs_column]),      
                                ],
                                width=300,
                                spacing=0,
                            ),
                            ft.Column(
                                [
                                    ft.OutlinedButton(
                                        "Plant", on_click=self.open_seed_popups
                                    ),
                                    ft.OutlinedButton("Use prop",on_click=self.open_prop_popups),
                                    ft.OutlinedButton("Buy land",on_click=self.menuitem_buy_land),
                                ],
                            ),
                        ],
                    ),
                    padding=10,
                ),
                width=500,
                height=140,
            )

            # 种植弹窗
            self.grow_popups = ft.AlertDialog(
                title=ft.Text("Select Land & Seed                        "),
                content=ft.Text("Please select your land and seed to grow."),
                actions=[
                    ft.Dropdown(
                        width=50,
                        options=[ft.dropdown.Option("1"), ft.dropdown.Option("2")],
                    ),
                    ft.Dropdown(
                        width=150,
                        options=[],
                    ),
                    ft.TextButton("Grow", on_click=self.menuitem_plant),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            # 种植弹窗添加植物
            for plant in plants:
                self.grow_popups.actions[1].options.append(ft.dropdown.Option(plant.name))
            self.player_card.content.content.controls.append(self.grow_popups)


            # 选择道具弹窗
            self.prop_popups = ft.AlertDialog(
                title=ft.Text("Select Player & Prop                        "),
                content=ft.Text("Please select your prop player to use."),
                actions=[
                    ft.Dropdown(
                        width=50,
                        options=[ft.dropdown.Option("1"), ft.dropdown.Option("2"),ft.dropdown.Option("3"),ft.dropdown.Option("4")],
                    ),
                    ft.Dropdown(
                        width=150,
                        options=[],
                    ),
                    ft.TextButton("Use", on_click=self.menuitem_use),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            for prop in props:
                self.prop_popups.actions[1].options.append(ft.dropdown.Option(prop.name))
            self.player_card.content.content.controls.append(self.prop_popups)

        # 打开选择种子窗口
        def open_seed_popups(self, e):
            self.grow_popups.open = True
            page.update()

        def open_prop_popups(self, e):
            self.prop_popups.open = True
            page.update()

        # 种植
        def menuitem_plant(self, e):
            # land_num = int(input("Input land number: (1-{}): ".format(len(self.lands))))
            land_num = int(self.grow_popups.actions[0].value)
            for i in range(len(plants)):
                if plants[i].name == self.grow_popups.actions[1].value:
                    plant_num = i
                    break
            if land_num > len(self.lands):
                print("🚫 Invalid land number!")
                return
            if self.lands[land_num - 1].plant == None:
                # plant_num = int(input("Input plant: (1-{}): ".format(len(plants))))
                # self.lands[land_num - 1].plant = plants[plant_num - 1]
                self.lands[land_num - 1].grow_crops(plants[plant_num])
                self.grow_popups.open = False
                page.update()
            else:
                print("🚫 Land is not empty!")
                return
        
        # 使用道具
        def menuitem_use(self, e):
            # prop_num = int(input("Input prop number (1-{}): ".format(len(props))))
            for i in range(len(props)):
                if props[i].name == self.prop_popups.actions[1].value:
                    prop_num = i
                    break
                # print("🚫 Invalid prop number!")
                # return
            player_num = int(self.prop_popups.actions[0].value)
            players[player_num - 1].get_buff(Prop.create_copy(props[prop_num]))
            self.prop_popups.open = False
            page.update()

        def get_buff(self, prop):
            self.buffs.append(prop)
            self.buffs_column.controls.append(self.buffs[-1].display)
            page.update()

        # 购买土地
        def menuitem_buy_land(self, e):
            print("===Buy Land===")
            if len(self.lands) >= 2:
                print("Land is full!")
                return
            else:
                # confirm = input("Buy land? Have enough money? (y/n): ")
                # if confirm == "y":
                self.lands.append(Land(None))
                self.lands_column.controls.append(self.lands[-1].display)
                page.update()
                print("✅ Buy Land successfully!")

    # 添加玩家
    players = []
    players.append(Player("Player 1", Land(None)))
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
