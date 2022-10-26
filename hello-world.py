from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
)

# Setzen der Koppler h_ij
h = {
    (0,0): -1,  # Qubit 0 soll 1 werden
    (1,1):  1,  # Qubit 1 soll 0 werden
    (1,2):  1,  # Qubit 1 und 2 sollen nicht gleichzeitig 1 werden
    (1,3): -1,  # Qubit 1 und 3 sollen beide 1 werden
}

response = sampler.sample_qubo(
    h, 
    num_reads=100,
)

dwave.inspector.show(response)
