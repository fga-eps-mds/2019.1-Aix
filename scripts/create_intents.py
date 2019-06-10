tipo_de_intent = input("Insira o tipo de intent:")

print("Insira o nome do conteudo e suas variacoes")
print("Quando acabar, digite QQ para continuar a execucao")

conteudos = []
content = ""

while(content != "QQ"):
    content = input()
    if content == "QQ":
        break
    conteudos.append(content)


filename = "intents/" + tipo_de_intent + ".txt"
fileToWrite = open("result.txt", "w")

fileToWriteContent = []

for conteudo in conteudos:
    fileToRead = open(filename, "r")
    for line in fileToRead:
        fileToWriteContent.append(line.replace("[CONTEUDO]", conteudo))
    fileToRead.close()

fileToWriteContent.sort()
fileToWrite.writelines(fileToWriteContent)

fileToWrite.close()    