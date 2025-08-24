// Crea una función esPar(n) que devuelva true si el número es par.

export function esPar(n) {
    return n % 2 === 0;
};

// Crea una función es_primo(n) que determine si un número es primo.
export function esPrimo(n){
    if (n < 2) return false;
    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false;
    }
    return true;
};

// Crea una función filtrarTareas(tareas) que devuelva solo las tareas no completadas.
const tareas = [
    { id: 1, descripcion: "Aprender JavaScript", completada: true },
    { id: 2, descripcion: "Hacer la compra", completada: false },
    { id: 3, descripcion: "Estudiar para el examen", completada: true }
];

export function tareasNoCompletadas() {
    return tareas.filter(tarea => !tarea.completada);
};

