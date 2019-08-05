# MCOC-Proyecto-0



Introducción
==============

  Bajo pérdida de significancia se entiende numéricamente la pérdida de exactitud en la resta de valores casi exactamente iguales, vale decir la perdida de dígitos en números muy cercanos a cero debido al truncamiento de estos. Esto puede generar errores importantes en cálculos que implican números muy cercanos a cero.
  Siendo un error que viene en la naturaleza de los computadores, al ser capaces de procesar una cantidad finita de dígitos, existen diversas formas de burlar este problema, mejorando significativamente el error como evitando la sustracción de números casi idénticos.

Perdida de Significancia en Algoritmo de Arquímedes para el cálculo del número de pi.
==============

  Arquímedes demostró que el perímetro de una circunferencia se relaciona con el diámetro de la misma forma que el área con el cuadrado del radio. Sin poder calcularlo completamente, dejó explicaciones de como se podría calcular utilizando un polígono inscrito y uno transcrito mejorando la exactitud mediante el aumento de secciones de estos. Él llegó a calcular hasta un polígono de 96 lados, dejando una de las inecuaciones más antiguas conocidas, con 3,140845... < π < 3,1428571...
  Hoy, por medios computacionales, se puede calcular con mucha mayor exactitud llegando a errores minimos, entmínimoso la geometría básica del problema: 
https://github.com/jrsharmanUandes/MCOC-Proyecto-0/blob/master/Calculo%20de%20Pi.png

donde s_n = AB es un lado de una figura inscrita en un círculo unitario, MA = MB = MC = 1
con esto para el duangulo s_2 = 2, para un triangulo s_3 = raiz(3), para un cuadrado s_4 = raiz(2) o para un hexágono s_6 = 1
También se utiliza s_2n = AC que sería el lado de una figura de doble cantidad de lados y ρ_n = MS se calcula con la doble utilización del teorema de Pitagoras, AM^2 = MS^2 + AS^2, 1 = ρ_n^2+s_n^2/4 equivalente a ρ_n = raiz(1-s_n^2/4) y de la misma forma se obtiene a partir de AC^2 = AS^2 + SC^2, S_2n = raiz(2-2*raiz(1-s_n^2/4))

  Con estas cuatro fórmulas se puede comenzar a calcular los largos de los lados y el perímetro de polígonos inscritos e ir tendiendo al número π. Lamentablemente en la práctica esto no resulta del todo, la primera tabla de resultados muestra la tendencia partiendo por un polígono de n = 2 lados con una distancia de 1 - ρ_n de la mitad de un lado al borde del circulo. Tomando S_n = A'B' = s_n/ρ_n como la medida del lado del polígono transcrito, su perímetro A_n = n*S_n/2 debería converger con el perímetro a_n = n*s_n*ρ_n/2 del polígono inscrito. 
  
  Siendo esto calculado en python con aproximadamente 18 decimales lo que induce a errores de significancia, se puede obtar por evitar la resta haciendo un cambio d variable por medio de una suma por su diferencia donde a^2+b^2 = (a+b)*(a-b) --> a-b = (a^2-b^2)/(a+b) con a = 2 y b = 2*raiz(1-s_n^2/4) con esto s_2n = raiz(2-2*raiz(1-s_n^2/4)) = raiz(1/2*s_n^2/(1+raiz(1-s_n^2/4))). Esto evitará problemas posteriores.


Resultados
==============

Por medio de la explicación anterior se obtienen los siguientes resultados, utilizando el método sin modificar entregado por Arquímedes:

			  n					          1-ρ_n					           s_n					           S_n 					           a_n				           A_n 
