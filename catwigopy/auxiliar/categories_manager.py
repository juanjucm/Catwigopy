# Functions to create categories and operate with them.
# Mainly for internal use.
import xlrd



#############
# This function receives a csv file in the first arg containing the definition of the IAB Categories v2.0
# and returns a .json containing the categories used in this concrete problem and its respective keywords
# to perform twitter search.
#############
def import_categories_from_csv(input_file, output_file):

    doc = xlrd.open_workbook(input_file)