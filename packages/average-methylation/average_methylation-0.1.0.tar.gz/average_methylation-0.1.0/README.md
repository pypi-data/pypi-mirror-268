Average Methylation Calculation

This Python package, average_methylation, is designed to process large datasets of methylation scores, calculate average methylation scores per gene per sample in defined windows upstream of gene start sites, and compile the results for further genomic analysis. It is intended for bioinformaticians and researchers studying epigenetic modifications.
Features

    1. Split large datasets: Break down comprehensive methylation datasets into manageable parts by chromosome.
    2. Calculate averages: Compute average methylation scores for genes in specific genomic windows.
    3. Combine results: Aggregate results into a concise format for downstream analysis.

Installation

You can install average_methylation directly via pip from PyPI:

    pip install average_methylation

Alternatively, if you have access to the GitHub repository and prefer to install the latest development version, you can install it directly using:

    pip install git+https://github.com/mrimis/average-methylation-calculation.git

Usage

After installation, the package can be used to run methylation analysis workflows. Here's a basic example of how to use the package in your Python scripts:

    from average_methylation.methylation_analysis import run_full_pipeline
    
    # Define the paths to your input files and output directory
    methylation_filepath = 'path/to/your/final_merged_dataset.csv'
    bed_filepath = 'path/to/your/hglft_genome_Methlylation_EPIC_GRCh38.bed'
    gene_coords_filepath = 'path/to/your/gene_coords.txt'
    output_directory = 'path/to/your/output/directory'
    
    # Run the full methylation analysis pipeline
    run_full_pipeline(methylation_filepath, bed_filepath, gene_coords_filepath, output_directory)

Function Parameters

    1. methylation_filepath: Path to the CSV file containing methylation scores.
    2. bed_filepath: Path to the BED file with genomic coordinates for methylation sites.
    3. gene_coords_filepath: Path to the file containing gene start and end coordinates.
    4. output_directory: Directory where the output files will be saved.

Contributing

Contributions to the average_methylation package are welcome! To contribute, please fork the repository, make your changes, and submit a pull request. We appreciate contributions in the form of code improvements, additional features, or bug fixes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Support

If you have any questions or encounter issues using the package, please open an issue on the GitHub repository issue tracker.
