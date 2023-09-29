import pandas as pd
import os

# List of perturbations added to images
keywords = ['bicubic', 'gaussian', 'noise']

# CSV files to read from containing (experiment, metric) pairs
csv_files = ['trial-1.csv', 'trial-2.csv', 'trial-3.csv']

for csv_file in csv_files:
    data = pd.read_csv(csv_file)

    # Create new DataFrame for Excel
    df = pd.DataFrame(columns=['potatoes', 'strawberries', 'asparagus'], \
                        index=['bicubic', 'gaussian', 'noise']) # Same as keywords

    # Iterate through each (dataset, metric) pair and place value into DF
    for index, row in data.iterrows():
        experiment = row['Experiment']
        psnr = row['Metric'] # Replace with desired metric, i.e. 'psnr'

        name_parts = experiment.split("_")

        dataset_name = []
        experiment_keywords = []
        for part in name_parts:
            if part not in keywords:
                dataset_name.append(part)
            else:
                experiment_keywords.append(part)

        # Append to dataset column
        dataset_name = '_'.join(dataset_name)
        experiment = '_'.join(experiment_keywords)

        # Use dataset and experiment to locate the correct location to insert psnr
        df.at[experiment, dataset_name] = psnr

    # Write DF to excel sheet
    if os.path.exists('results.xlsx'):
        with pd.ExcelWriter('results.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name=csv_file)
    else:
        df.to_excel('results.xlsx', sheet_name=csv_file)
