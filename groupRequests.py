import pandas
import re

#raise output size defaults so all data displays
#set these according to the size of your expected output
pandas.set_option('display.max_rows', 350)
pandas.set_option('max_columns', 20)
pandas.set_option('display.width', 1000)

#the path/filename of the request spreadsheet you downloaded goes here
requests = pandas.read_csv("photo-requests.csv")

#this regex replace goes a long way toward normalizing the data from the plot column
requests['normalizedPlot'] = requests['plot'].replace(to_replace=r'\b[^\d\W]{2,10}\b|\s|[^\w\-,]',value='',regex=True)
#create new columns out of section, row, and lot numbers so they can be sorted in turn
requests[['section','row','lot','overflow']] = requests['normalizedPlot'].str.split('-|,',expand=True)
#sort and print the columns you'll use at the cemetery
print(requests[['firstName','lastName','deathDate','plot','section','row','lot']].sort_values(by=['section','row','lot']))

