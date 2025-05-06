Proceso E_06_sumar_numeros_ingresados_por_el_usuario
	
	Definir i,n, suma Como Entero;
	suma<-0;
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "Digite numero que sera sumado: ";
		Leer n;
		suma<-suma+n;
		
	FinPara
	
	Escribir "La suma de los numeros ingresados es : ", suma;
	
FinProceso
