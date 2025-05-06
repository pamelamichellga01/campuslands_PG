SubProceso menu <- MostrarMenu ( opcion )
	Escribir "Calculadora Campus";
	Escribir "1. Suma";
	Escribir "2. Resta";
	Escribir "3. Multiplicacion";
	Escribir "4. Division";
	
	Leer opcion;
FinSubProceso

SubProceso cociente <- division ( num1,num2 )
	si num2 == 0 Entonces
		Escribir "No es posible dividir entre";
	FinSi
FinSubProceso

SubProceso producto <- multiplicacion ( num1,num2 )
	producto<-num1*num2;
FinSubProceso

SubProceso diferencia <- resta ( num1,num2 )
	resultado<- num1-num2;
FinSubProceso

SubProceso resultado <- suma ( num1, num2 )
	resultado<- num1+num2;
FinSubProceso



Proceso sin_titulo
	Definir n1,n2,resultado, opcion Como Entero;
	
	Escribir "Ingrese pirmer numero";
	Leer n1;
	
	Escribir "Ingrese segundo numero";
	Leer n1;
	
	
FinProceso
