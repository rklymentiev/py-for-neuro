DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
nucleotides = {
    "adenine": DNA.count("A"),
    "thymine": DNA.count("T"),
    "guanine": DNA.count("G"),
    "cytosine": DNA.count("C")
    }
print(nucleotides)
