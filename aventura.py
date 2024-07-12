import cmd
from mapa import estancias, conexiones
from pathlib import Path


class JuegoAventura(cmd.Cmd):
    prompt = '> '

    def __init__(self):
        super().__init__()
        self.habitacion_actual = 'entrada'
        self.inventario = ['nokia3310']
        print("Bienvenido a la aventura.")
        estancias[self.habitacion_actual].show()
    def do_ir(self, direccion):
        """Ir en una dirección: norte, sur, este, oeste"""
        if direccion in conexiones[self.habitacion_actual]:
            self.habitacion_actual = conexiones[self.habitacion_actual][direccion]
            self.do_mirar('')
        else:
            print("No puedes ir en esa dirección.")

    def do_mirar(self, _):
        """Mirar alrededor en la habitación actual"""
        estancias[self.habitacion_actual].show()
        if estancias[self.habitacion_actual].objects:
            print("Ves los siguientes objetos: " + ", ".join(estancias[self.habitacion_actual].objects))

    def do_tomar(self, objeto):
        """Tomar un objeto"""
        if objeto in estancias[self.habitacion_actual].objects:
            estancias[self.habitacion_actual].objects.remove(objeto)
            self.inventario.append(objeto)
            print(f"Has tomado {objeto}.")
        else:
            print(f"No hay {objeto} aquí.")

    def do_inventario(self, _):
        """Mostrar el inventario"""
        if self.inventario:
            print("Tienes: " + ", ".join(self.inventario))
        else:
            print("No tienes nada.")

    def do_salir(self, _):
        """Salir del juego"""
        print("Gracias por jugar.")
        return True

if __name__ == '__main__':
    juego = JuegoAventura()
    juego.cmdloop()