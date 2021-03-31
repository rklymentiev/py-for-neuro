DNA = "gatggaacttgactacgtaaatt"
RNA = DNA.replace("t", "u").upper()
# or
# RNA = DNA.upper().replace("T", "U")
print(RNA)
