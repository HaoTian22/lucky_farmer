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

    def __init__(self, plant) -> None:
        self.plant = plant
        self.plant_points = 0

    def clear(self):
        self.plant = None
        self.plant_points = 0
        self.plant_status = 0

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


# 定义玩家
class Player:
    playername = ""
    lands = []
    buff = []

    def __init__(self, playername) -> None:
        self.playername = playername
        self.lands = []
        self.buff = []


players = []
players.append(Player("Player 1"))
players.append(Player("Player 2"))
players.append(Player("Player 3"))
players.append(Player("Player 4"))


# 定义道具
class Prop:
    name = ""
    duration = 0

    def __init__(self, name, duration) -> None:
        self.name = name
        self.duration = duration

    def use(self, player):
        self.duration -= 1
        if self.duration == 0:
            player.buff.remove(self)


# def use_fertilizer(player):
#     print("===Use Fertilizer===")
#     print("input land number: ", end="")
#     landnum = int(input())
#     if landnum not in range(1, len(player.lands) + 1):
#         print("Invalid land number!")
#         return
#     land = player.lands[landnum - 1]
#     land.plant_points += 1
#     player.fruits["Fertilizer"] -= 1
#     print("Use Fertilizer on Land{} successfully!".format(landnum))

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


# 菜单
class MenuItem:
    name = ""
    operation = None

    def __init__(self, name, operation) -> None:
        self.name = name
        self.operation = operation


playermenuitems = []


# 购买土地
def menuitem_buyland(player):
    print("===Buy Land===")

    if len(player.lands) >= 2:
        print("Land is full!")
        return
    else:
        confirm = input("Buy land? Have enough money? (y/n): ")
        if confirm == "y":
            player.lands.append(Land(None))
            print("✅ Buy Land successfully!")


playermenuitems.append(MenuItem(name="Buy Land", operation=menuitem_buyland))


# 种植作物
def menuitem_plant(player):
    print("===Plant Fruit===")
    try:
        land_num = int(input("Input land number: (1-{}): ".format(len(player.lands))))
        if player.lands[land_num - 1].plant == None:
            plant_num = int(input("Input plant: (1-{}): ".format(len(plants))))
            player.lands[land_num - 1].plant = plants[plant_num - 1]
        else:
            print("🚫 Land is not empty!")
            return
    except:
        print("🚫 Invalid operation!")
        return


playermenuitems.append(MenuItem(name="Plant Fruit", operation=menuitem_plant))


# 使用道具
def menuitem_use(player):
    print("===Use Prop===")
    print("Input prop number (1-{}): ".format(len(props)), end="")
    prop_num = int(input())
    if prop_num not in range(1, len(props) + 1):
        print("🚫 Invalid prop number!")
        return
    player_num = int(input("Input player number (1-4): "))
    if player_num not in range(1, len(players) + 1):
        print("🚫 Invalid player number!")
        return
    players[player_num - 1].buff.append(props[prop_num - 1])


playermenuitems.append(MenuItem(name="Use Prop", operation=menuitem_use))


#  工具函数
def calc_grow(plant, temperature, water, light):
    point = 0
    if temperature in range(plant.temperature[0], plant.temperature[1] + 1):
        point += 1
    if water in range(plant.water[0], plant.water[1] + 1):
        point += 1
    if light in range(plant.light[0], plant.light[1] + 1):
        point += 1
    return point


def print_player(player):
    print("*[{}]*".format(player.playername))

    print("  Lands: ")
    for land in player.lands:
        if land.plant == None:
            print("    Land{}: ❌ Empty".format(player.lands.index(land) + 1))
        elif land.plant_status == 1:
            print(
                "    Land{}: {}, [✅ Ready to harvest]".format(
                    player.lands.index(land) + 1, land.plant.name
                )
            )
        else:
            print(
                "    Land{}: {}, 🕑 {}'[{}]".format(
                    player.lands.index(land) + 1,
                    land.plant.name,
                    land.plant_points,
                    "#" * land.plant_points + "-" * (10 - land.plant_points),
                )
            )

    # print("  Props: ", end="")
    # for prop in player.props:
    #     print("{} x{}".format(prop.name, player.props.count(prop)), end=" ")

    # 玩家状态
    print("  Buff: ")
    for buff in player.buff:
        print("    {}, Duration: {}".format(buff.name, buff.duration))
    print()


def playermenu_print():
    print("===User Menu===")
    print("  0. Exit")
    for item in playermenuitems:
        print("  {}. {}".format(playermenuitems.index(item) + 1, item.name))
    print("===============")


def playermenu_use(player):
    while 1:
        print_player(player)
        playermenu_print()
        print("Select: ", end="")
        select = input()
        if select == "0" or select == "":
            print()
            break
        select = int(select)
        if select not in range(1, len(playermenuitems) + 1):
            print("🚫 Invalid select!")
            continue
        playermenuitems[select - 1].operation(player)


#
# 主程序
#
# 初始化
for player in players:
    player.lands.append(Land(None))

# 主循环，包含游戏逻辑
while 1:
    for season in seasons:
        # disaster = random.choice(["Drought","Cold wave", None],weights=[0.02,0.02,0.96])

        for day in range(1, 11):
            weather = random.choice(list(season.weathers))
            print("\n\n=====[{}, Day {}]=====".format(season.name, day))

            # 输出当天环境数值
            temperature = random.randint(season.temperature[0], season.temperature[1])
            water = random.randint(weather.water[0], weather.water[1])
            light = random.randint(weather.light[0], weather.light[1])
            print("- Weather: ", weather.name)
            print("- Temperature: ", temperature)
            print("- Water: ", water)
            print("- Light: ", light)

            # 输出每种植物生长情况
            print("---plants---")
            for plant in plants:
                point = calc_grow(plant, temperature, water, light)
                print("  {}: {} points".format(plant.name, point))

            # 计算玩家土地生长情况
            for player in players:
                for land in player.lands:
                    if land.plant == None:
                        continue
                    # 生长
                    land.grow(temperature, water, light, player)
                    # 收获
                    if land.plant_status == 1:
                        land.clear()
                    # 更改植物状态
                    if land.plant_points >= 10:
                        land.plant_status = 1

            # 输出玩家面板
            print("---players---\n")
            for player in players:
                playermenu_use(player)
            #    print_player(player)

            input("Press Enter to continue...")
