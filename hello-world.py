from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
)

# Setzen der Koppler h_ij
h = {
    (0,0): -1,  # Koppler auf Qubit 0
    (1,1):  1,  # Koppler auf Qubit 1
    (2,2):  0,  # Koppler auf Qubit 2
    (1,5):  1,  # Koppler zwischen Qubits 1 und 5
    (1,6): -1,  # Koppler zwischen Qubits 1 und 6
}

# Anneal starten
response = sampler.sample_qubo(
    h, 
    num_reads=100,
)

# Loesungen ansehen
dwave.inspector.show(response)
