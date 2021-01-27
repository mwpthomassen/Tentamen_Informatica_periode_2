# leest het fasta bestand in en zet het in een lijst
def inlezen_fasta_file(bestandsnaam):
    with open(bestandsnaam) as inFile:
        Proteine = []
        for regel in inFile:
            if not regel.startswith(">"):
                print(regel)





if __name__ == '__main__':
    inlezen_fasta_file("Caenorhabditis_elegans.cds_pep.all.fa")
