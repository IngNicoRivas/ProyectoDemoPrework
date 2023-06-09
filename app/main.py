import re
import read_csv
import chart
import pandas as pd

def world_pop():
    # the same way with pandas
    df = pd.read_csv('./app/data_pop.csv') #df = dataframe the read_csv is from pandas
    df = df[df['Continent'] == 'Africa'] # in dataframe df select column 

    countries = df['Country/Territory'].values # values of column
    percentages = df['World Population Percentage'].values
    chart.generate_pie_chart('World_pop_Percentage', countries, percentages)

    """ without pandas
    data = read_csv.read_csv('./py_project/app/data_pop.csv')
    data = list(filter(lambda item : item['Continent'] == 'South America',data))
    
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    chart.generate_pie_chart('World_pop_Percentage', countries, percentages) """

def population_by_country(data, country):
    labels = []
    values = []
    filter_country = list(filter(lambda item : item['Country/Territory'] ==  country, data))
    for key, value in filter_country[0].items():
        if re.search('Population\Z', key): # \Z Returns a match if the specified characters are at the end of the string
            labels.append(key.replace(' Population','')) 
            values.append(int(value))
    return labels, values

if __name__ == '__main__':
    world_pop()
    data = read_csv.read_csv('./app/data_pop.csv')
    country = input('Type Country : ').capitalize()
    labels, values = population_by_country(data,country) 
    chart.generate_bar_chart(country, labels, values) # if the country was transformed, we can use country['Country/Territory'] to call the column.
