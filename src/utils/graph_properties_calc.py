
import numpy as np
import networkx as nx
from rdkit import Chem
from rdkit.Chem import rdmolops



def get_adj_matrix(smiles):
    """
    This fundamental utility function takes the SMILES string, generates an RDKit molecular object, and computes the
    mathematical Adjacency Matrix. This matrix is the numerical foundation upon which all subsequent topological algorithms operate
    :param smiles:
    :return: adj_matrix:
    """
    mol = Chem.MolFromSmiles(smiles)
    adj = rdmolops.GetAdjacencyMatrix(mol)
    return adj

def perron_frobenius(smiles):
    """
        Calculates the Perron-Frobenius eigenvalue (Spectral Radius)
        of a molecule from its SMILES string.
        """
    adj_matrix = get_adj_matrix(smiles)
    # Compute Eigenvalues for Symmetric Matrix
    # eigvalsh is optimized for symmetric matrices (Hermitian)
    eigenvalues = np.linalg.eigvalsh(adj_matrix)

    # The spectral radius is the maximum absolute eigenvalue.
    # For adjacency matrices of undirected graphs, the largest algebraic
    # eigenvalue is the Perron-Frobenius root.
    pf_eigenvalue = np.max(eigenvalues)
    return pf_eigenvalue

def fiedler_eigenvalue(smiles):
    """
        Computes the Fiedler eigenvalue (algebraic connectivity)
        of a graph given its adjacency matrix.
        """
    # Create the Degree matrix (diagonal matrix of row sums)
    degrees = np.sum(get_adj_matrix(smiles), axis=1)
    D = np.diag(degrees)

    # Compute Laplacian
    L = D - get_adj_matrix(smiles)

    # Compute eigenvalues (we use eigh for symmetric matrices)
    eigenvalues = np.linalg.eigh(L)[0]

    # Sort eigenvalues. The smallest is always 0 (or close to it due to precision).
    # The second smallest is the Fiedler eigenvalue.
    sorted_eigenvalues = np.sort(eigenvalues)

    # Return the second smallest
    return sorted_eigenvalues[1] if len(sorted_eigenvalues) > 1 else 0

def compute_cep(adj_matrix):
    n = adj_matrix.shape[0]
    # Start by grouping nodes by degree
    degrees = np.sum(adj_matrix, axis=1)
    unique_degrees = np.unique(degrees)
    partition = [np.where(degrees == d)[0].tolist() for d in unique_degrees]

    while True:
        new_partition = []
        # Map each node to its current cell index
        node_to_cell = {node: i for i, cell in enumerate(partition) for node in cell}

        for cell in partition:
            signatures = {}
            for node in cell:
                # Signature: how many neighbors does this node have in each current cell?
                sig = []
                for target_cell in partition:
                    count = sum(adj_matrix[node, neighbor] for neighbor in target_cell)
                    sig.append(count)

                sig = tuple(sig)
                if sig not in signatures:
                    signatures[sig] = []
                signatures[sig].append(node)

            # Add split cells to the new partition
            new_partition.extend(signatures.values())

        if len(new_partition) == len(partition):
            break
        partition = new_partition

    return partition

def compression_ratio(smiles):
    """
        Calculates the compression ratio of a SMILES string.
        Higher values = Simpler/More Repetitive Structure.
        Lower values = More Complex/Unique Structure.
        """
    G = nx.from_numpy_array(get_adj_matrix(smiles))
    # n_G: Number of vertices in original graph
    n_G = G.number_of_nodes()
    # m: Number of edges in original graph
    m = G.number_of_edges()

    if m == 0: return 0

    # 1. Get the Equitable Partition (CEP)
    # We'll use the refinement algorithm to ensure it works on your NX version
    partition = compute_cep(nx.to_numpy_array(G))
    n_QG = len(partition)

    # 2. Calculate 'a' (Number of arcs in the Quotient Graph)
    # An arc exists between cell i and cell j if any node in i
    # is connected to any node in j.
    a = 0
    for i in range(n_QG):
        for j in range(n_QG):  # Check pairs of cells
            # Pick a representative node from cell i
            u = partition[i][0]
            # Check if it has any neighbors in cell j
            has_edge = any(G.has_edge(u, v) for v in partition[j])

            if has_edge:
                a += 1

    cr = (n_QG / n_G) * (a / m)
    return round(cr, 4)

def information_content(smiles):
    # 1. Get the Adjacency Matrix
    adj = get_adj_matrix(smiles)

    # 2. Get total number of atoms (n) directly from the matrix shape
    n = adj.shape[0]
    if n == 0: return 0.0

    # 3. Compute the Partition of the graph using the same method as for CR
    partition = compute_cep(adj)

    # 4. Calculate Shannon Entropy (Information Content)
    ic = 0.0
    for cell in partition:
        # Probability of a random node falling into this symmetry cell
        p = len(cell) / n

        # Shannon Entropy Formula: -sum(p * log2(p))
        if p > 0:
            ic += -p * np.log2(p)
    return round(ic, 4)


if __name__ == "__main__":
    test_smiles = "CC(C)CC(C)(C)C"  # Example SMILES for testing
    result = information_content(test_smiles)
    G = get_adj_matrix(test_smiles)

    print(compute_cep(G), information_content(test_smiles), compression_ratio(test_smiles))
