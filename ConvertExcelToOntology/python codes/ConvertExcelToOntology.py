# Code for building an ontology with class names in an excel file.
# Contributed by Soheil Hoseini


from tkinter.filedialog import Open
from types import NoneType
from sympy import N
import openpyxl # Reading an excel file using Python
import os # Used for converting the txt file to owl file



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


# Takes a class name and adds it the ontology
def AddClassToOntology(className, fileName):
    fileName.write("\n    <Declaration>\n")
    middleTxt = '        <Class IRI="#' + ModifyEntityNameForOnto(className) + '"/>'
    fileName.write(middleTxt)
    fileName.write("\n    </Declaration>")


# Takes a relation name and adds it the ontology
def AddObjectPropToOntology(relationName, domainClass, rangeClass, fileName, objectPropertyType):
    
    # Declaration of the relation
    fileName.write("\n    <Declaration>\n")
    middleTxt = '        <ObjectProperty IRI="#' + ModifyEntityNameForOnto(relationName) + '"/>'
    fileName.write(middleTxt)
    fileName.write("\n    </Declaration>")
    
    # Determine the type of the object property
    if objectPropertyType != None:
        objPropStr = ObjectPropertyTypeString(objectPropertyType)
        
        startText = "\n    <" + objPropStr + ">\n"
        fileName.write(startText)
        
        middleTxt = '        <ObjectProperty IRI="#' + ModifyEntityNameForOnto(relationName) + '"/>'
        fileName.write(middleTxt)
        
        endingText = "\n    </" + objPropStr + ">"
        fileName.write(endingText)
    
    # Determine domains of the object properties
    fileName.write("\n    <ObjectPropertyDomain>\n")
    
    middleTxt = '        <ObjectProperty IRI="#' + ModifyEntityNameForOnto(relationName) + '"/>'
    fileName.write(middleTxt)
    
    middleTxt2 = '\n        <Class IRI="#' + ModifyEntityNameForOnto(domainClass) + '"/>'
    fileName.write(middleTxt2)
    
    fileName.write("\n    </ObjectPropertyDomain>")
    
    # Determine ranges of the object properties
    fileName.write("\n    <ObjectPropertyRange>\n")
    
    middleTxt = '        <ObjectProperty IRI="#' + ModifyEntityNameForOnto(relationName) + '"/>'
    fileName.write(middleTxt)
    
    middleTxt2 = '\n        <Class IRI="#' + ModifyEntityNameForOnto(rangeClass) + '"/>'
    fileName.write(middleTxt2)
    
    fileName.write("\n    </ObjectPropertyRange>")
    
    
# Takes a object property type and returns the corresponding string of it
def ObjectPropertyTypeString(objectProType):
    
    objectProType = objectProType.lower()#convert to lower case for case insensitive comparison
    
    switcher = {
        "functional" : "FunctionalObjectProperty",
        "inverse functional" : "InverseFunctionalObjectProperty",
        "symmetric" : "SymmetricObjectProperty",
        "asymmetric" : "AsymmetricObjectProperty",
        "transitive" : "TransitiveObjectProperty",
        "reflexive" : "ReflexiveObjectProperty",
        "irreflexive" : "IrreflexiveObjectProperty",
        "Functional" : "FunctionalObjectProperty",
        "Inverse Functional" : "InverseFunctionalObjectProperty",
        "Symmetric" : "SymmetricObjectProperty",
        "Asymmetric" : "AsymmetricObjectProperty",
        "Transitive" : "TransitiveObjectProperty",
        "Reflexive" : "ReflexiveObjectProperty",
        "Irreflexive" : "IrreflexiveObjectProperty"
    }
    
    return switcher.get(objectProType)


# Take a class name and its father and add it to the ontology
def AddSubclasses(fatherClass, subclass , fileName):
    fileName.write("\n    <SubClassOf>\n")
    middleTxt1 = '        <Class IRI="#' + ModifyEntityNameForOnto(subclass) + '"/>'
    fileName.write(middleTxt1)
    middleTxt2 = '\n        <Class IRI="#' + ModifyEntityNameForOnto(fatherClass) + '"/>'
    fileName.write(middleTxt2)
    fileName.write("\n    </SubClassOf>")
 
 
