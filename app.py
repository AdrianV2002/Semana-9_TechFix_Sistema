from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    equipos = ['PC-GAMER', 'LAPTOP', 'MACBOOK', 'IMPRESORA', 'CELULAR']
    numero = random.randint(100, 999)
    codigo_generado = f"{random.choice(equipos)}-{numero}"
    return render_template('index.html', ticket_aleatorio=codigo_generado)

@app.route('/ticket/<codigo>')
def consultar_ticket(codigo):
    return render_template('ticket.html', codigo=codigo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/servicios')
def servicios():
    lista_servicios = [
        {"nombre": "Mantenimiento Preventivo", "tiempo": "2 horas", "precio": 35.00},
        {"nombre": "Instalación de Sistema Operativo", "tiempo": "1 hora", "precio": 25.00},
        {"nombre": "Limpieza de Hardware", "tiempo": "3 horas", "precio": 45.00}
    ]
    return render_template('servicios.html', servicios=lista_servicios)

@app.route('/clientes')
def clientes():
    lista_clientes = [
        {"nombre": "Empresa ABC", "equipo": "Servidor Dell", "estado": "VIP"},
        {"nombre": "Carlos Mendoza", "equipo": "PC Gamer", "estado": "Regular"},
        {"nombre": "Ana Torres", "equipo": "MacBook Air", "estado": "Nuevo"}
    ]
    return render_template('clientes.html', clientes=lista_clientes)

if __name__ == '__main__':
    app.run(debug=True)