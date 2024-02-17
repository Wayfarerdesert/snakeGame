import random
import readchar
import os


POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

PLAYER = '@'
GROWN_TAIL = 'o'
RANDOM_OBJECTS = '*'
NUM_OF_MAP_OBJECTS = 1

# obstacle_definition ='''\
####### ########## ### ##
####     ####     ###
         ######   ##
###############      #####
###      #########      ##
################    ####
###         ######    #
####   ######
   ####     ####       ##
########## ####### ##
######### #  ##### ##
###         ######     #
####  #####     #
  #####     ###       ##
########## ##    #####  \
# '''

my_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
tail_length = 0
tail = []

END_GAME = False
died = False
map_objects = []

# Create obstacle map
# obstacle_definition = [list(row) for row in obstacle_definition.split('\n')]
# print(obstacle_definition)




# Main loop
while not END_GAME:

    # Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # draw map
    print('+' + '-' * MAP_WIDTH * 3 + '+')
    for coordinate_y in range(MAP_HEIGHT):
        print('|', end='')

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = ' '
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = RANDOM_OBJECTS
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = GROWN_TAIL
                    tail_in_cell = tail

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = PLAYER

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    END_GAME = True
                    died = True

                    os.system('cls')
                    if died:
                        print('\nGAME OVER\n')
                        end_game_answer = input('[R]estart\n'
                                                '[Q]uit\n')
                        if end_game_answer == 'r':
                            END_GAME = False
                            # tail_length.clear()
                        else:
                            exit()
                # if obstacle_definition[coordinate_y][coordinate_x] == '#':
                  #  char_to_draw = '#'

            print(' {} '.format(char_to_draw), end='')
        print('|')
    print('+' + '-' * MAP_WIDTH * 3 + '+')


    # ask user where he wants to move
    direction = readchar.readchar()
    if direction == 'w':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 's':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 'a':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'd':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'q':
        END_GAME = True
    os.system('cls')

if died:
    print('Has Muerto')


