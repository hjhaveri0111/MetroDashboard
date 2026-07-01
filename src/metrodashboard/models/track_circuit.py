class TrackCircuit:
    def __init__(self, raw_contents) -> None:
        self.circuit_id = raw_contents['CircuitId']
        self.neighbors = [Neighbor(neighbor) for neighbor in raw_contents['Neighbors']]
        self.track = raw_contents['Track']

    def __str__(self):
        neighbors_str = ', '.join(f"{n.neighbor_type}->{','.join(map(str, n.circuit_ids))}" for n in self.neighbors)
        return f"[Circuit {self.circuit_id} | Track {self.track} | Neighbors: {neighbors_str}]"

class Neighbor:
    def __init__(self, raw_contents) -> None:
        self.circuit_ids = raw_contents['CircuitIds']
        self.neighbor_type = raw_contents['NeighborType']

    def __str__(self):
        return f"{self.neighbor_type}->{','.join(map(str, self.circuit_ids))}"