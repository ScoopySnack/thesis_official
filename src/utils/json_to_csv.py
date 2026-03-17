import json
import csv

# Load the enriched JSON file
with open("alkanesStenutz.json", "r", encoding='utf-8') as file:
    data = json.load(file)

# Extract all alkanes
alkanes = data["alkanes"]

# Flatten each alkane's properties
flat_data = []

for name, props in alkanes.items():
    row = {
        "name": name,
        "number_ofC": props.get("number_ofC"),
        "molecular_weight": props.get("molecular_weight"),
        "density": props.get("Density"),
        "molar_volume": props.get("molar_volume"),
        "refractive_index": props.get("refractive_index"),
        "Molecular_refractive_power": props.get("Molecular_refractive_power"),
        "dielectric_constant": props.get("dielectric_constant"),
        "dipole_moment": props.get("dipole_moment"),
        "melting_point": props.get("melting_point"),
        "boiling_point": props.get("boiling_point"),
        "vapour_pressure": props.get("vapour_pressure"),
        "surface_tension": props.get("surface_tension"),
        "viscosity": props.get("viscosity"),
        "logP": props.get("logP"),
        "solubility_parameter": props.get("\δ"),
        "specific_heat_capacity": props.get("specific_heat_capacity")
    }

    # Add critical point fields
    crit = props.get("critical_point", {})
    row["Tc"] = crit.get("temperature_Tc")
    row["Pc"] = crit.get("pressure_Pc")
    row["Vc"] = crit.get("volume_Vc")

    # Add graph properties
    # graph = props.get("graph_properties", {})
    # row["perron_frobenius"] = graph.get("perron_frobenius")
    # row["fiedler_eigenvalue"] = graph.get("fiedler_eigenvalue")
    # row["compression_ratio"] = graph.get("compression_ratio")
    # row["information_content"] = graph.get("information_content")

    flat_data.append(row)

# Get all column headers
fieldnames = list(flat_data[0].keys())

# Write to CSV
with open("alkanes_Stenutz.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(flat_data)

print("✅ CSV created as 'alkanes_Stenutz.csv'")
