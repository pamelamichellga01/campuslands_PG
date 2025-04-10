Proceso E_13_Sumar_hasta_que_se_ingrese_0
	
	Definir i, suma Como Entero;
	
	suma<-0;
	
	Repetir
		Escribir "Digite un numero";
		Leer i;
		
		suma<-suma+i;
	Hasta Que i==0
	
	Escribir "La suma de los numeros digitados es: ", suma; 
	
FinProceso
