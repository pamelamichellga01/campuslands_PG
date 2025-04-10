SubProceso resultado<- MostrarResultado ( promedio )
	Definir resultado Como Logico;
	Si promedio>=12 Entonces
		resultado<- Verdadero;
	SiNo
		resultado<- falso;
	Fin Si	
FinSubProceso
//******************************************************************************************************
SubProceso promedio <- CalcularPromedio ( cantNotas,totalNotas)
	Definir promedio Como Real;
	
	Si totalNotas>0 Entonces
		promedio<-cantNotas/totalNotas;
	SiNo
		promedio<-0;
	Fin Si
	
FinSubProceso
//******************************************************************************************************
SubProceso notas <- IngresarCalificacion ( notas )
	
	Escribir "Ingrese su nota 0.1-20 (0 para salir)";
	Leer notas;
	
FinSubProceso
//******************************************************************************************************
Proceso Sistema_de_Calificaciones_Ej1
	Definir cont Como Entero;
	Definir nota_f,promedio_f,suma,resultado Como Real;
	Definir resultado_f Como Logico;
	
	cont<--1;
	
	Repetir
		resultado<-IngresarCalificacion(nota_f);
		Si resultado>=0.1 y resultado<=20 Entonces
			notas<-n;
			Escribir "La nota es valida";
			Escribir "";
		SiNo 
			Si resultado == 0 Entonces
				resultado<-0;
			SiNo
				Escribir "La nota no es valida";
				Escribir "";
				resultado<-IngresarCalificacion(nota_f);
			Fin Si
		Fin Si
		suma<-suma+resultado;
		cont<-cont+1;
	Hasta Que resultado==0
	
	//Escribir suma;
	//Escribir cont;
	
	promedio_f<-CalcularPromedio (suma,cont);
	//Escribir promedio_f;
	
	resultado_f<-MostrarResultado(promedio_f);
	
	Si resultado_f Entonces
		Escribir "El estudante aprobo con ",promedio_f, " de promedio";
	SiNo
		Escribir "El estudante reprobo con ",promedio_f, " de promedio";
	Fin Si

FinProceso
