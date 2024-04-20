def sort_foods_by_date(foods):
    """Sort a list of food objects by expiry date."""
    return sorted(foods, key=lambda food: food.expiry_date)