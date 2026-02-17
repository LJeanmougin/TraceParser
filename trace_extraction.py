import os
import sys
import re

extract_warp_idx = "(?<=warp )[0-9]+"
extract_ptx_instr = "(?<=\) ).*"
extract_instr_addr = "(?<=0x)[a-f0-9]+"
extract_exec_time = "(?<=kernel_execution_time : ).*"
extract_trace_name = "[_a-zA-Z0-9]*"
find_bra_target = "BB[a-zA-Z_0-9]*"
extract_bra_prefix = "[@%p0-9]* bra[\.a-zA-Z0-9]* "

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

class Instruction():
    def __init__(self, line : str):
        try:
            self._address = int(re.search(extract_instr_addr, line).group(0), 16)
        except:
            print(f"No address found in : {line}")
        try:
            self._ptx_instruction = re.search(extract_ptx_instr, line).group(0)
        except:
            print("No instruction found")
        try:
            self._warp_idx = re.search(extract_warp_idx, line).group(0)
        except:
            print("No warp idx")    
        
    @property
    def address(self):
        return self._address
    
    @property
    def ptx_instruction(self):
        return self._ptx_instruction
    
    @property
    def warp_idx(self):
        return self._warp_idx
    

def extract_traces(traces_dir : str, target_dir_name : str):
    for root, dir ,files in os.walk(traces_dir):   
        for file in files:
            if ".trace" in file:
                trace_path = os.path.join(root, file)
                res_dir = target_dir_name + "/" + re.search(extract_trace_name, file).group(0)
                try:
                    os.makedirs(res_dir)
                    print(f"Directory \"{res_dir}\" created..")
                except FileExistsError:
                    print(f"Current file is {file.__str__()} but :")
                    print(f"Directory \"{res_dir}\" already exists..")
                except PermissionError:
                    print(f"Permission denied to create \"{res_dir}\"")
                except Exception as e:
                    print(f"Error : {e}")
                trace_file = open(trace_path)
                out_files = dict()
                branch_uid = 0
                # To detect branch taken or not
                instructions : list[Instruction] = []
                for line in trace_file.readlines():
                    if "0x" in line:
                        instructions.append(Instruction(line))
                    else:
                        try:
                            exec_time = re.search(extract_exec_time, line).group(0)
                            exec_time_file = open(f"{res_dir}/exectime.txt", "w")
                            exec_time_file.write(exec_time)
                            exec_time_file.close()
                        except:
                            pass
                for i in range(len(instructions)):
                    try:
                        instruction = instructions[i]
                        warp_idx = instruction.warp_idx
                        if not warp_idx in out_files:
                            out_files[warp_idx] = open(f"{res_dir}/w{warp_idx}.ptx", "w")
                            out_files[warp_idx].write(ptx_header)
                        ptx_instr = instruction.ptx_instruction
                        try :
                            # getting branch target for block analyzer
                            branch_inst = re.search(extract_bra_prefix, ptx_instr).group(0)
                            taken = instruction.address + 8 != instructions[i+1].address
                            hint = "taken" if taken else ""
                            if abs(instruction.address - instructions[i+1].address) >= 512:
                                hint += "far"
                            if not '@' in branch_inst:
                                ptx_instr = "@" + branch_inst + "BB" + hint + "_" + str(branch_uid) + ";"
                            else:
                                ptx_instr = branch_inst + "BB" + hint + "_" + str(branch_uid) + ";"
                        except :
                            if "bra.uni" in ptx_instr:
                                taken = instruction.address + 8 != instructions[i+1].address
                                hint = "taken" if taken else ""
                                if abs(instruction.address - instructions[i+1].address) >= 512:
                                    hint += "far"
                                branch_inst = "bra.uni BB" + hint + "_" + str(branch_uid) + ";"
                                ptx_instr = branch_inst 
                            else:
                                branch_inst = None
                        out_files[warp_idx].write(ptx_instr + "\n")
                        if branch_inst:
                            out_files[warp_idx].write("\nBB" + hint + "_" + str(branch_uid) + ":\n")
                            branch_uid += 1
                    except:
                        print(f"Not an instruction line..")
                        try :
                            exec_time = re.search(extract_exec_time, line).group(0)
                            exec_time_file = open(f"{res_dir}/exectime.txt", "w")
                            exec_time_file.write(exec_time)
                            exec_time_file.close()
                        except :
                            print(f"Not an execution time info either..")
                for item in out_files:
                    out_files[item].write("}\n")
                    out_files[item].close()
                trace_file.close()
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage : {sys.argv[0]} traces_dir target_dir")
        exit(0)
    extract_traces(sys.argv[1], sys.argv[2])