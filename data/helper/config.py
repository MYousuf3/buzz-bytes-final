from datetime import datetime
from datetime import timedelta

now = datetime.now() + timedelta(days=int(input("Enter timedelta (days): ")))

DINING_HALLS = ["west-village", "north-ave-dining-hall", "brittain"]
MEALS = ["breakfast", "lunch", "dinner"]
URL_DATE = now.strftime("%Y/%m/%d/")
WEEK_INDEX = int(now.strftime("%w"))

print(URL_DATE)

NUTRIONIX_APPLICATION_ID = "xxxxxx"
NUTRIONIX_APPLICATION_KEY = "xxxxxx"
# NUTRIONIX_KEYS = ["food_name", "serving_qty", "serving_unit", "nf_calories", "nf_total_fat", 
#                   "nf_saturated_fat", "nf_cholesterol", "nf_sodium", "nf_total_carbohydrate", 
#                   "nf_dietary_fiber", "nf_sugars", "nf_protein","nf_potassium", "nf_p"]
NUTRIONIX_KEYS = ["nf_calories", "nf_total_fat", "nf_sodium", "nf_sugars", "nf_protein"]

FOOD_TYPE_WHITELIST = ["Vegetarian", "Gluten Friendly", "Halal", "Vegan"]
RESTAURANT_BLACKLIST = ["Ramblin' Coffee", "Ramblin' Sweets", "Hi Rez Pastries",
                        "Assorted Toppings 1", "Assorted Toppings 2",
                        "Dressings", "Dessert", "Salad Bar Toppings"]

def generateNutrisliceURL(diningHall, meal):
    return f"https://techdining.api.nutrislice.com/menu/api/weeks/school/{diningHall}/menu-type/{meal}/{URL_DATE}"

def generateNutrionixCall(query):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": NUTRIONIX_APPLICATION_ID,
        "x-app-key": NUTRIONIX_APPLICATION_KEY,
        "x-remote-user-id": "0"
    }
    data = {"query": query.name}

    return url, headers, data