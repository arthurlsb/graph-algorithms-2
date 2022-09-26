from Grafo import Grafo
from GrafoDirigido1 import GrafoDirigido1
from GrafoDirigido2 import GrafoDirigido2
import ComponentesFortementeConexas
import OrdenacaoTopologica
import Prim

def main():
    grafo_componentesFortementeConexas = GrafoDirigido1("ComponenteFortementeConexa.net")
    grafo_ordenacaoTopologica = GrafoDirigido2("OrdenacaoTopologica.net")
    grafo_prim = Grafo("Prim.net")

    print("\n--------------Componentes Fortemente Conexas-------------------")
    ComponentesFortementeConexas.ComponentesFortementeConexas(grafo_componentesFortementeConexas)
    print("---------------------------------------------------------------\n\n")
    
    print("----------------Ordenação Topológica---------------------------")
    OrdenacaoTopologica.ordenacaoTopologica(grafo_ordenacaoTopologica)
    print("---------------------------------------------------------------\n\n")

    print("-----------------Prim------------------------------------------")
    Prim.prim(grafo_prim)
    print("---------------------------------------------------------------\n\n")

if __name__ == '__main__':
    main()
