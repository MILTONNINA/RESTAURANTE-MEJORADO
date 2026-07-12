from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_menu():
    gestor_restaurante = Restaurante()

    while True:
        print("\n=========================================")
        print("          SISTEMA DE RESTAURANTE         ")
        print("=========================================")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("-----------------------------------------")
        print("4. Registrar cliente")
        print("5. Listar clientes")
        print("6. Buscar cliente")
        print("-----------------------------------------")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO PRODUCTO ---")
            try:
                nom = input("Nombre del producto: ")
                cat = input("Categoría: ")
                pre = float(input("Precio: "))
                nuevo_prod = Producto(nombre=nom, categoria=cat, precio=pre)
                gestor_restaurante.registrar_producto(nuevo_prod)
            except ValueError as error:
                print(f"Error de validación: {error}")

        elif opcion == "2":
            gestor_restaurante.listar_productos()

        elif opcion == "3":
            print("\n--- BUSCAR PRODUCTO ---")
            nombre_b = input("Ingrese el nombre del producto a buscar: ")
            encontrado = gestor_restaurante.buscar_producto(nombre_b)
            if encontrado:
                print(f"Resultado: {encontrado.mostrar_informacion()}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("\n--- REGISTRAR NUEVO CLIENTE ---")
            nom_c = input("Nombre del cliente: ").strip()
            correo_c = input("Correo electrónico: ").strip()
            id_c = input("Identificación (ID/Cédula): ").strip()
            
            if not nom_c or not correo_c or not id_c:
                print("Error: Todos los campos del cliente son obligatorios.")
            else:
                nuevo_cli = Cliente(nombre=nom_c, correo=correo_c, id_cliente=id_c)
                gestor_restaurante.registrar_cliente(nuevo_cli)

        elif opcion == "5":
            gestor_restaurante.listar_clientes()

        elif opcion == "6":
            print("\n--- BUSCAR CLIENTE ---")
            id_b = input("Ingrese el ID o Cédula del cliente a buscar: ").strip()
            encontrado_c = gestor_restaurante.buscar_cliente(id_b)
            if encontrado_c:
                print(f"Resultado: {encontrado_c.mostrar_informacion()}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()