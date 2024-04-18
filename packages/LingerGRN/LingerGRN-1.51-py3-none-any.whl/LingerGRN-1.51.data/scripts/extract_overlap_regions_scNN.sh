
outdir=$1
mkdir $outdir
sed '1d' hg38/data/TSS_extend_1M.txt > data/TSS_extend_1M.bed 
cat data/Peaks.txt |sed '1d' |sed 's/:/\t/g'| sed 's/-/\t/g' > $outdir/Region.bed
bedtools intersect -a $outdir/Region.bed -b hg38/data/TSS_extend_1M.bed -wa -wb |awk '{print $1":"$2"-"$3"\t"$7"\t"$2"\t"$8}' > data/RE_gene_1M.bed 