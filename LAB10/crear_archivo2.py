import random


if __name__ == "__main__":
    contenido = "paciente ,edad , diagnostico \n"

    paciente= 1
    for i in range(10):
            linea = f"{paciente+i},"
            for _ in range(1):
                linea += f"{random.randint(20, 80)},{random.randint(0,1)},"
            contenido += f"{linea[:-1]}\n"

    with open("base_datos.csv", "w+", encoding="utf-8") as f:
        f.write(contenido)