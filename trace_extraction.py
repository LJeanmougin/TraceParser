import os
import sys
import re
from io import TextIOWrapper

extract_warp_idx = "(?<=warp )[0-9]+ "
extract_ptx_instr = "(?<=\) ).*"
extract_exec_time = "(?<=kernel_execution_time : ).*"

ptx_header=".version 7.0\n" \
".target sm_75\n" \
".address_size 64\n" \
".visible .entry _Z12vecaddKernelPiS_S_i(\n" \
".param .u64 _Z12vecaddKernelPiS_S_i_param_0,\n" \
".param .u64 _Z12vecaddKernelPiS_S_i_param_1,\n" \
".param .u64 _Z12vecaddKernelPiS_S_i_param_2,\n" \
".param .u32 _Z12vecaddKernelPiS_S_i_param_3\n" \
")\n" \
"{\n"

def extract_traces(trace_file_name : str, target_dir_name : str):
    try:
        os.mkdir(target_dir_name)
        print(f"Directory \"{target_dir_name}\" created..")
    except FileExistsError:
        print(f"Directory \"{target_dir_name}\" already exists..")
    except PermissionError:
        print(f"Permission denied to create \"{target_dir_name}\"")
    except Exception as e:
        print(f"Error : {e}")
    trace_file = open(trace_file_name)
    out_files = dict()
    for line in trace_file.readlines():
        try:
            warp_idx = re.search(extract_warp_idx, line).group(0)
            if not warp_idx in out_files:
                out_files[warp_idx] = open(f"{target_dir_name}/w{warp_idx}.ptx", "w")
                out_files[warp_idx].write(ptx_header)
            ptx_instr = re.search(extract_ptx_instr, line).group(0)
            out_files[warp_idx].write(ptx_instr + "\n")
        except:
            print(f"Not an instruction line..")
            try :
                exec_time = re.search(extract_exec_time, line)
                exec_time_file = open(f"{target_dir_name}/exectime.txt", "w")
                exec_time_file.write(exec_time)
            except :
                print(f"Not an execution time info either..")
    for item in out_files:
        out_files[item].write("}\n")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} trace_file target_dir")
        exit(0)
    extract_traces(sys.argv[1], sys.argv[2])