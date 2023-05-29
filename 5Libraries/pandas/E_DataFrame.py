import pandas as pd

data ={"Nombre":["Maira","David","Ivan","Jhon"],
        "Carrera":["Auditoria","Informatica","Derecho","Idioma"],
        "Correo":["maira@gmail.com","David@gmail.com","Ivan@gmail.com","Jhon@gmail.com"]}

estuidantes = pd.DataFrame(data)

print(estuidantes)

data2= pd.DataFrame([["maira",24],["David",18],["Ivan",34],["Jhon",27]],
                    columns=["Nombre","Edad"])

print(data2)

data3 = pd.DataFrame([[1,2,3],[4,5,6]],
                    columns=["cero","uno","dos"])
print(data3)