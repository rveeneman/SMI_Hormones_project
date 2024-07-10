#!/usr/bin/env python

import os 
import subprocess
# Paths to the directories
directory1 = "/gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/p1"
directory2 = "/gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/p2"

# Lists to store filenames from each directory
filenames1 = []
filenames2 = []

# Populate the lists with filenames from each directory
for filename in os.listdir(directory1):
    if filename.endswith(".sumstats.gz"):
        filenames1.append(filename)

for filename in os.listdir(directory2):
    if filename.endswith(".sumstats.gz"):
        filenames2.append(filename)

# Generate combinations of files between the two directories
for file1_name in filenames1:
    for file2_name in filenames2:
        file1 = os.path.join(directory1, file1_name)
        file2 = os.path.join(directory2, file2_name)

        # Construct the command with the current pair of files
        command = "./ldsc.py " \
                  "--rg {file1},{file2} " \
                  "--ref-ld-chr /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/ " \
                  "--w-ld-chr /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/ " \
                  "--out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/LDSC/{filename1}_{filename2}".format(
                      file1=file1,
                      file2=file2,
                      filename1=file1_name.split('.')[0],
                      filename2=file2_name.split('.')[0]
                  )
        # Execute the command
        subprocess.call(command, shell=True)

