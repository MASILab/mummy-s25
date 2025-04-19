import pandas as pd
import os
import subprocess
import time

def process(input_path, output_path):
    command = ["TotalSegmentator", "-i", input_path, "-o", output_path]

    try:
        subprocess.run(command, check=True)
    except:
        print("Could not process: " + input_path)


def findFile(input_path):
    nii_files = [f for f in os.listdir(input_path) if f.endswith(".nii.gz")]

    return nii_files[0]

if __name__ == "__main__":
    final_list = pd.read_excel("final_list.xlsx", sheet_name="Sheet1")
    processed = []
    input_path = "/home-local/allank1/converted_scans"
    output_path = "/home-local/allank1/processed_scans"
    tot_time = 0

    for index, row in final_list.iterrows():
        scan = [row["Grid"], row["Accession No"], row["Series Desc"]]
        cur_input = input_path + "/" + row["Grid"] + "/" + row["Accession No"] + "/" + row["Series Desc"] + "/" 
        cur_input += findFile(cur_input)
        cur_output = output_path + "/" + row["Grid"] + "/" + row["Accession No"] + "/" + row["Series Desc"] + "/"

        if scan not in processed:
            startTime = time.time()
            process(cur_input, cur_output)
            process.append(scan)
            endTime = time.time()

            tot_time += endTime - startTime
        
        print("Processed: " + str(index + 1) + "/" + str(len(final_list)))
        remaining = (tot_time / (index + 1)) * (len(final_list) - (index + 1)) / 3600
        print("Remaining Hours: " + str(remaining))
    

        


    
