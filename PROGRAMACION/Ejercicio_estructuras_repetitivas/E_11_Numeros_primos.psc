Proceso E_11_Numeros_primos
	
	Definir i,n,r,cont Como Entero;
	
	Escribir "Digite un numero";
	Leer n;
	
	cont<-0;
	
	Para i<-1 Hasta n Con Paso 1 Hacer
		r<-n%i;
		Si r==0 Entonces
			cont<-cont+1;
		SiNo
			cont<-cont+0;
		FinSi
	FinPara
	
	Si cont>2 Entonces
		Escribir "EL numero ", n," no es Primo";
	SiNo
		Escribir "EL numero ", n," es Primo";
	FinSi
	
FinProceso
