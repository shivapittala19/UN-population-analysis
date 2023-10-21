""" analysing indian population each year"""
import matplotlib.pyplot as plt
from main import population_data


def indian_population():
    """ analysing indian population each year"""
    india_dict = {}
    for row in population_data:
        if row['Region'] == 'India':
            india_dict[row['Year']] = row['Population']
    keys = india_dict.keys()
    values = india_dict.values()
    plt.bar(keys,values)
    plt.show()
    plt.xticks(rotation = 90)

indian_population()
