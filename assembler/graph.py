from collections import defaultdict


def build_graph(k: int, reads: list) -> tuple[set, dict]:
    """Builds a De Bruijn graph."""
    nodes = set()
    graph = defaultdict(set)
    for read in reads:
        for i in range(len(read) - k + 1):
            k_mer = read[i : k + i]
            prefix = k_mer[:-1]
            suffix = k_mer[1:]
            nodes.add(prefix)
            nodes.add(suffix)
            graph[prefix].add(suffix)
    return nodes, graph


def is_eulerian_cycle(nodes: set, graph: dict) -> bool:
    """Checks if a given graph is Eulerian."""
    counts_in = defaultdict(int)
    counts_out = defaultdict(int)
    for v in graph:
        for w in graph[v]:
            counts_in[w] += 1
            counts_out[v] += 1
    for node in nodes:
        if counts_in[node] != counts_out[node]:
            return False
    return True


def select_k_mer_size(reads: list) -> int:
    """Selects the best value of k to divide reads."""
    k = len(reads[0]) - 1
    is_cycle = False
    while k:
        tmp_nodes, tmp_graph = build_graph(k, reads)
        is_cycle = is_eulerian_cycle(tmp_nodes, tmp_graph)
        if is_cycle:
            break
        k -= 1
    return k


def mark_visited(track: list, graph: dict, v: str, cycle: list) -> None:
    """Recursively marks the nodes visited in the graph."""
    if v in graph:
        for w in graph[v]:
            if not track[(v, w)]:
                track[(v, w)] = True
                mark_visited(track, graph, w, cycle)
    cycle.append(v)


def reconstruct_genome(reads: list[str], k: int) -> str:
    """Reconstructs the genome from the given sequences."""
    nodes, graph = build_graph(k, reads)
    track = {}
    for v in graph:
        for w in graph[v]:
            track[(v, w)] = False
    source = min(nodes)
    cycle = []
    mark_visited(track, graph, source, cycle)
    genome = [cycle[-1]]
    for i in range(len(cycle) - 2, -1, -1):
        genome.append(cycle[i][-1])
    return "".join(genome[: -k + 1])
