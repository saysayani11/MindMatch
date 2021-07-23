import itertools
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from string import ascii_lowercase


# SECTION 1: PREPARE THE DATA  ------------------------------------------------
gsheet_id='1eaTqdDm9dSnwI5C9hv5K7gWONBJxKwBHWwJ6SHSHq70'
sheet_name1 = 'Sign_Ups'
sheet_name2 = 'Connection_Applications'
sheet_name3 = 'Connections'
sheet_name4 = 'Expert_Search_Requests'
sheet_name5 = 'Connection_Discovery_Requests'


g_sheet_url1 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name1)
g_sheet_url2 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name2)
g_sheet_url3 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name3)
g_sheet_url4 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name4)
g_sheet_url5 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name5)

sheetdf1 = pd.read_csv(g_sheet_url1)
sheetdf2 = pd.read_csv(g_sheet_url2)
sheetdf3 = pd.read_csv(g_sheet_url3)
sheetdf4 = pd.read_csv(g_sheet_url4)
sheetdf5 = pd.read_csv(g_sheet_url5)

#-- Create two fresh sheets using the collected data from Sheets 1-5
#-- 1. User_end_data_sheet
#-- 2. relation

length_of_database = len(list(sheetdf1['Phone']))  

#-- User_end_data_sheet

UserID = []
for i in range(length_of_database):
    UserID.append(i)
 
list_UserID = list(UserID)
list_firstname = list(sheetdf1['First Name'])
list_lastname = list(sheetdf1['Last Name'])
list_occupation = list(sheetdf1['Profession'])
list_cities = list(sheetdf1['City'])
list_contact = list(sheetdf1['Phone'])
list_email = list(sheetdf1['Email'])

# Zip up into a single dataframe and write a dataframe

#-- Include username
df1 = pd.DataFrame(list(zip(list_UserID, list_firstname, list_lastname, list_occupation, list_cities, list_contact, list_email)),columns=['Username_UID', 'User_Firstname', 'User_Lastname','User_Occupation', 'User_Location', 'User_Contact', 'User_email'])

#-- Do not include username
df2 = pd.DataFrame(list(zip(list_UserID, list_occupation, list_cities, list_contact, list_email)),columns=['Username_UID','User_Occupation', 'User_Location', 'User_Contact', 'User_email'])

#-- relation

list1 = list(sheetdf2['First Name of Connection'])
list2 = list(sheetdf2['Last Name of Connection'])
list3 = list(sheetdf2['Relationship with Connection'])
df3 = pd.DataFrame(list(zip(list1, list2, list3)),columns=['node1','node2', 'relation_type'])


# SECTION 2: ANALYSES  --------------------------------------------------------
print("------------------------------------------------------------------------")   
print("                           WELCOME TO MINDMATCH                         ")     
print("------------------------------------------------------------------------")  
print()
print("Choose type of operation from the menu")
print()
print("1. know_all_path                : Know who connects two users and how!")
print()
print("2. know_shortest_path           : Know the shortest possible connection between two users!")
print()
print("3. know_relation                : Know how two people are connected")
print()
print("4. look_for_people_around_me    : Who all are common friends among me and user 'n'? ")
print()

def know_all_path(G,source, target, cutoff):
    for path in nx.all_simple_paths(G, source, target, cutoff):
        n=list(path)
        print()
        print(n)
        m= list_relation(n)
        print()
    
        
def shortest_path(G, source, target):
    path_list=[]
    for path in nx.shortest_path(G, source, target):
        path_list.append(path)
    print(path_list)        
        
def relation(source,target):
    n1=list(df3['node1'])
    n2=list(df3['node2'])
    indices_list1 = [index for index, element in enumerate(n1) if (element == source) or (element == target)]
    indices_list2 = [index for index, element in enumerate(n2) if (element == target) or (element == source)]
   
    for i in indices_list1:
        for j in indices_list2:
            if i==j:
                print(df3.relation_type[j])
                
def list_relation(list1):
    rel_list = []
    for x, y in zip(list1[0::], list1[1::]):
        rel_list.append(relation(x,y))

                
def look_for_people_around_me():
    loc = list(sheetdf4["City"])
    occ = list(sheetdf4["Profession"])
    location = loc[-1]
    occupation = occ[-1] 

    # location = input("Enter Location: ")
    # occupation = input("Enter Occupation: ")
    
    query_res=df1[(df1["User_Location"]==location) & (df1["User_Occupation"]==occupation)]
    query_res.to_excel("Expert_Search_Results.xlsx")
