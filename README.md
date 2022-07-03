# MindMatch README

### Mindmatch is a simple network science implementation to fetch professional details of users and their connections. This is a case of a social network where people are connected to each other via social ties (eg: from work environments, travel friends, colleagues, or simply next door neighbours). 

The dataset used comprises 10000 users with user details randomly generated using Python. The script is divided into four sections: Section 1: Building the model network, Section 2: Preparing the dataset (Part 1) , Section 3: Preparing the dataset (Part 2) , and Section 4:  Functions and Analysis. Check the script for more information.

FUNCTIONS
To test the script, plug in values for any of the functions from the function manual:
1. know_all_path : _Know who connects two users and how_
2. know_shortest_path : _Know the shortest possible connection between two users_
3. know_relation : _Know how two people are connected_
4. look_for_people_around_me : _Who all are common friends among me and user 'n' ?_

INPUT ARGUMENTS
1.know_all_path (G,source, target, cutoff)
2. know_shortest_path (G, source, target)
3. know_relation (source,target)
4. look_for_people_around_me (user_id)

MORE DETAILS
G : An Albert-Barabasi graph object of 10000 nodes (users) and starting degree = 2
source : source node (user), datatype = int
target : target node (user), datatype = int
cutoff : hops cutoff, datatype = int
user_id:  source node (user), datatype = int

EXAMPLE RUN
1. know_all_path (G,4, 50, 3)
2. know_shortest_path (G, 7, 40)
3. know_relation (5,80)
4. look_for_people_around_me (50)
