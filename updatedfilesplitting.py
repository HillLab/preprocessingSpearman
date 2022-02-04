from Bio import SeqIO
d = {}
fh = open('newplantviralsequences.fasta')
for seq_record in SeqIO.parse(fh, 'fasta'):
    species_name = seq_record.id.split('-')[-1]
    if species_name not in d:
        d[species_name] = open(f"{species_name}.fasta", 'w')
    d[species_name].write(seq_record.format("fasta"))
fh.close()