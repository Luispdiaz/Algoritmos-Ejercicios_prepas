# A continuación se te presentan 5 códigos postales escritos en código Morse, todos almacenados en un mismo string y separados por “*”.
# Tu labor consiste en descifrar cuáles son los números que componen cada código.
# codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____.*"

bienvenida = "Bienvenido al descifrador de codigo morse"
bienvenida = bienvenida.center(50,"*")
print(bienvenida)
codigospostales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____."
codigospostales = codigospostales.replace(".____","1").replace("..___","2").replace("...__","3").replace("...._","4").replace(".....","5").replace("_....","6").replace("__...","7").replace("___..","8").replace("____.","9").replace("_____","0").replace("*","\n")
print(codigospostales)