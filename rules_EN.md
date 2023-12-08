# Lucky Farmer

Here, players are treated as individual farmers, and their goal is to complete orders as soon as possible by planting and selling crops. 

This is a casual, moderately strategic game, and players are encouraged to communicate during the game.

Game duration is approximately 1-1.5 hours.

## Game Flow

At the start of the game, each player draws a seed from 4 basic crop types, gets $100, and draws a mission from 4 basic crop missions.

Next, players take actions in the order shown on the computer, which will give a menu of possible actions. 

Possible actions include (may have others): Wait | Trade | Plant | Shop

Players need to pay attention to the daily [Weather](#weather) and shop items to make appropriate choices, and tell the computer or reflect those on their cards.

Players not taking actions should press Enter to move to the next round.

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

- 16 total seeds in game, 8 types, 2 of each type. Players can only hold seeds equal to number of their plots
- Players can trade in shop or between themselves
- Planting consumes 1 seed. Mature plant gives 1 seed and 1 fruit of that type
- Seeds gain growth points based on conditions, 1 point per satisfied condition (can be calculated automatically)
- 10 growth points = mature

## Shop 

- Players can purchase items from the system
- Players can sell seeds to the system, then buy seeds back. Sold seeds go into inventory for later draws
- 4 random seeds drawn and put up for sale every 20 days
- Price list:

| Produce | Corn | Wheat | Banana | Carrot | Potato | Apple | Sugarcane | Mushroom |  
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Buyback Price | 40 | 40 | 40 | 30 | 40 | 40 | 60 | 60 |
| Sell Price | 80 | 80 | 80 | 70 | 80 | 80 | 100 | 100 |

## Fruit

Mature plants can be harvested for fruit. Players can choose to keep for later mission turn-ins or sell for $50.

Turning in or selling can be done anytime.

## Environment Items 

- Can purchase anytime
- Affects all owned plots (starting next day) 
- Item list:

| Item | Effect | Price | Duration |
| :-: | :-: | :-: | :-: |  
| Water Channel | +20 Water | $150 | 20 days |
| Light | +20 Sunlight | $150 | 20 days |  
| Greenhouse | +5 Temperature | $150 | 20 days |
| Land | Get 1 more plot | $400 | Permanent |

## Treasure Chest Items

- Chest 1: $100 

| Card | Effect | Duration | Total |
| :-: | :-: | :-: | :-: |
| Steal Crop | Take 1 fruit from target | One-time | 2 |
| Coupon | 50% off shop items | One-time | 5 | 
| Purchase Order | 2x fruit sell price | One season | 2 |
| Fake Mission | +1 to completed missions | One-time | 1 |

- Chest 2: $150, debuffs for others

| Card | Effect | Duration | Total |
| :---: | :---: | :---: | :---: |
| Ruin Rival | Remove 1 completed mission from target | One-time | 1 |   
| Cold Snap | -5 Temperature | 10 days | 3 |
| Drought | -20 Water | 10 days | 3 |
| Overcast | -20 Sunlight | 10 days | 3 |

## Random Disasters

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
| Corn | 20-30 | 60-999 | 70-999 |  
| Wheat | 20-30 | 70-999 | 50-999 |
| Banana | 25-30 | 40-999 | 50-999 |
| Carrot | 20-30 | 40-999 | 60-999 |
| Potato | 10-20 | 70-999 | 20-999 |
| Apple | 12-24 | 70-999 | 10-999 | 
| Sugarcane | 20-30 | 80-999 | 80-999 |
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

Player Sheet: Track personal fruit stores, max 9 each type  

### Open Issues  

+ Player decision and discussion times too long, extends game duration
+ Beginner guidance insufficient, too much upfront info overwhelming
+ Early/late game difference unclear, low difficulty variance leads to boredom
