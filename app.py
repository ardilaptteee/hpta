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
    nuevo_dato = pd.DataFrame({"Nombre": [nombre], "Correo": [correo]})

    if os.path.exists("datos_contactos.csv"):
        df = pd.read_csv("datos_contactos.csv")
        df = pd.concat([df, nuevo_dato], ignore_index=True)
    else:
        df = nuevo_dato
        df.to_csv("datos_contactos.csv", index=False)   

    print(f"Nombre: {nombre}, Correo: {correo}")
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200


df = pd.DataFrame({
    "Nombre": ["Ana", "luis", "Carlos"],
    "Edad": [23, 30, 28],
})
print(df)

df = pd.read_excel("data\intento 1.xlsx")
print(df.head())

if __name__ == '__main__':
    app.run(debug=True)
