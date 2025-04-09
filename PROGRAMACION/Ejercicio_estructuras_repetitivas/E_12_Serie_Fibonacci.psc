Proceso E_12_Serie_Fibonacci
	Definir a, n, b, c, i Como Entero;
	
	a<-0;
	b<-1;
	
	Escribir "Cuatos terminos de la serie desea escribir";
	Leer n;
	
	Escribir a;
	Escribir b;
	
	Para i<-1 Hasta n Hacer
		c<-a+b;
		Escribir c;
		
		a<-b;
		b<-c;
	FinPara
FinProceso
