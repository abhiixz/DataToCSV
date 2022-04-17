#########################################
# Required Python Packages
#########################################
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#########################################
# File Paths
#########################################

INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

#########################################
# Function name : read_data
# Description : Read the data into pandas dataframe
# Inpt :  path of CSV file
# Output : Gives the data
# Author : Abhishek Supe
#########################################

def read_data(path):
    data = pd.read_csv(path)
    return data

#########################################
# Function name : add_headers
# Description :    Add the headers to the dataset
# Input : dataset
# Output : Updated dataset
# Author : Abhishek Supe

#########################################

def add_headers(dataset, headers):
    dataset.columns = headers
    return dataset

 #########################################
# Function name : data_file_to_csv
# Input : Nothing
# Output : Write the data to CSV
# Author : Abhishek Supe
#########################################

def data_file_to_csv():
    headers = ["CodeNumber", "ClumpThickness", "UniformityCellSize", "UniformityCellShape", "MarginalAdhesion",
               "SingleEpithelialCellSize", "BareNuclei", "BlandChromatin", "NormalNucleoli", "Mitoses",
               "CancerType"]

    dataset = read_data(INPUT_PATH)
    dataset = add_headers(dataset, headers)
    dataset.to_csv(OUTPUT_PATH, index=False)

    print ("File saved ...!")

#########################################
# Function name : main
# Description :  Main function from where execution starts
# Author : Abhishek Supe
#########################################

def main():
    data_file_to_csv()
    
if __name__ == "__main__":
    main()
