import pandas as pd
import json
import sys
import numpy as np
import os

# matrix_filename = os.path.abspath("./submission.xlsx")
# filepath = os.path.abspath("./submission.xlsx")

# Correct Values - Spring 2025
correct_eff_voltedge = .962789878
correct_eff_ampere = .956997766
correct_cost_voltedge = 204900
correct_cost_ampere = 198400
correct_vol_voltedge = 8.125
correct_vol_ampere = 9.775

A = np.array([[0, 1, -2],[-2, 0, 1],[1, 1, 1]])
b = np.array([[0],[0],[1]])
[correct_eff_wt, correct_cost_wt, correct_vol_wt] = np.matmul(np.linalg.inv(A),b)

# 33 spaces in decision matrix. 0 = wrong, 1 = right. Assume right.
grades = np.ones(33)
grade_notes = []

# Define function to compute whether or not values are within a certain acceptable error
def is_within_tolerance(studVal, solnVal, tolerance):
    #studVal is a number, solnVal is a number, studVal can be between tolerance +/- solnVal
    if solnVal - tolerance <= studVal <= solnVal+tolerance:
    # if abs(studVal-solnVal) <= tolerance*solnVal:
        return True
    else:
        return False

# Create functions to implement normalization
# efficiency norm
def normalize_col_max(vals):
    return vals / vals.max()

# cost and volume norm
def normalize_col_min(vals):
    return vals.min() / vals

# weight values
def weight_vals(norm_vals, wt):
    return norm_vals * wt

# total values
def total_vals(wt_vals):
    return np.sum(wt_vals)

