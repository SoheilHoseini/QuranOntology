# Refine input data to ontology to homogenize Persian and Arabic phonetics
# Contributed by Soheil Hoseini


import openpyxl# Reading an excel file using Python
import xlsxwriter # Create and fill xlsx file 

class RefineOntologyData:
    
    def __init__(self) -> None:
        self.modified_y_cnt = 0
    
    def modify_enitiy_name(self, name):
        # در فایل پدر و فرزندی، "ی" فارسی هست و کیبورد رو میخونه برعکس فایل روابط
        names_list = list(name.split())

        for j in range(len(names_list)):
            
            word = names_list[j]
            ans = ""
            for k in range(len(word)):
                
                # Convet Arabic format to Persian
                if word[k] == "ى":
                    ans += "ی"
                    self.modified_y_cnt += 1
                
                else:
                    ans += word[k]
                
                
                # if "ى"!=  "ی":
                #     print(f"Bingo: {name}, character index: {j}")
            
            names_list[j] = ans
        return " ".join(names_list)  
    

refine_engine = RefineOntologyData()
        
path = "xlsx files\\IndividualOntology\\Phase2\\" 
excel_file_name = "FatherChildList"

excel_file = openpyxl.load_workbook(path + excel_file_name + ".xlsx")
records_list = excel_file.active


# Create a new xlsx file combined of the last two 
dest_xlsx_file = "RefinedFatherChildList"
workbook = xlsxwriter.Workbook(path + dest_xlsx_file + ".xlsx")
worksheet = workbook.add_worksheet() 


row = 1
# Add the original file headers
worksheet.write(0, 0, records_list.cell(1,1).value)
worksheet.write(0, 1, records_list.cell(1,2).value)
worksheet.write(0, 2, records_list.cell(1,4).value)

for i in range(2, records_list.max_row + 1):
    
    cell1 = records_list.cell(i, 1).value
    modified_cell1 = refine_engine.modify_enitiy_name(cell1)
    worksheet.write(row, 0, modified_cell1)
    
    cell2 = records_list.cell(i, 2).value
    modified_cell2 = refine_engine.modify_enitiy_name(cell2)
    worksheet.write(row, 1, modified_cell2)
    
    cell3 = records_list.cell(i, 3).value
    modified_cell3 = refine_engine.modify_enitiy_name(cell3)
    worksheet.write(row, 2, cell3)
    
    # cell4 = records_list.cell(i, 4).value
    # modified_cell4 = refine_engine.modify_enitiy_name(cell4)
    # worksheet.write(row, 3, modified_cell4)
    
    row += 1

workbook.close()


print("Congrats my friend! Your data has been successfully refined. ")
print(f"\nStats:\n      Modified ی counts: {refine_engine.modified_y_cnt}\n")