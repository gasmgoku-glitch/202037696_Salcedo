
# UNAD - Lenguajes Interpretados (Código: 202037696)
# Tarea 5: Sustentacion Critica del Proyecto de Automatizacion 
# Autor: Gustavo Salcedo Mercado

import sys
from modulo_baterias.control_baterias import ejecutar_simulacion_baterias
from modulo_phocos.consulta_phocos import ejecutar_consulta_interactiva


def mostrar_menu():
    """Despliega el menú principal de selección de submódulos."""
    print("=" * 70)
    print("   SUSTENTACION CRITICA DEL PROYECTO DE AUTOMATIZACION ")
    print("   Autor: Gustavo Salcedo Mercado")
    print("=" * 70)
    print("1. Ejecutar Monitoreo de Baterías 24V (INA219 - Tarea 2)")
    print("2. Consultar Mapa de Memoria Phocos MPPT (Tarea 3)")
    print("3. Salir del Sistema")
    print("=" * 70)


def main():
    """Función principal que coordina la ejecución de los módulos."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            print("\n[INFO] Iniciando Módulo de Baterías...")
            ejecutar_simulacion_baterias()
        elif opcion == "2":
            print("\n[INFO] Iniciando Módulo Phocos MPPT...")
            ejecutar_consulta_interactiva()
        elif opcion == "3":
            print("\n[INFO] Sistema finalizado por el usuario.")
            sys.exit(0)
        else:
            print("\n[ERROR] Opción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()