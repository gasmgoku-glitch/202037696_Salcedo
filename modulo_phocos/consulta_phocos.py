# UNAD - Lenguajes Interpretados (202037696)
# Tarea 3 - Paso 4: Consulta segura del controlador Phocos MPPT
mppt_phocos = {
    "0x10": {"hardware_source": "PV_ARRAY", "max_safe_value": 150.0, "system_flag": True},
    "0x11": {"hardware_source": "BATTERY", "max_safe_value": 60.0, "system_flag": True},
    "0x15": {"hardware_source": "LOAD_RELAY", "max_safe_value": 20.0, "system_flag": False},
}
MAX_INTENTOS = 5


def ejecutar_consulta_interactiva():
    print("CONSULTA DE REGISTROS - PHOCOS MPPT")
    print("Registros disponibles:")
    for direccion in mppt_phocos:
        print(direccion, "->", mppt_phocos.get(direccion).get("hardware_source"))
    print("Escriba una dirección (ej: 0x10) o una fuente (ej: BATTERY). Escriba 'salir' para terminar.\n")
    for intento in range(1, MAX_INTENTOS + 1): # Control numérico: máximo 5 consultas
        entrada = input(f"Consulta {intento} de {MAX_INTENTOS}: ").strip()
        if entrada.lower() == "salir":
            print("Programa finalizado.")
            break
        # Buscar por dirección hexadecimal
        registro = mppt_phocos.get(entrada.lower())
        # Si no es una dirección, buscar por el nombre de la fuente
        if registro is None:
            for direccion in mppt_phocos:
                if mppt_phocos.get(direccion).get("hardware_source") == entrada.upper():
                    registro = mppt_phocos.get(direccion)
        if registro is None:
            print("Error: el registro", entrada, "no existe.\n")
        else:
            print("Fuente:", registro.get("hardware_source"))
            print("Valor máximo seguro:", registro.get("max_safe_value"))
            print("Bandera del sistema:", registro.get("system_flag"), "\n")
        if intento == MAX_INTENTOS:
            print("Se alcanzó el límite de consultas.")


if __name__ == "__main__":
    ejecutar_consulta_interactiva()