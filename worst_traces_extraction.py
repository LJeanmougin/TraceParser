import os
import sys
import re
import shutil
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
                            self._ptx_path_dict[kernel_name.group(1)] = (bench_name, path_to_ptx)
    
    def getKernelPtxPath(self, kernel_name : str):
        return self._ptx_path_dict[kernel_name][PTX_PATH]
    
    def getKernelBenchName(self, kernel_name : str):
        return self._ptx_path_dict[kernel_name][BENCH_NAME]
           
class InstanceData():
    
    def __init__(self, res_dir_path : str, kernel_name : str, warp_count : int, instance_exec_time : int):
        self._res_dir_path : str = res_dir_path
        self._kernel_name : str = kernel_name
        self._instance_exec_time : int = instance_exec_time
        self._exec_time_path : str = os.path.join(res_dir_path, "exectime.txt")
        self._warp_count : int = warp_count
        self._ptx_src_path : str = None
        self._warp_traces_paths : set[str] = None
        self.setWarpTracesPaths()
        
    @property
    def instance_exec_time(self) -> int:
        return self._instance_exec_time
    
    @property
    def res_dir_path(self) -> str:
        return self._res_dir_path
    
    @property
    def warp_traces_paths(self) -> set[str]:
        return self._warp_traces_paths
    
    @property
    def exec_time_path(self) -> str:
        return self._exec_time_path

    def setPtxSrcPath(self, ptx_src_path : str):
        self._ptx_src_path = ptx_src_path
    
    def setWarpTracesPaths(self):
        self._warp_traces_paths = set()
        for root, _, files in os.walk(self._res_dir_path):
            for file in files:
                if ".ptx" in file:
                    warp_trace_path = os.path.join(root, file)
                    self._warp_traces_paths.add(warp_trace_path)

    def __str__(self):
        return f"Instance name : {self._res_dir_path} | Exec time : {self._instance_exec_time}"

class ResultsParser():
    
    def __init__(self, sim_res_dir : str):
        self._sim_res_dir = sim_res_dir
        self._worst_traces_dict = None
        self._config_name = None
        self.registerWorstInstances()
        self.setConfigName()
            
    def __str__(self):
        res = ""
        instance_count = 0
        for kernel_name in self._worst_traces_dict.keys():
            configs_dict = self._worst_traces_dict[kernel_name]
            res += f"Kernel name : {kernel_name}\n"
            for warp_count in sorted(configs_dict.keys()):
                if warp_count > 1:
                    instance_count += 1
                    res += f"   {warp_count} warps :\n"
                    res += f"       exec time : {configs_dict[warp_count].instance_exec_time}\n"
                    res += f"       path : {configs_dict[warp_count].res_dir_path}\n"
        res += f"Results total {instance_count} instances"
        return res
    
    @property
    def config_name(self):
        return self._config_name

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

    def registerWorstInstances(self):
        worst_traces : dict[str, dict[int, InstanceData]] = dict()
        for root, dirs, _ in os.walk(self._sim_res_dir):
            for instance_name in dirs:
                dir_path = Path(os.path.join(root, instance_name))
                kernel_name = self.extractKernelName(instance_name)
                exec_time = self.getTraceExectime(dir_path)
                warp_count = self.getTraceWarpCount(dir_path)
                kernel_data = InstanceData(dir_path, kernel_name, warp_count, exec_time)
                # NOTE : Only for incomplete simulations. REMOVE WHEN SIMS ARE DONE
                if kernel_data.instance_exec_time:
                    if kernel_name in worst_traces.keys():
                        data_dict : dict[int, InstanceData] = worst_traces[kernel_name]
                        if warp_count in data_dict.keys():
                            registered_data = data_dict[warp_count]
                        if registered_data.instance_exec_time < kernel_data.instance_exec_time:
                            data_dict[warp_count] = kernel_data
                        else:
                            data_dict[warp_count] = kernel_data
                    else:
                        worst_traces[kernel_name] = dict()
                        worst_traces[kernel_name][warp_count] = kernel_data
        self._worst_traces_dict = worst_traces
     
    def setConfigName(self):
        res_path = Path(self._sim_res_dir)
        self._config_name = res_path.name
        
        
class ResultsDirProducer():
    
    def __init__(self, res_parser : ResultsParser, ptx_paths : PtxPaths):
        self._res_parser : ResultsParser = res_parser
        self._ptx_paths : PtxPaths = ptx_paths
    
    def generateExpDir(self, target_dir_name : str):
        self.createDir(target_dir_name)
        config_dir_name = os.path.join(target_dir_name, self._res_parser.config_name)
        self.createDir(config_dir_name)
        res_dict = self._res_parser._worst_traces_dict
        for kernel_name in res_dict.keys():
            bench_name = self._ptx_paths.getKernelBenchName(kernel_name)
            bench_res_dir = os.path.join(config_dir_name, bench_name)
            self.createDir(bench_res_dir)
            kernel_res_dir = os.path.join(bench_res_dir, kernel_name)
            ptx_src_path = self._ptx_paths.getKernelPtxPath(kernel_name)
            kernel_data = res_dict[kernel_name]
            for warp_count in kernel_data.keys():
                instance_dir = os.path.join(kernel_res_dir, f"{warp_count}warps")
                instance_data = kernel_data[warp_count]
                self.createDir(instance_dir, verbose=True)
                self.copyWarpTraces(instance_data.warp_traces_paths, instance_dir)
                shutil.copy(ptx_src_path, instance_dir)
                shutil.copy(instance_data.exec_time_path, instance_dir)
                # TODO : At this point, populate the folder with all required files
                #   This includes : - warp traces : DONE
                #                   - ptx src file : DONE
                #                   - exec time : DONE
                #                   - bounds : IN PROGRESS
    
    def copyWarpTraces(self, warps_trace_src : set[str], dst : str):
        for trace_src in warps_trace_src:
            shutil.copy(trace_src, dst)
    
    def createDir(self, target_dir_name : str, verbose : bool = False):
        try:
            os.makedirs(target_dir_name)
            if(verbose):
                print(f"Directory \"{target_dir_name}\" created.")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"Error : {e}")
            exit(-2)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage : {sys.argv[0]} traces_dir ptx_src_dir exp_target_dir")
        exit(1)
    traces_dir_name = sys.argv[1]
    ptx_src_dir = sys.argv[2]
    exp_target_dir = sys.argv[3]
    res_parser = ResultsParser(traces_dir_name)
    ptx_paths = PtxPaths(ptx_src_dir)
    res_producer = ResultsDirProducer(res_parser, ptx_paths)
    res_producer.generateExpDir(exp_target_dir)
    exit(0)