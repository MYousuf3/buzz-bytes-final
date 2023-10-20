import openai
import re
#from validMeal import validMeal
from src.gpt.mealJSONretriever import get_foods, get_calories
from src.gpt.validMeal import mealDirector
import json
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPEN-AI-KEY")

def extract_lists(input_string):
    # Regular expression pattern to match lists in the input string
    pattern = r'\[([^\]]+)\]'
    
    # Find all matches of the pattern in the input string
    list_matches = re.findall(pattern, input_string)
    
    # Initialize an empty list to store the parsed lists
    parsed_lists = []
    
    # Iterate over the list matches and convert them to actual lists
    for match in list_matches:
        # Split the matched string into individual elements
        elements = [element.strip().replace('"', '') for element in match.split(',')]
        # Append the elements as a list to the parsed_lists
        parsed_lists.append(elements)
    
    return parsed_lists

def apiCall(location, meal, targetCalories, dietaryRestrictions):
  dietaryRestrictions = eval(dietaryRestrictions)
  targetCalories = int(targetCalories)
  finalFoodData = {
     "meals": [
        
     ]
  }
  calorieRange = f"{targetCalories-50} - {targetCalories+50}"
  if len(dietaryRestrictions) != 0:
    if (dietaryRestrictions == "halal"):
      dietaryRestrictions = "halal or vegetarian or vegan"
    elif (dietaryRestrictions == "vegetarian"):
      dietaryRestrictions = "vegetarian or vegan"
    additionalParam = f"Every meal item should EXPLICITLY have {dietaryRestrictions} in the type array."
  else:
    additionalParam = ""

  inputPrompt = "From these menu options, I want you to construct 5 different meals very close to " + calorieRange + " calories based on the provided meal options." + additionalParam + "I want each meal to have at most 4 items. Give 5 arrays of length <= 4 separated by commas. For example, a complete response would be: \n\n[\"Hamburger\", \"Fries\", \"Berries\", \"Water\"],[\"Cheese Pizza\", \"Broccoli\", \"Strawberries\"],[\"Greek Yogurt\", \"Granola\", \"Blueberries\", \"Milk\"],[\"Prime Rib with Au Jus\", \"Grilled Asparagus\"],[\"Herb Roasted Chicken\", \"Roasted Carrots\", \"Steamed Broccoli\"]\n\n\nDo not output the same food more than one time. In your response, only include the arrays and DO NOT WAIVER FROM THIS FORMAT OR INCLUDE ANY OTHER WORDS AND ENSURE THE CALORIES FALL IN THE GIVEN RANGE."
  stringMeals = get_foods(location, meal, dietaryRestrictions, "src/gpt/data/ALL_FOOD_10-16-23.json")

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
      {
        "role": "system",
        "content": inputPrompt
      },
      {
        "role": "user",
        "content": stringMeals
      }
    ],
    temperature=0.7,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  extractedResponse = response['choices'][0]['message']['content']
  cleanedResponses = extract_lists(extractedResponse)

  for fullMeal in cleanedResponses:
    finalFoodData["meals"].append(get_calories(fullMeal, location, meal, "src/gpt/data/ALL_FOOD_10-16-23.json"))

  for meal in finalFoodData["meals"]:
    foodItems = meal["constituentFoods"]

    totalCalories = 0
    foodCalories = [int(i["calories"]) for i in foodItems.values()]
    foodQuantity =  mealDirector(targetCalories, *foodCalories)
    keys = list(foodItems.keys())

    print(foodCalories, foodQuantity)

    for i in range(len(foodCalories)):
        calorie, quantity = foodCalories[i], foodQuantity[i]
        totalCalories += (calorie * quantity)

        meal["constituentFoods"][keys[i]]["serving"] = foodQuantity[i]

    meal["totalCalories"] = totalCalories

    finalFoodData["meals"][0] = meal

  print(finalFoodData)

  return finalFoodData