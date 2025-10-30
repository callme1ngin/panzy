# pantry/utils.py

DEFAULT_LOCATIONS = [
    {"name": "Холодильник", "color": "#A1DBF1"},
    {"name": "Шкаф", "color": "#C2F1A1"},
    {"name": "Полка", "color": "#F1E3A1"},
    {"name": "Морозильник", "color": "#F1A1A1"},
    {"name": "Балкон", "color": "#BDE1F9"},
    {"name": "Ящик", "color": "#F1B6A1"},
    {"name": "Корзина", "color": "#A1F1B2"},
    {"name": "Погреб", "color": "#B2A1F1"}
]

def create_default_locations():
    from pantry.models import Location
    for loc in DEFAULT_LOCATIONS:
        Location.objects.create(name=loc["name"])

DEFAULT_CATEGORIES = [
    {"name": "Молочные продукты"},
    {"name": "Овощи"},
    {"name": "Фрукты"},
    {"name": "Мясо"},
    {"name": "Бакалея"},
    {"name": "Консервы"},
    {"name": "Заморозка"},
    {"name": "Напитки"},
    {"name": "Сладости"},
    {"name": "Соусы"},
    {"name": "Хлеб"},
    {"name": "Яйца"}
]

def create_default_categories():
    from pantry.models import Category
    for cat in DEFAULT_CATEGORIES:
        Category.objects.create(name=cat["name"])

