class CaloriesLibrary:
    def __init__(self):
        self.dish_calories = {
            "pancakes":150,
            "croissants":120, 
            "sandwiches":160, 
            "salad":150, 
            "buger":450, 
            "wraps":350, 
            "latte":220, 
            "soup":350, 
            "smoothies":150, 
            "pasta":350, 
            "americano":50, 
            "cappuccino":250,
            "espresso":250,
            "chai":150,
            "muffins":250,
            "pizza":450,
            "spaghetti":350,
        }

    def add_dish(self, dishName, calories):
        self.dish_calories[dishName] = calories
        
        
    def getCalories(self,dishName):
        return self.dish_calories.get(dishName,0)