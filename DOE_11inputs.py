# -*- coding: latin-1 -*-
import numpy as np
import pandas as pd
import itertools

# Set Pandas options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Define the levels for each parameter for the first design
param_levels_1 = {
    'Number of holes, nh': np.array([3, 4 ,5], dtype='float32'),
    'Web-post width, WP (mm)': np.array([3.5, 4.0, 4.5], dtype='float32'),
    'Web opening diameter, Do (mm)': np.array([35, 40, 45], dtype='float32'),
    'Ply 1 (°)': np.array([-45, 0, 45, 90], dtype='float32'),
    'Ply 2 (°)': np.array([-45, 0, 45, 90], dtype='float32'),
    'Ply 3 (°)': np.array([-45, 0, 45, 90], dtype='float32'),
    'Ply 4 (°)': np.array([-45, 0, 45, 90], dtype='float32')
}

# Generate combinations of the first four parameters without repetition for the first design
combinations_1_to_4_1 = itertools.product(param_levels_1['Number of holes, nh'],
                                        param_levels_1['Web-post width, WP (mm)'],
                                        param_levels_1['Web opening diameter, Do (mm)'],
                                        param_levels_1['Ply 1 (°)'],
                                        param_levels_1['Ply 2 (°)'],
                                        param_levels_1['Ply 3 (°)'],
                                        param_levels_1['Ply 4 (°)'])

# Filter out combinations where all four plies are the same for the first design
filtered_combinations_1_to_4_1 = filter(lambda x: len(set(x[3:7])) == 4, combinations_1_to_4_1)

# Create DataFrame from filtered combinations for plies 1 to 4 for the first design
design_1_to_4_1 = pd.DataFrame(filtered_combinations_1_to_4_1, columns=param_levels_1.keys())

# Add symmetric combinations for plies 5 to 8 for the first design
design_5_to_8_1 = design_1_to_4_1.copy()
design_5_to_8_1[['Ply 5 (°)', 'Ply 6 (°)', 'Ply 7 (°)', 'Ply 8 (°)']] = design_1_to_4_1[['Ply 4 (°)', 'Ply 3 (°)', 'Ply 2 (°)', 'Ply 1 (°)']].values

# Concatenate designs for plies 1 to 4 and plies 5 to 8 for the first design
final_design_1 = pd.concat([design_1_to_4_1, design_5_to_8_1], ignore_index=True)

# Remove rows where any ply is blank for the first design
final_design_1 = final_design_1.dropna()

# Add a new column for row numbering for the first design
final_design_1['Number'] = range(1, len(final_design_1) + 1)

# Reorder columns to have the 'Number' column as the first column for the first design
final_design_1 = final_design_1[['Number'] + [col for col in final_design_1.columns if col != 'Number']]

# Define the levels for each parameter for the second design
param_levels_2 = {
    'Number of holes, nh': np.array([3, 4 ,5], dtype='float32'),
    'Web-post width, WP (mm)': np.array([3.5, 4.0, 4.5], dtype='float32'),
    'Web opening diameter, Do (mm)': np.array([35, 40, 45], dtype='float32'),
    'Ply 1 (°)': np.array([0, 30, 60, 90], dtype='float32'),
    'Ply 2 (°)': np.array([0, 30, 60, 90], dtype='float32'),
    'Ply 3 (°)': np.array([0, 30, 60, 90], dtype='float32'),
    'Ply 4 (°)': np.array([0, 30, 60, 90], dtype='float32')
}

# Generate combinations of the first four parameters without repetition for the second design
combinations_1_to_4_2 = itertools.product(param_levels_2['Number of holes, nh'],
                                        param_levels_2['Web-post width, WP (mm)'],
                                        param_levels_2['Web opening diameter, Do (mm)'],
                                        param_levels_2['Ply 1 (°)'],
                                        param_levels_2['Ply 2 (°)'],
                                        param_levels_2['Ply 3 (°)'],
                                        param_levels_2['Ply 4 (°)'])

# Filter out combinations where all four plies are the same for the second design
filtered_combinations_1_to_4_2 = filter(lambda x: len(set(x[3:7])) == 4, combinations_1_to_4_2)

# Create DataFrame from filtered combinations for plies 1 to 4 for the second design
design_1_to_4_2 = pd.DataFrame(filtered_combinations_1_to_4_2, columns=param_levels_2.keys())

# Add symmetric combinations for plies 5 to 8 for the second design
design_5_to_8_2 = design_1_to_4_2.copy()
design_5_to_8_2[['Ply 5 (°)', 'Ply 6 (°)', 'Ply 7 (°)', 'Ply 8 (°)']] = design_1_to_4_2[['Ply 4 (°)', 'Ply 3 (°)', 'Ply 2 (°)', 'Ply 1 (°)']].values

# Concatenate designs for plies 1 to 4 and plies 5 to 8 for the second design
final_design_2 = pd.concat([design_1_to_4_2, design_5_to_8_2], ignore_index=True)

# Remove rows where any ply is blank for the second design
final_design_2 = final_design_2.dropna()

# Add a new column for row numbering for the second design
final_design_2['Number'] = range(len(final_design_1) + 1, len(final_design_1) + len(final_design_2) + 1)

# Reorder columns to have the 'Number' column as the first column for the second design
final_design_2 = final_design_2[['Number'] + [col for col in final_design_2.columns if col != 'Number']]

# Concatenate both dataframes into a single dataframe
combined_design = pd.concat([final_design_1, final_design_2], ignore_index=True)

# Write the combined dataframe to an Excel file
combined_design.to_excel('doe_11inputs.xlsx', index=False)