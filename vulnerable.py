import yaml
import subprocess
import pickle
import hashlib
from flask import Flask, request

app = Flask(__name__)

# === Ejemplo 1: PyYAML inseguro ===
def load_config(path):
    with open(path, "r") as f:
        # yaml.load sin Loader seguro → vulnerable a ejecución arbitraria
        return yaml.load(f, Loader=None)


# === Ejemplo 2: Subprocess con shell=True ===
def run_command(cmd):
    # Permite inyección de comandos si 'cmd' viene de input externo
    subprocess.Popen(cmd, shell=True)


# === Ejemplo 3: Uso inseguro de pickle ===
def deserialize(data):
    # Pickle carga objetos arbitrarios → RCE si el input es controlado
    return pickle.loads(data)


# === Ejemplo 4: Hash inseguro (MD5) ===
def hash_password(password):
    # MD5 es inseguro para contraseñas
    return hashlib.md5(password.encode()).hexdigest()


# === Ejemplo 5: XSS / Inyección en Flask ===
@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    # Devolver input sin escapar → XSS reflejado
    return f"<h1>Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
