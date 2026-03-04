import os
import sys
import re
from pathlib import Path

BENCH_NAME = 0
PTX_PATH = 1

class PtxPaths():
    
    def __init__(self, ptx_src_dir : str):
        self._kernel_name_pattern = r'(.*?).ptx'
        self._ptx_src_dir : str = ptx_src_dir
        self._ptx_path_dict : dict[str, (str, str)] = None
        self.findPtxSrcFiles()
    
    def __str__(self):
        kernel_count = 0
        res = ""
        for kernel_name in self._ptx_path_dict.keys():
            kernel_count += 1
            path_info = self._ptx_path_dict[kernel_name]
            res += "Kernel name : " + kernel_name + "\n"
            res += "\tBench name : " + path_info[BENCH_NAME] + "\n"
            res += "\tPtx path : " + path_info[PTX_PATH] + "\n"
        res += "KERNEL COUNT : " + str(kernel_count) + "\n"
        return res
            
        
    def findPtxSrcFiles(self):
        self._ptx_path_dict = dict()
        for root, dirs, _ in os.walk(self._ptx_src_dir):
            for dir_name in dirs:
                bench_name = dir_name
                ptx_dir_path = os.path.join(root, dir_name)
                for _, _, files in os.walk(ptx_dir_path):
                    for file in files:
                        if ".ptx" in file:
                            path_to_ptx = os.path.join(ptx_dir_path, file)
                            kernel_name = re.search(self._kernel_name_pattern, file)
                            self._ptx_path_dict[kernel_name.group(0)] = (bench_name, path_to_ptx)
    
        
        
class KernelData():
    
    def __init__(self, res_dir_path : str, kernel_name : str, warp_count : int, instance_exec_time : int):
        self._res_dir_path : str = res_dir_path
        self._kernel_name : str = kernel_name
        self._instance_exec_time : int = instance_exec_time
        self._warp_count : int = warp_count
        self._ptx_src_path : str = None
    
    @property
    def instance_exec_time(self) -> int:
        return self._instance_exec_time
    
    @property
    def res_dir_path(self) -> str:
        return self._res_dir_path
    
    def setPtxSrcPath(self, ptx_src_path : str):
        self._ptx_src_path = ptx_src_path
        
    def __str__(self):
        return f"Instance name : {self._res_dir_path} | Exec time : {self._instance_exec_time}"

class ResultsParser():
    
    def __init__(self, sim_res_dir : str, ptx_src_dir : str):
        self._sim_res_dir = sim_res_dir
        self._worst_traces_dir = None
            
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

    def getPtxPath(self, bench_name : str, kernel_name : str):
        pass

    def findWorstInstances(self) -> dict[str, KernelData]:
        worst_traces : dict[str, dict[int, KernelData]] = dict()
        for root, dirs, _ in os.walk(traces_dir_name):
            for instance_name in dirs:
                dir_path = Path(os.path.join(root, instance_name))
                print(root)
                kernel_name = self.extractKernelName(instance_name)
                exec_time = self.getTraceExectime(dir_path)
                warp_count = self.getTraceWarpCount(dir_path)
                kernel_data = KernelData(dir_path, kernel_name, warp_count, exec_time)
                # NOTE : Only for incomplete simulations. REMOVE WHEN SIMS ARE DONE
                if kernel_data.instance_exec_time:
                    if kernel_name in worst_traces.keys():
                        data_dict : dict[int, KernelData] = worst_traces[kernel_name]
                        if warp_count in data_dict.keys():
                            registered_data = data_dict[warp_count]
                        if registered_data.instance_exec_time < kernel_data.instance_exec_time:
                            data_dict[warp_count] = kernel_data
                        else:
                            data_dict[warp_count] = kernel_data
                    else:
                        worst_traces[kernel_name] = dict()
                        worst_traces[kernel_name][warp_count] = kernel_data
        self._worst_traces_dir = worst_traces

    def dumpTracesDict(self):
        instance_count = 0
        for kernel_name in self._worst_traces_dir.keys():
            configs_dict = self._worst_traces_dir[kernel_name]
            print(f"Kernel name : {kernel_name}")
            for warp_count in sorted(configs_dict.keys()):
                instance_count += 1
                print(f"    {warp_count} warps :")
                print(f"        exec time : {configs_dict[warp_count].instance_exec_time}")
                print(f"        path : {configs_dict[warp_count].res_dir_path}")
        print(f"Results total {instance_count} instances")
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
    if len(sys.argv) != 4:
        print(f"Usage : {sys.argv[0]} traces_dir ptx_src_dir worst_traces_dir")
        exit(1)
    traces_dir_name = sys.argv[1]
    ptx_src_dir = sys.argv[2]
    worst_traces_dir_name = sys.argv[3]
    # res_parser = ResultsParser(traces_dir_name)
    # res_parser.findWorstInstances()
    # res_parser.dumpTracesDict()
    # createTargetDir(worst_traces_dir_name)
    ptxPaths = PtxPaths(ptx_src_dir)
    print(ptxPaths)
    exit(0)