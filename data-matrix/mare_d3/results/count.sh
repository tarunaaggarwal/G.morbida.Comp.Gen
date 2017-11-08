cat seqCat_sequences_unwrapped.fasta_reduced | while read line
do

count=$(echo $line | wc -c)
echo $count

done
