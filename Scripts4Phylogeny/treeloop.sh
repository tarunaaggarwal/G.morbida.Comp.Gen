#!/bin/bash

for phy in *.phy
do
        raxmlHPC-PTHREADS -T 16 -m PROTGAMMALG -s $phy -p 12345 -n ${phy}.tre
done
