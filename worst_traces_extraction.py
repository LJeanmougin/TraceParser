import os
import sys
import re
from pathlib import Path

class KernelData():
    
    def __init__(self, res_dir_path : str, kernel_name : str, warp_count : int, instance_exec_time : int):
        self._res_dir_path : str = res_dir_path
        self._kernel_name : str = kernel_name
        self._instance_exec_time : int = instance_exec_time
        self._warp_count : int = warp_count
    
    @property
    def instance_exec_time(self) -> int:
        return self._instance_exec_time
        
    def __str__(self):
        return f"Instance name : {self._res_dir_path} | Exec time : {self._instance_exec_time}"

class ResultsParser():
    
    def __init__(self, sim_res_dir : str):
        self._sim_res_dir = sim_res_dir
            
    def extractKernelName(self, dirname : str) -> str:
        kernel_name_pattern = r'[0-9_a-zA-Z]+-(.*?)-instance'
        match = re.search(kernel_name_pattern, dirname)
        return match.group(1)

    def getTraceExectime(self, trace_dir_path : Path) -> int | None:
        for file in trace_dir_path.iterdir():
            if "exectime" in file.name:
                exectime_file = open(file)
                exectime = int(exectime_file.readline())
                return exectime
        return None

    def getTraceWarpCount(self, trace_dir_path : Path) -> int:
        warp_count = 0
        for file in trace_dir_path.iterdir():
            if ".ptx" in file.name:
                warp_count += 1
        return warp_count

    def findWorstInstances(self) -> dict[str, KernelData]:
        worst_traces : dict[str, dict[int, KernelData]] = dict()
        for root, dirs, _ in os.walk(traces_dir_name):
            for instance_name in dirs:
                dir_path = Path(os.path.join(root, instance_name))
                print(f"Dir path = {dir_path}")
                kernel_name = self.extractKernelName(instance_name)
                print(f"Kernel name : {kernel_name}")
                print(f"Instance name : {instance_name}")
                exec_time = self.getTraceExectime(dir_path)
                warp_count = self.getTraceWarpCount(dir_path)
                print(f"Warp count : {warp_count}")
                kernel_data = KernelData(dir_path, kernel_name, warp_count, exec_time)
                # NOTE : Only for incomplete simulations. REMOVE WHEN SIMS ARE DONE
                if kernel_data.instance_exec_time:
                    if kernel_name in worst_traces.keys():
                        data_dict : dict[int, KernelData] = worst_traces[kernel_name]
                        if warp_count in data_dict.keys():
                            registered_data = data_dict[warp_count]
                            print(kernel_data)
                        if registered_data.instance_exec_time < kernel_data.instance_exec_time:
                            data_dict[warp_count] = kernel_data
                        else:
                            data_dict[warp_count] = kernel_data
                    else:
                        worst_traces[kernel_name] = dict()
                        worst_traces[kernel_name][warp_count] = kernel_data
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
    res_parser = ResultsParser(traces_dir_name)
    worst_traces = res_parser.findWorstInstances()
    # createTargetDir(worst_traces_dir_name)
    exit(0)