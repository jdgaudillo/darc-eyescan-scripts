from itertools import repeat
import pandas as pd 
import numpy as np
import re

filename = 'raw.csv'
dataframe = pd.read_csv(filename)

df_findings = dataframe[['FINDINGS']]
df_ID = dataframe[['Patient']]

np_findings = df_findings.values
np_ID = df_ID.values

ID = np.reshape(np_ID, (121))

def convert_to_lowercase(findings):
	str_findings = str(findings)
	text = str_findings.lower()
	return text

def search_keywords(text):
	regexp = re.compile(r'optic nerve|retina|macula|vitreal|cornea|conjunctival|lens|pupil|eyelids')
	hit = re.findall(regexp, text)
	return hit

def score_keywords(patient, hit):
	keywords = ['optic nerve', 'retina', 'macula', 'vitreal', 'cornea',
			'lens', 'conjunctival', 'pupil', 'eyelids']
	score = list(repeat(0,9))

	if not hit:
		score.insert(0, patient)
		return score
	else:
		for w in hit:
			for i, word in enumerate(keywords):
				if w == word:
					score[i] = 1
					break

	score.insert(0,patient)
	return score

def list_to_dataframe(output):
	fields = ['Patient', 'OpticNerve', 'Retina', 'Macula', 'Vitreous', 'Cornea',
			'Lens', 'Conjunctival', 'Pupil', 'Eyelids']
	df_output = pd.DataFrame(output, columns=fields)

	file = 'Labelled.csv'
	write_to_csv(df_output, file)	


def write_to_csv(output, file):
	output.to_csv(file, index = False)

output = []
for i, findings in enumerate(np_findings):
	hit_words = []
	series_score = []
	text = convert_to_lowercase (findings)
	hit_words = search_keywords(text)
	score = score_keywords(ID[i], hit_words)
	output.append(score)

list_to_dataframe(output)
