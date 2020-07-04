#########################################################################
# Imports                                                               #
#########################################################################

import os
import readline
from colours import *

#########################################################################
# Paths                                                                 #
#########################################################################

# need ascii and sort screaming hand

#paths for python
repo_path            = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/Mods/SkaterXL/SkaterXL_Repo/Board_Shapes/"
steam_folder_path    = '/mnt/c/Program Files (x86)/Steam/steamapps/common/Skater XL/SkaterXL_Data/'

#paths for terminal
os_repo_path         = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/Mods/SkaterXL/SkaterXL_Repo/Board_Shapes/"
os_steam_folder_path = '/mnt/c/Program\\ Files\\ \\(x86\\)/Steam/steamapps/common/Skater\\ XL/SkaterXL_Data/'

#########################################################################
# General Functions                                                     #
#########################################################################

def ascii():
    """
    ascii art for begining og program
    """
    print("""#############################################################################################
  __  _  __ __ _____ ___ ___ __   ___     __  __   __  ___ __     __  _  _  __  ___ ___  __  
 /' _/| |/ //  \_   _| __| _ \\ \_/ / |   |  \/__\ /  \| _ \ _\  /' _/| || |/  \| _,\ __/' _/ 
`._`.|   <| /\ || | | _|| v / > , <| |_  | -< \/ | /\ | v / v | `._`.| >< | /\ | v_/ _|`._`. 
|___/|_|\_\_||_||_| |___|_|_\/_/ \_\___| |__/\__/|_||_|_|_\__/  |___/|_||_|_||_|_| |___|___/ 
#############################################################################################""")

def print_subdirs_dirs_in_dir(path_to_dir):
    """
    shows the user the directories within the supplied directory
    """
    repo_list = []
    for d in os.listdir(path_to_dir) :
        if '.' not in d:
            print(' - '+green+str(d)+white)
            repo_list.append(d)

    return repo_list

def set_tab_complete_options(options):
    """
    allows user to tab complete inputs
    """

    readline.parse_and_bind("tab: complete")

    def complete(text,state):
        if text:
            results = [s for s in options if s and s.startswith(text)]
        else: 
            results = results[:]

        return results[state]

    readline.set_completer(complete)

def set_current_board_shape(newname):
    """
    sets txt log to be the name of the current file in the RPCS3 folder
    """
    file = repo_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'w') as f:
        f.write(newname)

def get_current_board_shape():
    """
    retrieve the name of the current board shape file in the steam file from the log txt
    """
    file = repo_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'r') as f:
       cont = f.read()
    print('\nCurrent board shape in Steam folder:')
    print(' - '+green+cont+white)
    return cont

def replace_board_shapes_saves():
    """
    swaps out custom board shape files in steam folder via a user input
    """
    
    get_current_board_shape()
    print('\nCustom board shapes in your repository:')
    choice_list = print_subdirs_dirs_in_dir(repo_path)
    set_tab_complete_options(choice_list)
    choice = input('\nInput which board shape you want to play:\n'+input_colour)
    print(''+white)

    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        ostr = "cp {}* {}".format(os_repo_path+choice+'/',os_steam_folder_path)
        os.system(ostr)
        print('{} files copied into Steam folder'.format(choice))
        set_current_board_shape(choice)
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')

#########################################################################

# run this
ascii()
replace_board_shapes_saves()