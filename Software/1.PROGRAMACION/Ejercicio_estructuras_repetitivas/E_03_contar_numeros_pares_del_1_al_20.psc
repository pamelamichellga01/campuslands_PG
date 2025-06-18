Proceso E_03_contar_numeros_pares_del_1_al_20
	
	Definir i,count Como Entero;
	count<-0;
	
	Para i<-1 Hasta 20 Con Paso 1 Hacer
		
		Si i%2=0 Entonces
			count<-count+1;
		FinSi
		
	FinPara
	
	Escribir "La cantidad de numeros pares en ese rango son ", count;
	
FinProceso
