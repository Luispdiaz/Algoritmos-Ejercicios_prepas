valores_x = [2,5,9,13]
result = []
for x in valores_x:
    y = 2**x 
    coordenadas = (x,y)
    result.append(coordenadas)
print(result)
coord2 = [(4,1),(25,11),(8,5),(16,8),(45,77),(10,10),(4,1),(34,2),(25,11),(8,5)]
coord2 = set(coord2)
coord2 = sorted(coord2)
print("X       Y")
print("---------")
for x in coord2:
    print(f"{x[0]}      {x[1]}")
