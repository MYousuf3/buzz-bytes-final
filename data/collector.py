from helper.food import Food
from helper.config import *
import requests
import json

outputData = {}

# with open("data/datasets/ALL_FOOD_10-15-23.json", "r") as file:
#     outputData = json.load(file)

for diningHall in ["north-ave-dining-hall"]:#, "north-ave-dining-hall", "brittain"]:
    for meal in ["dinner"]:#["breakfast", "lunch", "dinner"]:

        URL = generateNutrisliceURL(diningHall, meal)

        response = requests.get(URL, headers={"Content-Type": "application/json"})
        data = response.json()

        currentRestaurant = ""
        menuItems = data["days"][WEEK_INDEX]["menu_items"]
        foodItems = []

        for menuItem in menuItems:
            if menuItem["is_section_title"]:
                currentRestaurant = menuItem["text"]
            
            else:
                foodDetails = menuItem["food"]

                if (foodDetails != None) and (currentRestaurant not in RESTAURANT_BLACKLIST):
                    foodItems.append(Food(
                        name=foodDetails["name"],
                        diningHall=DINING_HALLS[0],
                        restaurant=currentRestaurant,
                        foodType=[foodType["name"] for foodType in foodDetails["icons"]["food_icons"] if foodType["name"] in FOOD_TYPE_WHITELIST],
                        nutritionData={}
                    ))

        for foodItem in foodItems:
            nUrl, nHeaders, nData = generateNutrionixCall(foodItem)

            response = requests.post(
                url=f"https://trackapi.nutritionix.com/v2/natural/nutrients",
                data=nData,
                headers=nHeaders,
            )
            data = response.json()
            print("\n", data)

            try:
                returnData = data["foods"][0]
                nutritionData = {
                    key : returnData[key] for key in NUTRIONIX_KEYS
                }

                foodItem.nutritionData = nutritionData
            except KeyError:
                pass

        for foodItem in foodItems:
            outputData[diningHall][meal][foodItem.name] = {
                "type": foodItem.foodType,
                "restaurant": foodItem.restaurant,
                "nutritionData": foodItem.nutritionData
            }


# dataToSave = json.dumps(outputData, indent=4)
# with open("data/datasets/ALL_FOOD_10-15-23.json", "w") as file:
#     file.write(dataToSave)