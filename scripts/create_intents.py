import sys

if sys.version_info.major == 2:
    tipo_de_intent = raw_input("Insira o tipo de intent:")
elif sys.version_info.major == 3:
    tipo_de_intent = input("Insira o tipo de intent:")

print("Insira o nome do conteudo e suas variacoes")
print("Quando acabar, digite QQ para continuar a execucao")

conteudos = []
content = ""

while(content != "QQ"):
    if sys.version_info.major == 2:
        content = raw_input()
    elif sys.version_info.major == 3:
        content = input()
    if content == "QQ":
        break
    conteudos.append(content)


filename = "intents/" + tipo_de_intent + ".txt"
fileToWrite = open("result.txt", "w")

fileToWriteContentTemp = []

for conteudo in conteudos:
    fileToRead = open(filename, "r")
    for line in fileToRead:
        fileToWriteContentTemp.append(line.replace("[CONTEUDO]", conteudo))
    fileToRead.close()

fileToWriteContentTemp.sort()

fileToWriteContent = []

for contentLine in fileToWriteContentTemp:
    fileToWriteContent.append("- " + contentLine)

fileToWrite.writelines(fileToWriteContent)

fileToWrite.close()   