import itertools
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from string import ascii_lowercase


# SECTION 1: MODEL NETWORK  ---------------------------------------------------
# Generate a (Albert-Barabasi) Network of size 10000 (users) and starting degree size=2
# Numbers are User IDs
# Write the graph on to a .gexf file (or other compatible file formats)

G =nx.barabasi_albert_graph(10000, 2)
nx.write_gexf(G, "Mindmatch.gexf")
# Collect the edgelist in a list "data"
data=list(G.edges())

# Convert the edgelist to a dataframe for further manipulations
df1 = DataFrame(data,columns=['node1','node2'])
df1.to_excel("who_do_I_know.xlsx")


# SECTION 2:  PREPARE THE DATASET (PART 1) ------------------------------------

# Generate the nodes set of 10000 users to prepare the dataset
list_UserID=list(G.nodes())

# Generate Occupation
occupation= ['General Physician', 'Cardiologist', 'Subject matter expert', 'Physicist', 'Virologist', 'Classical dancer', 'Painter', 'Chemical Engineer', 'Gynaecologist', 'Pharmacist', 'Data Scientist', 'Banker', 'Enterpreneur', 'Artist','Software engineer', 'Product manager','Geologist', 'ENT surgeon', 'High school teacher', 'Salesman']
list_occupation=[]
for i in range(10000):
    list_occupation.append(random.choice(occupation))

# Generate Location
places=['Mumbai', 'Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur','Lucknow','Kanpur','Nagpur','Indore','Thane','Bhopal','Visakhapatnam','Patna','Vadodara','Ghaziabad','Ludhiana','Agra']
list_cities=[]
for i in range(10000):
    list_cities.append(random.choice(places))
    
# Generate Contact Details
list_contact=[]
for i in range(10000):
    list_contact.append(random.randint(1000000000, 10000000000))
    
# Generate Email IDs

def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)
series=[]
for s in itertools.islice(iter_all_strings(), 10000):
    series.append(s)
suffix = []
for i in range(10000):
    suffix.append("@gmail.com")
    
list_email = [i + j for i, j in zip(series, suffix)]

# Generate charges
charge_1st=[0,30,40,60]
charge_2nd=[60,70,80,90]
charge_3rd=[100,130,150]
charge_4th=[200,250,350,500]

charge_1st_all=[]
charge_2nd_all=[]
charge_3rd_all=[]
charge_4th_all=[]

for i in range(10000):
    charge_1st_all.append(random.choice(charge_1st)) 
for i in range(10000):
    charge_2nd_all.append(random.choice(charge_2nd)) 
for i in range(10000):
    charge_3rd_all.append(random.choice(charge_3rd)) 
for i in range(10000):
    charge_4th_all.append(random.choice(charge_4th)) 
    
# Zip up into a single dataframe and write a sheet
df2 = pd.DataFrame(list(zip(list_UserID, list_occupation, list_cities, list_contact, list_email, charge_1st_all, charge_2nd_all, charge_3rd_all, charge_4th_all )),columns=['Username_UID]','User_Occupation', 'User_Location', 'User_Contact', 'User_email', 'User_1st_degree_charges', 'User_2nd_degree_charges', 'User_3rd_degree_charges' , 'User_4th_degree_charges'])
df2.to_excel("User_end_data_sheet.xlsx")

#  SECTION 3: PREPARE THE DATASET  (PART 2)------------------------------------
# Relation type between users
# Create a univeral set to populate relationships

# Create list1
list1=df1['node1']

# Create list2
list2=df1['node2']

relation=['neighbour','colleague','batchmate','friend', 'was a neighbour', 'travel_buddy', 'mentor', 'co_authors']
list_relation=[]
for i in range(10000):
    list_relation.append(random.choice(relation)) 
df3 = pd.DataFrame(list(zip(list1, list2, list_relation)),columns=['node1','node2', 'relation_type'])
df3.to_excel("relation.xlsx")    


# SECTION 4: ANALYSES  --------------------------------------------------------

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
    
                
def look_for_people_around_me(user_id):
    location = input("Enter Location: ")
    occupation = input("Enter Occupation: ")
    query_res=df2[(df2["User_Location"]==location) & (df2["User_Occupation"]==occupation)]
    
    query_res.to_excel("query_request.xlsx")
    
    #retrieve the user IDs from query search
    user_id3=list(list(query_res.iloc[:,0]))
    
    #Print all paths from (user_id) to (user_id3)
    
    for i in user_id3:
        print(know_all_path(G,user_id,i,3))
        
        
        
        
    
    
    
    
    
    
    