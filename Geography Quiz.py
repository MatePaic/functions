import random

def quiz():
    countries_dict = {"Croatia": "Zagreb", "Spain": "Madrid", "Austria": "Vienna", "Slovenia": "Ljubljana",
                      "Italy": "Rome", "Germany": "Berlin", "France": "Paris", "Hungary": "Budapest"}

    for country in countries_dict:
        country = random.choice(list(countries_dict))
        question = input(f'What is the capital city of {country}? \nUser: ').title()
        if question == countries_dict[country]:
            return 'Game: This is correct'
        else:
            return  'Game: This is not correct'

print(quiz())
