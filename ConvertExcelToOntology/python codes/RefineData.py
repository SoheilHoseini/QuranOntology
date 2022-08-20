# Refine input data to ontology to homogenize Persian and Arabic phonetics
# Contributed by Soheil Hoseini


import openpyxl
from sympy import refine # Reading an excel file using Python
import xlsxwriter # Create and fill xlsx file 

class RefineOntologyData:
    
    def __init__(self) -> None:
        pass
    
    def modify_enitiy_name(self, name):
        # در فایل پدر و فرزندی، "ی" عربی هست و کیبورد رو نمیخونه برعکس فایل روابط
        pass
    
 
        
path = "xlsx files\\IndividualOntology\\Phase2\\" 
excel_file_name = "FatherChildList"

excel_file = openpyxl.load_workbook(path + excel_file_name + ".xlsx")
records_list = excel_file.active

refine_engine = RefineOntologyData()
