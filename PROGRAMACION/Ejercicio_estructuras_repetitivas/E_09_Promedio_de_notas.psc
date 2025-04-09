Proceso E_09_Promedio_de_notas
	Definir i, n Como Entero;
	Definir promedio, notas, suma Como Real;
	suma <- 0;
	n <- 3;
	Para i<-1 Hasta n Con Paso 1 Hacer
		Escribir 'Escribir nota: ';
		Leer notas;
		suma <- suma+notas;
	FinPara
	promedio <- suma/n;
	Escribir 'El promedio de las ', n, 'notas es: ', promedio;
FinProceso
