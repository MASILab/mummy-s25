import os
import pandas as pd
import subprocess
import time

def convert(input_path, output_path):
    command = [
        "dcm2niix",
        "-z", "y",             # compress to .nii.gz
        "-o", output_path,     # output directory
        "-f", "%p_%s",         # filename: protocol name and series number
        input_path             # input directory
    ]

    try:
        subprocess.run(command, check=True)
    except:
        print("Could not convert: " + input_path)


if __name__ == "__main__":
    final_list = pd.read_excel("final_list.xlsx", sheet_name="Sheet1")
    converted = []
    tot_time = 0

    # Check to ensure that this is correct
    input_path = "/valiant02/masi/Van_Schaik_ImageVU_Pull/"
    output_path = "/home-local/allank1/converted_scans/"


    for index, row in final_list.iterrows():
        scan = [row["Grid"], row["Accession No"], row["Series Desc"]]
        cur_input = input_path + row["Grid"] + "/" + row["Accession No"] + "/" + row["Series Desc"] + "/"
        cur_output = output_path + row["Grid"] + "/" + row["Accession No"] + "/" + row["Series Desc"] + "/"

        if scan not in converted:
            start_time = time.time()
            convert(cur_input, cur_output)
            end_time = time.time()
            tot_time += end_time - start_time
        
        print("Processed: " + str(index + 1) + "/" + str(len(final_list)))
        remaining = (tot_time / len(converted)) * (len(final_list) - (index + 1)) / 3600
        print("Remaining Hours: " + str(remaining))


