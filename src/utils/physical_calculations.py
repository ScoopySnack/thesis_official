import pandas as pd

#df = pd.read_csv('../../data/raw/alkanes_Stenutz.csv')


def molar_volume(MW, density):
    return MW / density


def calculate_rm_experimental(n, rho, M):
    """
    Calculates Molar Refraction (Rm) using the Lorentz-Lorenz equation.

    Parameters:
    n   (float): Refractive Index (dimensionless)
    rho (float): Density (g/mL)
    M   (float): Molar Mass (g/mol)

    Returns:
    float: Molar Refraction (mL/mol)
    """
    fraction = (n ** 2 - 1) / (n ** 2 + 2)
    Rm = fraction * (M / rho)
    return Rm


def calculate_rm_theoretical(num_C, num_H):
    """
    Calculates theoretical Molar Refraction based on atomic contributions.

    Parameters:
    num_C (int): Number of Carbon atoms
    num_H (int): Number of Hydrogen atoms

    Returns:
    float: Theoretical Molar Refraction (mL/mol)
    """
    # Standard atomic refraction constants (Vogel)
    R_C = 2.418  # Contribution per Carbon
    R_H = 1.100  # Contribution per Hydrogen

    Rm = (num_C * R_C) + (num_H * R_H)
    return Rm

Ref_idx = 1.403  # Refractive Index
density = 0.716  # Density (g/mL)
MW = 128.26  # Molar Mass (g/mol)
num_C=9
num_H=2*num_C

# 2. Calculate
rm_exp = calculate_rm_experimental(Ref_idx, density, MW)
rm_theo = calculate_rm_theoretical(num_C, num_H)

# 3. Output
print(f"Experimental Rm: {rm_exp:.3f} mL/mol")
print(f"Theoretical Rm:  {rm_theo:.3f} mL/mol")