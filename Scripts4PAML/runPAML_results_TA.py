#!/usr/bin/python3
# A program for calculating adjusted P-value for PAML's codemls outputs.
# USAGE: ./runPAML_results_TA.py
# Author: Taruna Aggarwal
# Affiliation: University of New Hampshire, Durham, NH, USA
# Date: 01/27/2016
# Purpose is

import sys
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description="This script calculates p-value for PAML's output.")
parser.add_argument('--null', help="PATH to null files", required=True)
parser.add_argument('--alt', help="PATH to alt files", required=True)
args = parser.parse_args()


def analyzePAML(nullfile, altfile):
    analyzePAML_cmd = "python results_paml.py {0} {1} | tee -a PAML.results".format(nullfile, altfile)
    subprocess.call(analyzePAML_cmd, shell=True)

for file in os.listdir(args.null):
  if file.endswith(".null.out"):
    output = analyzePAML(args.null + "/" + file, args.alt + "/" + file[:-9] + ".alt.out")
