"""stacked data of population from years 2004 to 2014 in asean countries"""
import matplotlib.pyplot as plt
# from main import ASEAN_COUNTRIES, population_data, color_codes
import main

def asean_grouped_data():
    """stacked data of population from years 2004 to 2014 in asean countries"""
    population_data = main.load_csv('population-estimates_csv.csv')
    asean_countries = main.asean_country()
    color_codes = main.colors()
    asean_dict = {}
    for record in population_data:
        year = record['Year']
        region = record['Region']
        citizens = float(record['Population'])
        if  '2004' <=year <= '2014'  and region in asean_countries :
            if year in asean_dict:
                asean_dict[year][region] = citizens
            else:
                asean_dict[year] = {region : citizens}
    population = {}
    years  = list(asean_dict.keys())
    for country in asean_countries:
        population[country] = []
        for year in years:
            if asean_dict[year][country]:
                population[country].append(asean_dict[year][country])
            else:
                population[country].append(0)
    width = 0.1
    number_of_years = range(len(years))
    for index, country in enumerate(asean_countries):
        plt.bar(
            [pos + index * width for pos in number_of_years],
            population[country],
            label=country,
            width=width,
            color = color_codes[index]
            )
        plt.legend()
        plt.xticks([pos + 2.5 * width for pos in number_of_years], years)
        plt.xlabel("Country")
        plt.ylabel("Population")
        plt.title("Population of asean countries from 2004 to 2014")
    plt.show()

asean_grouped_data()
