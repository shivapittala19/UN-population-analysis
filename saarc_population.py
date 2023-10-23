""" saarc country population analysis"""
import matplotlib.pyplot as plt
import main

def saarc_country_plot():
    """ saarc country population analysis"""
    population_data = main.load_csv('population-estimates_csv.csv')
    sarrc_countries = main.saarc_country()
    sarrc_population = {}
    for record in population_data:
        if record['Region'] in sarrc_countries:
            year = record['Year']
            population = float(record['Population'])
            if year in sarrc_population:
                sarrc_population[year] += population
            else:
                sarrc_population[year] = population
    year = sarrc_population.keys()
    pop = sarrc_population.values()
    plt.bar(year,pop)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("SAARC countries population by each year")
    plt.xticks(rotation=90)
    plt.show()

saarc_country_plot()
