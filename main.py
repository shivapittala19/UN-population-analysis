""" main file """
import csv

def load_csv(file_name):
    """ read tehe csv data"""
    file = open(file_name,'r',encoding='latin-1')
    lines = csv.DictReader(file)
    return lines


# population_data = load_csv('population-estimates_csv.csv')


def asean_country():
    """ keep a record of asean countries"""
    asean_countries = [
        'Brunei Darussalam',
        'Cambodia',
        'Indonesia',
        'Lao People\'s Democratic Republic',
        'Malaysia',
        'Myanmar',
        'Philippines',
        'Singapore',
        'Thailand',
        'Viet Nam'
    ]
    return asean_countries

def saarc_country():
    """ keep a record of Saarc countries"""
    sarrc_countries = [
        'Afghanistan',
        'Bangladesh',
        'Bhutan',
        'India',
        'Maldives',
        'Nepal',
        'Pakistan',
        'Sri Lanka',
    ]
    return sarrc_countries

def colors():
    """ define color used for plotting"""
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
    return color_codes
