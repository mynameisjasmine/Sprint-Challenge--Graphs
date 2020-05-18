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
#the previous rooms the player has been in
previous_rooms = [] 


# rooms that have been visited
visited = {}
#create opposite directions dict for the stack if I need to back up
# opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'} # access the values for the stack ( ie  opposite['n'] )

#change the get_exits array to a dictionary with '?' values
exits = player.current_room.get_exits()
new_exits = {i: '?' for i in exits}

#add the player's current room to the visited dictionary as a key
visited[player.current_room.id] = new_exits
# visited[player.current_room.id] = player.current_room.get_exits()


#this array will keep the traversal path directions and use them in a stack to go backwards if we hit a dead end
path = []

#count and total for the check to see if there are unvisited rooms
count = 0
total = 0





while len(visited) < len(room_graph):
    
    if player.current_room.id not in visited:
        visited[player.current_room.id] = new_exits.copy()


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
        
        #add the current_room_id to the previous_rooms array
        previous_rooms.append(current_room_id)
        
        #storing the room's current direction (taken from the traversal_path array)
        curr_dir = traversal_path[-1]
        
        # store the previous room's direction that is saved in the traversal_path array
        if len(traversal_path) > 1:
            prev_dir = traversal_path[-2]
        
        #store the previous room's id
        if len(previous_rooms) > 1:
            prev_id = previous_rooms[-2]
        
        #update the visited dictionary directions keys with their room id values 
        if len(visited) > 1:
            visited[current_room_id][prev_dir] = prev_id
            visited[prev_id][curr_dir] = current_room_id
        

        #Checking to see if there are any rooms left unvisited
        for i in range(len(visited)):
            for j in visited[i]:
                if visited[i][j] == '?':
                    count += 1
                total = count
        if total > 0:
            continue
        
        elif total == 0:
            break

        
    
        '''#Can I update here to add the id to the visited array as a value to the direction key? Can I use something else?'''
        
        
        
        
        
        
        

        '''#Escaping the previous while loop (while there are exits available)...is this indentation correct for escape?''' 
        #If we are reach a dead-end
        if len(player.current_room.get_exits()) < 1:
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
        


            


        


        




    
    

    




    



