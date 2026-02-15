from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ticket/<codigo>')
def consultar_ticket(codigo):
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="card shadow border-info">
                <div class="card-header bg-info text-white">
                    <h5>Consulta de Estado</h5>
                </div>
                <div class="card-body text-center">
                    <h2 class="card-title">Ticket: {codigo}</h2>
                    <p class="card-text mt-3">Estado actual: <span class="badge bg-warning text-dark">En Diagnóstico</span></p>
                    <hr>
                    <a href="/" class="btn btn-primary">Volver al Inicio</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)