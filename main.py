import pandas as pd
import inquirer

def get_taxonomic_group(df):
    try:
        unique_taxonomic_groups = get_taxonomic_groups_from_df(df)
        questions = [
            inquirer.List(
                'taxonomic_group',
                message="Please select a taxonomic group:",
                choices=unique_taxonomic_groups,
                carousel=True
            )
        ]
        answers = inquirer.prompt(questions)
        return answers['taxonomic_group']

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {e}")

def get_taxonomic_groups_from_df(df):
    taxonomic_groups = df["taxonomicGroup"].unique()
    return taxonomic_groups
    

def main():
    print("Starting out.")
    df = pd.read_csv("./data/bioatlas_sample_observations.csv")
    taxonomic_group = get_taxonomic_group(df)
    result = df.query("taxonomicGroup == @taxonomic_group")
    print(result)

if __name__ == "__main__":
    main()