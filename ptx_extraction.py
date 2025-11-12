import os
import sys
import shutil
import re

extract_file_name = "[_a-zA-Z0-9]+"

def extract_programs(src_dir : str, target_dir_name : str):
    copied_files = []
    try:
        os.makedirs(target_dir_name)
    except FileExistsError:
        print(f"Directory \"{target_dir_name}\" already exists.")
    except PermissionError:
        print(f"Permission denied to create \"{target_dir_name}\"")
    except Exception as e:
        print(f"Error : {e}")
    for root, _, files in os.walk(src_dir):
        for file in files:
            if (("sm_60.ptx" in file) and
                (not("sm_60.ptxas" in file))):
                ptx_file_path = os.path.join(root, file)
                file_name = re.search(extract_file_name, file).group(0)
                if not file_name in copied_files:    
                    shutil.copyfile(ptx_file_path, os.path.join(target_dir_name, file_name + ".ptx"))
                    copied_files.append(file_name)
                    print(f"Copied \"{file_name + '.ptx'}\"...")
                
                               
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} ptx_dir target_dir")
        exit(0)
    extract_programs(sys.argv[1], sys.argv[2])