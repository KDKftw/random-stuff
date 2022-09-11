import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file=r'C:\Users\KDK\Desktop\google_docs\keyInto.json')
#gc = pygsheets.authorize(service_file=r'C:\Users\KDK\Desktop\google_docs\keyIntoV2.json')
#gc = pygsheets.authorize(service_file=r'C:\Users\KDK\Desktop\google_docs\client_secret_714585461842-ha4io8og2d83qde3pgbke4efifdfhvcn.apps.googleusercontent.com.json')
# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['kks'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Test123')

#select the first sheet
wks = sh[0]

#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df,(1,1))