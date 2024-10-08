import cobra
from cobra.flux_analysis import flux_variability_analysis
from datetime import datetime

# Load the metabolic model
model = cobra.io.read_sbml_model(r"C:\Users\samuel.ayensu\Desktop\project_folder\iCTH669_w_GLGC.sbml")

start_time = datetime.now()  # Record the start time of FVA
fva_result = flux_variability_analysis(model, reaction_list=model.reactions, fraction_of_optimum=0.9)
end_time = datetime.now()  # Record the end time of FVA
solution_time = end_time - start_time  # Calculate the solution time of FVA

print("Solution time:", solution_time)

# Display FVA results
fva_result
