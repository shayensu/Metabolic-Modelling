import cobra
from cobra.flux_analysis import flux_variability_analysis
from datetime import datetime

# Code to load the metabolic model
model = cobra.io.read_sbml_model(r"C:\Users\SamuelHayford\Desktop\FBA\iCTH669_w_GLCL\iCTH669_w_GLGC.sbml")

# Define the FVA class
class FVA:
    def __init__(self, model):
        # Initialize and assign the model to the instance attribute "model"
        self.model = model

    def run_fva(self, reaction_list=None, fraction_of_optimum=0.9):
        # Run FVA using COBRApy's in-built method
        start_time = datetime.now()  # Record the start time of FVA
        fva_result = flux_variability_analysis(self.model, reaction_list=reaction_list, fraction_of_optimum=fraction_of_optimum)
        end_time = datetime.now()  # Record the end time of FVA
        self.solution_time = end_time - start_time  # Calculate the solution time of FVA
        return fva_result

    def display_fva_results(self, fva_result):
        # Print the FVA results 
        print("FVA Results")
        print("\nModel: ", self.model.id)
        print("\nSolution Time: ", self.solution_time)
        print("\nReactions\tMin Flux\tMax Flux")
        for reaction_id, row in fva_result.iterrows():
            min_flux = row['minimum']
            max_flux = row['maximum']
            print(f"{reaction_id}\t{min_flux}\t{max_flux}")

# Create an instance of FVA with the loaded metabolic model
fva_instance = FVA(model)

# Run FVA on the model
fva_results = fva_instance.run_fva()

# Display FVA results
fva_instance.display_fva_results(fva_results)
