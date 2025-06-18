SubProceso saldo_rta <- Retirar ( saldo_retirar,saldo_depositado,saldo)
	Definir saldo_rta Como Real;
	Si saldo_depositado>saldo_retirar Entonces
		saldo_rta<-saldo-saldo_retirar;
		Escribir "Retiro exitoso. Nuevo saldo: $",saldo_rta;
	SiNo
		Escribir "Error: fondos insuficientes: $",saldo;
	FinSi
FinSubProceso

SubProceso saldo_rta <- Depositar ( saldo )
	Definir saldo_rta Como Real;
	saldo_rta<-0;
	Si saldo>0 Entonces
		saldo_rta <-saldo_rta + saldo;
	SiNo
		Escribir "Esta cantidad no puede ser depositada";
	FinSi
	
FinSubProceso

SubProceso saldo_rta<-ConsultarSaldo(saldo)
	Definir saldo_rta Como Real;
	Escribir "Su saldo es de ",saldo;
	
FinSubProceso

SubProceso Menu
	
	Escribir "--------------------------------";
	Escribir "CAJERO AUTOMATICO";
	Escribir "--------------------------------";
	Escribir "1. Consiltar saldo";
	Escribir "2. Depositar dinero";
	Escribir "3. Retirar dinero";
	Escribir "4. salir (0)";
	Escribir "--------------------------------";
	
FinSubProceso

Proceso Cajero_Automatico
	
	Definir saldo, respuesta, saldo_depositar,saldo_retirar Como Real;
	Definir opcion Como Entero;
	
	saldo<-1000;
	
	Repetir
		
		Menu;
		
		Escribir "Seleccione una opcion: ";
		Leer opcion;
		
		Si opcion<>0 Entonces
			Segun opcion Hacer
				opcion 1:
					respuesta<-ConsultarSaldo(saldo);
				opcion 2:
					Escribir "Ingrese el monto a depositar ";
					Leer saldo_depositar;
					respuesta<-Depositar(saldo_depositar);
					saldo<-saldo+respuesta;
					Escribir "Deposito exitoso. Nuevo saldo: $", saldo;
				opcion 3:
					Escribir "Ingrese el monto a retirar";
					Leer saldo_retirar;
					respuesta<-Retirar(saldo_retirar,saldo_depositar,saldo);
					saldo<-saldo+respuesta;
				De Otro Modo:
					Escribir "Opcion incorrecat";
			FinSegun
		FinSi
	Hasta Que opcion==0
	
	Escribir "Gracias por usar el cajero. !Hasta luego¡.";
	
	
	
FinProceso
