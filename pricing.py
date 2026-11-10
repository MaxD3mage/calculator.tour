DESTINATIONS = {
    "turkey": {"name": "Турция", "flight": 29_000, "base_night": 4_200},
    "thailand": {"name": "Таиланд", "flight": 61_000, "base_night": 3_600},
    "uae": {"name": "ОАЭ", "flight": 38_000, "base_night": 5_300},
    "russia": {"name": "Сочи, Россия", "flight": 12_000, "base_night": 3_000},
}
DEPARTURE_NAMES = {"ekb": "Екатеринбург", "msk": "Москва", "spb": "Санкт-Петербург"}
DEPARTURE_FEES = {"ekb": 0, "msk": 5_000, "spb": 7_000}
HOTEL_MULTIPLIERS = {"3": 1.0, "4": 1.55, "5": 2.35}
MEAL_PER_PERSON_NIGHT = {"breakfast": 900, "half": 1_800, "all": 3_200}
MEAL_NAMES = {"breakfast": "Завтраки", "half": "Завтрак и ужин", "all": "Все включено"}
SEASON_MULTIPLIERS = {
    "turkey": {"peak": {6, 7, 8}, "shoulder": {5, 9}, "quiet": {10, 11, 12, 1, 2, 3, 4}},
    "thailand": {"peak": {11, 12, 1, 2}, "shoulder": {3, 4, 10}, "quiet": {5, 6, 7, 8, 9}},
    "uae": {"peak": {11, 12, 1, 2, 3}, "shoulder": {4, 5, 10}, "quiet": {6, 7, 8, 9}},
    "russia": {"peak": {6, 7, 8}, "shoulder": {5, 9}, "quiet": {10, 11, 12, 1, 2, 3, 4}},
}
SEASON_RATES = {"peak": 1.25, "shoulder": 1.10, "quiet": 0.90}


def calculate_tour(data):
    destination = DESTINATIONS[data["destination"]]
    adults = data["adults"]
    children = data["children"]
    travelers = adults + children
    nights = data["nights"]
    hotel_multiplier = HOTEL_MULTIPLIERS[data["hotel"]]
    month = data["departure_date"].month
    season = next(
        label
        for label, months in SEASON_MULTIPLIERS[data["destination"]].items()
        if month in months
    )
    season_multiplier = SEASON_RATES[season]

    flight = (destination["flight"] + DEPARTURE_FEES[data["departure"]]) * travelers
    accommodation = round(destination["base_night"] * hotel_multiplier * nights * travelers)
    meals = MEAL_PER_PERSON_NIGHT[data["meal"]] * nights * travelers
    transfer = 5_000 if data.get("transfer") else 0
    insurance = 160 * nights * travelers if data.get("insurance") else 0
    subtotal = flight + accommodation + meals + transfer + insurance
    seasonal_adjustment = round(subtotal * (season_multiplier - 1))
    group_discount = round((subtotal + seasonal_adjustment) * 0.05) if travelers >= 5 else 0
    total = subtotal + seasonal_adjustment - group_discount

    return {
        "destination": destination["name"],
        "departure": DEPARTURE_NAMES[data["departure"]],
        "departure_date": data["departure_date"],
        "nights": nights,
        "travelers": travelers,
        "adults": adults,
        "children": children,
        "hotel": f"{data['hotel']} звезды",
        "meal": MEAL_NAMES[data["meal"]],
        "flight": flight,
        "accommodation": accommodation,
        "meals": meals,
        "transfer": transfer,
        "insurance": insurance,
        "seasonal_adjustment": seasonal_adjustment,
        "season_name": {"peak": "Высокий сезон", "shoulder": "Межсезонье", "quiet": "Низкий сезон"}[season],
        "group_discount": group_discount,
        "total": total,
        "per_person_total": round(total / travelers),
    }