# Take a class name and its individuals and add it to the ontology
def AddIndividualsToOntology(className, individualName, fileName): 
    
    fileName.write("\n    <Declaration>\n")
    middleTxt = '        <NamedIndividual IRI="#' + ModifyEntityNameForOnto(individualName) + '"/>'
    fileName.write(middleTxt)
    fileName.write("\n    </Declaration>")
    
    fileName.write("\n    <ClassAssertion>\n")
    middleTxt2 = '        <Class IRI="#' + ModifyEntityNameForOnto(className) + '"/>'
    fileName.write(middleTxt2)
    middleTxt3 = '\n        <NamedIndividual IRI="#' + ModifyEntityNameForOnto(individualName) + '"/>'
    fileName.write(middleTxt3)
    fileName.write("\n    </ClassAssertion>")


# Adds the initializing tags, needed for building an ontology
def InitializeOntology(ontoFile, ontologyName, annotation):
    
    ontoFile.write('<?xml version="1.0"?>\n')
    ontoFile.write('<Ontology xmlns="http://www.w3.org/2002/07/owl#"\n')
    ontoFile.write('     xml:base="http://www.sem0anticweb.org/rayan-tech/ontologies/2022/2/' + ontologyName + '"\n')
    ontoFile.write('     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n')
    ontoFile.write('     xmlns:xml="http://www.w3.org/XML/1998/namespace"\n')
    ontoFile.write('     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n')
    ontoFile.write('     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"\n')
    ontoFile.write('     ontologyIRI="http://www.sem0anticweb.org/rayan-tech/ontologies/2022/2/' + ontologyName + '">\n')
    ontoFile.write('     <Prefix name="" IRI="http://www.sem0anticweb.org/rayan-tech/ontologies/2022/2/' + ontologyName + '"/>\n')
    ontoFile.write('     <Prefix name="owl" IRI="http://www.w3.org/2002/07/owl#"/>\n')
    ontoFile.write('     <Prefix name="rdf" IRI="http://www.w3.org/1999/02/22-rdf-syntax-ns#"/>\n')
    ontoFile.write('     <Prefix name="xml" IRI="http://www.w3.org/XML/1998/namespace"/>\n')
    ontoFile.write('     <Prefix name="xsd" IRI="http://www.w3.org/2001/XMLSchema#"/>\n')
    ontoFile.write('     <Prefix name="rdfs" IRI="http://www.w3.org/2000/01/rdf-schema#"/>\n')
    
    ontoFile.write('     <Annotation>\n')
    ontoFile.write('         <AnnotationProperty abbreviatedIRI="rdfs:comment"/>\n')
    ontoFile.write('         <Literal>' + annotation + '</Literal>\n')
    ontoFile.write('     </Annotation>')
    
    
# Adds final tags for creating the ontology
def FinalizeOntology(file):
    file.write("\n</Ontology>")
    file.write('\n\n\n<!--' + 'Contributed by Soheil Hoseini' + '-->')
    
    
# Take ontology name and annotation from user
ontologyName = input("Enter the name of your ontology: \n") # There shouldn't be any spaces in the ontology name
annotation = input("Enter a brief annotation for your ontology: \n")


# Create a txt file for the ontology to write initializing owl tags to it
newOntology = open("txt files\\" + ontologyName + ".txt", 'w', encoding="utf8")

# Initialize the Ontology
InitializeOntology(newOntology, ontologyName, annotation)
newOntology.close()

# Open the txt file again to append class names
newOntology = open("txt files\\" + ontologyName + ".txt", 'a', encoding="utf8")

allClassesList = []

'''
# Load class names excel with its path
ontologyClasses = openpyxl.load_workbook("SmallQuranWords - Test.xlsx")
classNamesList = ontologyClasses.active



# Iterate through excel file of classes and add classes to ontology
for i in range(2, classNamesList.max_row+1):
    className = classNamesList.cell(row=i, column=1).value
    allClassesList.append(className)
    AddClassToOntology(className, newOntology)
'''



# Load classes and subclasses excel
hirarchyOntoExcelName = "Classes"
ontologySubclasses = openpyxl.load_workbook("xlsx files\\IndividualOntology\\" + hirarchyOntoExcelName + ".xlsx")
subclassList = ontologySubclasses.active 


