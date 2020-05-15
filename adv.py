from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes. 
# map_file = "maps/test_line.txt"   shortest test
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


#helper to reverse directions
def backtrack(direction):
  opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

  if direction == 'n':
    return opposite['n']
  
  elif direction == 's':
    return opposite['s']
  
  elif direction == 'e':
    return opposite['e']
  
  elif direction == 'w':
    return opposite['w']
 


# Fill this out with directions to walk
# traversal_path = ['n', 'n']

#keeps track of the directions
traversal_path = []
#the previous room the player was in
previous_room = [] # while previous is > 0

#the player's current room
current = []
# rooms that have been visited
visited = {}
#create opposite directions dict for the stack if I need to back up
# opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'} # access the values for the stack ( ie  opposite['n'] )

#add the player's current room to the visited dictionary as a key
visited[player.current_room.id] = player.current_room.get_exits()

#this array will keep the traversal path directions and use them in a stack to go backwards if we hit a dead end
path = []

while len(visited) < len(room_graph):

    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()


    #move around map
    #If there are exits available
    '''while there are available exits'''
    while len(player.current_room.get_exits()) > 0:

    #choose a random available direction to travel in
        
        #save the available random directions in a variable
        random_move = random.choice(player.current_room.get_exits())
        player.travel(random_move)
        
        #add the direction moved in to the "path" array
        path.append(random_move)

        #add the direction moved in to the "traversal_path" array
        traversal_path.append(random_move)
        
        #store the current room id in a variable
        current_room_id = player.current_room.id
        
        #add the current room id to the "current" array
        current.append(current_room_id)
        
    
        '''#Can I update here to add the id to the visited array as a value to the direction key? Can I use something else?'''
        
        
        # if len(path) > 1:
        #store previous room's id in a variable
        
        #Move one step back in the array to store the previous room's id
        

        #add the previous room id to the "previous" array

        

        
        

    '''#Escaping the previous while loop (while there are exits available)...is this indentation correct for escape?''' 
    #If we are reach a dead-end
    if len(player.current_room.get_exits()) < 0:
    #backtrack through the maze by using the "path" route as a stack and switch the direction to opposite
        
        #get the route from the "path" array
        while len(path) > 0:
            #store the the last element removed from path array in a variable
            removed = path.pop()
            #add directions to traversal path array
            traversal_path.append(removed)
            # use the backtrack method here by storing in a variable
            reverse_dir = backtrack(removed)
            #move in the new opposite direction
            player.travel(reverse_dir)

        #


    #add the directions to the 'traversal_path array'


    #get the available exits




    #add the player's current room to the 'current' array
    current.append(player.current_room.id)

    #loop over the exits




    #While loop
    player.current_room.id



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
