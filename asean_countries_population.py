""" asean countries population in year 2014"""
import matplotlib.pyplot as plt
from main import population_data , ASEAN_COUNTRIES

def plot_asean_data():
    """ asean countries population in year 2014"""
    data_dict = {}
    # dictinary with keys-> country , value -> it's population
    for record in population_data:
        if record['Year'] == '2014' and record['Region'] in ASEAN_COUNTRIES:
            data_dict[record['Region']] = record['Population']
    plt.bar(data_dict.keys(),data_dict.values())
    plt.show()

plot_asean_data()
