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
    def __init__(self):
        super().__init__()
        self.title("Sistema de calificaciones escolares")
        self.geometry("980x860")
        self.configure(bg="#f5f5f4")

        # INMUTABILIDAD EN ESTRUCTURAS DE DATOS:
        # En programación funcional se evita cambiar el estado de los datos existentes.
        # Las calificaciones se almacenan como TUPLAS. Al ser inmutables, 
        # Python garantiza que sus valores no sufrirán efectos secundarios (side-effects) imprevistos.
        self.alumnos_data = [
            {
                "info": ["Carlos Pérez", 18, "Semestre 1", "Av. Juárez #123, Guadalajara"],
                "materias": {
                    "Semestre 1": [
                        {"nombre": "Álgebra Básica", "calificaciones": (80, 90)},
                        {"nombre": "Introducción a la Programación", "calificaciones": (90, 94)}
                    ]
                }
            },
            {
                "info": ["Sofía Gómez", 19, "Semestre 2", "Calle Morelos #45, Tlajomulco"],
                "materias": {
                    "Semestre 1": [
                        {"nombre": "Álgebra Básica", "calificaciones": (95, 95)},
                        {"nombre": "Introducción a la Programación", "calificaciones": (98, 98)}
                    ],
                    "Semestre 2": [
                        {"nombre": "Cálculo Diferencial", "calificaciones": (88, 92)},
                        {"nombre": "Programación Orientada a Objetos", "calificaciones": (90, 94)}
                    ]
                }
            },
            {
                "info": ["Luis Martínez", 20, "Semestre 3", "Blvd. Rosales #89, Zapopan"],
                "materias": {
                    "Semestre 1": [
                        {"nombre": "Álgebra Básica", "calificaciones": (70, 70)},
                        {"nombre": "Introducción a la Programación", "calificaciones": (60, 70)}
                    ],
                    "Semestre 2": [
                        {"nombre": "Cálculo Diferencial", "calificaciones": (55, 65)},
                        {"nombre": "Programación Orientada a Objetos", "calificaciones": (70, 80)}
                    ],
                    "Semestre 3": [
                        {"nombre": "Cálculo Integral", "calificaciones": (75, 85)},
                        {"nombre": "Estructura de Datos", "calificaciones": (60, 76)}
                    ]
                }
            },
            {
                "info": ["Ana Torres", 20, "Semestre 4", "Paseo de los Tulipanes #12, Tlaquepaque"],
                "materias": {
                    "Semestre 1": [
                        {"nombre": "Álgebra Básica", "calificaciones": (85, 91)}
                    ],
                    "Semestre 2": [
                        {"nombre": "Cálculo Diferencial", "calificaciones": (80, 90)}
                    ],
                    "Semestre 3": [
                        {"nombre": "Cálculo Integral", "calificaciones": (75, 83)}
                    ],
                    "Semestre 4": [
                        {"nombre": "Matemáticas Discretas", "calificaciones": (90, 92)},
                        {"nombre": "Bases de Datos I", "calificaciones": (85, 91)}
                    ]
                }
            },
            {
                "info": ["Raúl Sánchez", 21, "Semestre 5", "Calle Hidalgo #500, Tlajomulco"],
                "materias": {
                    "Semestre 3": [
                        {"nombre": "Cálculo Integral", "calificaciones": (55, 61)},
                        {"nombre": "Estructura de Datos", "calificaciones": (70, 74)}
                    ],
                    "Semestre 4": [
                        {"nombre": "Matemáticas Discretas", "calificaciones": (60, 68)},
                        {"nombre": "Bases de Datos I", "calificaciones": (65, 75)}
                    ],
                    "Semestre 5": [
                        {"nombre": "Probabilidad y Estadística", "calificaciones": (72, 78)},
                        {"nombre": "Sistemas Operativos", "calificaciones": (64, 72)}
                    ]
                }
            }
        ]

        self._configurar_estilos()
        self._construir_interfaz()
        self.mostrar_json_alumno()

    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.dark_gray = "#292524"
        self.style.configure(".", background="#f5f5f4", font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#e7e5e4", foreground=self.dark_gray, borderwidth=0)
        self.style.map("TButton", background=[("active", "#d6d3d1")])

    def _construir_interfaz(self):
        header = tk.Frame(self, bg="#e7e5e4", height=70)
        header.pack(fill=tk.X)
        tk.Label(header, text="🎓 Control Académico de Estudiantes", font=("Segoe UI", 16, "bold"), bg="#e7e5e4", fg=self.dark_gray).pack(pady=18)
        
        main_card = tk.Frame(self, bg="#ffffff", highlightbackground="#d6d3d1", highlightthickness=1)
        main_card.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        control_panel = tk.Frame(main_card, bg="#ffffff")
        control_panel.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(control_panel, text="Estudiante:", font=("Segoe UI", 10, "bold"), bg="#ffffff").pack(side=tk.LEFT, padx=(0, 5))
        nombres = [a["info"][0] for a in self.alumnos_data]
        self.combo_alumnos = ttk.Combobox(control_panel, values=nombres, state="readonly", width=25)
        self.combo_alumnos.current(0)
        self.combo_alumnos.pack(side=tk.LEFT, padx=5)
        self.combo_alumnos.bind("<<ComboboxSelected>>", lambda e: self.mostrar_json_alumno())
        
        ttk.Button(control_panel, text="Modificar Datos", command=self.abrir_menu_modificacion).pack(side=tk.RIGHT, padx=5)
        ttk.Separator(main_card, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=20, pady=5)

        btn_frame = tk.Frame(main_card, bg="#ffffff")
        btn_frame.pack(fill=tk.X, padx=20, pady=15)
        
        botones = [
            ("Aprobadas / Reprobadas", self.demo_filter_aprobadas_reprobadas),
            ("Escala de Letras", self.demo_map_letras),
            ("Reporte Unidades", self.demo_generador),
            ("Avance Curricular", self.demo_avance_curricular)
        ]
        
        for i, (texto, comando) in enumerate(botones):
            tk.Button(btn_frame, text=texto, command=comando, font=("Segoe UI", 9, "bold"), bg="#e7e5e4", relief="flat", padx=8, pady=8).grid(row=0, column=i, padx=5, sticky="ew")
            btn_frame.columnconfigure(i, weight=1)

        console_frame = tk.Frame(main_card, bg="#1c1917")
        console_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(5, 20))
        tk.Label(console_frame, text=" Información del estudiante", font=("Segoe UI", 9, "bold"), bg="#292524", fg="#d6d3d1", anchor="w").pack(fill=tk.X)
        
        self.texto_resultado = tk.Text(console_frame, height=17, font=("Consolas", 10), bg="#1c1917", fg="#f5f5f4", relief="flat", padx=15, pady=15)    
        scrollbar = ttk.Scrollbar(console_frame, orient=tk.VERTICAL, command=self.texto_resultado.yview)
        self.texto_resultado.configure(yscrollcommand=scrollbar.set)
        
        self.texto_resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    # Usa 'next', iterando solo lo necesario hasta hallar coincidencia, sin cargar toda la lista en memoria.
    def _obtener_alumno_actual(self):
        nombre = self.combo_alumnos.get()
        return next((a for a in self.alumnos_data if a["info"][0] == nombre), None)


    # FUNCIÓN PURA:
    # 1. Su resultado depende ÚNICAMENTE de los parámetros de entrada (cal_u1, cal_u2).
    # 2. No lee ni modifica variables externas.
    # 3. SIEMPRE devolverá la misma salida.
    def evaluar_materia_pura(self, cal_u1, cal_u2):
        if cal_u1 == 0 and cal_u2 == 0: return "Calificación pendiente"
        return "Aprobado" if (cal_u1 + cal_u2) / 2 >= 70 else "Reprobado"


    def abrir_menu_modificacion(self):
        alumno = self._obtener_alumno_actual()
        if not alumno: return

        vent = tk.Toplevel(self)
        vent.title(f"Modificar: {alumno['info'][0]}")
        vent.geometry("450x500")
        vent.configure(bg="#f5f5f4")
        vent.grab_set()

        def crear_campo(texto, widget_class, **kwargs):
            tk.Label(vent, text=texto, bg="#f5f5f4", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=30, pady=(5,0))
            widget = widget_class(vent, **kwargs)
            widget.pack(padx=30, pady=2, fill=tk.X)
            return widget

        spin_edad = crear_campo("Edad:", tk.Spinbox, from_=17, to=60, state="readonly")
        spin_edad.insert(0, str(alumno["info"][1]))
        
        combo_sem = crear_campo("Semestre Actual:", ttk.Combobox, values=[f"Semestre {i}" for i in range(1, 9)], state="readonly")
        combo_sem.set(alumno["info"][2])
        
        entry_dir = crear_campo("Dirección:", ttk.Entry)
        entry_dir.insert(0, alumno["info"][3])

        tk.Label(vent, text="Gestión de Materias", font=("Segoe UI", 11, "bold"), bg="#f5f5f4").pack(pady=(15, 5))
        
        materias_actuales = {m["nombre"]: m["calificaciones"] for mats in alumno["materias"].values() for m in mats}
        combo_mat = crear_campo("Materia:", ttk.Combobox, values=list(materias_actuales.keys()))
        entry_u1 = crear_campo("Calificación Unidad 1:", ttk.Entry)
        entry_u2 = crear_campo("Calificación Unidad 2:", ttk.Entry)

        def autocompletar(event):
            materia = combo_mat.get()
            if materia in materias_actuales:
                u1, u2 = materias_actuales[materia]
                entry_u1.delete(0, tk.END); entry_u1.insert(0, str(u1))
                entry_u2.delete(0, tk.END); entry_u2.insert(0, str(u2))
        combo_mat.bind("<<ComboboxSelected>>", autocompletar)

        def guardar():
            try:
                alumno["info"][1] = int(spin_edad.get())
                alumno["info"][2] = combo_sem.get()
                alumno["info"][3] = entry_dir.get()
                
                mat_nombre = combo_mat.get().strip()
                if mat_nombre:
                    # MANTENIMIENTO DE INMUTABILIDAD:
                    # Al recibir nuevos datos, NO modificamos la tupla original. 
                    # En su lugar, creamos una tupla completamente nueva y reemplazamos la referencia.
                    nuevas_cals = (float(entry_u1.get() or 0), float(entry_u2.get() or 0))
                    
                    semestre_seleccionado = combo_sem.get()
                    if semestre_seleccionado not in alumno["materias"]:
                        alumno["materias"][semestre_seleccionado] = []
                    
                    lista_mats = alumno["materias"][semestre_seleccionado]
                    for m in lista_mats:
                        if m["nombre"] == mat_nombre:
                            m["calificaciones"] = nuevas_cals # Reemplazo por nueva tupla inmutable
                            break
                    else:
                        lista_mats.append({"nombre": mat_nombre, "calificaciones": nuevas_cals})

                self.mostrar_json_alumno()
                vent.destroy()
                messagebox.showinfo("Éxito", "Datos actualizados.")
            except ValueError:
                messagebox.showerror("Error", "Las calificaciones deben ser numéricas.")

        ttk.Button(vent, text="Guardar Cambios", command=guardar).pack(pady=15)


    def mostrar_json_alumno(self):
        alumno = self._obtener_alumno_actual()
        if not alumno: return
        self.texto_resultado.delete("1.0", tk.END)
        nombre, edad, sem_actual, direccion = alumno["info"]
        
        todas_mats = [m for mats in alumno["materias"].values() for m in mats]
        promedios = [(m["calificaciones"][0] + m["calificaciones"][1]) / 2 for m in todas_mats if sum(m["calificaciones"]) > 0]
        
        # REDUCE()
        # Combina los elementos de una colección para "reducirlos" a un solo valor.
        # Aplica una función lambda (acc, p) donde 'acc' almacena el acumulado y 'p' es el elemento actual.
        # En este caso, toma todos los promedios de la lista y los va sumando en 'acc' partiendo de un valor inicial.
        promedio_general = reduce(lambda acc, p: acc + p, promedios, 0) / len(promedios) if promedios else 0.0

        estructurado = {
            sem: [
                {
                    "materia": m["nombre"], 
                    "unidad_1": m["calificaciones"][0], 
                    "unidad_2": m["calificaciones"][1],
                    "promedio": round(sum(m["calificaciones"])/2, 1),
                    # Se pasa la tupla inmutable desempaquetada (*) a la función pura
                    "estatus": self.evaluar_materia_pura(*m["calificaciones"])
                } for m in mats
            ] for sem, mats in alumno["materias"].items()
        }

        salida = {
            "DatosPersonales": {"nombre": nombre, "edad": edad, "semestre": sem_actual, "direccion": direccion},
            "HistorialAcademico": {"promedio_general": round(promedio_general, 2), "materias": estructurado}
        }
        self.texto_resultado.insert(tk.END, json.dumps(salida, indent=4, ensure_ascii=False))


    def demo_filter_aprobadas_reprobadas(self):
        alumno = self._obtener_alumno_actual()
        self.texto_resultado.delete("1.0", tk.END)
        
        lista_mats = [{"nombre": m["nombre"], "estatus": self.evaluar_materia_pura(*m["calificaciones"])} 
                      for mats in alumno["materias"].values() for m in mats]
        
        # FILTER()
        # Filtra elementos de un iterable descartando los que no cumplan una condición.
        # Recibe una función lambda que devuelve True/False y una lista. 
        # Genera listas nuevas que contienen solamente materias aprobadas o reprobadas.
        datos = {
            "alumno": alumno["info"][0],
            "aprobadas": list(filter(lambda m: m["estatus"] == "Aprobado", lista_mats)),
            "reprobadas": list(filter(lambda m: m["estatus"] == "Reprobado", lista_mats))
        }
        self.texto_resultado.insert(tk.END, json.dumps(datos, indent=4, ensure_ascii=False))


    def demo_map_letras(self):
        alumno = self._obtener_alumno_actual()
        self.texto_resultado.delete("1.0", tk.END)
        
        # Función auxiliar para transformar el tipo de dato de entrada
        def a_letra(cal):
            if cal == 0: return "N/A"
            return "A" if cal >= 90 else "B" if cal >= 80 else "C" if cal >= 70 else "F"
            
        todas_mats = [m for mats in alumno["materias"].values() for m in mats]
        
        # MAP()
        # Aplica un cambio a todos los elementos de una colección y devuelve un iterador nuevo.
        # Se le pasa una función lambda y la lista de origen. La lambda extrayendo el nombre de la materia 
        # y mapea las calificaciones numéricas a sus equivalentes en letras.
        mapeadas = list(map(lambda m: {
            "materia": m["nombre"], 
            "u1_letra": a_letra(m["calificaciones"][0]),
            "u2_letra": a_letra(m["calificaciones"][1])
        }, todas_mats))
        
        self.texto_resultado.insert(tk.END, json.dumps({"alumno": alumno["info"][0], "resultado": mapeadas}, indent=4, ensure_ascii=False))


    def demo_generador(self):
        alumno = self._obtener_alumno_actual()
        self.texto_resultado.delete("1.0", tk.END)
        
        # GENERADORES (YIELD)
        # En lugar de calcular y retornar toda una colección gigante desde el principio, solo se basa en unos cuantos.
        # La función emite el valor calculado en ese ciclo y "pausa" su ejecución guardando su estado actual. Se reanuda cuando se solicita el siguiente valor.
        def generador_reporte():
            for sem, mats in alumno["materias"].items():
                for m in mats:
                    for i, cal in enumerate(m["calificaciones"], 1):
                        estado = f"Acreditada ({cal})" if cal >= 70 else ("No acreditada" if cal > 0 else "Sin cal.")
                        yield {"semestre": sem, "materia": m["nombre"], "unidad": i, "estado": estado}
                        
        self.texto_resultado.insert(tk.END, json.dumps({"bitacora": list(generador_reporte())}, indent=4, ensure_ascii=False))


    def demo_avance_curricular(self):
        alumno = self._obtener_alumno_actual()
        self.texto_resultado.delete("1.0", tk.END)
        
        # Se genera el historial completo iterando diccionarios sin modificar variables de estado intermedias.
        avance = {
            sem: [
                {"materia": m["nombre"], "promedio": round(sum(m["calificaciones"])/2, 1)} 
                for m in mats
            ] for sem, mats in alumno["materias"].items()
        }
        self.texto_resultado.insert(tk.END, json.dumps({"historial": avance}, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    app = SistemaEscolar()
    app.mainloop()
