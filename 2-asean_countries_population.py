from main import population_data , ASEAN_COUNTRIES
import matplotlib.pyplot as plt

def plot_asean_data():
    data_dict = {}
    # dictinary with keys-> country , value -> it's population
    for row in population_data:
        if row['Year'] == '2014' and row['Region'] in ASEAN_COUNTRIES:
            data_dict[row['Region']] = row['Population']
    
    plt.bar(data_dict.keys(),data_dict.values())
    plt.show()

plot_asean_data()