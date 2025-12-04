import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def calculate_fleiss_kappa(data_matrix):
    """Calculate Fleiss' Kappa for inter-rater agreement on categorical data
    
    Fleiss' Kappa = (P - Pe) / (1 - Pe)
    where P is the observed agreement and Pe is the expected agreement by chance
    """
    
    if data_matrix.shape[0] == 0 or data_matrix.shape[1] == 0:
        return np.nan
    
    n = data_matrix.shape[0]  # number of subjects
    k = data_matrix.shape[1]  # number of categories
    
    # Calculate total number of ratings
    N = data_matrix.sum().sum()
    
    if N == 0:
        return np.nan
    
    # Calculate observed agreement (P)
    # Sum of squared elements divided by total ratings
    P = (data_matrix ** 2).sum().sum() / (N * (n - 1))
    
    # Calculate expected agreement by chance (Pe)
    # Sum of squared column sums divided by total ratings squared
    col_sums = data_matrix.sum(axis=0)
    Pe = (col_sums ** 2).sum() / (N ** 2)
    
    # Calculate Fleiss' Kappa
    if Pe == 1:
        kappa = np.nan
    else:
        kappa = (P - Pe) / (1 - Pe)
    
    return kappa

def load_data_from_excel(file_path):
    """Load data from Excel file"""
    try:
        # Try to read Excel file
        df = pd.read_excel(file_path)
        print(f"Successfully loaded data from Excel file: {file_path}")
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def load_data_from_csv(file_path):
    """Load data from CSV file"""
    try:
        # Try to read CSV file with semicolon separator
        df = pd.read_csv(file_path, sep=';')
        print(f"Successfully loaded data from CSV file: {file_path}")
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

def prepare_data_for_fleiss_kappa(df):
    """Prepare data in the format needed for Fleiss' Kappa calculation
    
    For Fleiss' Kappa, we need a matrix where:
    - Rows represent questions
    - Columns represent categories (A, B, C)
    - Values represent the count of responses for each category
    """
    fleiss_data = []
    
    for question in df['Question'].unique():
        question_data = df[df['Question'] == question]
        
        # Get counts for each category
        a_count = question_data[question_data['Categorical Answers'] == 'A']['Total'].iloc[0] if len(question_data[question_data['Categorical Answers'] == 'A']) > 0 else 0
        b_count = question_data[question_data['Categorical Answers'] == 'B']['Total'].iloc[0] if len(question_data[question_data['Categorical Answers'] == 'B']) > 0 else 0
        c_count = question_data[question_data['Categorical Answers'] == 'C']['Total'].iloc[0] if len(question_data[question_data['Categorical Answers'] == 'C']) > 0 else 0
        
        fleiss_data.append({
            'Question': question,
            'Category_A': a_count,
            'Category_B': b_count,
            'Category_C': c_count,
            'Total_Responses': a_count + b_count + c_count
        })
    
    return pd.DataFrame(fleiss_data)

def analyze_agreement_by_question(fleiss_df):
    """Analyze agreement for each question using Fleiss' Kappa statistic"""
    results = []
    
    # Calculate Fleiss' Kappa for each question
    for _, row in fleiss_df.iterrows():
        question = row['Question']
        
        # Create data matrix for Fleiss' Kappa calculation
        # For Fleiss' Kappa, we need to create a matrix where each row represents a "subject"
        # and each column represents a category, with values indicating how many raters chose that category
        
        # Since we have aggregate counts, we'll create a matrix where each "subject" (student) 
        # contributes to the category they chose
        
        total_responses = row['Total_Responses']
        a_count = row['Category_A']
        b_count = row['Category_B']
        c_count = row['Category_C']
        
        # Create data matrix: rows = total responses, columns = categories (A, B, C)
        # Each row represents one student's choice
        data_matrix = np.zeros((total_responses, 3))
        
        # Fill the matrix based on the counts
        current_row = 0
        
        # Add A responses
        for _ in range(int(a_count)):
            data_matrix[current_row, 0] = 1
            current_row += 1
        
        # Add B responses
        for _ in range(int(b_count)):
            data_matrix[current_row, 1] = 1
            current_row += 1
        
        # Add C responses
        for _ in range(int(c_count)):
            data_matrix[current_row, 2] = 1
            current_row += 1
        
        # Calculate Fleiss' Kappa
        kappa = calculate_fleiss_kappa(data_matrix)
        
        results.append({
            'Question': question,
            'Fleiss_Kappa': kappa,
            'N_Responses': total_responses,
            'Answer_A_Count': a_count,
            'Answer_B_Count': b_count,
            'Answer_C_Count': c_count,
            'Agreement_Level': interpret_fleiss_kappa(kappa)
        })
    
    return pd.DataFrame(results)

