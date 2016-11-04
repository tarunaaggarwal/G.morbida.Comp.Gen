### khmer (version 1.1)
#### Interleave the PE reads
```
/forKhmer/khmerEnv/bin/interleave-reads.py \
-o file.interleaved.fastq \
file_R1.fastq file_R2.fastq
```

### bfc (version r181)
```
bfc -s 26m -k 55 -t 20 file.interleaved.fastq > file.interleaved.corrected.pre.fastq
```
#### fix headers in the bfc generated file
```
awk '{print $1}' \
file.interleaved.corrected.pre.fastq > file.interleaved.corrected.fastq
```
#### remove the `pre.fastq`
```
rm file.interleaved.corrected.pre.fastq
```

### Khmer (version 1.1)
#### Split the corrected, interleaved file

```
/forKhmer/khmerEnv/bin/split-paired-reads.py file.interleaved.corrected.fastq
```
#### Rename split files
```
mv file.interleaved.corrected.fastq.1 file_bfc_k55.1.corrected.fastq
mv file.interleaved.corrected.fastq.2 file_bfc_k55.2.corrected.fastq
```
### Trim bfc corrected PE reads using Trimmomatic V0.32
```
java -jar /opt/Trimmomatic-0.32/trimmomatic-0.32.jar PE -threads 4 \
-baseout file_bfc55_trimphred4 \
file_bfc_k55.1.corrected.fastq \
file_bfc_k55.2.corrected.fastq \
ILLUMINACLIP:/opt/Trimmomatic-0.32/adapters/TruSeq3-PE-2.fa:2:30:10 \
LEADING:4 TRAILING:4 SLIDINGWINDOW:4:4 MINLEN:30
```

### Assembly with Abyss (v. )
```

for k in 61 71 81 91; do
	mkdir trimk$k; \
	abyss-pe -C trimk$k lib='pe100' np=8 s=202 l=40 name=file_trimk$k \
	k=$k n=5 \
	pe100='~/file_bfc55_trimphred4_1P ~/file_bfc55_trimphred4_2P'2P \
	se='~/file_bfc55_trimphred4_1U ~/file_bfc55_trimphred4_2U_2U'
done
```



