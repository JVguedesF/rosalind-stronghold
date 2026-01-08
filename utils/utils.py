import os
import inspect

def _get_path(filename):
    if os.path.isabs(filename):
        return filename
    frame = inspect.stack()[2]
    module_path = os.path.dirname(os.path.abspath(frame.filename))
    return os.path.join(module_path, filename)

def read_input(filename="input.txt"):
    path = _get_path(filename)
    with open(path, "r") as f:
        return f.read().strip()
    
def read_fasta(filename="input.txt"):
    path = _get_path(filename) 
    sequences = {}
    current_id = None
    current_sequence = []
    
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_sequence)
                
                current_id = line[1:]
                current_sequence = []
            
            else:
                current_sequence.append(line)
        
        if current_id is not None:
            sequences[current_id] = "".join(current_sequence)
            
    return sequences

def read_lines(filename="input.txt"):
    path = _get_path(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]