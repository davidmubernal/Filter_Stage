# Filter_Stage
## Índice:
Este es el Workbench para la generación de la plataforma del filtro óptico.

- [Filter_Stage](#filterstage)
	- [Índice:](#%C3%ADndice)
	- [Instalación](#instalaci%C3%B3n)
	- [Funcionamiento del Workbench](#funcionamiento-del-workbench)
	- [Trabajando en:](#trabajando-en)
## Instalación
Será necesario tener instalado el programa *FreeCAD*, se puede descargar en todos los sistemas operativos seleccionando el tuyo desde [este enlace][dir]

[dir]: https://www.freecadweb.org/downloads.php


También será necesario descargar los archivos que se encuentran [aquí][dir2].

[dir2]: https://github.com/davidmubernal/Filter_Stage/tree/master/src

Para la instalación del Workbench deberemos acceder a la carpeta de instalación de *FreeCAD*. Por defecto sera:

	C:\Program Files\FreeCAD 0.17


Deberemos acceder a la carpeta *Mod* y dentro de esta **crear una carpeta**.  
Es importante que **el nombre de esta carpeta viene fijado dentro del archivo principal del Workbench llamado _InitGui.py_**.
Si el nombre de la carpeta es distinto al nombre que está especificado en el archivo no veremos el Workbench en *FreeCAD*.  
En este caso la carpeta se llamará **Filter_Stage**.

Tras crear la carpeta debemos introducir en ella los siguientes archivos principales del Workbench:

	filter_stage_fun.py
	Filter_StageGui.py
	Init.py
	InitGui.py

Estos tres archivos contienen el código para generar el Workbench.

También deberemos introducir los siguientes archivos necesarios para que funcione el *Workbench* que se encuentran en la carpeta *comps* y son:

	beltcl.py
	comps.py
	fc_clss.py
	fcfun.py
  	filter_holder_clss.py
	kcomp.py
	kcomp-optic.py
	kpart.py
	partgroup.py
	parts.py
	partset.py
	shp_clss.py
	tensioner_clss.py

Una vez tengamos estos archivos en nuestra carpeta sólo queda añadir la carpeta *icons* a la misma para poder ver en **FreeCAD** el Workbench.

Si hemos seguido todos los pasos de manera correcta deberíamos tener en la carpeta Filter_Stage lo siguiente:

![imagen](img/carpeta.jpg)

## Funcionamiento del Workbench
En este Workbench tendremos varios botones, cada uno con el fin de cumplir una finalidad.
1. El primer botón realiza el filter stage según se diseñó.

  ![imagen](img/Filter_Stage_cmd.png)

2. El segundo botón nos permite modificar las siguientes 5 variables:

  ![imagen](img/Filter_Stage_Mod_cmd.png)

  - Tipo de rosca: limitado al conjunto de roscas definidas en el programa.
  - Altura de la correa.
  - Tensioner stroke.
  - Ancho de la base: limitado al tamaño del perfil de aluminio definido en el programa.
  - Espesor de la pared.

## Trabajando en:
Actualmente se trabrabaja en:
- *Botones adicionales para la realización de las piezas principales del proyecto*
- *Mejora del segundo botón limitando las opciones de las roscas a las definidas*
