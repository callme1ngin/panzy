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
    {"name": "Молочные продукты", "icon": "milk"},
    {"name": "Овощи", "icon": "vegetables"},
    {"name": "Фрукты", "icon": "fruits"},
    {"name": "Мясо", "icon": "meat"},
    {"name": "Бакалея", "icon": "groceries"},
    {"name": "Консервы", "icon": "canned"},
    {"name": "Заморозка", "icon": "frozen"},
    {"name": "Напитки", "icon": "drinks"},
    {"name": "Сладости", "icon": "sweets"},
    {"name": "Соусы", "icon": "sauces"},
    {"name": "Хлеб", "icon": "bread"},
    {"name": "Яйца", "icon": "eggs"},
]


def create_default_categories():
    from pantry.models import Category
    for cat in DEFAULT_CATEGORIES:
        Category.objects.create(name=cat["name"], icon_name=cat["icon"])



DEFAULT_UNITS = [
    {"name": "шт"},
    {"name": "граммы"},
    {"name": "килограммы"},
    {"name": "миллилитры"},
    {"name": "литры"},
    {"name": "чашки"},
    {"name": "столовые ложки"},
    {"name": "чайные ложки"},
    {"name": "унции"},
    {"name": "фунты"},
    {"name": "жидкие унции"}
]

def create_default_units():
    from pantry.models import Unit
    for unit in DEFAULT_UNITS:
        Unit.objects.create(name=unit["name"])




