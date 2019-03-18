import papermill as pm
import json

index = 1
fp = './beams_test.json'
with open(fp) as f:
	beam_data = json.load(f)
for i in range(2):
	pm.execute_notebook('./concrete_beam_design.ipynb', './nboutput/cb_out' + str(i) + '.ipynb', parameters=beam_data[i])