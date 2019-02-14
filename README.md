# Filter_Stage
## Instalación
Para la instalación del Workbench deberemos acceder a la carpeta de instalación de FreeCAD. Por defecto sera:

	C:\Program Files\FreeCAD 0.17

Deberemos acceder a la carpeta Mod y dentro de esta crear una carpeta. 
En este caso la carpeta se llamará Filter_Stage.
Es importante que el nombre de esta carpeta viene fijado por los archivos principales del Workbench.
Si el nombre de la carpeta es distinto al nombre de los archivos no lo veremos en FreeCAD.

Tras crear la carpeta debemos introducir los archivos principales del Workbench:

	Filter_StageGui.py
	Init.py
	InitGui.py
Estos tres archivos contienen el código para generar el Workbench.

Ahora deberemos introducir los archivos necesarios para ejecutar el workbench. Para ello
debemos mirar los *import* de los archivos.
En *Filter_StageGui.py* se realiza el *import* de *filter_stage_fun.py*, por tanto
debemos añadir a nuestra carpeta dicho archivo.

Si abrimos *filter_stage_fun.py* veremos nuevos *imports*. Estos archivos se encuentran en la 
carpeta *comps* y son:

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

Una vez tengamos estos archivos en nuestra carpeta sólo queda añadir la carpeta *icons* a la misma para poder ver en **FreeCAD** el Workbench

## Funcionamiento del Workbench
En este Workbench tendremos varios botones, cada uno con el fin de cumplir una finalidad.