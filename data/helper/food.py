class Food:
    def __init__(self, name, diningHall, restaurant, foodType, nutritionData):
        self.name = name
        self.diningHall = diningHall
        self.restaurant = restaurant
        self.foodType = foodType
        self.nutritionData = nutritionData

    def __str__(self):
        return f"{self.name} from {self.restaurant} from {self.diningHall} with types: {self.foodType}"

    def hasNutritionData(self):
        return bool(self.nutritionData)
    
    #vegetarian, vegan, halal, gluten friendly