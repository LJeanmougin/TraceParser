import os
import sys
import re

extract_file_name = r'(?<=PTX\/)[_a-zA-Z0-9\+]+'
ptx_func_header = ".version 7.0\n"\
                   ".target sm_75\n"\
                   ".address_size 64\n"



def extractPtxFunctions(ptx_file_path) -> list[str]:
    file = open(ptx_file_path, 'r')
    file_content = file.read()
    ptx_pattern = r'\.visible.*?}'
    matches = re.findall(ptx_pattern, file_content, re.DOTALL)
    return matches

def addPtxHeader(ptx_progs : list[str]) -> list[str]:
    for i in range(len(ptx_progs)):
        ptx_progs[i] = ptx_func_header + ptx_progs[i]
    return ptx_progs

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
         
def writeFuncFile(path : str, func : str):
    try:
        with open(path + ".ptx", "w") as f:
            f.write(func)
    except Exception as e:
        print(e)

def createProgFuncFiles(dir_path : str, func_dict : dict[str, str]):
    for func_name in func_dict:
        func_file_path = dir_path + "/" + func_name
        func_body = func_dict[func_name]
        writeFuncFile(func_file_path, func_body)

def extract_programs(src_dir : str, target_dir_name : str):
    ptx_files_paths = getPtxFilesPaths(src_dir)
    progPathsDict = makeProgPathDict(ptx_files_paths)
    progs = list(progPathsDict.keys())
    createPtxProgDirectories(progs, target_dir_name)
    for prog in progs:
        for path in progPathsDict[prog]:
            functions = extractPtxFunctions(path)
            functions = addPtxHeader(functions)
            func_dict = makePtxFuncDict(functions)
            dir_path = target_dir_name + "/" + prog
            createProgFuncFiles(dir_path, func_dict)
                    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} ptx_dir target_dir")
        exit(0)
    extract_programs(sys.argv[1], sys.argv[2])