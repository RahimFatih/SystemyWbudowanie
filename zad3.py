import re

replaceFrom = "249031@student.pwr.edu.pl"
replaceTo = "test@test.pwr.edu.pl"
replaceUserAgent = "GrzmotowyPtak 1.2.3.4"
replaceMime = "1.0000000000001"

fIn = open("input.txt", "r")
fOut=open("output.txt","w")

text=fIn.read() 
print("\n\n--------------------\n",text,"\n--------------------\n\n")
text=re.sub(r'(?<=From: )\S+@\S+',replaceFrom,text)
text=re.sub(r'(?<=To: )\S+@\S+',replaceTo,text)
text=re.sub(r'(?<=User-Agent: )\S.*',replaceUserAgent,text)
text=re.sub(r'(?<=MIME-Version: )\S.*',replaceMime,text)
fOut.write(text)
print("Po zamianie danych:")
print("\n\n--------------------\n",text,"\n--------------------\n\n")
fIn.close()
fOut.close()
