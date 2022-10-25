def roll_call_dwarves(dwarves):
    order_number = 1
    for dwarf in dwarves:
        print(f'{order_number}. {dwarf}')
        order_number += 1
    pass

def summon_captain_planet(calls):
    i = 0
    while i < (len(calls)):
        calls[i] = calls[i][0].upper() + f'{calls[i][1:]}!'
        i += 1
    
    return calls
    pass

def long_planeteer_calls(words):
    for word in words:
        if(len(word) > 4):
            return True
    
    return False
    pass

def find_the_cheese(foods):
    cheeses = ["cheddar", 'gouda', 'camembert']
    for cheese in cheeses:
        if cheese in foods:
            return cheese
    pass
