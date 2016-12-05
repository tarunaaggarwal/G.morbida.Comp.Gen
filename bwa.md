### BWA 

### Index the genome assembly

```
bwa index assembly.fasta
```

### Map paired-end reads to the indexed genome

```
bwa mem assembly.fasta \
file_R1.fastq file_R2.fastq > file.sam 
```

### Sort PE sam file

```
samtools sort file.sam file.sorted
```

### Find mapping metrics
```
samtools flagstat file.sorted.bam
```