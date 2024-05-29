# Interfaz web - Batalla naval

## ¿Quién hizo esto? (Autores)

- Luis Pablo Goez.
- Mateo Molina.


## ¿Qué es y para qué es?

La aplicacion del juego de batalla naval ofrecen una experiencia digital del clásico juego de mesa, donde el objetivo es hundir todos los barcos del oponente en un tablero de 8x8 casillas. Más allá del entretenimiento, estas aplicaciones brindan beneficios como ejercitar la mente a través de la estrategia y el pensamiento crítico.


## Reglas del juego

1. **Preparación:**
   - El jugador coloca sus barcos en su tablero, tiene un total de 10 barcos que puede ubicar como desee.

2. **Turnos:**
   - El jugador se turna con la IA para adivinar las coordenadas en el tablero enemigo.
   - Si el disparo alcanza un barco enemigo, se marca como "hit" y la casilla se pinta de rojo.
   - Si el disparo no alcanza ningún barco, se marca como "miss"y la casilla se pinta de amarillo.

3. **Ganar:**
   - El primero en hundir todos los barcos enemigos gana.


## ¿Cómo lo hago funcionar?

### Prerequisitos
- **Editor de codigo fuente:** Asegúrate de tener instalado un editor de codigo funete en tu sistema. Te recomendamos Visual Studio Code puedes descargarlo e instalarlo desde el sitio oficial de Visual Studio Code: [Descargar VS Code](https://code.visualstudio.com/Download).
- **Python:** Debes tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde el sitio oficial de Python: [Descargar Python](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la casilla "Agregar Python al PATH".
- **Flask:** Debes instalar flask en tu sistema. Es posible decargarlo utilizando el comando **pip install flask** en la terminal de tu sistema.


## ¿Cómo lo hago funcionar?
Tener en cuenta: primeramente debe descargar el repositorio, para hacerlo ten en cuenta los siguientes pasos:
1. Instalada la aplicación Git. [Descargar Git](https://git-scm.com/download/win)
2. Copiar el link del repositorio. 
3. Entra a el escritorio de tu computadora, das click derecho y presiona la opción open git bash here.
4. En la consola de git bash escribe el comando "git clone" y pega el link del repositorio, recuerde que para pegar el link debes presionar click derecho y luego presiona en pegar, despues le das entrer y el repositorio se comenzara a descargar en el escritorio. 


### Configuracion Base de datos
1. Debes ingresar a la pagina Neon. [Neon.Tech](https://neon.tech/)
2. Te registrar/logea, una vez registrado debes crear un proyecto, el titulo del proyecto a tu preferencia y el nombre de la base de datos puede porle: "BattleShip" y le das es crear proyecto.
3. Una vez  creado el proyecto y la base de datos te dirijes a la opcion **Dashboard**.
4. Desplegas el menu donde dice **Connection string**, alli seleccionas la opcion de **Parameters only**.
5. Copias todo lo que se encuentra en el campo de texto y te dirijes donde tienes el repositorio abierto.
6. En la carpeta del proyecto encontraras una carpeta llamada **controller**, Alli encontraras un archivo llamado **SecretConfigSample.py**.
7. En este archivo debes pegar los parametros que copias en el Neon de tu base de datos.
8. Por Ultimo debes cambiar el nombre del archivo SecretConfigSample.py por **SecretConfig.py**.


### Ejecutar la interfaz web
1. Abra la terminal en su computadora.
2. En la terminal utilice el comando **cd** para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
3. Utilice el mismo comando para entrar a la aplicación "cd Interfaz_Web_Batalla_Naval-main".
4. Despues utilice el comando "python app.py".
5. Una vez ejecutado el comando anterior busca, dirigete donde dice "Running on" y en el url preciona las teclas **CTRL + Click**, esto abrira directamente la pagina.
6. Disfruta del juego.


### Ejecutar pruebas unitarias
1. Abra la terminal en su computadora.
2. En la terminal utilice el comando **cd** para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
3. Utilice el mismo comando para entrar a la aplicación "cd Interfaz_Web_Batalla_Naval-main".
4. Utilice el mismo comando "cd" para ingresar a la carpeta test, "cd test"
4. Despues utilice el comando "python Test.py".
5. Una vez ejecutado el comando anterior podras observar el resultado de las pruebas unitarias.