def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']), # using int because in the csv the values are strings
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


""" def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values """

def population_by_country(data, country): # receive a list that contain dictionaries
    result = list(filter(lambda item : item['Country/Territory'] == country, data)) # filter if input Country exist in the list
    return result
