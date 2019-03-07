# Filter Stage
---
---
Select your lenguage:
- [English](index)
- [Spanish](índice)

---
---
## Inglés
This is the Workbench to do the stage of the optical filter.
![imagen](img/filter_stage.jpg)

### Index
-[Intall](install)
-[How it's work](how-it's-work)
-[Working on](working-on)

#### Install
Before the installation of the workbench, it is necessary have installed FreeCAD.  You can download in [this page][dirFreeCADing]

[dirFreeCADing]: https://www.freecadweb.org/downloads.php

Also, we need to download the workbench files that we can find [here][dirFolder] 

[dirFolder]: https://github.com/davidmubernal/Filter_Stage/tree/master/src

For the installation of the workbench we need to go in the installation folder of FreeCAD. The default folder is:

	C:\Program Files\FreeCAD 0.17

We have to enter in the folder *Mod* and **make a new folder**.
**The name of the new folder is set in the main file of the workbench (InitGui.py)**.
If the name of the folder is not the set name the workbench will not show.  
In this case the name of the folder is **Filter_Stage**.

When the folder is made we need to bring in the folder the main files of the workbench that we had downloaded previously:

	Filter_StageGui.py
	Init.py
	InitGui.py
	
This three files have the code to generate the workbench.

Also, we need to bring in the folder the next files what makes the workbench work. These files are in the folder *comps* into the folder we have downloaded before.

	beltcl.py
	comps.py
	fc_clss.py
	fcfun.py
	kcomp.py
	kcomp-optic.py
	kpart.py
	partgroup.py
	parts.py
	partset.py
	shp_clss.py

It is necessary to add the functions where the piece is generated. These files are [here][dirFunction].

[dirFunction]:  https://github.com/davidmubernal/Filter_Stage/tree/master/src/func

	filter_holder_clss.py
    filter_stage_fun.py
	tensioner_clss.py

When these files are in the folder it is necessary to add the icons. To do that bring in the folde Filter_Stage the folder *icons*.

If all these steps was followed now we have something similar to this:

![imagen](img/carpeta.jpg)

---
---
#### How it work
This workbench has two buttons  
![imagen](img/botones.jpg)

1. The first button creates the filter stage how it is designed.  
![imagen](img/filter_stage.jpg)

---
2. The second button enables setting the values of 5 variable :

  - Move distance.    
![imagen](img/filter_stage_top.jpg)

  - Base width: is limited to the aluminum profile size (10mm, 15mm, 20mm, 30mm and 40mm).    
![image](img/tensioner_holder_ex_3profiles_side.jpg)

  - Tensioner stroke.  
![imagen](img/idler_tensioner_stroke_draw.png)

  - Wall thickness.    
![imagen](img/idler_tensioner_wallthick.jpg)

  - Nut type: limit to set metric (M3, M4, M5 and M6).  
![imagen](img/nut_metric.jpg)  
![imagen](img/nut_metric_2.jpg)

---
---
#### Working on
---
Currently working:
- New buttons to generate the different pieces of the project.

---
---
## Español   
Este es el Workbench para la generación de la plataforma del filtro óptico.

![imagen](img/filter_stage.jpg)

### Índice
- [Instalación](#instalaci%C3%B3n)
- [Funcionamiento del Workbench](#funcionamiento-del-workbench)
- [Trabajando en:](#trabajando-en)
---
#### Instalación
Será necesario tener instalado el programa *FreeCAD* el cual se puede descargar desde [este enlace][dirFreeCADesp]

[dirFreeCADesp]: https://www.freecadweb.org/downloads.php


También será necesario descargar los archivos que se encuentran [aquí][dirCarpeta].

[dirCarpeta]: https://github.com/davidmubernal/Filter_Stage/tree/master/src

Para la instalación del Workbench deberemos acceder a la carpeta de instalación de *FreeCAD*. Por defecto sera:

	C:\Program Files\FreeCAD 0.17

Deberemos acceder a la carpeta *Mod* y dentro de esta **crear una carpeta**.  
Es importante que **el nombre de esta carpeta viene fijado dentro del archivo principal del Workbench llamado _InitGui.py_**.
Si el nombre de la carpeta es distinto al nombre que está especificado en el archivo no veremos el Workbench en *FreeCAD*.  
En este caso la carpeta se llamará **Filter_Stage**.

Tras crear la carpeta debemos introducir en ella los siguientes archivos principales del Workbench que hemos descargado anteriormente:

	Filter_StageGui.py
	Init.py
	InitGui.py

Estos tres archivos contienen el código para generar el Workbench.

También deberemos introducir los siguientes archivos necesarios para que funcione el *Workbench* que se encuentran en la carpeta *comps* dentro de la carpeta descargada inicialmente y son:

	beltcl.py
	comps.py
	fc_clss.py
	fcfun.py
	kcomp.py
	kcomp-optic.py
	kpart.py
	partgroup.py
	parts.py
	partset.py
	shp_clss.py

Queda añadir las funciones dónde se genera la pieza y se encuentran [aquí][dirfun].

[dirfun]: https://github.com/davidmubernal/Filter_Stage/tree/master/src/func

	filter_holder_clss.py
    filter_stage_fun.py
	tensioner_clss.py

Una vez tengamos estos archivos en nuestra carpeta sólo queda crear una carpeta *icons* e introducir los [iconos][dir3] a la misma para poder ver en **FreeCAD** el Workbench.

[dir3]: https://github.com/davidmubernal/Filter_Stage/tree/master/icons

Si hemos seguido todos los pasos de manera correcta deberíamos tener en la carpeta Filter_Stage lo siguiente:

![imagen](img/carpeta.jpg)

---
---
#### Funcionamiento del Workbench
En este Workbench tendremos varios botones, cada uno con el fin de cumplir una finalidad.  
  ![imagen](img/botones.jpg)
  
1. El primer botón realiza el filter stage según fue diseñado.  
![imagen](img/filter_stage.jpg)

---
2. El segundo botón nos permite modificar las siguientes 5 variables:

  - Distancia de movimiento.  
![imagen](img/filter_stage_top.jpg)

  - Ancho de la base: limitado al perfil de aluminio (10mm, 15mm, 20mm, 30mm y 40mm).  
![image](img/tensioner_holder_ex_3profiles_side.jpg)

  - Tensioner stroke.  
![imagen](img/idler_tensioner_stroke_draw.png)

  - Espesor de la pared.  
![imagen](img/idler_tensioner_wallthick.jpg)

  - Tipo de tuerca: limitado a las métricas (M3, M4, M5 y M6).  
![imagen](img/nut_metric.jpg)  
![imagen](img/nut_metric_2.jpg)

---
---
#### Trabajando en:
Actualmente se trabaja en:
- *Botones adicionales para la realización de las piezas principales del proyecto*