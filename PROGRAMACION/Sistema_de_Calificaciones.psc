SubProceso resultadoooo <- MostrarResultado ( Argumentos )
	
FinSubProceso

SubProceso promedio <- CalcularPromedio ( Argumentos )
	
FinSubProceso

SubProceso notas <- IngresarCalificacion ( n )
	Definir nota Como Real;
	
	Escribir "Ingrese su nota";
	Leer n;
	
FinSubProceso


Proceso Sistema_de_Calificaciones
	
	Definir nota_f,promedio,suma,cont, resultado Como Real;
	cont<-0;
	nota_f<-0;
	suma<-0;
	
	Repetir
		resultado<-IngresarCalificacion(nota_f);
		Si nota_f>=0 y nota_f<=20 Entonces
			suma<-suma+nota_f;
			cont<-cont+1;
			Escribir "La Nota es valida";
		SiNo
			Escribir "La nota no es valida";
		FinSi
	Hasta Que nota_f==0
FinProceso
