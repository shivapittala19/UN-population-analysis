"""stacked data of population from years 2004 to 2014 in asean countries"""
import matplotlib.pyplot as plt
from main import ASEAN_COUNTRIES, population_data, color_codes

def asean_grouped_data():
    """stacked data of population from years 2004 to 2014 in asean countries"""
    asean_dict = {}
    for row in population_data:
        if row['Year'] >= '2004' and row['Year'] <= '2014' and row['Region'] in ASEAN_COUNTRIES :
            if row['Year'] in asean_dict:
                asean_dict[row['Year']][row['Region']] = float(row['Population'])
            else:
                asean_dict[row['Year']] = {row['Region'] : float(row['Population'])}
    population = {}
    years  = list(asean_dict.keys())
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
