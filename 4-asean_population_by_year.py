from main import ASEAN_COUNTRIES, population_data, color_codes
import matplotlib.pyplot as plt
import numpy as np


def asean_grouped_data():
    asean_dict = {}
    
    # dict format
    # {
    #     'year1' :{
    #         'country1' : 'population','country2':'population2'
    #     },
    #     'year2':{
    #         ...
    #     }
    # }
    
    for row in population_data:
        if row['Year'] >= '2004' and row['Year'] <= '2014' and row['Region'] in ASEAN_COUNTRIES :
            if row['Year'] in asean_dict:
                asean_dict[row['Year']][row['Region']] = float(row['Population'])
            else:
                asean_dict[row['Year']] = {row['Region'] : float(row['Population'])}
    
    
    population = {}
    # making a list of all countries population by each year
    # {
    #     'country' : ['pop_in_2004','pop_in_2005', and soon]
    # }
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