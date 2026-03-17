import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import rdmolops
import cirpy

def get_smiles(name):
    name_clean = name.strip()

    # 1. Try PubChem (Fast, strict)
    try:
        compounds = pcp.get_compounds(name_clean, 'name')
        if compounds is not None:
            return compounds[0].connectivity_smiles
    except:
        pass

    # 2. Try CIRPy (Smarter, fixes numbering errors like 3,3-dimethyl...)
    try:
        # returns SMILES string directly
        smiles = cirpy.resolve(name_clean, 'smiles')
        if smiles:
            return smiles
    except:
        pass
    return None


def name_to_matrix(chemical_name):
    try:
        # 1. Search PubChem for the compound
        compound = pcp.get_compounds(chemical_name, 'name')[0]

        # 2. Get the Canonical SMILES from the result
        smiles = compound.connectivity_smiles

        # 3. Convert to Matrix using RDKit
        mol = Chem.MolFromSmiles(smiles)
        matrix = rdmolops.GetAdjacencyMatrix(mol)

        return matrix, smiles
    except IndexError:
        print(f"Could not find '{chemical_name}'")
        return None, None