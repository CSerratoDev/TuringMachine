
## Authors

- [@cserratodev](https://github.com/CSerratoDev)


# System Turing Machine

[USA] This project implements a visual Turing Machine simulator, using Python, Tkinter and Graphviz.

[MX] Este proyecto implementa un simulador visual de Máquina de Turing, usando Python, Tkinter y Graphviz.




## Functions
[USA]

✔️ Load a Turing machine from a **file.txt**

✔️ File **Display the tape** dynamically 

✔️ **Draw the state diagram** and **highlight transitions** 

✔️ **Show acceptance or rejection**

[MX]

✔️ Cargar una máquina de Turing desde un **archivo .txt**

✔️ **Visualizar la cinta** dinámicamente

✔️ **Dibujar el diagrama de estados** y **resaltar transiciones**

✔️ **Mostrar aceptación o rechazo**
## Deployment

- [USA] Before you begin, make sure you have installed **Python 3.9+**
- [MX] Antes de comenzar, asegúrate de tener instalado **Python 3.9+**

- [USA] Clone Repository (SSH)
- [MX] Clonar Repositorio (SSH)
```bash
  git clone git@github.com:CSerratoDev/TuringMachine.git
```
- [USA] Enter the previously cloned Repository folder 
- [MX] Ingresar a la carpeta del Repositorio previamente clonado
```bash
    cd <carpeta_del_proyecto>
```
- [USA] Create a Virtual Environment (recommended)
- [MX] Crear un Entorno Virtual (recomendado)
```bash
  python3 -v venv venv
```
- [USA] Install Dependencies
- [MX] Instalar Dependencias
```bash
  pip install -r requirements.txt
```
- [USA] Execution
- [MX] Ejecución
```bash
  python main.py
```




## TXT file format
[USA]       
Conforms to **6 lines** of the **6-tuple**:

1 - **States**      
2 - **Word**        
3 - **Ribbon Alphabet**         
4 - **Entry Status**        
5 - **Final Statements**        
6 - **Transitions (from line 6 to (n) lines below)**        

*Note: Transitions are formulated as follows* 

(current_state, symbol_read) -> (symbol_to_write, direction, next_state) 

[MX]        
Se conforma de **6 lineas** de la **6-Tuple**:

1 - **Estados**     
2 - **Palabra**         
3 - **Alfabeto de la cinta**        
4 - **Estado de Entrada**       
5 - **Estados Finales**     
6 - **Transiciones (desde la linea 6 hasta (n) lineas por debajo)**     

*Nota:
Las transiciones se formulan de la siguiente manera*

(estado_actual, simbolo_leído) -> (simbolo_a_escribir, dirección, estado_siguiente)


## [USA] Turing Machine Example | [MX] Ejemplo de Maquina de Turing 
[USA]
**Function: word copy 1^n**     
[MX]
**Función: Copia de palabra 1^n**

q0 q1 q2 q3 q4 qf  
$ 1 1 1 Δ Δ Δ Δ  
$ 1 x ■ Δ  
q0  
qf  
q0 $ $ R q1  
q1 1 1 R q1     
q1 Δ ■ L q2     
q2 X X L q2     
q2 1 X R q3     
q3 X X R q3     
q3 ■ ■ R q3     
q3 1 1 R q3     
q3 Δ 1 L q4     
q4 1 1 L q4     
q4 ■ ■ L q2     
q2 $ $ R qf     
qf X 1 R qf     
qf ■ ■ R qf     
qf 1 1 R qf