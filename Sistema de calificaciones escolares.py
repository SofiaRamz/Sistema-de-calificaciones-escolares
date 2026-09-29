"""
SISTEMA DE CALIFICACIONES ESCOLARES
Descripción: 
    Aplicación para la gestión y control de expedientes académicos de estudiantes. 
    Implementa listas, tuplas, diccionarios, funciones de orden superior y generadores.

Autor: Sofía Ramirez Chavez
Institución: TecNM Campus Tlajomulco
Fecha: 23 de septiembre del 2026
"""

import tkinter as tk
from tkinter import ttk, messagebox
from functools import reduce
import json

class SistemaEscolar(tk.Tk):
    """
    CLASE PARA CONSTRUIR LA INTERFAZ GRÁFICA Y GESTIONAR LA LÓGICA DEL SISTEMA DE EXPEDIENTES ACADÉMICOS.
    """
    def __init__(self):
        super().__init__()
        self.title("Sistema de calificaciones escolares")
        self.geometry("980x860")
        self.configure(bg="#f5f5f4")

        # BASE DE DATOS SIMULADA DE 15 ESTUDIANTES.
        # 'INFO: LISTA MUTABLE PARA DATOS MODIFICABLES EN TIEMPO REAL.
        # 'MATERIAS_POR_SEMESTRE': TUPLA ANIDADA INMUTABLE PARA PROTEGER EL HISTORIAL ACADÉMICO.
        self.alumnos_data = [
            {
                "info": ["Carlos Pérez", 18, "Semestre 1", "Av. Juárez #123, Guadalajara"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 80, "cal_u2": 90}, {"nombre": "Introducción a la Programación", "cal_u1": 90, "cal_u2": 94})),
                )
            },
            {
                "info": ["Sofía Gómez", 19, "Semestre 2", "Calle Morelos #45, Tlajomulco"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 95, "cal_u2": 95}, {"nombre": "Introducción a la Programación", "cal_u1": 98, "cal_u2": 98})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 88, "cal_u2": 92}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 90, "cal_u2": 94})),
                )
            },
            {
                "info": ["Luis Martínez", 20, "Semestre 3", "Blvd. Rosales #89, Zapopan"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 70, "cal_u2": 70}, {"nombre": "Introducción a la Programación", "cal_u1": 60, "cal_u2": 70})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 55, "cal_u2": 65}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 70, "cal_u2": 80})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 75, "cal_u2": 85}, {"nombre": "Estructura de Datos", "cal_u1": 60, "cal_u2": 76})),
                )
            },
            {
                "info": ["Ana Torres", 20, "Semestre 4", "Paseo de los Tulipanes #12, Tlaquepaque"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 85, "cal_u2": 91}, {"nombre": "Introducción a la Programación", "cal_u1": 88, "cal_u2": 92})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 80, "cal_u2": 90}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 82, "cal_u2": 82})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 75, "cal_u2": 83}, {"nombre": "Estructura de Datos", "cal_u1": 80, "cal_u2": 88})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 90, "cal_u2": 92}, {"nombre": "Bases de Datos I", "cal_u1": 85, "cal_u2": 91})),
                )
            },
            {
                "info": ["Raúl Sánchez", 21, "Semestre 5", "Calle Hidalgo #500, Tlajomulco"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 58, "cal_u2": 62}, {"nombre": "Introducción a la Programación", "cal_u1": 50, "cal_u2": 60})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 68, "cal_u2": 72}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 60, "cal_u2": 70})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 55, "cal_u2": 61}, {"nombre": "Estructura de Datos", "cal_u1": 70, "cal_u2": 74})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 60, "cal_u2": 68}, {"nombre": "Bases de Datos I", "cal_u1": 65, "cal_u2": 75})),
                    ("Semestre 5", ({"nombre": "Probabilidad y Estadística", "cal_u1": 72, "cal_u2": 78}, {"nombre": "Sistemas Operativos", "cal_u1": 64, "cal_u2": 72})),
                )
            },
            {
                "info": ["Valeria Ríos", 21, "Semestre 6", "Av. Patria #1400, Zapopan"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 96, "cal_u2": 100}, {"nombre": "Introducción a la Programación", "cal_u1": 100, "cal_u2": 100})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 92, "cal_u2": 98}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 94, "cal_u2": 98})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 90, "cal_u2": 94}, {"nombre": "Estructura de Datos", "cal_u1": 92, "cal_u2": 96})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 88, "cal_u2": 92}, {"nombre": "Bases de Datos I", "cal_u1": 92, "cal_u2": 98})),
                    ("Semestre 5", ({"nombre": "Probabilidad y Estadística", "cal_u1": 95, "cal_u2": 99}, {"nombre": "Sistemas Operativos", "cal_u1": 89, "cal_u2": 93})),
                    ("Semestre 6", ({"nombre": "Ingeniería de Software", "cal_u1": 98, "cal_u2": 100}, {"nombre": "Redes de Computadoras", "cal_u1": 92, "cal_u2": 96})),
                )
            },
            {
                "info": ["Jorge Morales", 22, "Semestre 7", "Calle Niños Héroes #30, Guadalajara"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 78, "cal_u2": 82}, {"nombre": "Introducción a la Programación", "cal_u1": 80, "cal_u2": 84})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 72, "cal_u2": 78}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 75, "cal_u2": 81})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 68, "cal_u2": 72}, {"nombre": "Estructura de Datos", "cal_u1": 82, "cal_u2": 88})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 85, "cal_u2": 91}, {"nombre": "Bases de Datos I", "cal_u1": 0, "cal_u2": 0})),
                    ("Semestre 5", ({"nombre": "Probabilidad y Estadística", "cal_u1": 70, "cal_u2": 74}, {"nombre": "Sistemas Operativos", "cal_u1": 76, "cal_u2": 82})),
                    ("Semestre 6", ({"nombre": "Ingeniería de Software", "cal_u1": 79, "cal_u2": 83}, {"nombre": "Redes de Computadoras", "cal_u1": 82, "cal_u2": 86})),
                    ("Semestre 7", ({"nombre": "Inteligencia Artificial", "cal_u1": 88, "cal_u2": 92}, {"nombre": "Arquitectura de Software", "cal_u1": 85, "cal_u2": 91})),
                )
            },
            {
                "info": ["Carmen Luna", 20, "Semestre 1", "Circuito del Sol #77, Tlaquepaque"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 88, "cal_u2": 92}, {"nombre": "Introducción a la Programación", "cal_u1": 86, "cal_u2": 90})),
                )
            },
            {
                "info": ["David Garza", 21, "Semestre 2", "Av. Vallarta #2200, Guadalajara"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 76, "cal_u2": 80}, {"nombre": "Introducción a la Programación", "cal_u1": 78, "cal_u2": 82})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 80, "cal_u2": 84}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 83, "cal_u2": 87})),
                )
            },
            {
                "info": ["Lucía Méndez", 22, "Semestre 3", "Calle Acueducto #55, Zapopan"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 62, "cal_u2": 68}, {"nombre": "Introducción a la Programación", "cal_u1": 70, "cal_u2": 74})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 65, "cal_u2": 71}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 72, "cal_u2": 76})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 68, "cal_u2": 72}, {"nombre": "Estructura de Datos", "cal_u1": 58, "cal_u2": 62})),
                )
            },
            {
                "info": ["Mario Cárdenas", 22, "Semestre 4", "Calle Luna #10, Zapopan"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 80, "cal_u2": 84}, {"nombre": "Introducción a la Programación", "cal_u1": 83, "cal_u2": 87})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 78, "cal_u2": 82}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 77, "cal_u2": 81})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 86, "cal_u2": 90}, {"nombre": "Estructura de Datos", "cal_u1": 82, "cal_u2": 86})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 74, "cal_u2": 78}, {"nombre": "Bases de Datos I", "cal_u1": 88, "cal_u2": 92})),
                )
            },
            {
                "info": ["Daniela Ruiz", 23, "Semestre 5", "Av. Las Torres #400, Tlaquepaque"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 90, "cal_u2": 92}, {"nombre": "Introducción a la Programación", "cal_u1": 93, "cal_u2": 95})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 87, "cal_u2": 91}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 90, "cal_u2": 94})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 83, "cal_u2": 87}, {"nombre": "Estructura de Datos", "cal_u1": 85, "cal_u2": 89})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 88, "cal_u2": 92}, {"nombre": "Bases de Datos I", "cal_u1": 86, "cal_u2": 90})),
                    ("Semestre 5", ({"nombre": "Probabilidad y Estadística", "cal_u1": 91, "cal_u2": 95}, {"nombre": "Sistemas Operativos", "cal_u1": 93, "cal_u2": 97})),
                )
            },
            {
                "info": ["Fernando Vega", 24, "Semestre 6", "Calle Robles #15, Guadalajara"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 68, "cal_u2": 72}, {"nombre": "Introducción a la Programación", "cal_u1": 66, "cal_u2": 70})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 70, "cal_u2": 74}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 73, "cal_u2": 77})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 63, "cal_u2": 67}, {"nombre": "Estructura de Datos", "cal_u1": 68, "cal_u2": 72})),
                    ("Semestre 4", ({"nombre": "Matemáticas Discretas", "cal_u1": 76, "cal_u2": 80}, {"nombre": "Bases de Datos I", "cal_u1": 67, "cal_u2": 71})),
                    ("Semestre 5", ({"nombre": "Probabilidad y Estadística", "cal_u1": 78, "cal_u2": 82}, {"nombre": "Sistemas Operativos", "cal_u1": 80, "cal_u2": 84})),
                    ("Semestre 6", ({"nombre": "Ingeniería de Software", "cal_u1": 83, "cal_u2": 87}, {"nombre": "Redes de Computadoras", "cal_u1": 86, "cal_u2": 90})),
                )
            },
            {
                "info": ["Paola Herrera", 20, "Semestre 2", "Blvd. Aeropuerto #300, Tlajomulco"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 94, "cal_u2": 98}, {"nombre": "Introducción a la Programación", "cal_u1": 93, "cal_u2": 97})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 90, "cal_u2": 94}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 92, "cal_u2": 96})),
                )
            },
            {
                "info": ["Esteban Ramos", 22, "Semestre 3", "Calle Obregón #50, Tlaquepaque"],
                "materias_por_semestre": (
                    ("Semestre 1", ({"nombre": "Álgebra Básica", "cal_u1": 53, "cal_u2": 57}, {"nombre": "Introducción a la Programación", "cal_u1": 58, "cal_u2": 62})),
                    ("Semestre 2", ({"nombre": "Cálculo Diferencial", "cal_u1": 48, "cal_u2": 52}, {"nombre": "Programación Orientada a Objetos", "cal_u1": 63, "cal_u2": 67})),
                    ("Semestre 3", ({"nombre": "Cálculo Integral", "cal_u1": 0, "cal_u2": 0}, {"nombre": "Estructura de Datos", "cal_u1": 56, "cal_u2": 60})),
                )
            }
        ]

        # CONFIGURACIÓN DE ESTILOS VISUALES DE LA INTERFAZ
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.dark_gray = "#292524"
        self.style.configure(".", background="#f5f5f4", font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#e7e5e4", foreground=self.dark_gray, borderwidth=0, focuscolor="none")
        self.style.map("TButton", background=[("active", "#d6d3d1")])

        # CREACIÓN DE COMPONENTES VISUALES PRINCIPALES (ENCABEZADO, CONTROLES Y CONSOLA DE SALIDA)
        header_frame = tk.Frame(self, bg="#e7e5e4", height=70)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="🎓 Control Académico de Estudiantes", font=("Segoe UI", 16, "bold"), bg="#e7e5e4", fg=self.dark_gray).pack(pady=18)
        main_card = tk.Frame(self, bg="#ffffff", highlightbackground="#d6d3d1", highlightthickness=1)
        main_card.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        control_panel = tk.Frame(main_card, bg="#ffffff")
        control_panel.pack(fill=tk.X, padx=20, pady=15)
        tk.Label(control_panel, text="Estudiante:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg=self.dark_gray).pack(side=tk.LEFT, padx=(0, 5))
        nombres_alumnos = [a["info"][0] for a in self.alumnos_data]
        self.combo_alumnos = ttk.Combobox(control_panel, values=nombres_alumnos, state="readonly", width=25, font=("Segoe UI", 10))
        self.combo_alumnos.current(0)
        self.combo_alumnos.pack(side=tk.LEFT, padx=5)
        self.combo_alumnos.bind("<<ComboboxSelected>>", lambda e: self.mostrar_json_alumno())
        btn_modificar = ttk.Button(control_panel, text="Modificar Estudiante / Materias", command=self.abrir_menu_modificacion)
        btn_modificar.pack(side=tk.RIGHT, padx=5)
        ttk.Separator(main_card, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=20, pady=5)

        # BOTONERA DE OPERACIONES FUNCIONALES (FILTER, MAP, GENERADORES)
        btn_frame = tk.Frame(main_card, bg="#ffffff")
        btn_frame.pack(fill=tk.X, padx=20, pady=15)
        btn_config = {"font": ("Segoe UI", 9, "bold"), "bg": "#e7e5e4", "fg": "#292524", "activebackground": "#d6d3d1", "relief": "flat", "padx": 8, "pady": 8}
        tk.Button(btn_frame, text="Aprobadas / Reprobadas", command=self.demo_filter_aprobadas_reprobadas, **btn_config).grid(row=0, column=0, padx=5, sticky="ew")
        tk.Button(btn_frame, text="Escala de Letras", command=self.demo_map_letras, **btn_config).grid(row=0, column=1, padx=5, sticky="ew")
        tk.Button(btn_frame, text="Reporte Unidades", command=self.demo_generador, **btn_config).grid(row=0, column=2, padx=5, sticky="ew")
        tk.Button(btn_frame, text="Avance Curricular", command=self.demo_avance_curricular, **btn_config).grid(row=0, column=3, padx=5, sticky="ew")
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

        # CONSOLA ESTILO JSON PARA MOSTRAR LOS RESULTADOS PROCESADOS
        console_frame = tk.Frame(main_card, bg="#1c1917", highlightbackground="#44403c", highlightthickness=1)
        console_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(5, 20))
        console_header = tk.Frame(console_frame, bg="#292524", height=30)
        console_header.pack(fill=tk.X)
        tk.Label(console_header, text="  Información del estudiante", font=("Segoe UI", 9, "bold"), bg="#292524", fg="#d6d3d1").pack(side=tk.LEFT, pady=5)
        self.texto_resultado = tk.Text(console_frame, height=17, font=("Consolas", 10), bg="#1c1917", fg="#f5f5f4", insertbackground="white", relief="flat", bd=0, padx=15, pady=15)    
        scrollbar = ttk.Scrollbar(console_frame, orient=tk.VERTICAL, command=self.texto_resultado.yview)
        self.texto_resultado.configure(yscrollcommand=scrollbar.set)
        self.texto_resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.mostrar_json_alumno()

    # FUNCIÓN PURA PARA EVALUAR EL ESTATUS DE UNA MATERIA BASADO EN SUS CALIFICACIONES.
    def evaluar_materia_pura(self, cal_u1, cal_u2):
        if cal_u1 == 0 and cal_u2 == 0:
            return "Calificación pendiente"
        promedio = (cal_u1 + cal_u2) / 2
        return "Aprobado" if promedio >= 70 else "Reprobado"

    # ABRE UNA VENTANA EMERGENTE PARA MODIFICAR DATOS PERSONALES Y ACTUALIZAR NOTAS.
    def abrir_menu_modificacion(self):
        nombre_actual = self.combo_alumnos.get()
        alumno = next(a for a in self.alumnos_data if a["info"][0] == nombre_actual)
        ventana = tk.Toplevel(self)
        ventana.title(f"Modificar: {nombre_actual}")
        ventana.geometry("450x570")
        ventana.configure(bg="#f5f5f4")
        ventana.grab_set()
        tk.Label(ventana, text="Actualizar datos del estudiante", font=("Segoe UI", 11, "bold"), bg="#f5f5f4", fg="#292524").pack(pady=10)

        # EDAD CONTROLADA MEDIANTE UN SPINBOX
        tk.Label(ventana, text="Edad:", bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30)
        spin_edad = tk.Spinbox(ventana, from_=17, to=60, width=33, font=("Segoe UI", 10), state="readonly")
        spin_edad.delete(0, tk.END)
        spin_edad.insert(0, str(alumno["info"][1]))
        spin_edad.pack(padx=30, pady=5)

        # SEMESTRE ACTUAL CONTROLADO MEDIANTE UN COMBOBOX RESTRINGIDO (DEL 1 AL 8)
        tk.Label(ventana, text="Semestre Actual:", bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30)
        semestres_disponibles = [f"Semestre {i}" for i in range(1, 9)]
        combo_sem = ttk.Combobox(ventana, values=semestres_disponibles, width=33, font=("Segoe UI", 10), state="readonly")
        combo_sem.set(alumno["info"][2])
        combo_sem.pack(padx=30, pady=5)

        tk.Label(ventana, text="Dirección:", bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30)
        entry_dir = ttk.Entry(ventana, width=35)
        entry_dir.insert(0, alumno["info"][3])
        entry_dir.pack(padx=30, pady=5)
        tk.Label(ventana, text="Seleccionar o Agregar Materia y Calificaciones", font=("Segoe UI", 11, "bold"), bg="#f5f5f4", fg="#292524").pack(pady=(15, 5))
        tk.Label(ventana, text="Materia (Escribe o despliega con la flecha):", bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30)
        mapa_materias = {m["nombre"]: (m["cal_u1"], m["cal_u2"]) for sem, mats in alumno["materias_por_semestre"] for m in mats}
        materias_actuales = list(mapa_materias.keys())
        combo_materia = ttk.Combobox(ventana, values=materias_actuales, width=33, font=("Segoe UI", 10))
        combo_materia.set("")
        combo_materia.pack(padx=30, pady=3)
        tk.Label(ventana, text="Calificación Unidad 1:", bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30)
        entry_u1 = ttk.Entry(ventana, width=35)
        entry_u1.insert(0, "0")
        entry_u1.pack(padx=30, pady=3)
        tk.Label(ventana, text="Calificación Unidad 2:", bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30)
        entry_u2 = ttk.Entry(ventana, width=35)
        entry_u2.insert(0, "0")
        entry_u2.pack(padx=30, pady=3)

        # CARGA AUTOMÁTICA DE CALIFICACIONES EXISTENTES AL SELECCIONAR UNA MATERIA DEL MENÚ.
        def al_seleccionar_materia(event):
            mat_seleccionada = combo_materia.get()
            if mat_seleccionada in mapa_materias:
                u1, u2 = mapa_materias[mat_seleccionada]
                entry_u1.delete(0, tk.END)
                entry_u1.insert(0, str(u1))
                entry_u2.delete(0, tk.END)
                entry_u2.insert(0, str(u2))
        combo_materia.bind("<<ComboboxSelected>>", al_seleccionar_materia)

        # GUARDA LOS CAMBIOS APLICANDO EL PRINCIPIO DE RECONSTRUCCIÓN INMUTABLE DE TUPLAS.
        def guardar_cambios():
            try:
                alumno["info"][1] = int(spin_edad.get())
                nuevo_sem = combo_sem.get().strip()
                alumno["info"][2] = nuevo_sem
                alumno["info"][3] = entry_dir.get()
                nombre_materia = combo_materia.get().strip()
                if nombre_materia:
                    u1_val = float(entry_u1.get())
                    u2_val = float(entry_u2.get())
                    lista_semestres = list(alumno["materias_por_semestre"])
                    semestre_encontrado = False    
                    for idx, (sem_nombre, mats) in enumerate(lista_semestres):
                        if sem_nombre == nuevo_sem:
                            semestre_encontrado = True
                            nueva_lista_mats = list(mats)
                            materia_existente = False
                            for m_idx, mat in enumerate(nueva_lista_mats):
                                if mat["nombre"] == nombre_materia:
                                    nueva_lista_mats[m_idx] = {"nombre": nombre_materia, "cal_u1": u1_val, "cal_u2": u2_val}
                                    materia_existente = True
                                    break                            
                            if not materia_existente:
                                nueva_lista_mats.append({"nombre": nombre_materia, "cal_u1": u1_val, "cal_u2": u2_val})
                            lista_semestres[idx] = (sem_nombre, tuple(nueva_lista_mats))
                            break                    
                    if not semestre_encontrado:
                        lista_semestres.append((nuevo_sem, ({"nombre": nombre_materia, "cal_u1": u1_val, "cal_u2": u2_val},)))                    
                    alumno["materias_por_semestre"] = tuple(lista_semestres)
                messagebox.showinfo("Éxito", "Los datos del estudiante se actualizaron correctamente.")
                ventana.destroy()
                self.mostrar_json_alumno()
            except ValueError:
                messagebox.showerror("Error", "Por favor verifica que las calificaciones sean valores numéricos.")
        ttk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).pack(pady=15)

    # MUESTRA EN LA CONSOLA DE LA INTERFAZ EL EXPEDIENTE COMPLETO FORMATEADO EN JSON.
    def mostrar_json_alumno(self):
        self.texto_resultado.delete("1.0", tk.END)
        nombre_sel = self.combo_alumnos.get()
        if not nombre_sel:
            return 
        alumno = next(a for a in self.alumnos_data if a["info"][0] == nombre_sel)
        nombre, edad, semestre_actual, direccion = alumno["info"]
        historial_semestres = alumno["materias_por_semestre"]
        promedios_materias = [(m["cal_u1"] + m["cal_u2"]) / 2 for sem, mats in historial_semestres for m in mats if (m["cal_u1"] > 0 or m["cal_u2"] > 0)]
        
        # USO DE REDUCE() PARA SUMAR LOS PROMEDIOS Y CALCULAR EL PROMEDIO GENERAL ACUMULADO
        if promedios_materias:
            suma = reduce(lambda acc, p: acc + p, promedios_materias, 0)
            promedio_general = suma / len(promedios_materias)
        else:
            promedio_general = 0.0
        semestres_estructurados = {}
        for sem_nombre, mats in historial_semestres:
            semestres_estructurados[sem_nombre] = [
                {
                    "materia": m["nombre"],
                    "unidad_1": m["cal_u1"],
                    "unidad_2": m["cal_u2"],
                    "calificacion_final_promedio": round((m["cal_u1"] + m["cal_u2"]) / 2, 1) if (m["cal_u1"] > 0 or m["cal_u2"] > 0) else 0,
                    "estatus": self.evaluar_materia_pura(m["cal_u1"], m["cal_u2"])
                } for m in mats
            ]
        datos_arbol = {
            "DatosPersonales": {
                "nombre": nombre,
                "edad": edad,
                "semestre_actual": semestre_actual,
                "direccion": direccion
            },
            "HistorialAcademico": {
                "promedio_general_acumulado": round(promedio_general, 2),
                "materias_por_semestre": semestres_estructurados
            }
        }
        self.texto_resultado.insert(tk.END, f"// EXPEDIENTE ACUMULADO HASTA: {semestre_actual.upper()}\n")
        self.texto_resultado.insert(tk.END, json.dumps(datos_arbol, indent=4, ensure_ascii=False))

    # FILTRA Y CLASIFICA LAS MATERIAS UTILIZANDO FILTER() SEPARANDO APROBADAS Y REPROBADAS.
    def demo_filter_aprobadas_reprobadas(self):
        self.texto_resultado.delete("1.0", tk.END)
        alumno = next(a for a in self.alumnos_data if a["info"][0] == self.combo_alumnos.get())
        historial_semestres = alumno["materias_por_semestre"]
        todas_mats = [
            {
                "nombre": m["nombre"], 
                "promedio": round((m["cal_u1"] + m["cal_u2"]) / 2, 1) if (m["cal_u1"] > 0 or m["cal_u2"] > 0) else 0,
                "estatus": self.evaluar_materia_pura(m["cal_u1"], m["cal_u2"])
            } for sem, mats in historial_semestres for m in mats
        ]
        aprobadas = list(filter(lambda m: m["estatus"] == "Aprobado", todas_mats))
        reprobadas = list(filter(lambda m: m["estatus"] == "Reprobado", todas_mats))
        datos_json = {
            "Accion": "Clasificación de Materias usando filter()",
            "alumno": alumno["info"][0],
            "materias_aprobadas": aprobadas,
            "materias_reprobadas": reprobadas
        }
        self.texto_resultado.insert(tk.END, json.dumps(datos_json, indent=4, ensure_ascii=False))

    # TRANSFORMA LAS CALIFICACIONES NUMÉRICAS EN ESCALA DE LETRAS UTILIZANDO MAP().
    def demo_map_letras(self):
        self.texto_resultado.delete("1.0", tk.END)
        alumno = next(a for a in self.alumnos_data if a["info"][0] == self.combo_alumnos.get())
        todas_mats = [m for sem, mats in alumno["materias_por_semestre"] for m in mats]
        def convertir_a_letra(cal):
            if cal == 0: return "N/A"
            elif cal >= 90: return "A (Excelente)"
            elif cal >= 80: return "B (Notable)"
            elif cal >= 70: return "C (Suficiente)"
            else: return "F (No Acreditado)"
        materias_mapeadas = list(map(lambda m: {
            "materia": m["nombre"],
            "unidad_1_letra": convertir_a_letra(m["cal_u1"]),
            "unidad_2_letra": convertir_a_letra(m["cal_u2"]),
            "promedio_final": round((m["cal_u1"] + m["cal_u2"]) / 2, 1) if (m["cal_u1"] > 0 or m["cal_u2"] > 0) else 0
        }, todas_mats))
        datos_json = {
            "Accion": "Conversión de Calificaciones a Escala de Letras (map)",
            "alumno": alumno["info"][0],
            "resultados_mapeados": materias_mapeadas
        }
        self.texto_resultado.insert(tk.END, json.dumps(datos_json, indent=4, ensure_ascii=False))

    # GENERA UN REPORTE DETALLADO UNIDAD POR UNIDAD UTILIZANDO FUNCIONES GENERADORAS (YIELD).
    def demo_generador(self):
        self.texto_resultado.delete("1.0", tk.END)
        alumno = next(a for a in self.alumnos_data if a["info"][0] == self.combo_alumnos.get())
        def generar_reporte_detallado():
            for sem_nombre, materias in alumno["materias_por_semestre"]:
                for mat in materias:
                    u1_val = mat["cal_u1"]
                    estado_u1 = f"Acreditada ({u1_val})" if u1_val >= 70 else (f"No acreditada ({u1_val})" if u1_val > 0 else "Sin calificación")
                    yield {"semestre": sem_nombre, "materia": mat["nombre"], "unidad": "Unidad 1", "estado": estado_u1}
                    
                    u2_val = mat["cal_u2"]
                    estado_u2 = f"Acreditada ({u2_val})" if u2_val >= 70 else (f"No acreditada ({u2_val})" if u2_val > 0 else "Sin calificación")
                    yield {"semestre": sem_nombre, "materia": mat["nombre"], "unidad": "Unidad 2", "estado": estado_u2}
        datos_json = {
            "Accion": "Generación de Reporte Detallado de Unidades",
            "alumno": alumno["info"][0],
            "semestre_actual": alumno["info"][2],
            "bitacora_completa_unidades": list(generar_reporte_detallado())
        }
        self.texto_resultado.insert(tk.END, json.dumps(datos_json, indent=4, ensure_ascii=False))

    # CONSTRUYE UN ÁRBOL JERÁRQUICO DEL AVANCE CURRICULAR POR SEMESTRE Y UNIDADES.
    def demo_avance_curricular(self):
        self.texto_resultado.delete("1.0", tk.END)
        alumno = next(a for a in self.alumnos_data if a["info"][0] == self.combo_alumnos.get())
        def evaluar_nodo(prom):
            if prom == 0: return "Materia Nueva sin Calificación / Dada de Baja"
            elif prom >= 90: return "Aprobado con Honores"
            elif prom >= 70: return "Aprobado"
            else: return "Reprobado (Debe repetir materia)"
        avance_por_semestre = {}
        for sem_nombre, mats in alumno["materias_por_semestre"]:
            lista_ramas = []
            for m in mats:
                u1 = m["cal_u1"]
                u2 = m["cal_u2"]
                if u1 == 0 and u2 == 0:
                    promedio_final = 0
                    st1, st2 = "", ""
                else:
                    promedio_final = round((u1 + u2) / 2, 1)
                    st1 = "Completada" if u1 >= 70 else "No acreditada"
                    st2 = "Completada" if u2 >= 70 else "No acreditada"
                lista_ramas.append({
                    "materia": m["nombre"],
                    "calificacion_final_promedio": promedio_final,
                    "estatus": evaluar_nodo(promedio_final),
                    "unidades": [{"unidad": 1, "estado": st1}, {"unidad": 2, "estado": st2}]
                })
            avance_por_semestre[sem_nombre] = lista_ramas
        arbol_avance = {
            "EstructuraArbolCurricular": {
                "alumno": alumno["info"][0],
                "semestre_actual": alumno["info"][2],
                "historial_academico_arbol": avance_por_semestre
            }
        }
        self.texto_resultado.insert(tk.END, json.dumps(arbol_avance, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    app = SistemaEscolar()
    app.mainloop()