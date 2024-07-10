
#!/usr/bin/env python

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Epre_bin_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Epre_bin

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Epre_cont_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Epre_cont

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Epost_bin_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Epost_bin

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Epost_cont_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Epost_cont

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/E_males_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/E_males

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/E_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/E_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Tpre_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Tpre

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Tpost_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Tpost

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/T_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/T_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/T_m_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/T_m

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/T_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/T_mf

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SHBGpre_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SHBGpre

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SHBGpost_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SHBGpost

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SHBG_m_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SHBG_m

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SHBG_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SHBG_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SHBG_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SHBG_mf

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/AgeMen_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/AgeMen

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/AgeMc_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/AgeMc

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/DeprB_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/DeprB_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/DeprS_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/DeprS_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/DeprB_m_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/DeprB_m

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/DeprS_m_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/DeprS_m

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/DeprW_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/DeprW_mf

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/DeprH_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/DeprH_mf

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SCZ_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SCZ_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SCZ_m_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SCZ_m

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/SCZ_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/SCZ_mf

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Bip_f_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Bip_f

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/Bip_m_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/Bip_m

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/BDnoUKB_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/BDnoUKB_mf

./munge_sumstats.py \
  --sumstats /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/BD_mf_oc.txt \
  --N-col samplesize \
  --snp SNP \
  --a1 effect_allele \
  --a2 other_allele \
  --signed-sumstats beta,0 \
  --chunksize 500000 \
  --p pval \
  --merge-alleles  /gpfs/home4/rveeneman/ldsc/eur_w_ld_chr/w_hm3.snplist \
  --out /gpfs/home4/rveeneman/SMI_Hormones/Data/LDSC/output/BD_mf




