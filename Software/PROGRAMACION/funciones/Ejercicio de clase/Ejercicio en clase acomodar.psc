SubProceso cociente <- division ( num1,num2 )
	Definir cociente Como Entero;
	si num2 == 0 Entonces
		Escribir "No es posible dividir entre";
	FinSi
FinSubProceso

SubProceso producto <- multiplicacion ( num1,num2 )
	Definir producto Como Entero;
	producto<-num1*num2;
FinSubProceso

SubProceso diferencia <- resta ( num1,num2 )
	Definir diferencia Como Entero;
	diferencia<- num1-num2;
FinSubProceso

SubProceso resultado <- suma ( num1, num2 )
	Definir resultado Como Entero;
	resultado<- num1+num2;
FinSubProceso

Proceso sin_titulo
	Definir n1,n2,resultado, opcion Como Entero;
	Repetir
		
		Escribir "Calculadora Campus";
		Escribir "1. Suma";
		Escribir "2. Resta";
		Escribir "3. Multiplicacion";
		Escribir "4. Division";
		Escribir "0. salir";
		
		Leer opcion;
		
		si opcion <> 0 Entonces
			
			Escribir "Ingrese pirmer numero";
			Leer n1;
			
			Escribir "Ingrese segundo numero";
			Leer n2;
			
			Segun opcion Hacer
				opcion 1:
					resultado<-suma(n1,n2);
					Escribir "El resultado de la operacion  es ", resultado;
					Escribir "";
				opcion 2:
					resultado<-resta(n1,n2);
					Escribir "El resultado de la operacion  es ", resultado;
					Escribir "";
				opcion 3:
					resultado<-multiplicacion(n1,n2);
					Escribir "El resultado de la operacion  es ", resultado;
					Escribir "";
				opcion 4:
					resultado<-division(n1,n2);
					si n2 <> 0 Entonces
						Escribir "El resultado de la operacion es ",resultado;
						Escribir "";
					SiNo
						Escribir "No se puede dividir ";
					FinSi
					
				De Otro Modo:
					Escribir "Opcion no valida";
			FinSegun
		FinSi
	
		Hasta Que opcion ==0
	
	Escribir "Saliendo de la calculadora...";
	
FinProceso