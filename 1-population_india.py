from main import population_data
import matplotlib.pyplot as plt


def indian_population():
    india_dict = {}
    
    # dictinary of indian population in each year
    # {'year' : 'population'}
    
    for row in population_data:
        if row['Region'] == 'India':
            india_dict[row['Year']] = row['Population']
    
    keys = india_dict.keys()
    values = india_dict.values()
    
    plt.bar(keys,values)
    plt.show()
    plt.xticks(rotation = 90)
    
indian_population()