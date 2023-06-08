import csv

def read_csv(path): # where is the file
    with open(path, 'r') as csvfile: # open file to just read
        reader = csv.reader(csvfile, delimiter=',') # creating a reader of the file, using the import module csv to start reading, the delimiter is the separate data form, could be ',' ';' depends on the file
        header = next(reader) # get first column name to use as key because the iterable starts reading by lines and the first is the header
        data = [] # return a list with the dictionaries 
        #print(header)
        for row in reader: # iterable to read line by line
            iterable = zip(header, row) # two arrays union, header as key and body/row as values. Union in a tuple where the first position is column and the second position is the row.
            country_dict = {key: value for key, value in iterable}  # dictionary comprehension syntax. Key and value that iterate through for in the iterable variable. It is possible to use dict(iterable) 
            data.append(country_dict) # add dictionaries as list
        return data
            #print('****' *5)
            #print(country_dict)
            # print(row) 

if __name__ == '__main__': # to execute the file as a script from terminal
    data = read_csv('./py_project/app/data_pop.csv') # cal function to read
    print(data[0]) # to print just one [0] the first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 