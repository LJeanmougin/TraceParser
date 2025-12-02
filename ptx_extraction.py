import os
import sys
import shutil
import re

extract_file_name = r'(?<=PTX\/)[_a-zA-Z0-9\+]+'


def extractPtxPrograms(ptx_file_path):
    file = open(ptx_file_path, 'r')
    file_content = file.read()
    ptx_pattern = r'\.visible.*?}'
    matches = re.findall(ptx_pattern, file_content, re.DOTALL)
    return matches

def findFuncName(ptx_prog : str):
    func_name_pattern = r'(?<=.entry )[a-zA-Z0-9_]*'
    matches = re.findall(func_name_pattern, ptx_prog)
    return matches

def getPtxFilesPaths(src_dir : str) -> list[str]:
    ptx_files_paths = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            if(("sm_60.ptx" in file) and
               not("sm_60.ptxas" in file)):
                ptx_files_paths.append(os.path.join(root, file))
    return ptx_files_paths

def makeProgPathDict(ptx_files_paths : list[str]) -> dict[str, list[str]]:
    progPathsDict : dict[str, list[str]] = dict()
    for ptx_file_path in ptx_files_paths:
        print(ptx_file_path)
        prog_name = re.search(extract_file_name, ptx_file_path).group(0)
        print(prog_name)
        if not prog_name in progPathsDict:
            progPathsDict[prog_name] = []
        progPathsDict[prog_name].append(ptx_file_path)
    return progPathsDict

def createDirectory(path : str):
    try:
        os.makedirs(path)
    except FileExistsError:
        print(f"Directory \"{path}\" already exists.")
    except PermissionError:
        print(f"Permission denied to create \"{path}\"")
    except Exception as e:
        print(f"Error : {e}")
    

def createPtxProgDirectories(progs : list[str], target_dir_name : str):
    createDirectory(target_dir_name)
    for prog in progs:
        prog_dir_name = target_dir_name + "/" + prog
        createDirectory(prog_dir_name)
            

def extract_programs(src_dir : str, target_dir_name : str):
    ptx_files : dict[str, list[str]] = dict()
    try:
        os.makedirs(target_dir_name)
    except FileExistsError:
        print(f"Directory \"{target_dir_name}\" already exists.")
    except PermissionError:
        print(f"Permission denied to create \"{target_dir_name}\"")
    except Exception as e:
        print(f"Error : {e}")
    
    ptx_files_paths = getPtxFilesPaths(src_dir)
    progPathsDict = makeProgPathDict(ptx_files_paths)
    progs = list(progPathsDict.keys())
    createPtxProgDirectories(progs, target_dir_name)
    
    
    exit(0)
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if (("sm_60.ptx" in file) and
                (not("sm_60.ptxas" in file))):
                ptx_file_path = os.path.join(root, file)
                file_name = re.search(extract_file_name, file).group(0)
                if not file_name in ptx_files:
                    print(file_name)
                    ptx_files[file_name] = []
                ptx_files[file_name].append(ptx_file_path)
    for files in ptx_files:
        for file in ptx_files[files]:
            ptx_programs = extractPtxPrograms(file)
            print(len(ptx_programs))
            for program in ptx_programs:
                for func_name in findFuncName(ptx_prog=program):
                    print(func_name)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} ptx_dir target_dir")
        exit(0)
    extract_programs(sys.argv[1], sys.argv[2])