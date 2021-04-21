# dictionaries

nucleotidos = {
               "A": "Adenina",
               "C": "Citosina",
               "G": "Guanina", 
               "T": "Timina"
               }

print ("Length: ")
print (len(nucleotidos))

print nucleotidos

print (nucleotidos["A"])
print (nucleotidos["C"])
print (nucleotidos["G"])
print (nucleotidos["T"])

nucleotidos["A"] = "ADENINA"
nucleotidos["C"] = "CITOSINA"
nucleotidos["G"] = "GUANINA"
nucleotidos["T"] = "TIMINA"

print (nucleotidos)

nucleotidos.pop('T', None)
nucleotidos.pop('G', None)
nucleotidos.pop('C', None)
nucleotidos.pop('A', None)

print (nucleotidos)

