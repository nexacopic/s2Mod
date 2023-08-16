#What folders to look for, and pack into the pak01 vpk set.
target_folders = [ "textures", "soundevents", "resource", "scripts", "particles", "particles", "maps", "models", "materials" ]
#What files to look for, in the aforementioned folders.
# file_types = ["."]
#which vpk.exe to use. do not use \!
vpk_path = "D:/GitHub/s2Mod/game/bin/win64/vpk.exe"

# Script begins
import os,subprocess
from os.path import join
response_path = join(os.getcwd(),"vpk_list.txt")

out = open(response_path,'w')
len_cd = len(os.getcwd()) + 1

for user_folder in target_folders:
	for root, dirs, files in os.walk(join(os.getcwd(),user_folder)):
		for file in files:
			out.write(os.path.join(root[len_cd:].replace("/","\\"),file) + "\n")

out.close()

#the "pak01" here specifies the multi-chunk vpk names. Could be changed to "pak02" or "hl2_textures", or whatever your mod needs.
subprocess.call([vpk_path, "-M", "a", "pak01", "@" + response_path])