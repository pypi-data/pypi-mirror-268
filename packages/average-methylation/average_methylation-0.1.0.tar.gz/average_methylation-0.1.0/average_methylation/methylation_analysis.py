import pandas as pd
import numpy as np
import glob

def split_and_save_data(df, num_parts, output_dir):
    chunks = np.array_split(df, num_parts)
    for i, chunk in enumerate(chunks):
        filename = f"{output_dir}/chr_part_{i+1}.csv"
        chunk.to_csv(filename, index=False)
        print(f"Part {i+1} saved to {filename}")

def calculate_averages(input_dir, output_dir, gene_coords_file):
    genes_df = pd.read_csv(gene_coords_file, sep='\t')
    for file_index in range(1, num_parts + 1):
        methylation_df = pd.read_csv(f'{input_dir}/chr_part_{file_index}.csv')
        results = []
        for idx, gene in genes_df.iterrows():
            gene_id = gene['Gene_ID']
            gene_start = gene['start']
            upstream_limit = gene_start - 500000
            relevant_sites = methylation_df[(methylation_df['site_start'] >= upstream_limit) & (methylation_df['site_start'] < gene_start)]
            if not relevant_sites.empty:
                avg_scores = relevant_sites.groupby('SubjectID')['methylation_score'].mean().reset_index()
                avg_scores['Gene_ID'] = gene_id
                results.append(avg_scores)
        if results:
            final_df = pd.concat(results)
            pivoted_df = final_df.pivot(index='Gene_ID', columns='SubjectID', values='methylation_score')
            pivoted_df.to_csv(f'{output_dir}/chr_part_{file_index}_averages.csv')
            print(f"Processed and saved averages for file: chr_part_{file_index}.csv")
        else:
            print(f"No relevant methylation sites found for file index {file_index}")

def combine_files(input_pattern, output_filepath):
    files = glob.glob(input_pattern)
    dataframes = []
    for file in files:
        df = pd.read_csv(file, index_col=0)
        df.reset_index(inplace=True)
        melted_df = df.melt(id_vars='Gene_ID', var_name='SubjectID', value_name='MethylationScore')
        dataframes.append(melted_df)
    combined_df = pd.concat(dataframes)
    final_df = combined_df.groupby(['Gene_ID', 'SubjectID']).mean().reset_index()
    final_pivoted_df = final_df.pivot(index='Gene_ID', columns='SubjectID', values='MethylationScore')
    final_pivoted_df.fillna(0, inplace=True)
    final_pivoted_df.to_csv(output_filepath)
    print("All files have been successfully combined and the result is saved.")

def run_full_pipeline(methylation_filepath, bed_filepath, gene_coords_filepath, output_directory, num_parts=500):
    # Reading and processing methylation and BED file
    coords_df = pd.read_csv(bed_filepath, sep='\t', header=None, names=['chr', 'start', 'end', 'cgID'])
    coords_df['coordinates'] = coords_df['chr'].astype(str) + ':' + coords_df['start'].astype(str) + '-' + coords_df['end'].astype(str)
    methylation_data_df = pd.read_csv(methylation_filepath)
    methylation_long_df = methylation_data_df.melt(id_vars=['SubjectID', 'TOEID'], var_name='cgID', value_name='methylation_score')
    merged_df = pd.merge(methylation_long_df, coords_df[['cgID', 'coordinates']], on='cgID', how='left')
    cleaned_df = merged_df.dropna(subset=['coordinates']).copy()
    split_and_save_data(cleaned_df, num_parts, f"{output_directory}/split")

    # Calculate averages
    calculate_averages(f"{output_directory}/split", f"{output_directory}/averages", gene_coords_filepath)

    # Combine files
    combine_files(f"{output_directory}/averages/chr_part_*_averages.csv", f"{output_directory}/final_combined_avg_methylation_scores.csv")

if __name__ == "__main__":
    # Example paths; replace these with actual paths when using the package
    run_full_pipeline('path/to/final_merged_dataset.csv',
                      'path/to/hglft_genome_Methlylation_EPIC_GRCh38.bed',
                      'path/to/gene_coords.txt',
                      'path/to/output')
