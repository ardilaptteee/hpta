import os
import pandas as pd
from flask import Flask, render_template, request, jsonify

#Iicializar flask
app = Flask(__name__)

# Configuración de carpetas estatícas
app.config['static'] = 'static'
  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Contacto')
def Contacto(): 
   return render_template('Contacto.html')

@app.route('/Biblioteca')
def Biblioteca():
    return render_template('Biblioteca.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    datos = request.get_json()
    nombre = datos.get('nombre')
    correo = datos.get('correo')
    df = pd.DataFrame({"Nombre": [nombre], "Correo": [correo]})
    
    if os.path.isfile('datos.csv'):
        df.to_csv('datos.csv', index=False)
    else:
        pd.DataFrame(columns=["Nombre", "Correo"]).to_csv('datos.csv', index=False)



if __name__ == '__main__':
    app.run(debug=True)