def grade_decision_matrix(file_path):

    df = pd.read_excel(file_path, header=1)
    
    # Set this flag to let students know whether or not CFD was enabled
    CFD = False

    # tolerance for normalized vals
    tolerance_norm = .005
    # tolerance for weighted vals
    tolerance_wtvals = .005
    # tolerance for computed efficiency
    tolerance_eff = .005
    # tolerance for matrix totals
    tolerance_totals = .005
    # tolerance for weights
    tolerance_wts = .01
    # tolerance for cost
    tolerance_cost = 100
    # tolerance for volume
    tolerance_vol = .1

    # -----------------------------------------------
    # ------------------- WEIGHTS -------------------
    # -----------------------------------------------

    # Extract from spreadsheet
    # These are in the first row (row 0) of actual data (3rd row of table)
    # don't read final column which is totals
    [student_eff_wt, student_cost_wt, student_vol_wt] = df.iloc[0, 1:9:3]

    # Efficiency Weight
    if not is_within_tolerance(student_eff_wt, correct_eff_wt, tolerance_wts):
        use_eff_wt = student_eff_wt
        grades[0] = 0
        grade_notes.append('Efficiency Weight Computed Incorrectly')
        CFD = True
    else:
        use_eff_wt = correct_eff_wt

    # Cost Weight
    if not is_within_tolerance(student_cost_wt, correct_cost_wt, tolerance_wts):
        use_cost_wt = student_cost_wt
        grades[1] = 0
        grade_notes.append('Cost Weight Computed Incorrectly')
        CFD = True
    else:
        use_cost_wt = correct_cost_wt

    # Volume Weight
    if not is_within_tolerance(student_vol_wt, correct_vol_wt, tolerance_wts):
        use_vol_wt = student_vol_wt
        grades[2] = 0
        grade_notes.append('Volume Weight Computed Incorrectly')
        CFD = True
    else:
        use_vol_wt = correct_vol_wt

    # -----------------------------------------------
    # ------------- COMPUTED VALUES -----------------
    # -----------------------------------------------

    [student_eff_voltedge, student_eff_ampere, student_eff_design]  = df.iloc[2:5, 1]

    [student_cost_voltedge, student_cost_ampere, student_cost_design]  = df.iloc[2:5, 4]

    [student_vol_voltedge, student_vol_ampere, student_vol_design]  = df.iloc[2:5, 7]

    # Efficiency 
    if not is_within_tolerance(student_eff_voltedge, correct_eff_voltedge, tolerance_eff):
        use_eff_voltedge = student_eff_voltedge
        grades[3] = 0
        grade_notes.append('VoltEdge Efficiency Computed Incorrectly')
        CFD = True
    else:
        use_eff_voltedge = correct_eff_voltedge

    if not is_within_tolerance(student_eff_ampere, correct_eff_ampere, tolerance_eff):
        use_eff_ampere = student_eff_ampere
        grades[4] = 0
        grade_notes.append('Ampere Efficiency Computed Incorrectly')
        CFD = True
    else:
        use_eff_ampere = correct_eff_ampere

    # assume correct efficiency value computed by student
    use_eff_design = student_eff_design

    # Cost 
    if not is_within_tolerance(student_cost_voltedge*1000, correct_cost_voltedge, tolerance_cost):
        use_cost_voltedge = student_cost_voltedge*1000
        grades[12] = 0
        grade_notes.append('VoltEdge Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_voltedge = correct_cost_voltedge

    if not is_within_tolerance(student_cost_ampere*1000, correct_cost_ampere, tolerance_cost):
        use_cost_ampere = student_cost_ampere*1000
        grades[13] = 0
        grade_notes.append('Ampere Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_ampere = correct_cost_ampere

    # assume correct cost value computed by student
    use_cost_design = student_cost_design*1000

    # Volume 
    if not is_within_tolerance(student_vol_voltedge, correct_vol_voltedge, tolerance_vol):
        use_vol_voltedge = student_vol_voltedge
        grades[21] = 0
        grade_notes.append('VoltEdge Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_voltedge = correct_vol_voltedge

    if not is_within_tolerance(student_vol_ampere, correct_vol_ampere, tolerance_vol):
        use_vol_ampere = student_vol_ampere
        grades[22] = 0
        grade_notes.append('Ampere Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_ampere = correct_vol_ampere

    # assume correct cost value computed by student
    use_vol_design = student_vol_design

    # -----------------------------------------------
    # ------------- NORMALIZED VALUES ---------------
    # -----------------------------------------------

    [student_eff_voltedge_norm, student_eff_ampere_norm, student_eff_design_norm]  = df.iloc[2:5, 2]
    [student_cost_voltedge_norm, student_cost_ampere_norm, student_cost_design_norm]  = df.iloc[2:5, 5]
    [student_vol_voltedge_norm, student_vol_ampere_norm, student_vol_design_norm]  = df.iloc[2:5, 8]

    # Find correct values
    [correct_eff_voltedge_norm, correct_eff_ampere_norm, correct_eff_design_norm] = normalize_col_max(np.array([use_eff_voltedge, use_eff_ampere, use_eff_design]))
    [correct_cost_voltedge_norm, correct_cost_ampere_norm, correct_cost_design_norm] = normalize_col_min(np.array([use_cost_voltedge, use_cost_ampere, use_cost_design]))
    [correct_vol_voltedge_norm, correct_vol_ampere_norm, correct_vol_design_norm] = normalize_col_min(np.array([use_vol_voltedge, use_vol_ampere, use_vol_design]))


    # CHECK Efficiency
    if not is_within_tolerance(student_eff_voltedge_norm, correct_eff_voltedge_norm, tolerance_norm):
        use_eff_voltedge_norm = student_eff_voltedge_norm
        grades[6] = 0
        grade_notes.append('Voltedge Normalized Efficiency Computed Incorrectly ') # + str(correct_eff_voltedge_norm))
        CFD = True
    else:
        use_eff_voltedge_norm = correct_eff_voltedge_norm

    if not is_within_tolerance(student_eff_ampere_norm, correct_eff_ampere_norm, tolerance_norm):
        use_eff_ampere_norm = student_eff_ampere_norm
        grades[7] = 0
        grade_notes.append('Ampere Normalized Efficiency Computed Incorrectly ') # + str(correct_eff_ampere_norm))
        CFD = True 
    else:
        use_eff_ampere_norm = correct_eff_ampere_norm

    if not is_within_tolerance(student_eff_design_norm, correct_eff_design_norm, tolerance_norm):
        use_eff_design_norm = student_eff_design_norm
        grades[8] = 0
        grade_notes.append('Your Design Normalized Efficiency Computed Incorrectly ') # + str(correct_eff_design_norm))
        CFD = True
    else:
        use_eff_design_norm = correct_eff_design_norm


    # CHECK Cost 
    if not is_within_tolerance(student_cost_voltedge_norm, correct_cost_voltedge_norm, tolerance_norm):
        use_cost_voltedge_norm = student_cost_voltedge_norm
        grades[15] = 0
        grade_notes.append('Voltedge Normalized Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_voltedge_norm = correct_cost_voltedge_norm

    if not is_within_tolerance(student_cost_ampere_norm, correct_cost_ampere_norm, tolerance_norm):
        use_cost_ampere_norm = student_cost_ampere_norm
        grades[16] = 0
        grade_notes.append('Ampere Normalized Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_ampere_norm = correct_cost_ampere_norm

    if not is_within_tolerance(student_cost_design_norm, correct_cost_design_norm, tolerance_norm):
        use_cost_design_norm = student_cost_design_norm
        grades[17] = 0
        grade_notes.append('Your Design Normalized Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_design_norm = correct_cost_design_norm

    # CHECK Volume 
    if not is_within_tolerance(student_vol_voltedge_norm, correct_vol_voltedge_norm, tolerance_norm):
        use_vol_voltedge_norm = student_vol_voltedge_norm
        grades[24] = 0
        grade_notes.append('Voltedge Normalized Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_voltedge_norm = correct_vol_voltedge_norm

    if not is_within_tolerance(student_vol_ampere_norm, correct_vol_ampere_norm, tolerance_norm):
        use_vol_ampere_norm = student_vol_ampere_norm
        grades[25] = 0
        grade_notes.append('Ampere Normalized Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_ampere_norm = correct_vol_ampere_norm

    if not is_within_tolerance(student_vol_design_norm, correct_vol_design_norm, tolerance_norm):
        use_vol_design_norm = student_vol_design_norm
        grades[26] = 0
        grade_notes.append('Your Design Normalized Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_design_norm = correct_vol_design_norm


    # -----------------------------------------------
    # --------------- WEIGHTED VALUES ---------------
    # -----------------------------------------------

    [student_eff_voltedge_wt, student_eff_ampere_wt, student_eff_design_wt]  = df.iloc[2:5, 3]
    [student_cost_voltedge_wt, student_cost_ampere_wt, student_cost_design_wt]  = df.iloc[2:5, 6]
    [student_vol_voltedge_wt, student_vol_ampere_wt, student_vol_design_wt]  = df.iloc[2:5, 9]

    # Find correct values
    [correct_eff_voltedge_wt, correct_eff_ampere_wt, correct_eff_design_wt] = weight_vals(np.array([use_eff_voltedge_norm, use_eff_ampere_norm, use_eff_design_norm]), use_eff_wt)
    [correct_cost_voltedge_wt, correct_cost_ampere_wt, correct_cost_design_wt] = weight_vals(np.array([use_cost_voltedge_norm, use_cost_ampere_norm, use_cost_design_norm]), use_cost_wt)
    [correct_vol_voltedge_wt, correct_vol_ampere_wt, correct_vol_design_wt] = weight_vals(np.array([use_vol_voltedge_norm, use_vol_ampere_norm, use_vol_design_norm]), use_vol_wt)

    # CHECK Efficiency
    if not is_within_tolerance(student_eff_voltedge_wt, correct_eff_voltedge_wt, tolerance_wtvals):
        use_eff_voltedge_wt = student_eff_voltedge_wt
        grades[9] = 0
        grade_notes.append('Voltedge Weighted Efficiency Computed Incorrectly')
        CFD = True
    else:
        use_eff_voltedge_wt = correct_eff_voltedge_wt

    if not is_within_tolerance(student_eff_ampere_wt, correct_eff_ampere_wt, tolerance_wtvals):
        use_eff_ampere_wt = student_eff_ampere_wt
        grades[10] = 0
        grade_notes.append('Ampere Weighted Efficiency Computed Incorrectly')
        CFD = True
    else:
        use_eff_ampere_wt = correct_eff_ampere_wt

    if not is_within_tolerance(student_eff_design_wt, correct_eff_design_wt, tolerance_wtvals):
        use_eff_design_wt = student_eff_design_wt
        grades[11] = 0
        grade_notes.append('Your Design Weighted Efficiency Computed Incorrectly')
        CFD = True
    else:
        use_eff_design_wt = correct_eff_design_wt


    # CHECK Cost 
    if not is_within_tolerance(student_cost_voltedge_wt, correct_cost_voltedge_wt, tolerance_wtvals):
        use_cost_voltedge_wt = student_cost_voltedge_wt
        grades[18] = 0
        grade_notes.append('Voltedge Weighted Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_voltedge_wt = correct_cost_voltedge_wt

    if not is_within_tolerance(student_cost_ampere_wt, correct_cost_ampere_wt, tolerance_wtvals):
        use_cost_ampere_wt = student_cost_ampere_wt
        grades[19] = 0
        grade_notes.append('Ampere Weighted Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_ampere_wt = correct_cost_ampere_wt

    if not is_within_tolerance(student_cost_design_wt, correct_cost_design_wt, tolerance_wtvals):
        use_cost_design_wt = student_cost_design_wt
        grades[20] = 0
        grade_notes.append('Your Design Weighted Cost Computed Incorrectly')
        CFD = True
    else:
        use_cost_design_wt = correct_cost_design_wt

    # CHECK Volume 
    if not is_within_tolerance(student_vol_voltedge_wt, correct_vol_voltedge_wt, tolerance_wtvals):
        use_vol_voltedge_wt = student_vol_voltedge_wt
        grades[27] = 0
        grade_notes.append('Voltedge Weighted Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_voltedge_wt = correct_vol_voltedge_wt

    if not is_within_tolerance(student_vol_ampere_wt, correct_vol_ampere_wt, tolerance_wtvals):
        use_vol_ampere_wt = student_vol_ampere_wt
        grades[28] = 0
        grade_notes.append('Ampere Weighted Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_ampere_wt = correct_vol_ampere_wt

    if not is_within_tolerance(student_vol_design_wt, correct_vol_design_wt, tolerance_wtvals):
        use_vol_design_wt = student_vol_design_wt
        grades[29] = 0
        grade_notes.append('Your Design Weighted Volume Computed Incorrectly')
        CFD = True
    else:
        use_vol_design_wt = correct_vol_design_wt

    # -----------------------------------------------
    # ------------------ TOTAL VALUES ---------------
    # -----------------------------------------------

    [student_total_voltedge, student_total_ampere, student_total_design]  = df.iloc[2:5, 10]

    correct_total_voltedge = total_vals(np.array([use_eff_voltedge_wt, use_cost_voltedge_wt, use_vol_voltedge_wt]))
    correct_total_ampere = total_vals(np.array([use_eff_ampere_wt, use_cost_ampere_wt, use_vol_ampere_wt]))
    correct_total_design = total_vals(np.array([use_eff_design_wt, use_cost_design_wt, use_vol_design_wt]))

    # CHECK totals 
    if not is_within_tolerance(student_total_voltedge, correct_total_voltedge, tolerance_totals):
        grades[30] = 0
        grade_notes.append('VoltEdge Total Computed Incorrectly')
        CFD = True

    if not is_within_tolerance(student_total_ampere, correct_total_ampere, tolerance_totals):
        grades[31] = 0
        grade_notes.append('Ampere Total Computed Incorrectly')
        CFD = True

    if not is_within_tolerance(student_total_design, correct_total_design, tolerance_totals):
        grades[32] = 0
        grade_notes.append('Your Design Total Computed Incorrectly')
        CFD = True

    # -----------------------------------------------
    # ------------ GRADESCOPE OUTPUTS ---------------
    # -----------------------------------------------

    # Calculate total score - THIS IS WHAT GRADESCOPE REFLECTS
    # score = 1.0 if np.sum(grades) == 33 else 0.0
    
    if CFD:
        score = 0.0 # cadet will receive 0/1 for submission
        output_message = "Autograder completed.\n" + "CFD enabled. \n" + "\n".join(grade_notes) # cadet will see which cells were wrong
    else:
        score = 1.0 # cadet will receive 1/1 for submission
        output_message = "Autograder completed.\n" + "Assuming computed values for your design are right, all entries otherwise are correct. Nice work!"

    output = {"score": score, "visibility": "visible", "stdout_visibility": "visible", "output": output_message}

    with open(os.path.abspath('../results/results.json'),'w') as f:
        json.dump(output,f)

# Read student submission file -- must be excel!
if __name__ == "__main__":
    grade_decision_matrix(os.path.abspath("./submission.xlsx"))
