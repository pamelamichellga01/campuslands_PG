SubProceso areaTriangulo <- CalcularArea ( base, altura )
	Definir areaTriangulo Como Entero;
	areaTriangulo <- (base*ALTURA)/2;
FinSubProceso

Proceso sin_titulo
	Definir base, altura, area Como Entero;
	
	Escribir "Escriba la base";
	Leer base;
	
	Escribir "Escriba la altura";
	Leer altura;
	
	area <- CalcularArea(base,altura);
	Escribir area;
	
FinProceso
