import os
import sys
import re

extract_warp_idx = "(?<=warp )[0-9]+"
extract_ptx_instr = "(?<=\) ).*"
extract_instr_addr = "(?<=0x)[a-f0-9]+"
extract_exec_time = "(?<=kernel_execution_time : ).*"
extract_trace_name = "[_a-zA-Z0-9]*-instance_[0-9]+"
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
    
    def setPtxInstruction(self, ptx_instruction : str):
        self._ptx_instruction = ptx_instruction
        
    @property
    def address(self):
        return self._address
    
    @property
    def ptx_instruction(self):
        return self._ptx_instruction
    
    @property
    def warp_idx(self):
        return self._warp_idx
    
    @property
    def is_branch(self):
        return "bra" in self._ptx_instruction

    def isContiguous(self, next_instr : 'Instruction'):
        return self.address + 8 == next_instr.address
    
class WarpTrace():
    
    def __init__(self, warp_id : int):
        self._warp_id : int = warp_id
        self._instructions : list[Instruction] = []
        self._branch_uid = 0
    
    def addInstruction(self, instr : Instruction):
        self._instructions.append(instr)
        
    def addTakenHint(self, branch_instr : Instruction, next_instr : Instruction):
        try:
            prefix = re.search(extract_bra_prefix, branch_instr.ptx_instruction).group(0)
            if not "@" in prefix:
                prefix = f"@{prefix}"
        except:
            if "bra.uni" in branch_instr.ptx_instruction:
                prefix = "bra.uni "
            else:
                print(f"Not a branch instruction : {branch_instr.ptx_instruction}")
                exit()
        if not branch_instr.isContiguous(next_instr):
            label = f"BBtaken_{self._branch_uid}"
        else:
            label = f"BB_{self._branch_uid}"
            
        new_ptx_instruction = f"{prefix}{label};\n\n{label}:"
        self._branch_uid += 1
        branch_instr.setPtxInstruction(new_ptx_instruction)
        
    def writeTrace(self, trace_dir : str):
        warp_trace_path = os.path.join(trace_dir, f"w{self._warp_id}.ptx")
        warp_trace_file = open(warp_trace_path, "w")
        warp_trace_file.write(ptx_header)
        for i in range(len(self._instructions)):
            instr = self._instructions[i]
            if instr.is_branch:
                self.addTakenHint(instr, self._instructions[i+1])
            warp_trace_file.write(f"{instr.ptx_instruction}\n")
        warp_trace_file.write("}")
        warp_trace_file.close()
        
class KernelTraces():
    
    def __init__(self):
        self._traces : dict[int, WarpTrace] = dict()
    
    def addInstruction(self, instr : Instruction):
        warp_idx = instr.warp_idx
        if not warp_idx in self._traces.keys():
            self._traces[warp_idx] = WarpTrace(warp_idx)
        self._traces[warp_idx].addInstruction(instr)
        
    def writeTraces(self, res_dir : str):
        for warp in self._traces.keys():
            self._traces[warp].writeTrace(res_dir)    

def extract_results(traces_dir : str, target_dir_name : str):
    for root, _, files in os.walk(traces_dir):
        for file in files:
            if ".trace" in file:
                trace_path = os.path.join(root, file)
                data_name = os.path.split(os.path.dirname(os.path.dirname(trace_path)))[1]
                res_dir = f"{target_dir_name}/{data_name}-{re.search(extract_trace_name, file).group(0)}"
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
                kernel_traces = KernelTraces()
                for line in trace_file.readlines():
                    if "0x" in line:
                        kernel_traces.addInstruction(Instruction(line))
                    else:
                        try:
                            exec_time = re.search(extract_exec_time, line).group(0)
                            exec_time_file = open(f"{res_dir}/exectime.txt", "w")
                            exec_time_file.write(exec_time)
                            exec_time_file.close()
                        except:
                            print(f"Couldn't extract an execution time for {file}")
                kernel_traces.writeTraces(res_dir)

def extract_traces(traces_dir : str, target_dir_name : str):
    for root, dir ,files in os.walk(traces_dir):   
        for file in files:
            if ".trace" in file:
                trace_path = os.path.join(root, file)
                data_name = os.path.split(os.path.dirname(os.path.dirname(trace_path)))[1]
                res_dir = target_dir_name + "/" + data_name + "-" + re.search(extract_trace_name, file).group(0)
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
                last_instruction : dict[int, Instruction] = dict()
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
                        pred_instruction = None
                        if warp_idx in last_instruction.keys():
                            pred_instruction = last_instruction[warp_idx]
                        if not warp_idx in out_files:
                            out_files[warp_idx] = open(f"{res_dir}/w{warp_idx}.ptx", "w")
                            out_files[warp_idx].write(ptx_header)
                        ptx_instr = instruction.ptx_instruction
                        if pred_instruction and pred_instruction.is_branch:
                            if pred_instruction.address + 8 != instruction.address:
                                branch_inst = re.search(extract_bra_prefix, pred_instruction.ptx_instruction).group(0)
                                hint = "taken"
                                if abs(pred_instruction.address - instruction.address) >= 512:
                                    hint += "far"
                                if not '@' in pred_instruction:
                                    ptx_instr = "@" + pred_instruction + "BB" + hint + "_" + str(branch_uid) + ";"
                                else:
                                    ptx_instr = branch_inst + "BB" + hint + "_" + str(branch_uid) + ";"
                            out_files[warp_idx].write(ptx_instr + "\n")
                            out_files[warp_idx].write("\nBB" + hint + "_" + str(branch_uid) + ":\n")
                            branch_uid += 1
                        if not instruction.is_branch:
                            out_files[warp_idx].write(ptx_instr + "\n")
                        last_instruction[warp_idx] = instruction
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
    # extract_traces(sys.argv[1], sys.argv[2])
    extract_results(sys.argv[1], sys.argv[2])