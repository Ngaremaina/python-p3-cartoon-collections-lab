def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(planets):
    capitalized = []
    for planet in planets:
        capitalized_call = planet.capitalize() + "!"
        capitalized.append(capitalized_call)
    return capitalized

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(cheeses):
    for cheese in cheeses:
        if cheese =="cheddar"or cheese ==  "gouda" or cheese ==  "camembert":
            return cheese
    return None

