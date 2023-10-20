def mealDirector(targetCal, *args):
    if len(args) == 1:
        for meal1Serving in range(1,5):
            totalCalories = meal1Serving * args[0]
            if totalCalories > targetCal:
                return (meal1Serving,)
        return (3,)
    elif len(args) == 2:
        for meal2Serving in range(1, 4):  # Ensure at least 1 serving and at most 3 servings of meal2
            for meal1Serving in range(1, 4):  # Ensure at least 1 serving and at most 3 servings of meal1
                totalCalories = meal1Serving * args[0] + meal2Serving * args[1]
                if totalCalories > targetCal:
                    return (meal1Serving, meal2Serving)
        return (3,3)
    elif len(args) == 3:
        for meal2Serving in range(1, 4):
            for meal1Serving in range(1, 4):
                for meal3Serving in range(1, 4):
                    totalCalories = meal1Serving * args[0] + meal2Serving * args[1] + meal3Serving * args[2]
                    if totalCalories > targetCal:
                        return (meal1Serving, meal2Serving, meal3Serving)
        return (2,3,3)
    elif len(args) == 4:
        for meal2Serving in range(1, 4):
            for meal1Serving in range(1, 4):
                for meal3Serving in range(1, 4):
                    for meal4Serving in range(1, 4):
                        totalCalories = meal1Serving * args[0] + meal2Serving * args[1] + meal3Serving * args[2] + meal4Serving * args[3]
                        if totalCalories > targetCal:
                            return (meal1Serving, meal2Serving, meal3Serving, meal4Serving)
        return (2,2,2,2)

# def mealDirector(targetCal, *args):
#     if len(args) == 2:
#         validMeal(args[0], args[1], targetCal)
#     elif len(args) == 3:
#         validMeal(args[0], args[1], args[2], targetCal)
#     elif len(args) == 4:
#         validMeal(args[0], args[1], args[2], args[3], targetCal)

# def validMeal(meal1Cal, meal2Cal, targetCal):
#     for meal2Serving in range(1, 4):  # Ensure at least 1 serving and at most 3 servings of meal2
#         for meal1Serving in range(1, 4):  # Ensure at least 1 serving and at most 3 servings of meal1
#             totalCalories = meal1Serving * meal1Cal + meal2Serving * meal2Cal
#             if totalCalories > targetCal:
#                 return meal1Serving, meal2Serving
#     return None  # Return None if no valid combination is found

# def validMeal(meal1Cal, meal2Cal, meal3Cal, targetCal):
#     for meal2Serving in range(1, 4):
#         for meal1Serving in range(1, 4):
#             for meal3Serving in range(1, 4):
#                 totalCalories = meal1Serving * meal1Cal + meal2Serving * meal2Cal + meal3Serving * meal3Cal
#                 if totalCalories > targetCal:
#                     return meal1Serving, meal2Serving, meal3Serving
#     return None

# def validMeal(meal1Cal, meal2Cal, meal3Cal, meal4Cal, targetCal):
#     for meal2Serving in range(1, 4):
#         for meal1Serving in range(1, 4):
#             for meal3Serving in range(1, 4):
#                 for meal4Serving in range(1, 4):
#                     totalCalories = meal1Serving * meal1Cal + meal2Serving * meal2Cal + meal3Serving * meal3Cal + meal4Serving * meal4Cal
#                     if totalCalories > targetCal:
#                         return meal1Serving, meal2Serving, meal3Serving, meal4Serving
#     return None