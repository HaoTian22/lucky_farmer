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
    Season(name="spring", temperature=(10, 25), weathers={
        Weather(name="Sunny", light=(80, 999), water=(10, 999)),
        Weather(name="Cloudy", light=(50, 999), water=(20, 999)),
        Weather(name="Light Rain", light=(40, 999), water=(40, 999)),
        Weather(name="Heavy Rain", light=(40, 999), water=(70, 999)),
    }),
    Season(name="summer", temperature=(25, 40), weathers={
        Weather(name="Sunny", light=(100, 999), water=(0, 999)),
        Weather(name="Cloudy", light=(70, 999), water=(10, 999)),
        Weather(name="Light Rain", light=(50, 999), water=(30, 999)),
        Weather(name="Heavy Rain", light=(50, 999), water=(90, 999)),
    }),
    Season(name="autumn", temperature=(10, 25), weathers={
        Weather(name="Sunny", light=(70, 999), water=(10, 999)),
        Weather(name="Cloudy", light=(40, 999), water=(10, 999)),
        Weather(name="Light Rain", light=(30, 999), water=(30, 999)),
        Weather(name="Heavy Rain", light=(30, 999), water=(60, 999)),
    }),
    Season(name="winter", temperature=(-10, 10), weathers={
        Weather(name="Sunny", light=(50, 999), water=(0, 999)),
        Weather(name="Cloudy", light=(40, 999), water=(20, 999)),
        Weather(name="Light Rain", light=(20, 999), water=(40, 999)),
        Weather(name="Heavy Rain", light=(20, 999), water=(50, 999)),
    }),
]

class Land:
    plant = None
    plant_points = 0

    def __init__(self, plant) -> None:
        self.plant = plant
        self.plant_points = 0

# 定义玩家
class Player:
    playername = ""
    money = 0
    taskcnt = 0
    lands = []
    fruits = {}
    tasks = []
    props = []

    def __init__(self, playername) -> None:
        self.playername = playername
        self.money = 100
        self.taskcnt = 0
        self.lands = []
        self.fruits = {}
        self.tasks = []
        self.props = []

players = []
players.append(Player("Player 1"))
players.append(Player("Player 2"))
players.append(Player("Player 3"))
players.append(Player("Player 4"))

# 定义任务
class Task:
    discription = ""
    finish = None

    def __init__(self, discription, finish) -> None:
        self.discription = discription
        self.finish = finish

tasks = []

def task_3apple(player):
    if "Apple" not in player.fruits:
        return False
    if player.fruits["Apple"] < 3:
        return False
    player.fruits["Apple"]-=3
    return True
tasks.append(Task(discription="Plant 3 apples", finish=task_3apple))



# 定义道具
class Prop:
    name = ""
    discription = ""
    price = 0
    use = None

    def __init__(self, name, discription, price, use) -> None:
        self.name = name
        self.discription = discription
        self.price = price
        self.use = use

props = []

def use_fertilizer(player):
    print("===Use Fertilizer===")
    print("input land number: ", end="")
    landnum = int(input())
    if landnum not in range(1, len(player.lands)+1):
        print("Invalid land number!")
        return
    land = player.lands[landnum-1]
    land.plant_points+=1
    player.fruits["Fertilizer"]-=1
    print("Use Fertilizer on Land{} successfully!".format(landnum))
props.append(Prop(name="Fertilizer", discription="Use Fertilizer on a land to increase 1 point", price=10, use=use_fertilizer))

# 菜单
class MenuItem:
    name=""
    operation=None

    def __init__(self, name, operation) -> None:
        self.name = name
        self.operation = operation
playermenuitems = []

def menuitem_buyland(player):
    print("===Buy Land===")
    if player.money < 10:
        print("Not enough money!")
        return
    player.money-=10
    player.lands.append(Land(None))
    print("Buy Land successfully!")
playermenuitems.append(MenuItem(name="Buy Land", operation=menuitem_buyland))

def menuitem_buytask(player):
    print("===Add Task===")
    if player.money < 10:
        print("Not enough money!")
        return
    player.money-=10
    player.tasks.append(random.choice(tasks))
    print("Add Task successfully!")
playermenuitems.append(MenuItem(name="Add Task", operation=menuitem_buytask))

def menuitem_finishtask(player):
    print("===Finish Task===")
    for task in range(1, len(player.tasks)+1):
        print("  {}. {}".format(task, player.tasks[task-1].discription))
    taskid = int(input("input task id: "))
    if taskid not in range(1, len(player.tasks)+1):
        print("Invalid task id!")
        return
    task = player.tasks[taskid-1]
    if task.finish(player):
        player.tasks.remove(task)
        player.taskcnt+=1
        print("Task finished!")
    else:
        print("Task not finished :(")
playermenuitems.append(MenuItem(name="Finish Task", operation=menuitem_finishtask))

#  工具函数
def calc_grow(plant, temperature, water, light):
    point = 0
    if temperature in range(plant.temperature[0], plant.temperature[1]+1):
        point+=1
    if water in range(plant.water[0], plant.water[1]+1):
        point+=1
    if light in range(plant.light[0], plant.light[1]+1):
        point+=1
    return point

def print_player(player):
    print("*[{}]*".format(player.playername))

    print("  Lands: ")
    for land in player.lands:
        if land.plant == None:
            print("    Land{}: Empty".format(player.lands.index(land)+1))
        else:
            print("    Land{}: {}, {}'[{}]".format(player.lands.index(land)+1, land.plant.name, land.plant_points, '#'*land.plant_points + '-'*(10-land.plant_points)))

    print("  Money: ${}".format(player.money))

    print("  Fruits: ", end="")
    for item in player.fruits:
        print("{} x{}".format(item, player.fruits[item]), end=" ")
    print()

    print("  Tasks: ")
    for task in player.tasks:
        print("      {}".format(task.discription))

    print("  Props: ", end="")
    for prop in player.props:
        print("{} x{}".format(prop.name, player.props.count(prop)), end=" ")
    print()

def playermenu_print():
    print("===User Menu===")
    print("  0. Exit")
    for item in playermenuitems:
        print("  {}. {}".format(playermenuitems.index(item)+1, item.name))
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
        if select not in range(1, len(playermenuitems)+1):
            print("Invalid select!")
            continue
        playermenuitems[select-1].operation(player)

#
# 主程序
#

# 随机分配植物
for player in players:
    player.lands.append(Land(random.choice(plants)))

# 主循环，包含游戏逻辑
while 1:
    for season in seasons:
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
                    land.plant_points+=calc_grow(land.plant, temperature, water, light)
                    if land.plant_points >= 10:
                        if land.plant.name not in player.fruits:
                            player.fruits[land.plant.name]=0
                        player.fruits[land.plant.name]+=1
                        land.plant_points=0

            # 输出玩家面板
            print("---players---\n")
            for player in players:
                playermenu_use(player)
            #    print_player(player)


            input("Press Enter to continue...")
