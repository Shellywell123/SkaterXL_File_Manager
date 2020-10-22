
import os
import readline
from colours import *

##############################################################

path_to_downloads = '/mnt/c/Users/benja/Downloads/'
path_to_sxl_docs  = '/mnt/c/Users/benja/Documents/SkaterXL/'
path_to_maps      = path_to_sxl_docs + 'Maps/'
path_to_gear      = path_to_sxl_docs + 'Gear/'

##############################################################

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

def print_zips_in_dir(path_to_dir):
    """
    shows the user the directories within the supplied directory
    """
    repo_list = []
    for d in os.listdir(path_to_dir) :
        if '.zip' in d:
            print(' - '+green+str(d)+white)
            repo_list.append(d)

    return repo_list

def unzip_map():
    """
    """
    print('\nMap files in your downloads:')
    choice_list = print_zips_in_dir(path_to_downloads)
    set_tab_complete_options(choice_list)
    choice = input('\nInput which map you want to unzip:\n'+input_colour)
    print(''+white)
    choice_formatted = choice.replace('[','_').replace('(','_').replace(']','_').replace(')','_').replace('.zip','')
    

    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        ostr = "unzip {} -d {}".format(path_to_downloads+'/'+choice,path_to_maps+'/'+choice_formatted)
        os.system(ostr)
        print('{} file unzipped into map folder'.format(choice))
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')

def unzip_gear():
    """
    """
    print('\nMap files in your downloads:')
    choice_list = print_zips_in_dir(path_to_downloads)
    set_tab_complete_options(choice_list)
    choice = input('\nInput which gear file you want to unzip:\n'+input_colour)
    print(''+white)

    choice_formatted = choice.replace('[','_').replace('(','_').replace(']','_').replace(')','_').replace('.zip','')
    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        ostr = "unzip {} -d {}".format(path_to_downloads+'/'+choice,path_to_gear+'/'+choice_formatted)
        os.system(ostr)
        print('{} file unzipped into gear folder'.format(choice))
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')

def main_menu():
    """
    main function of this file which acts as an interactive menu call other functions
    """
    print('\nSkaterXL Download Manager options:')
    choice_list = ['exit','unzip_gear','unzip_map']
    for choice in choice_list:
        print (' - ',green,choice,white)

    set_tab_complete_options(choice_list)
    choice = input('\nInput the file category you want to unpack:\n'+input_colour)
    print(''+white)

    if choice == 'exit':
        exit(0)

    if choice == 'unzip_gear':
        unzip_gear()
        
    if choice == 'unzip_map':
        unzip_map()

main_menu()