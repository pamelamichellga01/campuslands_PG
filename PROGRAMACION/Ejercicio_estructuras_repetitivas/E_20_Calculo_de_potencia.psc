Proceso E_20_Calculo_de_potencia
	
	Definir base, exponente, resultado, i, cont Como Entero;
	
	resultado <- 1;
	
	Escribir "Escriba la base";
	Leer base;
	
	Escribir "Escribir el exponente:";
	Leer exponente;
	
	Para i<-1 Hasta exponente Con Paso 1 Hacer
		resultado <- resultado*base;
		Escribir resultado;
	FinPara
	
	Escribir "El resultado de ", base," ^ ",exponente, " es ", resultado;
	
FinProceso
