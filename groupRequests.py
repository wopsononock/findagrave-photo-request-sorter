import pandas
import re

#depends on the number of rows in the request sheet
pandas.set_option('display.max_rows', 350)
#read-in the request sheet
r = pandas.read_csv("../photo-requests.csv")
plot = r['plot']
#this regex replace goes a long way toward cleaning up the plot column
r['normalizedPlot'] = plot.replace(to_replace=r'\b[^\d\W]{2,10}\b|\s|[^\w\-,]',value='',regex=True)
#select and print out whatever columns you want for your search out in the field
norms=r[['firstName','lastName','birthDate','deathDate','plot','normalizedPlot']]
print(norms.sort_values(by=['normalizedPlot']))

