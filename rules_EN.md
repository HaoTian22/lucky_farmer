# Lucky Farmer

Welcome to Lucky Farmer game!

---

You are a young enthusiast with a passion for agriculture, dreaming of cultivating a variety of delicious crops on your own farm to feed the world.  
Now, a major food corporation is conducting a global tender for downstream agricultural raw materials.  They have organized a bidding conference, issuing 10 tasks for farmers to complete, with the first to finish gaining the opportunity for an exclusive long-term partnership.  
At this conference, you will engage in fierce competition with several other contestants on a virtual farm.  
However, this is no easy feat; you must strategically plan your planting schedule according to different seasons and weather conditions, purchase and utilize various tools, and even trade or compete with other players.  
Can you complete the tasks first in this challenging and opportunistic farm bidding conference and win the favor of the leading company? Join the game "Lucky Farmer" now, and show off your wisdom and courage!

This is a casual, moderately strategic game, and players are encouraged to communicate during the game.

Game duration is approximately 1-1.5 hours.

## Game Flow

Preparation: Each player takes 10 tokens, placing 9 in front of each "1" to represent 0, and 1 to indicate the current task. This token will later be placed on the icon of the crop required by the task.

At the start of the game, each player draws a seed from 4 basic crop types (Corn, Wheat, Carrot, Potato), gets $100, and draws a mission from 4 basic crop missions.

Next, players take actions in the order shown on the computer (basically is from player 1 to player 4), which will give a menu of possible actions.

Possible actions include (may have others): Wait | Discuss & Trade | Plant | Purchase

