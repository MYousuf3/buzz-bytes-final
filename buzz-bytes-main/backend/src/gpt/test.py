# [197, 127, 22, 2] (3, 2, 3, 1)
# [527, 165, 30, 15] (2, 1, 1, 1)
# [114, 22, 15] (3, 3, 3)
# [100, 63] (3, 3)
# [200, 45, 19, 3] (3, 3, 3, 3)

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
        return (3,3,3)
    elif len(args) == 4:
        for meal2Serving in range(1, 4):
            for meal1Serving in range(1, 4):
                for meal3Serving in range(1, 4):
                    for meal4Serving in range(1, 4):
                        totalCalories = meal1Serving * args[0] + meal2Serving * args[1] + meal3Serving * args[2] + meal4Serving * args[3]
                        if totalCalories > targetCal:
                            return (meal1Serving, meal2Serving, meal3Serving, meal4Serving)
        return (3,3,3,3)

print(mealDirector(900, *[197, 127, 22, 2]))
print(mealDirector(900, *[527, 165, 30, 15]))
print(mealDirector(900, *[114, 22, 15]))
print(mealDirector(900, *[100, 63]))