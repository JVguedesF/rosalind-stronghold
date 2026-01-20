from utils.io import read_fasta

def calculate_overlap(s1: str, s2: str) -> int:
    max_possible_overlap = min(len(s1), len(s2))
    
    for length in range(max_possible_overlap, 0, -1):
        if s2.startswith(s1[-length:]):
            return length
    return 0

def build_overlap_graph(sequences: list[str]):
    n = len(sequences)
    graph = {}
    
    for i in range(n):
        graph[i] = []
        for j in range(n):
            if i == j:
                continue
            
            overlap = calculate_overlap(sequences[i], sequences[j])
            min_overlap = len(sequences[i]) // 2 + 1
            
            if overlap >= min_overlap:
                graph[i].append((j, overlap))
    
    return graph

def find_hamiltonian_path(graph, n):
    def dfs(node, visited, path):
        if len(path) == n:
            return path
        
        for neighbor, overlap in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, visited, path + [neighbor])
                if result:
                    return result
                visited.remove(neighbor)
        
        return None
    
    for start in range(n):
        visited = {start}
        path = dfs(start, visited, [start])
        if path:
            return path
    
    return None

def build_superstring(sequences: list[str], path: list[int]):
    if not path:
        return ""
    
    result = sequences[path[0]]
    
    for i in range(1, len(path)):
        prev_idx = path[i-1]
        curr_idx = path[i]
        
        overlap = calculate_overlap(sequences[prev_idx], sequences[curr_idx])
        result += sequences[curr_idx][overlap:]
    
    return result

def solve():
    sequences = list(read_fasta().values())
    
    if not sequences:
        return ""
    
    if len(sequences) == 1:
        return sequences[0]
    
    graph = build_overlap_graph(sequences)
    
    path = find_hamiltonian_path(graph, len(sequences))
    
    if not path:
        return ""
    
    return build_superstring(sequences, path)

if __name__ == "__main__":
    print(solve())