SubProceso NewPIN<-CambiarPIN 
	Definir NewPIN Como Caracter;
	Escribir "Digite su nuevo pin";
	Leer NewPIN;
Fin SubProceso

SubProceso MostrarMenuDeUsuario
	Escribir "Menú";
	Escribir "1. Consultar datos";
	Escribir "2. Cambiar PIN";
	Escribir "3. Salir";
Fin SubProceso

SubProceso respuesta <- ValidarPIN ( intentos )
	Definir respuesta Como Entero;
	respuesta<-0;
	Si intentos ==4 Entonces
		Escribir "PIN correcto, se procede a incio se sesion.";
		respuesta<-3;
	SiNo
		Si intentos<>4 Entonces
				respuesta<-respuesta+1;
				Escribir "PIN incorrecto, Digita tu pin nuevamnete.";
				Escribir "Llevas ", respuesta, " Intentos";
		Fin Si
	Fin Si
	
	Si respuesta==3 Entonces
		Escribir "Cuenta bloqueada";
		respuesta<-3;
	FinSi
Fin SubProceso

Proceso Control_de_Acceso_con_PIN
	
	Definir i,long1,long2, cont, prueba,intento,respuesta, opcion Como Entero;
	Definir PIN,PINUsuario,num1,num2 Como Caracter;
	
	cont<-0;
	prueba<-0;
	PIN<-"1234";
	intento<-0;
	
	
	
	Repetir
		prueba<-0;
		Escribir "Ingrese su PIN";
		Leer PINUsuario;
		
		long<-Longitud(PIN);
		long2<-Longitud(PINUsuario);
		
		Si long2==4 Entonces
			Para i<-1 Hasta 4 Con Paso 1 Hacer
				num1<- Subcadena(PIN,i,i);
				num2<- Subcadena(PINUsuario,i,i);
				
				Escribir num1,num2;
				
				Si num1=num2 Entonces
					prueba<-prueba+1;
				SiNo
					prueba<-prueba+0;
				Fin Si
			FinPara
			Escribir "";
			Escribir prueba;
		SiNo
			Escribir "El numero de digitos de su PIN es incorrecto";
		Fin Si
		respuesta<-ValidarPIN ( prueba );
	Hasta Que respuesta==3
	
	Repetir
		
		MostrarMenuDeUsuario;
		Leer opcion;
		
		Si opcion <> 0 Entonces
			Segun opcion Hacer
				opcion 1:
					Escribir "Datos consultados";
				opcion 2:
					PIN<-CambiarPIN;
					Escribir "Su nuevo PIN es, ",PIN;
				De Otro Modo:
					Escribir "Opcion no valida";
			Fin Segun
		Fin Si
	Hasta Que opcion==0
	Escribir "PROGRAMA A FINALIZADO CON EXITO";
	
	
FinProceso
