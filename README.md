# MindMatch README

### Mindmatch is a simple network science implementation to fetch professional details of users and their connections. This is a case of a social network where people are connected to each other via social ties (eg: from work environments, travel friends, colleagues, or simply next door neighbours). 

For more details on what MindMatch is, please go over to https://github.com/saysayani11/MindMatch/blob/main/Mindmatch.pdf


### TEST DATASET
The dataset used comprises 10000 users with user details randomly generated using Python. The script is divided into four sections: 
Section 1: Building the model network
Section 2: Preparing the dataset (Part 1)
Section 3: Preparing the dataset (Part 2)
Section 4:  Functions and Analysis. 

Check the script for more information.

### FUNCTIONS
To test the script, plug in values for any of the functions from the function manual:
1. know_all_path : _Know who connects two users and how_
2. know_shortest_path : _Know the shortest possible connection between two users_
3. know_relation : _Know how two people are connected_
4. look_for_people_around_me : _Who all are common friends among me and user 'n' ?_

### INPUT ARGUMENTS
1.know_all_path (G,source, target, cutoff)
2. know_shortest_path (G, source, target)
3. know_relation (source,target)
4. look_for_people_around_me (user_id)

### MORE DETAILS
G : An Albert-Barabasi graph object of 10000 nodes (users) and starting degree = 2
**source** : source node (user), datatype = int
**target** : target node (user), datatype = int
**cutoff** : hops cutoff, datatype = int
**user_id**:  source node (user), datatype = int

### EXAMPLE RUN

Download and run the python script and run each of these functions:
1. know_all_path (G, 4, 50, 3) 
   
   This means that in the users dataset G comprising 10000 people, we would like to know the number of people that connects user 4 and user 50. "Connections" can happen
   by way of other people that "know" or "connect" user 4, leading to a "path" till user 50. The fourth argument is the cut-off on the "path" length, i.e, the path between 
   user 4 and 50 should have no more than 3 people.
   
2. know_shortest_path (G, 7, 40)

   This function returns the shortest path between two users. From the users dataset of 10000 people, we would like to know the shortest route from user 7 to user 40. In 
   social terms, we wouldl like to know who all are the closest mutuals between user 7 and user 40.
   
3. know_relation (5,80)

   Wondering how any two given users can possibly be "connected"? This function does exactly that. Given two users, it can tell you how they are connected (eg: colleagues, 
   same workplace, went to same university and so on)
   
4. look_for_people_around_me (50)

   Given any user, cuious to know how you two can be possibly connected? This function gives you a lsit of all the users that connects you to the other user.
