Proceso E_07_factorial_de_un_numero
	
	Definir n,i,f Como Entero;
	
	Escribir "Ingrese un numero : ";
	Leer n;
	i<-0;
	f<-1;

	Mientras (n-1)>=i Hacer
		i<-i+1;
		f<-f*i;
	FinMientras
	
	Escribir "El resultado del factorial de ",n," es : ", f; 
FinProceso