# Iterate file of subclasses and declare each subclasses as a class in the ontology
for i in range(2, subclassList.max_row+1):
    
    fatherClassName  = subclassList.cell(row=i, column=2).value
    subclassName = subclassList.cell(row=i, column=1).value

    if (fatherClassName not in allClassesList):
        AddClassToOntology(fatherClassName , newOntology)
        allClassesList.append(fatherClassName)
    
    if (type(subclassName) == NoneType):
        continue 
     
    if (subclassName not in allClassesList):
        AddClassToOntology(subclassName, newOntology)
        allClassesList.append(subclassName)

        

# Create connection between father class and its subclasses
for i in range(2, subclassList.max_row+1):
    
    fatherClassName  = subclassList.cell(row=i, column=2).value
    subclassName = subclassList.cell(row=i, column=1).value
    
    if (type(subclassName) == NoneType):
        continue
        
    AddSubclasses(fatherClassName, subclassName, newOntology)
       
'''
ontologySubclasses2 = openpyxl.load_workbook("HierarchyOfQuranConcepts.xlsx")
subclassList2 = ontologySubclasses2.active
       
for i in range(2, subclassList2.max_row+1):
    
    #second file of classes
    fatherClassName2  = subclassList2.cell(row=i, column=1).value
    subclassName2 = subclassList2.cell(row=i, column=2).value
    
    if (fatherClassName2 not in allClassesList):
        AddClassToOntology(fatherClassName2 , newOntology)
        allClassesList.append(fatherClassName2)
    
    if (type(subclassName2) == NoneType):
        continue 
     
    if (subclassName2 not in allClassesList):
        AddClassToOntology(subclassName2, newOntology)
        allClassesList.append(subclassName2)
        

# Create connection between father class and its subclasses for the second list
for i in range(2, subclassList2.max_row+1):
    
    fatherClassName2  = subclassList2.cell(row=i, column=1).value
    subclassName2 = subclassList2.cell(row=i, column=2).value
    
    if (type(subclassName2) == NoneType):
            continue
        
    AddSubclasses(fatherClassName2, subclassName2, newOntology)
'''


'''
# Load object properties excel with its path
ontologyObjProp = openpyxl.load_workbook("QuranObjectProperties.xlsx")
objPropList = ontologyObjProp.active

# Iterate through excel file of relations and add classes to ontology
for i in range(2, objPropList.max_row+1):
    domainClass = objPropList.cell(row=i, column=1).value
    rangeClass = objPropList.cell(row=i, column=2).value
    relationName = objPropList.cell(row=i, column=3).value
    objectPropertyType = objPropList.cell(row=i, column=4).value
    AddObjectPropToOntology(relationName, domainClass, rangeClass, newOntology, objectPropertyType)
'''  



# Load Individuals
concept_indv_excel_name = "QuranConceptIndv"
ontologyIndv = openpyxl.load_workbook("xlsx files\\IndividualOntology\\" + concept_indv_excel_name + ".xlsx")
indvList = ontologyIndv.active

# Iterate file of individuals and add them to the ontology
for i in range(2, indvList.max_row+1):
    classNameForIndv = indvList.cell(row=i, column=2).value
    indvName = indvList.cell(row=i, column=1).value
    
    if(type(indvName) == NoneType):
        continue
    
    AddIndividualsToOntology(classNameForIndv, indvName, newOntology)


# Load Individuals
science_indv_excel_name = "QuranScienceIndv"
ontologyIndv = openpyxl.load_workbook("xlsx files\\IndividualOntology\\" + science_indv_excel_name + ".xlsx")
indvList = ontologyIndv.active

# Iterate file of individuals and add them to the ontology
for i in range(2, indvList.max_row+1):
    classNameForIndv = indvList.cell(row=i, column=2).value
    indvName = indvList.cell(row=i, column=1).value
    
    if(type(indvName) == NoneType):
        continue
    
    AddIndividualsToOntology(classNameForIndv, indvName, newOntology)



# Add final tags to the ontology file
FinalizeOntology(newOntology)
newOntology.close()

# Convert the txt file to owl file
convertedFile = "txt files\\" + ontologyName + ".txt"
base = os.path.splitext(convertedFile)[0]
base = "owl" + base[3:] # Save the ontology in the "owl files" folder
os.rename(convertedFile, base + '.owl')

print('Congratulations! You have successfully built your new ontology.')

