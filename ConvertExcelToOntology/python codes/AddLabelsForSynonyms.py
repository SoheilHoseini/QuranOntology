# Code to add labels to class names as their synonyms.
# Contributed by Soheil Hoseini


from io import TextIOWrapper
import os
import string
import openpyxl # Reading an excel file using Python

class Synonyms:
    
    def __init__(self, file: TextIOWrapper) -> None:
        self.onto_file = file
        
        
    # Converts the Persian class names to .owl format
    def ModifyEntityNameForOnto(self, className):
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


    def AppendAnnotationLabels(self, entity_name: string, synonym: string, final_onto: TextIOWrapper):
        final_onto.write("    <AnnotationAssertion>")
        final_onto.write("        <AnnotationProperty abbreviatedIRI=\"rdfs:label\"/>")
        final_onto.write(f"        <IRI>#{entity_name}</IRI>")
        final_onto.write(f"        <Literal>{synonym}</Literal>")
        final_onto.write("    </AnnotationAssertion>")


    def AppendAnnotLablesProcess(self, 
                                 syn_excel_path: string, 
                                 syns_excel_name: string, 
                                 final_onto_name: string, 
                                 final_onto_path: string):
        
        
        finalOntology = open(final_onto_path + final_onto_name + ".txt", "w", encoding="utf8")


        for line in self.onto_file:
            
            if line != "</Ontology>\n":
                finalOntology.write(line)
                
            else:
                ontology_synonyms = openpyxl.load_workbook(syn_excel_path + syns_excel_name + ".xlsx")
                synonyms_list = ontology_synonyms.active

                # Iterate through excel file of the synonyms
                for i in range(2, synonyms_list.max_row + 1):
                    
                    entity_name = synonyms_list.cell(i, 1).value
                    synonym = synonyms_list.cell(i, 2).value
                    self.AppendAnnotationLabels(entity_name, synonym, finalOntology)
                    
        self.FinalizeOntologyTags(finalOntology)
        self.ConvertTxtToOwl(final_onto_name)


    # Adds final tags for creating the ontology
    def FinalizeOntologyTags(self, file: TextIOWrapper):
        file.write("\n</Ontology>")
        file.write('\n\n\n<!--' + 'Contributed by Soheil Hoseini' + '-->')
    
    
    def ConvertTxtToOwl(self, ontology_name: string):
        
        # Convert the txt file to owl file
        convertedFile = "txt files\\" + ontology_name + ".txt"
        base = os.path.splitext(convertedFile)[0]
        base = "owl" + base[3:] # Save the ontology in the "owl files" folder
        os.rename(convertedFile, base + '.owl')

        print('Congratulations! You have successfully built your new ontology.')


path = "txt files\\"
orig_ontology_name = "IndvOnto3"
orig_ontology_file = open(path + orig_ontology_name + ".txt", "r")


# Load classes and subclasses excel
syn_path = "xlsx files\\HierarchyOntology\\Phase3\\"
onto_syn_excel_name = "QuranScienceSynonyms"

final_ontology_name = "FinalIndiRelTest"
final_ontology_path = "txt files\\"

# Start the adding synonyms process
synonyms_engine = Synonyms(orig_ontology_file)
synonyms_engine.AppendAnnotLablesProcess(syn_path, onto_syn_excel_name, final_ontology_name, final_ontology_path)

orig_ontology_file.close()


