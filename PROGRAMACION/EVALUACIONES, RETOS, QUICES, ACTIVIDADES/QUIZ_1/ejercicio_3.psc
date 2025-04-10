Proceso sin_titulo
	Definir s,t,i,j Como Entero;
	s<-0;
	t<-0;
	Para i<-0 Hasta 1 Con Paso 1 Hacer
		Para j<-0 Hasta 1 Con Paso 1 Hacer
			s<-s+1;
			Si i<j Entonces
				t<-t+1;
			FinSi
		FinPara
		Escribir "t",t;
		Escribir "s",s;
	FinPara
FinProceso
