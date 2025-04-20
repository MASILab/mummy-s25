# Mummy Project - Nirmal Alla

This repo is a collection of the work I have done over the course of the Spring 2025 Semester.

## Base Data Table
Within the file van_schaik_data.xlsx is all the available scans in the directory under valiant02/masi/. There are 2 sheets of note, the first is the "Base Table" which corresponds to all of the data with a row for each scan (not each individual). The other sheet is the "Base Pivot" this gives info on the most common types of scans found within the data

## Chart
The PDF file chart.pdf contains the flowchart displaying the data that was excluding through QA, along with the reasons that they were excluded.

## Final List
The file final_list.xlsx contains all the scans that made it through the QA process, and are thus to be processed with TotalSegmentator. Each row contains the Grid, Accession No, and Series Desc, all the info needed to find the directory contains the corresponding files

## Convert Scans
The file convert_scans.py is a script file to convert all files from an excel sheet from .dicom to .nii.gz.

## Process Scans
The file process_scans.py contains the script to go through all the scans from the final_list.xlsx file and process them with TotalSegmentator and place the results in another directory.
