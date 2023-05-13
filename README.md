# Lab_4

# Laboratorio 4 - Robótica de Desarrollo, Cinemática directa

En la siguiente práctica de laboratorio, se tuvo como objetivo crear Joint controllers con ROS para manipular los 4 servomotores Dynamixel AX-12 del robot Phantom X Pincher, a través de los tópicos de estado y los servicios. Así mismo, se hizo su manipulación por medio de una interfaz realizada en Python capaz de ir llamando los archivos correspondientes para el control del robot.

### Mediciones. 

Para llevar a cabo el análisis de la cinemática directa del robot, fue indispensable hacer las mediciones de las longitudes entre cada eslabón. Lo anterior, se realizó a través de un calibrador vernier. 
Los resultados obtenidos, fueron los siguientes:
| Longitud | Medición |
| --- | --- |
| L1 | 44 mm |
| L2 | 106.1 mm |
| L3 | 106.1 mm |
| L4 | 64.1 mm + 10.1 mm |

![image](https://github.com/jhoncale/Lab_4/assets/38961990/73a754c9-fd52-4240-9503-1bd049fe2a3d)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/499221a1-3667-4aa1-a96d-332ac8762a3a)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/540c43ef-e935-4f13-973e-3555efda5195)
### Cinemática directa:

Con la información anterior, se completó la tabla DH. Se ubicó la posición home, de tal forma que la articulación 3 tuviera una orientación de -90 respecto al home por defecto que trae el PhantomX.

En primera instancia, se realizó el análisis de su geometría y de sus sistemas de coordenadas en cada uno de los eslabones.
![image](https://github.com/jhoncale/Lab_4/assets/38961990/1f93feac-44d3-4ed7-b9bc-991770e2985d)
Y posteriormente, fue posible obtener la tabla DH.
![image](https://github.com/jhoncale/Lab_4/assets/38961990/24007e54-13c4-4b1a-a772-3da9b3c1ad40)

Posición de homing propuesta:
![image](https://github.com/jhoncale/Lab_4/assets/38961990/da6cc9c0-dafc-4cd8-a77e-4df99b09884a)

#### Python + ROS + Toolbox: : 

A través de Python se creó un interfaz humano máquina (HMI), la cual fuera capaz de llamar las funciones encargadas de publicar y hacer mover cada uno de los motores del robot. Así como también, poder suscribirse a un tópico que le permitiera retornar la configuración de 5 ángulos (unidades: grados). 
Es decir, mediante el envío de una posición en ángulos deseada, el robot debía mover sus articulaciones hasta llegar al punto dado, lo que debía coincidir con las posiciones graficadas con el toolbox de Matlab.


La HMI programada fue la siguiente:


![image](https://github.com/jhoncale/Lab_4/assets/38961990/ddc2bc48-ad23-453b-aa17-30ecb55d4386)

Como puede observarse, posee 5 fotos que funcionan como botón y como gif. En reposo dan la pose conseguida con el PhantomX, y al pasar el cursor por cada una, estas muestran la posición final dada por el toolbox. Y una vez se presione cualquiera de las fotos mostradas en pantalla, el robot se moverá hasta la pose indicada. Por otro lado, en la parte inferior derecha, es posible observar la posición final que adquiere cada una de las articulaciones (motores) teniendo en cuenta la posición de home propuesta anteriormente. 


#### Pose de Home.
#### q = [0, 0, 0, 0, 0]
 ![image](https://github.com/jhoncale/Lab_4/assets/38961990/49184cac-889b-4c38-8db4-1b59b70089c8)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/13908e34-32b5-4c93-9a8c-04b31f50c4e6)

#### Pose 1.
#### q = [-25, 15, -20, 20, 0]

![image](https://github.com/jhoncale/Lab_4/assets/38961990/732cfc18-7cf6-4556-a854-e45bffec0c4f)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/8de02cb2-3cef-47ed-8dbd-9d281fd99276)


#### Pose 2.
#### q = [35, -35, 30, -30, 0]

![image](https://github.com/jhoncale/Lab_4/assets/38961990/33bc6523-c5ab-48e3-8bfd-dc52d21c9283)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/174c4488-98b9-4978-ad10-8380282f680a)

#### Pose 3.
#### q = [-85, 20, -55, 17, 0]
![image](https://github.com/jhoncale/Lab_4/assets/38961990/9ac7b7aa-e3d7-4034-9eba-739e28ff6dbb)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/c8b066d0-7ea9-4242-826e-d93e9518f06e)

#### Pose 4.
#### q = [-80, 35, -55, 45, 0]


![image](https://github.com/jhoncale/Lab_4/assets/38961990/6a8e26e6-5167-49a4-b5a9-ce04ba010985)
![image](https://github.com/jhoncale/Lab_4/assets/38961990/04546149-4b72-48cd-9e4c-339e25d5e5c6)


#### Video cambio de poses.


https://github.com/jhoncale/Lab_4/assets/38961990/e403b909-0b5a-41eb-b6cf-185d6fcfe70e