2       		1.0     				        2       				        inf     				        0.0     				        inf
4       		0.29289321881345254    	1.4142135623730951     	2.0000000000000004     	2.0     				        4.000000000000001
8       		0.07612046748871326    	0.7653668647301797     	0.8284271247461903     	2.8284271247461907     	3.313708498984761
16      		0.01921471959676957    	0.3901806440322566     	0.39782473475931607    	3.0614674589207187     	3.1825978780745285
32      		0.004815273327803071   	0.1960342806591213     	0.19698280671432858    	3.1214451522580537     	3.1517249074292573
64      		0.001204543794827595   	0.0981353486548356     	0.09825369953893408    	3.1365484905459255     	3.1441183852458905
128     		0.00030118130379575003 	0.049082457045824326   	0.04909724421785064    	3.140331156954737      	3.142223629942441
256     		7.529816085549701e-05  	0.024543076571438636   	0.024544924759131337   	3.141277250932617      	3.141750369168811
512     		1.882471739889091e-05  	0.012271769298312042   	0.012272000315249896   	3.1415138011450923     	3.1416320807039733
1024    		4.70619042380882e-06   	0.006135913525937424   	0.006135942402850801   	3.1415729403698927     	3.14160251025961
2048    		1.1765482981207498e-06 	0.0030679603725631203  	0.0030679639821709222  	3.141587725270595      	3.1415951177430244
4096    		2.9413711777337426e-07 	0.0015339806375054086  	0.0015339810887061848  	3.141591421552159      	3.1415932696702664
8192    		7.353428210787882e-08  	0.0007669903751330577  	0.0007669904315331485  	3.1415923455302495     	3.141592807559776
16384   		1.8383570776769886e-08 	0.00038349519451455667 	0.00038349520156456785 	3.1415925757095575     	3.14159269121694
32768   		4.595892666436896e-09  	0.00019174759856003352 	0.00019174759944128492 	3.1415926403691667     	3.141592669246012
65536   		1.1489731388536484e-09 	9.58737989905156e-05   	9.587379910067202e-05  	3.14159264171161       	3.141592648930821
131072  		2.8724334022456333e-10 	4.793689891625549e-05  	4.7936898930025045e-05 	3.141592606473318      	3.1415926082781214
262144  		7.181089056729206e-11  	2.3968451774136908e-05 	2.3968451775858102e-05 	3.1415929107140723     	3.141592911165273
524288  		1.795275039739863e-11  	1.198423051908566e-05  	1.198423051930081e-05  	3.141594125138791      	3.1415941252515913
1048576  		4.488187599349658e-12  	5.992119891557349e-06  	5.9921198915842435e-06 	3.1415965536907193     	3.14159655371892
2097152  		1.1221024109886457e-12 	2.9960599457786747e-06 	2.9960599457820366e-06 	3.1415965537012944     	3.141596553708345
4194304  		2.8055335832277706e-13 	1.4980670285328662e-06 	1.4980670285332866e-06 	3.141674265020876      	3.141674265022639
8388608  		7.016609515630989e-14  	7.490705685351375e-07  	7.490705685351901e-07  	3.1418296818889813     	3.141829681889422
16777216 		1.7541523789077473e-14 	3.746093836419742e-07  	3.7460938364198075e-07 	3.1424512724940787     	3.142451272494189
33554432 		4.440892098500626e-15	  1.873046918209871e-07  	1.8730469182098791e-07 	3.14245127249412       	3.1424512724941476
67108864 		1.1102230246251565e-15	9.424321830774485e-08  	9.424321830774495e-08  	3.162277660168376      	3.162277660168383
134217728		3.3306690738754696e-16	4.712160915387242e-08  	4.7121609153872436e-08 	3.1622776601683786     	3.1622776601683804
268435456		1.1102230246251565e-16	2.5809568279517847e-08 	2.580956827951785e-08  	3.464101615137754      	3.464101615137755
536870912		0.0 					          1.4901161193847656e-08 	1.4901161193847656e-08	4.0 					          4.0

Acá se puede reconocer claramente en un comienzo la convergencia a π, pero tras alcanzar un poligono de 32768 caras, la sustracción de 2 y 2*raiz(1-s_n^2/4) alcanzan casi el mismo valor y aquí el resultado empieza a acumular error (2-2,000...000xx = 0). Como en muchos casos, como en este, esto se puede evitar, evitando esta sustracción, como descrito anteriormente. con esto se obtienen los siguientes resultados:

			  n					          1-ρ_n					           s_n					           S_n 					           a_n				           A_n 
