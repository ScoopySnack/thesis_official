# Data Dictionary: Alkane Physical Properties & Graph Descriptors

## 1. Overview
This dataset contains structural information, graph-theoretic descriptors, and experimental physical properties for linear and branched alkanes ($C_n H_{2n+2}$) ranging from $n=1$ to $n=9$. The data is used to train machine learning models to predict physical behavior from molecular symmetry.

## 2. Identifiers & Chemical Composition
| Column Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `name` | String | IUPAC systematic name of the molecule. | `2,2-dimethylpropane` |
| `formula` | String | Molecular formula. | `C5H12` |
| `smiles` | String | Simplified Molecular Input Line Entry System string. | `CC(C)(C)C` |
| `num_carbons` | Integer | Total count of Carbon atoms (Vertices $V$). | `5` |
| `molecular_weight` | Float | Molecular mass in $g/mol$. | `72.15` |

## 3. Graph-Theoretic Descriptors (Features)
These features are computed from the molecular graph $G=(V,E)$ where atoms are vertices and bonds are edges.

| Column Name | Symbol | Description | Theoretical Basis |
| :--- | :--- | :--- | :--- |
| `eig_pf` | $\lambda_{PF}$ | **Perron-Frobenius Eigenvalue**. The largest eigenvalue of the Adjacency matrix $A$. Measures branching and centrality. | Spectral Graph Theory |
| `eig_fiedler` | $\lambda_2$ | **Fiedler Value**. The second smallest eigenvalue of the Laplacian matrix $L$. Measures algebraic connectivity and rigidity. | Spectral Graph Theory |
| `wiener_idx` | $W$ | **Wiener Index**. Sum of distances between all pairs of vertices. Correlates with boiling point. | Topological Indices |
| `compression_ratio` | $\rho$ | **Graph Compression Ratio**. Ratio of vertices in the quotient graph vs. original graph ($|V_Q| / |V|$). Quantifies symmetry. | Algebraic Graph Theory |
| `num_automorphisms` | $|Aut(G)|$ | Size of the automorphism group. A direct measure of symmetry. | Group Theory |

## 4. Physical Properties (Targets)
Experimental values sourced from Stenutz (2023) and Lide (2005).

| Column Name | Units | Description |
| :--- | :--- | :--- |
| `boiling_point` | $^\circ C$ | Temperature at which the liquid turns to vapor at 1 atm. |
| `density` | $g/cm^3$ | Mass per unit volume (at standard conditions). |
| `molar_volume` | $cm^3/mol$ | Volume occupied by one mole of the substance. |
| `refractive_index` | $n_D$ | Measure of how light propagates through the medium. |

## 5. Data Sources
1. **Stenutz, R. (2023).** *Alkanes Dataset*. Retrieved from https://www.stenutz.eu/chem/set10.php.
2. **Lide, D. R. (2005).** *CRC Handbook of Chemistry and Physics* (86th ed.).