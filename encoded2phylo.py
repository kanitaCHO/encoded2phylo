#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

#input file 
df = pd.read_csv('corn_table_2.tsv', sep='\t')  # row = SNP, column = sample
genotype_data = df.iloc[:, 5:]  

#Encode Genotype
def encode_dosage(geno):
    if geno in ["0/0", "0|0"]:
        return 0
    elif geno in ["0/1", "1/0", "0|1", "1|0"]:
        return 1
    elif geno in ["1/1", "1|1"]:
        return 2
    elif geno in ["0/2", "2/0", "0|2", "2|0"]:
        return 3 
    elif geno in ["1/2", "2/1", "1|2", "2|1"]:
        return 4
    elif geno in ["2/2", "2|2"]:
        return 5
    else:
        return np.nan  

df_numeric = genotype_data.applymap(encode_dosage)
df_numeric = df_numeric.transpose()  #transpose: now rows = sample, columns = SNP

# Handle Missing Data
df_numeric = df_numeric.fillna(df_numeric.median())

# Compute Distances: (Euclidean distance by linkage)
linked = linkage(df_numeric, method='average', metric='euclidean')

# Plot Dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linked, labels=df_numeric.index.tolist())
plt.title('Phylogenetic Tree from SNP Data')
plt.ylabel('Distance')
plt.tight_layout()
plt.show()