2      			1.0     				        2       				        inf     				        0.0     				        inf
4      			0.29289321881345254     1.4142135623730951      2.0000000000000004      2.0     				        4.000000000000001
8      			0.07612046748871326     0.7653668647301797      0.8284271247461903      2.8284271247461907      3.313708498984761
16     			0.01921471959676957     0.3901806440322566      0.39782473475931607     3.0614674589207187      3.1825978780745285
32     			0.004815273327803071    0.19603428065912124     0.19698280671432852     3.121445152258053       3.1517249074292564
64     			0.001204543794827595    0.09813534865483604     0.09825369953893452     3.1365484905459398      3.1441183852459047
128    			0.00030118130379575003  0.04908245704582458     0.049097244217850895    3.1403311569547534      3.1422236299424573
256    			7.529816085549701e-05   0.024543076571439854    0.024544924759132555    3.141277250932773       3.141750369168967
512    			1.882471739889091e-05   0.012271769298308952    0.012272000315246806    3.1415138011443013      3.1416320807031823
1024   			4.70619042380882e-06    0.006135913525931953    0.00613594240284533     3.141572940367092       3.141602510256809
2048   			1.1765482981207498e-06  0.0030679603725695314   0.0030679639821773333   3.14158772527716        3.1415951177495893
4096   			2.9413711777337426e-07  0.0015339806374854092   0.0015339810886861854   3.1415914215112         3.1415932696293076
8192   			7.353428210787882e-08   0.0007669903751427912   0.000766990431542882    3.141592345570118       3.1415928075996447
16384  			1.8383570776769886e-08  0.00038349519462140664  0.0003834952016714178   3.1415925765848725      3.141592692092255
32768  			4.595892666436896e-09   0.0001917475981919547   0.0001917475990732061   3.141592634338563       3.1415926632154085
65536  			1.1489732498759508e-09  9.587379920613376e-05   9.58737993162902e-05    3.141592648776985       3.141592655996197
131072 			2.8724334022456333e-10  4.793689961683644e-05   4.7936899630605996e-05  3.141592652386591       3.1415926541913946
262144 			7.181089056729206e-11   2.3968449810139414e-05  2.396844981186061e-05   3.141592653288993       3.1415926537401937
524288 			1.795275039739863e-11   1.1984224905284857e-05  1.1984224905500007e-05  3.1415926535145933      3.1415926536273937
1048576     4.488187599349658e-12   5.9921124526693225e-06  5.992112452696217e-06   3.1415926535709935      3.141592653599194
2097152     1.1221024109886457e-12  2.996056226338023e-06   2.996056226341385e-06   3.1415926535850938      3.141592653592144
4194304     2.8055335832277706e-13  1.498028113169432e-06   1.4980281131698522e-06  3.141592653588619       3.141592653590382
8388608     7.016609515630989e-14   7.490140565847686e-07   7.490140565848211e-07   3.141592653589501       3.1415926535899414
16777216    1.7541523789077473e-14  3.7450702829239085e-07  3.745070282923974e-07   3.141592653589721       3.1415926535898313
33554432    4.440892098500626e-15   1.8725351414619625e-07  1.8725351414619707e-07  3.1415926535897762      3.1415926535898038
67108864    1.1102230246251565e-15  9.362675707309823e-08   9.362675707309834e-08   3.14159265358979        3.141592653589797
134217728   3.3306690738754696e-16  4.681337853654913e-08   4.681337853654914e-08   3.1415926535897936      3.1415926535897953
268435456   1.1102230246251565e-16  2.3406689268274567e-08  2.340668926827457e-08   3.1415926535897944      3.1415926535897953
536870912   0.0     				        1.1703344634137284e-08  1.1703344634137284e-08  3.141592653589795       3.141592653589795       
        
De esta forma, ya con el polígono de 268435456 lados se alcanza una exactitud de 18 decimales, la aproximación entrega 0,0 en la segúnda columna.

En el siguiente gráfico se puede observar la comparación de la tendencia hacia pi sin conciderar el ajuste y como el error se acumula y tambien haciendo el ajuste para evitar la perdida por significancia.
https://github.com/jrsharmanUandes/MCOC-Proyecto-0/blob/master/loss-of-significance.png
