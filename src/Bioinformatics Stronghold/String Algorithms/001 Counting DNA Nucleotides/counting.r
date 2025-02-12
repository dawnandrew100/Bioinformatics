library(stringr)

str = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
nucleotides <- c("A", "C", "G", "T")
nucleotide_count <- numeric()

for(nuc in nucleotides){
    nucleotide_count = c(nucleotide_count, str_count(str, nuc))
}

str.data = data.frame(
    nuc = nucleotides,
    nuc_count = nucleotide_count
)

print(str)
print(str.data, row.names=FALSE)
print(str.data$nuc_count)
