"""
functions to read the a CSV file
and put it into a dictionary
"""
import os
import csv
my_dict={}

def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """
    with open(palette_filename, 'r')  as f:
        read_csv= csv.reader(f)
        for row in read_csv:
            key=int(row[0])
            red=(row[1]).lstrip()
            green=(row[2]).lstrip()
            blue=(row[3]).lstrip()
            my_dict[key]=red, green, blue


    return my_dict
