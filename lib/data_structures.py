#!/usr/bin/env python3

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Retrieves names of the spicy foods."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns foods with a heat_level over 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Prints all foods formatted with 🌶 emojis."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the food that matches the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Prints foods with heat_level over 5 formatted with 🌶 emojis."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    """Returns the average of heat_levels in spicy_foods."""
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """Returns the original list of spicy_foods with a new spicy_food added."""
    spicy_foods.append(spicy_food)
    return spicy_foods
