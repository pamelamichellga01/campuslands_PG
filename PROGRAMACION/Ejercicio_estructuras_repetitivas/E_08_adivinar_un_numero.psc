Proceso E_08_adivinar_un_numero
	Definir i,n,x Como Entero;
	Escribir 
	
	x<- Azar(1000) + 1;
	i<-0;
	
	Repetir
		Escribir "Digite un numero del 1 al 10 : ";
		Leer n;
		
		Si n>=1 y n<=10 Entonces
			Si n=x Entonces
				Escribir "Adivinaste, el numero es correcto";
			siNo 
				Escribir "Sigue intntando";
			FinSi
		FinSi
		
		i<-i+1;
	Hasta Que i>=3
FinProceso
