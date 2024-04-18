GRNdir=$1
genome=$2
outdir=$3
workdir=$4
mkdir $outdir
cat $workdir/data/Peaks.txt |sed '1d' |sed 's/:/\t/g'| sed 's/-/\t/g' > $outdir/Region.bed
if [ $genome = "hg38"  ]; 
then 
bedtools intersect -a $outdir/Region.bed -b  $GRNdir/hg38_hg19_pair.bed -wa -wb |awk '{print $7"\t"$8"\t"$9"\t"$1"\t"$2"\t"$3}'> $outdir/match_hg19_peak.bed # the first 3 are the hg19 region origianl ; the last 3 is  the query data region
fi
if [ $genome = "hg19"  ]
then
bedtools intersect -a $outdir/Region.bed -b  $GRNdir/hg19_hg38_pair.bed -wa -wb |awk '{print $7"\t"$8"\t"$9"\t"$1"\t"$2"\t"$3}'> $outdir/match_hg19_peak.bed # the first 3 are the hg19 region origianl ; the last 3 is  the query data region
fi

bedtools intersect -a $outdir/match_hg19_peak.bed -b $GRNdir/RE_gene_corr_hg19.bed -wa -wb |awk '$2 == $8 && $3 == $9'|awk '{print $1":"$2"-"$3"\t"$4":"$5"-"$6"\t"$10}'|sort|uniq > $outdir/hg19_Peak_hg19_gene_u.txt # first is hg19  original and second is the overlaped  qurey rengion ; 3 is the target gene 
# the first column is hg the second col
## motif enrhchment mapping
for i in $(seq 1 22)
do
bedtools intersect -a  $outdir/match_hg19_peak.bed -b $GRNdir/MotifTarget_matrix_chr$i.bed -wa -wb  |awk '$1==$7 && $2==$8 && $3==$9 { print }' |awk '{print $4":"$5"-"$6"\t"$7":"$8"-"$9}' > $outdir/MotifTarget_hg19_hg38_chr$i.txt
done
i=X
bedtools intersect -a  $outdir/match_hg19_peak.bed -b $GRNdir/MotifTarget_matrix_chr$i.bed -wa -wb  |awk '$1==$7 && $2==$8 && $3==$9 { print }' |awk '{print $4":"$5"-"$6"\t"$7":"$8"-"$9}' > $outdir/MotifTarget_hg19_hg38_chr$i.txt
for i in $(seq 1 22); do
bedtools intersect -a "$GRNdir/${genome}_Peaks_chr$i.bed" -b $outdir/Region.bed -wa -wb > $outdir/"Region_overlap_chr$i.bed"
done
i=X
bedtools intersect -a "$GRNdir/${genome}_Peaks_chr$i.bed" -b $outdir/Region.bed -wa -wb > $outdir/"Region_overlap_chr$i.bed"