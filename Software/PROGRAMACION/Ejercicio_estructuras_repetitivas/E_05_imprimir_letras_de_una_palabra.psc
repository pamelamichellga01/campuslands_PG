Proceso E_05_imprimir_letras_de_una_palabra
	
	Definir i,long Como Entero;
	Definir palabra, letra Como Caracter;
	Leer palabra;
	
	long<-Longitud(palabra);
	
	Para i<-0 Hasta long Con Paso 1 Hacer
		letra<- Subcadena(palabra,i,i);
		Escribir letra;
	FinPara
	
	
FinProceso
