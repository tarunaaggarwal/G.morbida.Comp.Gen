#!/usr/bin/python3
# A program for converting several aligned CDS fasta files into phylip files.
# USAGE: ./fasta2phylip_TA.py
# Author: Taruna Aggarwal
# Affiliation: University of New Hampshire, Durham, NH, USA
# Date: 01/28/2016

import os
import sys
import argparse
from Bio import SeqIO

# set up arguments
parser = argparse.ArgumentParser(description="This script runs aligns coding sequences in files in a given directory.")
parser.add_argument('--fasta_dir', default="/home/mcclintock/ta2007/myscripts/Scripts4PAML/aligned_cds_fastas/", help="PATH to the directory with aligned CDS fasta files.")
parser.add_argument('--phy_dir', default="/home/mcclintock/ta2007/myscripts/Scripts4PAML/aligned_cds_phylips/", help="PATH to the directory for aligned CDS phylip files.")
args = parser.parse_args()

# assign filenames
Orig_fasta_dir = args.fasta_dir
New_phylip_dir = args.phy_dir

# make output dir
try:
    os.makedirs(New_phylip_dir)
except FileExistsError as e:
    pass

for currentFile in os.listdir(args.fasta_dir):
    if currentFile.endswith(".fa"):
        input_handle_fasta = open(args.fasta_dir + currentFile, "rU")
        output_handle_phylip = open(args.phy_dir + currentFile[:-2]+"phy", "w")
        sequences = SeqIO.parse(input_handle_fasta, "fasta")
        count = SeqIO.write(sequences, output_handle_phylip, "phylip")

output_handle_phylip.close()
input_handle_fasta.close()

