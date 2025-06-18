SubProceso fahrenheit <- ConvertirCelsiusAFahrenheit(celsius)
	Definir fahrenheit Como Real;
	
	fahrenheit<- (9/5)*celsius+32;
	
Fin SubProceso

SubProceso libras <- ConvertirKgALibras(kg)
	Definir libras Como Real;
	
	libras<-kg*(2.2046);
	
Fin SubProceso

SubProceso pies <-ConvertirMetrosAPies(metros)
	Definir pies Como Real;

	pies<-metros*(3.28);
	
Fin SubProceso

Proceso Menu_de_Conversión_de_Unidades
	
	Definir opcion Como Entero;
	Definir n,resultado Como Real;
	
	Repetir
		
		Escribir "Menú"; 
		Escribir "1.Metros a pies";
		Escribir "2.Kilogramos a libras"
		Escribir "3.Celsius a Fahrenheit"
		Escribir "4.Salir"
		Leer opcion;
		
		Si opcion<>0 Entonces
			
			Escribir "Digite el valor a convertir"
			Leer n;
			
			Segun opcion Hacer
				opcion 1:
					Si n>0 Entonces
						resultado<-ConvertirMetrosAPies(n);
						Escribir "El resultado de la operacion  es ", resultado," pies";
						Escribir "";
					SiNo
						Escribir "Valores negativos no estan permitidos"
					Fin Si
				opcion 2:
					Si n>0 Entonces
						resultado<-ConvertirKgALibras(n);
						Escribir "El resultado de la operacion  es ", resultado," libras";
						Escribir "";
					SiNo
						Escribir "Valores negativos no estan permitidos"
					Fin Si
				opcion 3:
					resultado<-ConvertirCelsiusAFahrenheit(n)
					Escribir "El resultado de la operacion  es ", resultado," libras";
					Escribir "";
				De Otro Modo:
			Fin Segun
		Fin Si
	Hasta Que opcion==0
	
	
	
FinProceso
