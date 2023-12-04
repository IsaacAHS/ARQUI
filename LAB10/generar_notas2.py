import random


if __name__ == "__main__":
    #contenido = "p1,p2,p3,p4,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,TA\n"

    practica_uno= random.randint(0,20)
    for i in range(1):
            linea = f"{practica_uno},"
            for _ in range(14):
                linea += f"{random.randint(0, 20)},"
            #contenido += f"{linea[:-1]}\n"

    with open("notas2.csv", "w+", encoding="utf-8") as f:
        f.write(linea)