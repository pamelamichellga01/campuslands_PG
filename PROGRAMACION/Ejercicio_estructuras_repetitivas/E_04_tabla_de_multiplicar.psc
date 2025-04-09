Proceso E_04_tabla_de_multiplicar
	
	Definir i,n,mult Como Entero;
	
	Escribir "digite un numero del 1 al 10";
	Leer n;
	
	Si n>=1 y n <= 10 Entonces
		Para i<-1 Hasta 10 Con Paso 1 Hacer
			mult<- n*i;
			Escribir n," X ",i," = ",mult;
		FinPara
	FinSi
	
	
FinProceso
