sequence = open('sequence.fasta', 'r') 
lines = sequence.readlines() 

letras = {"A": 0, "C": 0, "T": 0, "G": 0}
notLetras = 0

for line in lines:
   if line.startswith('>'):   
      continue
   for char in line:
      if char == "A":
         letras["A"] += 1   
      elif char == "C":
         letras["C"] += 1   
      elif char == "T":
         letras["T"] += 1  
      elif char == "G":
         letras["G"] += 1  
      else:
         notLetras += 1    

total = letras["A"] + letras["C"] + letras["T"] + letras["G"] + notLetras

print("Qnd A: ", letras["A"], "| Porcentagem: ", "{:.2f}%".format(letras["A"]/total * 100))
print("Qnd C: ", letras["C"], "| Porcentagem: ", "{:.2f}%".format(letras["C"]/total * 100))
print("Qnd T: ", letras["T"], "| Porcentagem: ", "{:.2f}%".format(letras["T"]/total * 100))
print("Qnd G: ", letras["G"], "| Porcentagem: ", "{:.2f}%".format(letras["G"]/total * 100))
print("Anomalias: ", notLetras, "| Porcentagem: ", "{:.2f}%".format(notLetras/total * 100))
