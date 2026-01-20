import requests
import re
from utils.io import read_lines

def solve():
    protein_ids = read_lines()
    
    motif = re.compile(r'(?=(N[^P][ST][^P]))')
    
    for full_id in protein_ids:
        access_id = full_id.split('_')[0]
        url = f"https://rest.uniprot.org/uniprotkb/{access_id}.fasta"
        
        response = requests.get(url)
        if response.status_code == 200:
            sequence = "".join(response.text.strip().split('\n')[1:])
            
            positions = [m.start() + 1 for m in motif.finditer(sequence)]
            
            if positions:
                print(full_id)
                print(*positions)

if __name__ == "__main__":
    solve()