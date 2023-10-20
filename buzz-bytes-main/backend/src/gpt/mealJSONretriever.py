import json
import os

def sortFoodDictionary(foodData):
    # Create a list of tuples (food item, calories)
    food_list = [(food, data["calories"]) for food, data in foodData.items()]
    
    # Sort the list by calories in descending order
    food_list.sort(key=lambda x: x[1], reverse=True)
    
    # Create a new ordered dictionary
    orderedFoodData = {}
    
    # Populate the ordered dictionary with the sorted data
    for food, calories in food_list:
        orderedFoodData[food] = {"calories": calories, "serving": 1}
    
    return orderedFoodData

test = {'Blueberry Pancake': {'calories': 139, 'serving': 1}, 'Scrambled Eggs': {'calories': 30, 'serving': 70}, 'Fresh Fruit': {'calories': 200, 'serving': 1}}
print(sortFoodDictionary(test))
def get_foods(location, meal_type, dietaryRestrictions, json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    if location in data and meal_type in data[location]:
        foods = data[location][meal_type]
        result = json.dumps(foods, indent=4)
        return result
    else:
        return "Location or meal type not found in the JSON data."

def get_calories(full_meal, location, meal_type, json_file):
    mealCalorieSum = 0
    mealDataToReturn = {}

    with open(json_file, 'r') as file:
        data = json.load(file)

    if (location in data) and (meal_type in data[location]):
        foods = data[location][meal_type]

        for foodItem in full_meal:
            try:
                foodDetails = foods[foodItem]
                nutrition_data = foodDetails["nutritionData"]

                if ("nf_calories" in nutrition_data):
                    mealDataToReturn[foodItem] = {
                        "calories": nutrition_data["nf_calories"],
                        "serving": 1
                    }
                    mealCalorieSum += nutrition_data["nf_calories"]


            except KeyError:
                try:
                    foodItem = foodItem.replace(" (Halal)", "").replace(" (Vegetarian)", "")
                    foodDetails = foods[foodItem]
                    nutrition_data = foodDetails["nutritionData"]

                    if ("nf_calories" in nutrition_data):
                        mealDataToReturn[foodItem] = {
                        "calories": nutrition_data["nf_calories"],
                        "serving": 1
                    }
                        mealCalorieSum += nutrition_data["nf_calories"]
                except KeyError:
                    pass
                
    return {
        "constituentFoods": sortFoodDictionary(mealDataToReturn),
        "totalCalories": int(mealCalorieSum)
    }
    