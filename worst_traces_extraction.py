import os
import sys
import re
from pathlib import Path

class KernelData():
    
    def __init__(self, instance_name : str, instance_exec_time : int):
        self.res_file_path = instance_name
        self.instance_exec_time = instance_exec_time
        
    def __str__(self):
        return f"Instance name : {self.instance_name} | Exec time : {self.instance_exec_time}"

def extractKernelName(dirname : str) -> str:
    kernel_name_pattern = r'(.+?)(?=\d+\b)'
    match = re.search(kernel_name_pattern, dirname)
    return match.group(0)

def getTraceExectime(trace_dir_path : Path) -> int | None:
    for file in trace_dir_path.iterdir():
        if "exectime" in file.name:
            exectime_file = open(file)
            exectime = int(exectime_file.readline())
            return exectime
    return None

def findWorstInstances(traces_dir_name : str) -> dict[str, KernelData]:
    worst_traces : dict[str, KernelData] = dict()
    for root, dirs, _ in os.walk(traces_dir_name):
        for instance_name in dirs:
            dir_path = Path(os.path.join(root, instance_name))
            kernel_name = extractKernelName(instance_name)
            exec_time = getTraceExectime(dir_path)
            if kernel_name in worst_traces.keys():
                current_worst_time = worst_traces[kernel_name].instance_exec_time
                if exec_time > current_worst_time:
                    worst_traces[kernel_name] = KernelData(instance_name, exec_time)
            else:
                worst_traces[kernel_name] = KernelData(instance_name, exec_time)
    return worst_traces

def createTargetDir(target_dir_name : str):
    try:
        os.makedirs(target_dir_name)
        print(f"Directory \"{target_dir_name}\" created.")
    except FileExistsError:
        print(f"[WARNING] Directory {target_dir_name} already exists.")
    except Exception as e:
        print(f"Error : {e}")
        exit(-2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} traces_dir worst_traces_dir")
        exit(1)
    traces_dir_name = sys.argv[1]
    worst_traces_dir_name = sys.argv[2]
    worst_traces = findWorstInstances(traces_dir_name)
    createTargetDir(worst_traces_dir_name)
    
    exit(0)