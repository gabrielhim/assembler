from collections import defaultdict


def build_graph(k_mers: list[str]) -> tuple[set, dict]:
    """
    Nuilds a De Bruijn graph.
    """
    nodes = set()
    graph = defaultdict(list)
    counter = 1
    for k_mer in k_mers:
        prefix = k_mer[:-1]
        suffix = k_mer[1:]
        nodes.add(prefix)
        nodes.add(suffix)
        graph[prefix].append((suffix, counter))
        counter += 1
    return nodes, graph


def find_source(nodes: set, graph: dict) -> str:
    """
    Finds the source node in the graph. If none is found,
    returns the first node of the iterator.
    """
    counts_in = defaultdict(int)
    counts_out = defaultdict(int)
    for v in graph:
        for w, _ in graph[v]:
            counts_in[w] += 1
            counts_out[v] += 1
    for node in nodes:
        if counts_in[node] < counts_out[node]:
            return node
    return next(iter(graph))


def mark_visited(track: list, graph: dict, v: str, cycle: list) -> None:
    """
    Recursively marks the nodes visited in the graph.
    """
    if v in graph:
        for w, x in graph[v]:
            if not track[(v, w, x)]:
                track[(v, w, x)] = True
                mark_visited(track, graph, w, cycle)
    cycle.append(v)


def reconstruct_genome(k_mers: list[str]) -> str:
    """
    Reconstructs the genome from the given k-mer sequences.
    """
    nodes, graph = build_graph(k_mers)
    track = {}
    for v in graph:
        for w, x in graph[v]:
            track[(v, w, x)] = False
    source = find_source(nodes, graph)
    cycle = []
    mark_visited(track, graph, source, cycle)
    genome = [cycle[-1]]
    for i in range(len(cycle) - 2, -1, -1):
        genome.append(cycle[i][-1])
    return "".join(genome)
