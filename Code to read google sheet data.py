import pandas as pd

#gsheet_id='1L2MZWi3ObrHK37vgO-rILcwMP-xPhCheiIS92I6560M'
gsheet_id='1eaTqdDm9dSnwI5C9hv5K7gWONBJxKwBHWwJ6SHSHq70'

sheet_name='Sign_Ups'

g_sheet_url= "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name)

sheetdf1= pd.read_csv(g_sheet_url)

print(sheetdf1)