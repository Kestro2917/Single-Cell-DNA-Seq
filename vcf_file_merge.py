def merge_files(file1_path, file2_path, output_file_path):
    data_dict = {}

    # Read file 1 and store values in dictionary
    with open(file1_path, 'r') as file1:
        for line in file1:
            values = line.strip().split('\t')
            key = values[0]
            data_dict[key] = values[1:]

    # Merge file 2 with dictionary values
    with open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
        for line in file2:
            values = line.strip().split('\t')
            key = values[0]
            if key in data_dict:
                output_line = '\t'.join([key] + data_dict[key] + values[1:])
                output_file.write(output_line + '\n')

    print("Files merged successfully!")


# Usage example
file1_path = "/alina-data2/Bikram/Germline_variant_tusse_1_2k/haplotype_sequence_generator/CNAsim_new_output_zeroerror/variant_analysis/final_merging/vcf_1000G_merged_file.txt"
file2_path = "/alina-data2/Bikram/Germline_variant_tusse_1_2k/haplotype_sequence_generator/CNAsim_new_output_zeroerror/variant_analysis/beagle_file_processing/beagle_data_2.txt"
output_file_path = 'vcf_1000G_beagle_merged_file.txt'

merge_files(file1_path, file2_path, output_file_path)

