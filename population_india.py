""" analysing indian population each year"""
import matplotlib.pyplot as plt
import main

def indian_population():
    """ analysing indian population each year"""
    population_data = main.load_csv('population-estimates_csv.csv')
    india_dict = {}
    for record in population_data:
        if record['Region'] == 'India':
            india_dict[record['Year']] = record['Population']
    year = india_dict.keys()
    population = india_dict.values()
    plt.bar(year,population)
    plt.xlabel("year")
    plt.ylabel("population")
    plt.title("Indian population in each year")
    plt.xticks(rotation = 90)
    plt.show()

indian_population()
