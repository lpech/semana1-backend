import * as utils from "./utils.js"

function mostrarPar() {
    const numero = parseInt(document.getElementById("numero").value);
    if (utils.esPar(numero)) {
        alert(numero + " es par");
    } else {
        alert(numero + " no es par");
    }
    document.getElementById("numero").value = "";
};

function mostrarPrimo(){
    const numero = parseInt(document.getElementById("numero").value);
    if (utils.esPrimo(numero)) {
        alert(numero + " es primo");
    } else {
        alert(numero + " no es primo");
    }
    document.getElementById("numero").value = "";
};

function mostrarTareasNoCompletadas() {
    const tareas = utils.tareasNoCompletadas();
    alert("Tareas no completadas:\n" + tareas.map(tarea => tarea.descripcion).join("\n"));
};

window.mostrarPar = mostrarPar;
window.mostrarPrimo = mostrarPrimo;
window.mostrarTareasNoCompletadas = mostrarTareasNoCompletadas;
window.utils = utils; // Para acceder a las funciones desde la consola del navegador
