from main import population_data , SAARC_COUNTRIES
import matplotlib.pyplot as plt


def saarc_country_plot():
    data_dict = {}
    for row in population_data:
        if row['Region'] in SAARC_COUNTRIES:
            if row['Year'] in data_dict:
                data_dict[row['Year']] += float(row['Population'])
            else:
                data_dict[row['Year']] = float(row['Population'])
               
    plt.bar(data_dict.keys(),data_dict.values())
    plt.show() 
    
saarc_country_plot()
