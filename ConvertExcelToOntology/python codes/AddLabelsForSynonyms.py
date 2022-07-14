# Code to add labels to class names as their synonyms.
# Contributed by Soheil Hoseini


import os
import openpyxl # Reading an excel file using Python

# Converts the Persian class names to .owl format
def ModifyEntityNameForOnto(className):
    nameList = list(className.split())
    
    #Remove paranthesis
    for i in range(len(nameList)):
        if nameList[i] == "(" or nameList[i] == ")":
            print(className)
            nameList[i] = "" 
            
        tmp = nameList[i]
        ans = ""
        
        for j in range(len(tmp)):
            
            if tmp[j] == "(" and tmp[j + 1] == "ع":
                ans += "_"
                continue
            
            if tmp[j] == "(" and tmp[j + 1] == "ص":
                ans += "_"
                continue
            
            if tmp[j] == "(" and tmp[j + 1] == "س":
                ans += "_"
                continue
            
            if tmp[j] != "(" and tmp[j] != ")":
                ans += tmp[j] 
                 
        nameList[i] = ans    
            
    return "_".join(nameList)


def AddAnnotationLabel():
    pass 


ontologyName = "SoheilRefinedOntoTxt"
origOntology = open("txt files\\" + ontologyName + ".txt","r")

# Load classes and subclasses excel
ontoSynExcelName = "QuranConceptSynonyms"
ontologySynonyms = openpyxl.load_workbook(ontoSynExcelName + ".xlsx")
synonymsList = ontologySynonyms.active

# Iterate through excel file of the synonyms
for i in range(2, synonymsList.max_row + 1):
    className = synonymsList.cell(row=i, column=1).value
    synonym = synonymsList.cell(row=i, column=2).value
    
    
origOntology.close()
