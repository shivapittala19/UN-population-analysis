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