import csv

def load_csv(file_name):
    file = open(file_name,'r')
    lines = csv.DictReader(file)
    return lines


population_data = load_csv('population-estimates_csv.csv')

    
ASEAN_COUNTRIES = [
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
SAARC_COUNTRIES = [
    'Afghanistan',
    'Bangladesh',
    'Bhutan',
    'India',
    'Maldives',
    'Nepal',
    'Pakistan',
    'Sri Lanka',
]

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