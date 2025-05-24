

#* Agenda de contactos: Implementa búsqueda, añadir y eliminar contactos

class Contacto:
    """
    Clase que representa un contacto con nombre y teléfono.
    """
    def __init__(self, nombre, telefono):
        # Corrección: eliminar la coma que convertía nombre en tupla
        self.nombre = nombre
        self.telefono = telefono
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"


class Agenda:
    """
    Clase para gestionar una agenda de contactos.
    Permite añadir, buscar, eliminar y mostrar contactos.
    """
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, contacto):
        """
        Añade un contacto a la agenda si no existe.
        
        Args:
            contacto: Objeto de la clase Contacto
        
        Returns:
            bool: True si se añade, False si ya existe
        """
        # Verificar si ya existe un contacto con el mismo nombre
        if self.buscar_contacto(contacto.nombre):
            print(f"Ya existe un contacto con el nombre '{contacto.nombre}'")
            return False
        
        self.contactos.append(contacto)
        return True

    def buscar_contacto(self, nombre):
        """
        Busca un contacto por nombre.
        
        Args:
            nombre: Nombre del contacto a buscar
            
        Returns:
            Contacto: El contacto encontrado o None
        """
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        """
        Elimina un contacto de la agenda por su nombre.
        
        Args:
            nombre: Nombre del contacto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        contacto_previo = len(self.contactos)
        self.contactos = [c for c in self.contactos if c.nombre != nombre]
        
        if contacto_previo > len(self.contactos):
            print(f"Contacto '{nombre}' eliminado correctamente")
            return True
        else:
            print(f"No se encontró el contacto '{nombre}'")
            return False

    def mostrar_contactos(self):
        """
        Muestra todos los contactos de la agenda.
        """
        if not self.contactos:
            print("La agenda está vacía")
            return
        
        print("\n=== LISTA DE CONTACTOS ===")
        print("-------------------------")
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i}. {contacto}")
        print("-------------------------")
        print(f"Total: {len(self.contactos)} contactos")


def menu_agenda():
    """Función principal que muestra un menú interactivo para gestionar la agenda."""
    agenda = Agenda()
    
    # Pre-cargar algunos contactos de ejemplo
    agenda.añadir_contacto(Contacto("Juan", "123456789"))
    agenda.añadir_contacto(Contacto("Maria", "987654321"))
    
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            nombre = input("Introduzca el nombre: ")
            telefono = input("Introduzca el teléfono: ")
            nuevo_contacto = Contacto(nombre, telefono)
            agenda.añadir_contacto(nuevo_contacto)
            
        elif opcion == "2":
            nombre = input("Introduzca el nombre a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print(f"\nContacto encontrado: {contacto}")
            else:
                print(f"\nNo se encontró ningún contacto con el nombre '{nombre}'")
                
        elif opcion == "3":
            nombre = input("Introduzca el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
            
        elif opcion == "4":
            agenda.mostrar_contactos()
            
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")


# Para ejecutar la versión interactiva, descomenta la siguiente línea:
# menu_agenda()

# Ejemplo de uso básico (para mostrar funcionamiento)
if __name__ == "__main__":
    agenda = Agenda()
    print("=== Demostración de la agenda ===")
    
    # Añadir contactos
    contacto1 = Contacto("Juan", "123456789")
    contacto2 = Contacto("Maria", "987654321")
    agenda.añadir_contacto(contacto1)
    agenda.añadir_contacto(contacto2)
    
    # Mostrar contactos
    agenda.mostrar_contactos()
    
    # Buscar un contacto
    nombre_buscar = "Juan"
    print(f"\nBuscando contacto '{nombre_buscar}':")
    contacto_encontrado = agenda.buscar_contacto(nombre_buscar)
    if contacto_encontrado:
        print(f"Contacto encontrado: {contacto_encontrado}")
    else:
        print(f"Contacto '{nombre_buscar}' no encontrado.")
    
    # Eliminar un contacto
    print(f"\nEliminando contacto '{nombre_buscar}':")
    agenda.eliminar_contacto(nombre_buscar)
    
    # Mostrar contactos después de eliminar
    agenda.mostrar_contactos()

# Fin del código
"""
=== Demostración de la agenda ===

=== LISTA DE CONTACTOS ===
------------------------- 
1. Nombre: Juan, Teléfono: 123456789
2. Nombre: Maria, Teléfono: 987654321
-------------------------
Total: 2 contactos

Buscando contacto 'Juan':
Contacto encontrado: Nombre: Juan, Teléfono: 123456789

Eliminando contacto 'Juan':
Contacto 'Juan' eliminado correctamente

=== LISTA DE CONTACTOS ===
-------------------------
1. Nombre: Maria, Teléfono: 987654321
-------------------------
Total: 1 contactos
"""