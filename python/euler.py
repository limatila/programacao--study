face = int(input("Número de faces: "))
aresta = int(input("Número de arestas: "))
vertice = int(input("Numero de vértices: "))

if face == 0:
    face = aresta + 2 - vertice
    print("\nO número de faces é ", face)
if vertice == 0:
    vertice = aresta + 2 - face
    print("\nO número de vértices é {}".format(vertice))
if aresta == 0:
    aresta = vertice + face - 2
    print("\nO número de arestas é {}".format(aresta))