def interpret_fleiss_kappa(kappa):
    """Interpret Fleiss' Kappa values according to Landis & Koch (1977) thresholds"""
    if pd.isna(kappa):
        return "No data"
    elif kappa >= 0.81:
        return "Almost perfect agreement"
    elif kappa >= 0.61:
        return "Substantial agreement"
    elif kappa >= 0.41:
        return "Moderate agreement"
    elif kappa >= 0.21:
        return "Fair agreement"
    elif kappa >= 0.01:
        return "Slight agreement"
    else:
        return "Poor agreement"


def main():
    """Main function to run the agreement analysis"""
    print("=== Fleiss' Kappa Agreement Analysis ===")
    print()
    
    # Try to load data from CSV first (has the correct structure), then Excel
    df = None
    csv_file = 'Students-ValidationAnalysis-EN.csv'
    excel_file = 'Students-ValidationAnalysis-EN.xlsx'
    
    if Path(csv_file).exists():
        df = load_data_from_csv(csv_file)
    
    if df is None and Path(excel_file).exists():
        print("Warning: CSV file not found, trying Excel file...")
        df = load_data_from_excel(excel_file)
    
    if df is None:
        print("Error: Could not load data from either Excel or CSV file")
        return
    
    print(f"Data loaded successfully. Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print()
    
    # Display first few rows
    print("First few rows of data:")
    print(df.head())
    print()
    
    # Prepare data for Fleiss' Kappa calculation
    print("Preparing data for Fleiss' Kappa calculation...")
    fleiss_df = prepare_data_for_fleiss_kappa(df)
    print(f"Data prepared for Fleiss' Kappa. Shape: {fleiss_df.shape}")
    print()
    
    # Display prepared data
    print("Data prepared for Fleiss' Kappa calculation:")
    print(fleiss_df)
    print()
    
    # Analyze agreement by question
    print("Analyzing agreement using Fleiss' Kappa statistic...")
    results = analyze_agreement_by_question(fleiss_df)
    
    # Display results
    print("Agreement Analysis Results:")
    print("=" * 80)
    print(results.to_string(index=False))
    print()
    
    # Summary statistics
    print("Summary Statistics:")
    print(f"Total questions analyzed: {len(results)}")
    print(f"Average Fleiss' Kappa: {results['Fleiss_Kappa'].mean():.3f}")
    print(f"Questions with almost perfect agreement (κ ≥ 0.81): {len(results[results['Fleiss_Kappa'] >= 0.81])}")
    print(f"Questions with substantial agreement (0.61 ≤ κ < 0.81): {len(results[(results['Fleiss_Kappa'] >= 0.61) & (results['Fleiss_Kappa'] < 0.81)])}")
    print(f"Questions with moderate agreement (0.41 ≤ κ < 0.61): {len(results[(results['Fleiss_Kappa'] >= 0.41) & (results['Fleiss_Kappa'] < 0.61)])}")
    print(f"Questions with fair agreement (0.21 ≤ κ < 0.41): {len(results[(results['Fleiss_Kappa'] >= 0.21) & (results['Fleiss_Kappa'] < 0.41)])}")
    print(f"Questions with slight agreement (0.01 ≤ κ < 0.21): {len(results[(results['Fleiss_Kappa'] >= 0.01) & (results['Fleiss_Kappa'] < 0.21)])}")
    print(f"Questions with poor agreement (κ < 0.01): {len(results[results['Fleiss_Kappa'] < 0.01])}")
    print()
    
    # Save results to CSV
    results.to_csv('fleiss_kappa_agreement_results.csv', index=False)
    print("Results saved to 'fleiss_kappa_agreement_results.csv'")
    
    
    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()
