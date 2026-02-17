import os
import sys
import re
from pathlib import Path

class KernelData():
    
    def __init__(self, instance_name : str, instance_exec_time : int):
        self.instance_name = instance_name
        self.instance_exec_time = instance_exec_time
        
    def __str__(self):
        return f"Instance name : {self.instance_name} | Exec time : {self.instance_exec_time}"

def extract_kernel_name(dirname : str) -> str:
    kernel_name_pattern = r'(.+?)(?=\d+\b)'
    match = re.search(kernel_name_pattern, dirname)
    return match.group(0)

def get_trace_exectime(trace_dir_path : Path) -> int | None:
    for file in trace_dir_path.iterdir():
        if "exectime" in file.name:
            exectime_file = open(file)
            exectime = int(exectime_file.readline())
            return exectime
    return None

def extract_worst_traces(traces_dir_name : str, worst_traces_dir_name : str) -> dict[str, KernelData]:
    worst_traces : dict[str, KernelData] = dict()
    for root, dirs, _ in os.walk(traces_dir_name):
        for instance_name in dirs:
            dir_path = Path(os.path.join(root, instance_name))
            kernel_name = extract_kernel_name(instance_name)
            exec_time = get_trace_exectime(dir_path)
            if kernel_name in worst_traces.keys():
                current_worst_time = worst_traces[kernel_name].instance_exec_time
                if exec_time > current_worst_time:
                    print(f"Exec time of {exec_time} cycles > {current_worst_time} cycles")
                    worst_traces[kernel_name] = KernelData(instance_name, exec_time)
            else:
                worst_traces[kernel_name] = KernelData(instance_name, exec_time)
    return worst_traces

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} traces_dir worst_traces_dir")
        exit(1)
    traces_dir_name = sys.argv[1]
    worst_traces_dir_name = sys.argv[2]
    worst_traces = extract_worst_traces(traces_dir_name, worst_traces_dir_name)
    exit(0)