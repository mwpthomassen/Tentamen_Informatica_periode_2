# leest het fasta bestand in
def inlezen_fasta_file(bestandsnaam):
    with open(bestandsnaam) as inFile:
        for regel in inFile:
            regel.split("")
            print(regel)


if __name__ == '__main__':
    inlezen_fasta_file("Caenorhabditis_elegans.cds_pep.all.fa")
