""" asean countries population in year 2014"""
import matplotlib.pyplot as plt
import main

def plot_asean_data():
    """ asean countries population in year 2014"""
    population_data = main.load_csv('population-estimates_csv.csv')
    asean_countires = main.asean_country()
    asean_population = {}
    # dictinary with keys-> country , value -> it's population
    for record in population_data:
        if record['Year'] == '2014' and record['Region'] in asean_countires:
            asean_population[record['Region']] = record['Population']
    year = asean_population.keys()
    pop = asean_population.values()
    plt.bar(year,pop)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("ASEAN countries population by each year")
    plt.show()

plot_asean_data()
