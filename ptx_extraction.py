import os
import sys
import shutil
import re

extract_file_name = r'(?<=PTX\/)[_a-zA-Z0-9\+]+'


def extractPtxFunctions(ptx_file_path) -> list[str]:
    file = open(ptx_file_path, 'r')
    file_content = file.read()
    ptx_pattern = r'\.visible.*?}'
    matches = re.findall(ptx_pattern, file_content, re.DOTALL)
    return matches

def findFuncNames(ptx_prog : str) -> list[str]:
    func_name_pattern = r'(?<=.entry )[a-zA-Z0-9_]*'
    matches = re.findall(func_name_pattern, ptx_prog)
    return matches

def findFuncName(ptx_prog : str) -> str:
    func_names = findFuncNames(ptx_prog)
    if len(func_names) > 1:
        print("More than one function found")
        exit()
    if len(func_names) == 0:
        print("No function found")
        exit
    return func_names[0]

def makePtxFuncDict(ptx_progs : list[str]):
    ptx_func_dict = dict()
    for prog in ptx_progs:
        func_name = findFuncName(prog)
        ptx_func_dict[func_name] = prog
    return ptx_func_dict

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
        prog_name = re.search(extract_file_name, ptx_file_path).group(0)
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
    ptx_files_paths = getPtxFilesPaths(src_dir)
    progPathsDict = makeProgPathDict(ptx_files_paths)
    progs = list(progPathsDict.keys())
    createPtxProgDirectories(progs, target_dir_name)
    # keep track of extracted functions to avoid duplicates
    written_func : set[str] = set() 
    for prog in progs:
        for path in progPathsDict[prog]:
            functions = extractPtxFunctions(path)
            func_dict = makePtxFuncDict(functions)
            func_names = func_dict.keys()
            for func_name in func_names:
                if not func_name in written_func:
                    written_func.add(func_name)
                    func_file_path = target_dir_name + "/" + prog + "/" + func_name
                    print(func_file_path)
                    try:
                        with open(func_file_path, "w") as f:
                            f.write(func_dict[func_name])
                    except Exception as e:
                        print(e)
    return
    for func in functions:
        func_names = findFuncNames(func)
        for func_name in func_names:
            if not func_name in written_func:
                written_func.add(func_name)
                func_file_path = path + "/" + func_name
                with open(func_file_path, "w") as f:
                    f.write()
                        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} ptx_dir target_dir")
        exit(0)
    extract_programs(sys.argv[1], sys.argv[2])