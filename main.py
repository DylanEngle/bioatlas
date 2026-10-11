import pandas as pd
import inquirer
import matplotlib.pyplot as plt

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

def get_top_ten_recorded_species(df):
    grouped_species = df.value_counts("commonName")
    return grouped_species.head(10)
    

def produce_dataset_chart(df):
    top_ten_species_df = get_top_ten_recorded_species(df)
    plt.bar(top_ten_species_df.index, top_ten_species_df.values, color='skyblue')

    # Rotate labels and add padding
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()  # Adjust layout for rotated labels

    # Adding labels and title
    plt.xlabel("Animal name")
    plt.ylabel("Count")
    plt.title("Top ten animal species recorded")

    plt.show()
    

def main():
    df = pd.read_csv("./data/bioatlas_sample_observations.csv")
    produce_dataset_chart(df)

if __name__ == "__main__":
    main()