Players need to pay attention to the daily [Weather](#weather) and shop items to make appropriate choices, and tell the computer or reflect those on their cards (tips: weather for plant growth is **very important**).

Players not taking actions should press Enter to move to the next round to speed up.

At the start of each season, be mindful to check the store for the seeds that are drawn and put up for sale. (This will be introduced in the [Shop](#shop) section)

Below introduces some game elements:

## Environment

- Each "year" has 4 "seasons"
- Each "season" has 10 "days"
- Each "day" represents one round
- Plant growth requires suitable temperature, sunlight, and water levels
- "Season" decides temperature, daily weather decides water and sunlight levels
- Environment scenes are randomly drawn by the program

## Missions

- Direct winning condition, player completing 10 missions can win the game
- Submitting specific fruit types completes missions
- Draw 1 mission from 4 basic crops at start
- Can submit completed missions any time
- Draw 1 new mission from 8 total immediately after completing one  

## Seeds

- 16 total seeds in game, 8 types, 2 of each type. Players can only hold seeds equal to number of their lands
- Players can trade seeds in shop or between themselves
- Planting consumes 1 seed. Mature plant gives 1 seed back and 1 fruit of that type
- Seeds gain growth points based on conditions, 1 point per satisfied condition (can be calculated automatically)
- Once a plant receives **10 growth points** and is considered mature (indicated by a ✔️), move the token for the corresponding crop on your panel back one number to represent the stored fruit.

## Shop

<a id='shop'></a>

- Players can purchase items from the system (Environment items & Treasure chest)
- Players can sell seeds to the system, then buy seeds back. Sold seeds go into inventory for later draws
- 4 random seeds drawn and put up for sale every 10 days
- Price list:

| Crop | Corn | Wheat | Banana | Carrot | Potato | Apple | Sugarcane | Mushroom |  
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Seeds Buyback Price | 40 | 40 | 60 | 20 | 40 | 40 | 60 | 60 |
| Seeds Sell Price | 60 | 60 | 80 | 40 | 60 | 60 | 80 | 80 |
| Fruit Buyback Price | 50 | 50 | 80 | 40 | 50 | 80 | 80 | 70 |

## Fruit

Once a crop matures, players can choose to either keep it for future task submissions or sell it in exchange for money.

The actions of submitting tasks or selling crops can be performed at any time.

## Environment Items

- Can purchase anytime
- Affects all owned plots (starting next day)
- Item list:

| Item | Effect | Price | Duration |
| :-: | :-: | :-: | :-: |  
| Water Channel | +20 Water | $80 | 15 days |
| Light | +20 Sunlight | $80 | 15 days |  
| Greenhouse | +5 Temperature | $80 | 15 days |
| Land | Get 1 more plot | $400 | Permanent |

## Treasure Chest Items

- Chest 1: $100

| Card | Effect | Duration | Total |
| :-: | :-: | :-: | :-: |
| Steal Crop | Take 1 fruit from target* | One-time | 2 |
| Coupon | 50% off shop items | One-time | 5 |
| Purchase Order | 2x fruit buyback price | One season | 2 |
| Fake Mission | +1 to completed missions | One-time | 1 |

*If there are no fruits in the specified storage repository, the harvested crop will be directly transferred after it matures.

- Chest 2: $150, debuffs for others

| Card | Effect | Duration | Total |
| :---: | :---: | :---: | :---: |
| Ruin Rival | Remove 1 completed mission from target player | One-time | 1 |
| Cold Snap | -5 Temperature | 15 days | 3 |
| Drought | -20 Water | 15 days | 3 |
| Overcast | -20 Sunlight | 15 days | 3 |

## Random Disasters (To-do)

- May occur randomly each new season
- In effect for that season
- Possible events: drought, flooding, cold spell
- Affects all players' plots

## Player Trading

Players can discuss intentions to trade seeds at any time

## Appendix

### Environment Conditions

<a id='weather'></a>

| Season | Temperature (°C) | Weather | Sunlight | Water |
| :-: | :-: | :-: | :-: | :-: |  
| Spring | 10-25 | Sunny | 80 | 10 |
|  |  | Cloudy | 50 | 20 |
|  |  | Light Rain | 40 | 40 |
|  |  | Heavy Rain | 40 | 70 |
| Summer | 25-40 | Sunny | 100 | 0 |  
|  |  | Cloudy | 70 | 10 |
|  |  | Light Rain | 50 | 30 |
|  |  | Heavy Rain | 50 | 90 |
| Fall | 10-25 | Sunny | 70 | 10 |
|  |  | Cloudy | 40 | 10 |
|  |  | Light Rain | 30 | 30 |
|  |  | Heavy Rain | 30 | 60 |  
| Winter | -10-10 | Sunny | 50 | 0 |
|  |  | Cloudy | 40 | 20 |
|  |  | Light Rain | 20 | 40 |
|  |  | Heavy Rain | 20 | 50 |

### Crop Info

| Produce | Temperature (°C) | Sunlight | Water |
| :-: | :-: | :-: | :-: |
| Corn | 20-30 | 60-999 | 60-999 |  
| Wheat | 15-30 | 70-999 | 50-999 |
| Banana | 22-35 | 60-999 | 50-999 |
| Carrot | 0-20 | 40-999 | 60-999 |
| Potato | 5-15 | 70-999 | 40-999 |
| Apple | 10-20 | 80-999 | 60-999 |
| Sugarcane | 20-30 | 60-999 | 80-999 |
| Mushroom | 15-25 | 10-30 | 80-999 |

## Game Design (players can skip)  

### Materials  

**Money**

| Value | Quantity |  
| :-: | :-: |
| $10 | 20 |
| $50 | 20 |
| $100 | 20 |
| $500 | 20 |  

**Item Cards**  

| Item | Quantity |
| :-: | :-: |
| Steal Crop | 2 |
| Coupon | 5 |
| Purchase Order | 2 |  
| Fake Mission | 1 |
| Ruin Rival | 1 |
| Cold Snap | 3 |
| Drought | 3 |
| Overcast | 3 |

**Seeds**  

Numbered and labeled with growing conditions

| Type | Quantity |  
| :-: | :-: |
| Corn | 2 |
| Wheat | 2 | 
| Banana | 2 |
| Carrot | 2 |
| Potato | 2 |
| Apple | 2 |
| Sugarcane | 2 |  
| Mushroom | 2 |  

**Mission Cards**  

Players record then return to deck 

| Mission | Quantity |
| :-: | :-: |
| Corn | 1 |
| Wheat | 1 |
| Banana | 1 |  
| Carrot | 1 |
| Potato | 1 |
| Apple | 1 | 
| Sugarcane | 1 |
| Mushroom | 1 |

Player Sheet (panel): Track personal fruit stores, max 9 each type  

Tokens: **40 in total**, used to indicate the storage capacity in the warehouse (**8 per player**), the number of tasks completed (**1 per player**), and to mark the current task (**1 per player**).

### Open Issues  

+ Player decision and discussion times too long, extends game duration
+ Beginner guidance insufficient, too much upfront info overwhelming
+ Early/late game difference unclear, low difficulty variance leads to boredom
+ Players must simultaneously manage the weather, crops, finances, and other players. With so many factors to consider, it can be overwhelming to keep track of the changing weather, leading to a somewhat hectic gameplay experience.
