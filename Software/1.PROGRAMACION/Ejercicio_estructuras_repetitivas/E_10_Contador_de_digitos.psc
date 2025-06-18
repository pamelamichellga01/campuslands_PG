Proceso E_10_Contador_de_digitos
	
	Definir i,long Como Entero;
	Definir n Como Caracter;
	
	Escribir "Digita un numero";
	Leer n;
	
	long<-Longitud(n);
	
	i<-0;
	
	Mientras i<=(long-1) Hacer
		i<-i+1;
	FinMientras
	
	Escribir "El numero tiene ",i," digitos";
	
	
FinProceso
