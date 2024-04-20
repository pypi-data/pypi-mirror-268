# food_pricing/calculator.py

class FoodPriceCalculator:
    @staticmethod
    def calculate_total_price(food_items):
        total_price = sum(item['price'] for item in food_items)
        return total_price
