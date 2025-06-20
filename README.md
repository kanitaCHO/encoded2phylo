# encoded2phylo

Phylogenetic Tree from SNP Data 

This Python script generates a phylogenetic tree from SNP genotype data stored in a .tsv file using hierarchical clustering. It converts genotype strings (e.g., "0/0", "1/1") to numeric dosage values and computes sample distances to visualize the relationships among samples.

Input File
	
  	• Format: .tsv (Tab-separated values)
 
	• Structure:
	            - First 5 columns: metadata (ignored)
						 
	            - Remaining columns: SNP genotypes for each sample (e.g., "0/1", "1|0", etc.)
						 
	• Example: SNP_table.tsv

How It Works

	1.	Read SNP Data:
			- Loads the SNP matrix, skipping the first 5 columns (assumed to be metadata).
	2.	Encode Genotype Dosage:
				Converts genotype strings to numeric dosage values:
				0/0 or 0|0 → 0
				0/1, 1/0 → 1
				1/1 → 2
				0/2, 2/0 → 3
				1/2, 2/1 → 4
				2/2 → 5
	3.	Handle Missing Data:
			- Fills missing values (NaN) using the median of each SNP column.
	4.	Compute Distances:
			- Uses Euclidean distance and average linkage to calculate distances between samples.
	5.	Plot Dendrogram:
			- Displays the dendrogram (phylogenetic tree) with sample labels.
	 
Requirements
Install the required Python packages:

	pip install numpy pandas scipy matplotlib

Usage
python encoded2phylo.py
Make sure your SNP_table.tsv file is in the same directory, or change the file path in the script.

Output
        - A dendrogram (hierarchical tree) showing the genetic relationships between samples based on SNP genotypes.

Notes

	• You can modify the encode_dosage() function to support other genotype formats.
	• Change the fillna() method if you prefer using mean or another imputation method.
	• You can switch linkage methods (average, single, complete, etc.) or distance metrics (euclidean, cityblock, etc.) for different clustering behaviors.

