# SkaterXL Tools
Python3 wrapper for basic linux terminal commands such as `mv`, for organising skaterxl mod files on your machine. Written with tab autocompletion and terminal printing for ease of use.
### SkaterXL_File_Manager
Is used for swapping moded board shapes (I use for back to future hoverboard)
```bash
foo@bar$ python3 SkaterXL_File_Manager.py
#############################################################################################
  __  _  __ __ _____ ___ ___ __   ___     __  __   __  ___ __     __  _  _  __  ___ ___  __
 /' _/| |/ //  \_   _| __| _ \ \_/ / |   |  \/__\ /  \| _ \ _\  /' _/| || |/  \| _,\ __/' _/
`._`.|   <| /\ || | | _|| v / > , <| |_  | -< \/ | /\ | v / v | `._`.| >< | /\ | v_/ _|`._`.
|___/|_|\_\_||_||_| |___|_|_\/_/ \_\___| |__/\__/|_||_|_|_\__/  |___/|_||_|_||_|_| |___|___/
#############################################################################################

Current board shape in Steam folder:
 - Original

Custom board shapes in your repository:
 - B2TF_Hoverboard
 - Original
 - Santa_Cruz_foot

Input which board shape you want to play:
B2TF_Hoverboard

B2TF_Hoverboard files copied into Steam folder
--------------------------------------------------------------
```
### SkaterXL_Downloads_Manager
unpacks maps or gear into correct `Documents/SkaterXL/` from a `.zip` file in `Downloads/` diretory.
```bash
foo@bar$ python3 SkaterXL_Downloads_Manager.py

SkaterXL Download Manager options:
 -   exit
 -   unzip_gear
 -   unzip_map

Input the file category you want to unpack:
unzip_gear


Map files in your downloads:
 - baker.zip
 - deck_element_nyjah_owl_used.zip
 - ea_skate_by_2th.zip

Input which gear file you want to unzip:
baker.zip

baker.zip file unzipped into gear folder
--------------------------------------------------------------
```