SubProceso variable_de_retorno <- ValidarPIN ( intentos )
	
FinSubProceso

SubProceso MostrarMenuDeUsuario
	Escribir "Menú";
	Escribir "1. Consultar datos";
	Escribir "2. Cambiar PIN";
	Escribir "3. Salir";
FinSubProceso

SubProceso variable_de_retorno <-CambiarPIN ( Argumentos )
	
FinSubProceso

Proceso Control_de_Acceso_con_PIN_2
	
	Definir PIN,PIN2 Como Entero;
	
	PIN<-1234;
	
	Escribir "Digite PIN";
	Leer PIN2;
	
	Si PIN2 Entonces
		acciones_por_verdadero
	SiNo
		acciones_por_falso
	FinSi
	
	
FinProceso
