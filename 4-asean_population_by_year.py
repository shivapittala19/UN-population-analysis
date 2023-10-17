from main import ASEAN_COUNTRIES , population_data
import matplotlib.pyplot as plt
import numpy as np


def asean_grouped_data():
    asean_dict = {} 
    for row in population_data:
        if row['Year'] >= '2004' and row['Year'] <= '2014' and row['Region'] in ASEAN_COUNTRIES :
            if row['Year'] in asean_dict:
                asean_dict[row['Year']][row['Region']] = float(row['Population'])
            else:
                asean_dict[row['Year']] = {row['Region'] : float(row['Population'])}
    
    
    population = {}
    years  = [year for year in asean_dict]
    for country in ASEAN_COUNTRIES:
        population[country] = []
        for year in years:
            if asean_dict[year][country]:
                population[country].append(asean_dict[year][country])
            else:
                population[country].append(0)
    
    width = 0.1
    x = range(len(years))
    color_codes = [
        "#FF5733",  # Red
        "#33FF57",  # Green
        "#FFFF33",  # Yellow
        "#FF33FF",  # Pink
        "#33FFFF",  # Cyan
        "#FF9933",  # Orange
        "#FF33CC",  # Magenta
        "#33CCFF",  # Sky Blue
        "#FFCC33",  # Gold
        "#33FFCC",  # Sea 
        "#CC33FF",  # Lavender
    ]
    for i, country in enumerate(ASEAN_COUNTRIES):
        plt.bar(
            [pos + i * width for pos in x],
            population[country],
            label=country,
            width=width,
            color = color_codes[i]
            )
        plt.legend()
        plt.xticks([pos + 2.5 * width for pos in x], years)
    plt.show()
    
     
asean_grouped_data()