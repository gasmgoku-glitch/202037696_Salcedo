# UNAD - Lenguajes Interpretados (202037696)
# Tarea 2: Control de voltaje del banco de baterías 24 V (sensor INA219)


def ejecutar_simulacion_baterias():
    chequeo_baterias = True
    lectura = 0

    voltios = float(input("Ingrese el voltaje inicial del banco: "))

    MAX_LECTURAS = float(input("\nIngrese el maximo de lecturas: "))

    while chequeo_baterias and lectura < MAX_LECTURAS:
        lectura += 1
        print("Lectura", lectura, "- Voltaje:", round(voltios, 1), "V")
        if voltios > 30:
            print("PELIGRO: Sobretensión extrema. Fusible abierto.")
            chequeo_baterias = False
        elif voltios < 21:
            print("Protección: Desconexión de carga por descarga")
            voltios += 1.0
        elif voltios >= 21 and voltios <= 27.5:
            print("Protección: Sistema operativo en flotación")
            voltios += 0.2
        else:
            print("Protección: Disipador térmico activado")
            voltios -= 1.5

    print("Monitoreo finalizado.")


if __name__ == "__main__":
    ejecutar_simulacion_baterias()