# SkaterXL Tools
Python3 wrapper for basic linux terminal commands such as `mv`, for organising skaterxl mod files on your machine. Written with tab autocompletion and terminal printing for ease of use.
### SkaterXL_File_Manager
Is used for swapping moded board shapes (I use for back to future hoverboard)
```bash
foo@bar$ python3 SkaterXL_File_Manager.py
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