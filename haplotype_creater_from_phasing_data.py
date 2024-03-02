#def parse_reference_file(reference_file):
#    """
#    Parse a FASTA format reference genome file.
#    Returns a dictionary with chromosome names as keys and the corresponding sequences as values.
#    """
reference_sequences = {}
with open("chr1.fa", 'r') as f:
	chromosome = ''
	sequence = ''
	for line in f:
		if line.startswith('>'):
			if chromosome != '':
				reference_sequences[chromosome] = sequence
				sequence = ''
			chromosome = line.strip()[1:]
		else:
			sequence += line.strip()
	reference_sequences[chromosome] = sequence

#print(reference_sequences)

#def parse_vcf_file(input_file):
#    """
#    Parse a VCF file.
#    Returns a dictionary with chromosome names as keys and a list of variants as values.
#    Each variant is represented as a tuple (pos, ref, alt, genotype).
#    """
variants = {}
with open("new_1000G_sample.txt", 'r') as f:
	for line in f:
		if line.startswith('#'):
			continue
		fields = line.strip().split('\t')
		chromosome = fields[0]
		if chromosome not in variants:
			variants[chromosome] = []
		pos = int(fields[1])
		ref = fields[3]
		alt = fields[4].split(',')
		genotype = fields[11].replace('|', '/')
		variants[chromosome].append((pos, ref, alt, genotype))
#print(variants)

#def generate_haplotype_sequences(chromosome, reference_sequence, variants):
#    """
#    Generate two haplotype sequences for the given chromosome and variants.
#    Returns a tuple (haplotype1, haplotype2).
#    """
ref = reference_sequences["chr1"]
ref = ref.upper()
print(len(ref))
haplotype1 = list(ref)
#print(len(haplotype1))
#print(haplotype1)
#exit()
haplotype2 = list(ref)
for pos, ref, alt, genotype in variants[chromosome]:
	#print(pos,"\t",ref,"\t",alt[0],"\t",genotype,"\n")
	pos = int(pos)
	ref = ref.strip()
	alt = alt[0].strip()
	genotype = genotype.strip()
	if genotype == '0/1' and len(ref) == 1 and len(alt) == 1 :
		#print(list(ref))
		#print(list(alt))
		haplotype1[pos-1:pos+len(ref)-1] = list(ref)
		haplotype2[pos-1:pos+len(ref)-1] = list(alt[0])
	elif genotype == '1/0' and len(ref) == 1 and len(alt) == 1:
		haplotype1[pos-1:pos+len(ref)-1] = list(alt[0])
		haplotype2[pos-1:pos+len(ref)-1] = list(ref)
	elif genotype == '1/1' and len(ref) == 1 and len(alt) == 1:
		haplotype1[pos-1:pos+len(ref)-1] = list(alt[0])
		haplotype2[pos-1:pos+len(ref)-1] = list(alt[0])
haplotype1 = ''.join(haplotype1)
haplotype2 = ''.join(haplotype2)
print(len(haplotype1))
print(len(haplotype2))
if haplotype1 == haplotype2:
	print("Both haplotypes are same")
else:
	print("Both haplotypes are not same")
#print(haplotype1)

# Example usage
#reference_file = 'reference.fasta'
#input_file = 'variants.vcf'
#chromosome = 'chr1'
#reference_sequence = parse_reference_file(reference_file)
#variants = parse_vcf_file(input_file)
#haplotype1, haplotype2 = generate_haplotype_sequences(chromosome, reference_sequence, variants)


with open("haplotype_chr1_1.txt",'w') as f1:
	f1.write('>chr1\n')
	f1.write(haplotype1+'\n')
	f1.close()

with open("haplotype_chr1_2.txt",'w') as f2:
	f2.write('>chr1\n')
	f2.write(haplotype2+'\n')
	f2.close()
