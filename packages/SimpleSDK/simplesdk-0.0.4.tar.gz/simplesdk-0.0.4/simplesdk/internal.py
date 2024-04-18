from datetime import datetime, timedelta
import requests
import random
from threading import Thread
from time import sleep
import hashlib
from os import environ as env
from uuid import uuid4
import yaml


def safe_hash(value: str, salt: str = str(env.get("ET_SALT"))):
    salted_password = salt[::-1] + value + salt
    salted_password = salted_password[::-1] + salted_password
    hash = hashlib.sha512(salted_password.encode()).hexdigest()
    return hash


class AlphacrmSDK:
    def __init__(self, user, password, base):
        self.user = user
        self.password = password
        self.base = base

    def auth(self):
        """Genera un token y header a partir del usuario y contraseña del cliente."""
        json_data = {
            "username": self.user,
            "password": self.password,
        }
        response = requests.post(self.base + "/api/auth", json=json_data)
        tok = response.json()["token"]
        headers = {"Authorization": "Bearer " + tok}
        return headers, tok

    def users(self):
        """Lista de aulas"""
        headers, tok = self.auth()
        response = requests.get(
            self.base + "/api/et_alphacrm/clientes/v1?verbose=1", headers=headers
        ).json()
        return response

    def productos(self):
        """Lista de aulas"""
        headers, tok = self.auth()
        response = requests.get(
            self.base + "/api/et_alphacrm/productos/v1?verbose=1", headers=headers
        ).json()
        return response

    def register(self, data):
        """Lista de aulas"""
        headers, tok = self.auth()
        response = requests.post(
            self.base + "/api/et_alphacrm/clientes/v1?verbose=1",
            headers=headers,
            json=data,
        ).json()
        return response

    def login_with_combo(self, email, password):
        """Lista de aulas"""
        hash = safe_hash(password)
        user = next(
            (
                user
                for user in self.users()
                if user["0(clientes)"]["correo"] == email
                and user["0(clientes)"]["clave_hash"] == hash
            ),
            None,
        )
        if user != None:
            update = user
            update["0(clientes)"]["session"] = uuid4().hex
            self.register(update)
            return update
        else:
            return None

    def login_with_session(self, session):
        """Lista de aulas"""
        user = next(
            (
                user
                for user in self.users()
                if user["0(clientes)"]["session"] == session
            ),
            None,
        )
        return user


class AulaSDK:
    def __init__(self, user, password, base):
        self.user = user
        self.password = password
        self.base = base

    def today(self):
        now = datetime.now()
        return f"{now.year}-{now.month:02d}-{now.day:02d}"

    def timestamp(self, value):
        now = datetime.fromtimestamp(value)
        return f"{now.year}-{now.month:02d}-{now.day:02d}"

    def today_rbetween(self, value, max_val: int, min_val: int):
        max = datetime.now() + timedelta(max_val, hours=3)
        min = datetime.now() - timedelta(min_val, hours=3)
        value = datetime.fromisoformat(value)
        if min <= value <= max:
            return True
        else:
            return False

    def auth(self):
        """Genera un token y header a partir del usuario y contraseña del cliente."""
        json_data = {
            "username": self.user,
            "password": self.password,
        }
        response = requests.post(self.base + "/api/auth", json=json_data)
        tok = response.json()["token"]
        headers = {"Authorization": "Bearer " + tok}
        return headers, tok

    ### Aulas
    def aulas__all(self):
        """Lista de aulas"""
        headers, tok = self.auth()
        response = requests.get(
            self.base + "/api/et_axelaula/aulas/v1?verbose=1", headers=headers
        ).json()
        return response

    def aulas__getByCode(self, code: str):
        """Ver aula por codigo"""
        aulas = self.aulas__all()
        aula = next(aula for aula in aulas if aula["0(aulas)"]["code"] == code)
        return aula

    def aulas__getById(self, id: str):
        """Ver aula por codigo"""
        aulas = self.aulas__all()
        aula = next(aula for aula in aulas if aula["0(aulas)"]["id"] == id)
        return aula

    ### Alumnos
    def alumnos__all(self):
        """Lista de alumnos"""
        headers, tok = self.auth()
        response = requests.get(
            self.base + "/api/et_axelaula/alumnos/v1?verbose=1", headers=headers
        ).json()
        return response

    def alumnos__filter(self, aula: int):
        """Lista filtrada de alumnos"""
        al = self.alumnos__all()
        e = [a for a in al if a["0(alumnos)"]["aula"] == aula]
        return e

    def alumnos__get(self, id: int):
        """Ver alumno por id"""
        alumnos = self.alumnos__all()
        aula = next(alumno for alumno in alumnos if alumno["0(alumnos)"]["id"] == id)
        return aula

    def alumnos__new(
        self, aula: int, correo: str, detalles: str, nombre: str, telefono: str
    ):
        """Nuevo alumno"""
        nid = random.randrange(314, 99999999)
        obj = {
            "0(alumnos)": {
                "id": nid,
                "aula": aula,
                "correo": correo,
                "detalles": detalles,
                "nombre": nombre,
                "telefono": telefono,
            }
        }
        headers, tok = self.auth()
        response = requests.post(
            self.base + "/api/et_axelaula/alumnos/v1?verbose=1",
            json=obj,
            headers=headers,
        ).json()
        return nid

    def alumnos__edit(
        self, id: int, aula: int, correo: str, detalles: str, nombre: str, telefono: str
    ):
        """Editar alumno"""
        obj = {
            "0(alumnos)": {
                "id": id,
                "aula": aula,
                "correo": correo,
                "detalles": detalles,
                "nombre": nombre,
                "telefono": telefono,
            }
        }
        headers, tok = self.auth()
        response = requests.post(
            self.base + "/api/et_axelaula/alumnos/v1?verbose=1",
            json=obj,
            headers=headers,
        ).json()
        return True

    def alumnos__delete(self, alumno: int):
        """Eliminar alumno"""
        headers, tok = self.auth()
        requests.delete(
            self.base + "/api/et_axelaula/alumnos/v1/" + str(alumno), headers=headers
        )
        return True

    ### Tareas
    def tareas__all(self):
        """Lista de tareas"""
        headers, tok = self.auth()
        response = requests.get(
            self.base + "/api/et_axelaula/tareas/v1?verbose=1", headers=headers
        ).json()
        return response

    def tareas__filter(self, aula: int):
        """Lista filtrada de tareas"""
        al = self.tareas__all()
        e = [a for a in al if a["0(tareas)"]["aula"] == aula]
        return e

    def tareas__get(self, id: int):
        """Ver tarea por id"""
        alumnos = self.tareas__all()
        aula = next(alumno for alumno in alumnos if alumno["0(tareas)"]["id"] == id)
        return aula

    def tareas__new(self, aula: int, alumno: str, tarea: str, fecha: str, orden: int):
        """Nueva tarea"""
        nid = random.randrange(314, 99999999)
        obj = {
            "0(tareas)": {
                "id": nid,
                "fecha": fecha,
                "orden": orden,
                "tarea": tarea,
                "alumno": alumno,
                "aula": aula,
            }
        }
        headers, tok = self.auth()
        requests.post(
            self.base + "/api/et_axelaula/tareas/v1?verbose=1",
            json=obj,
            headers=headers,
        )
        return nid

    def tareas__edit(
        self, id: int, aula: int, alumno: str, tarea: str, fecha: str, orden: int
    ):
        """Nuevo alumno"""
        obj = {
            "0(tareas)": {
                "id": id,
                "fecha": fecha,
                "orden": orden,
                "tarea": tarea,
                "alumno": alumno,
                "aula": aula,
            }
        }
        headers, tok = self.auth()
        requests.post(
            self.base + "/api/et_axelaula/tareas/v1?verbose=1",
            json=obj,
            headers=headers,
        )
        return True

    def tareas__delete(self, tarea: int):
        """Eliminar alumno"""
        headers, tok = self.auth()
        requests.delete(
            self.base + "/api/et_axelaula/tareas/v1/" + str(tarea), headers=headers
        )
        return True

    ### Comedor
    def comedor__all(self):
        """Menu Comedor"""
        headers, tok = self.auth()
        response = requests.get(
            self.base + "/api/et_axelaula/comedor/v1?verbose=1", headers=headers
        ).json()
        return response

    def comedor__filter(self, comedor: str):
        """Lista filtrada de Comedor"""
        al = self.comedor__all()
        e = (
            {
                "mensaje": str(alumno["0(comedor)"]["mensaje"]),
                "fecha": alumno["0(comedor)"]["fecha"],
            }
            for alumno in al
            if alumno["1(aulas)"]["code"] == comedor
            and self.today_rbetween(alumno["0(comedor)"]["fecha"], 12, 12)
        )
        return e

    def comedor__hoy(self, comedor):
        """Menu Comedor para Hoy"""
        all = self.comedor__filter(comedor)
        menu = next(
            (alumno["mensaje"] for alumno in all if alumno["fecha"] == self.today()),
            None,
        )
        return menu


class AulaData:
    obj = {
        "request": {
            "args": {},
        },
        "aula": {
            "exists": True,
        },
        "error": "",
        "alumnos": [],
        "tareas": [],
        "comedor": {},
        "comedor_reciente": [],
        "today": "",
        "funcs": [],
        "template": "base.html",
    }
    comedor_code = ""
    status = 0

    def __init__(self, aula_code: str, http_args: dict, client: AulaSDK):
        self.aula = client.aulas__getByCode(aula_code)["0(aulas)"]
        self.aula_code = aula_code
        self.comedor_code = self.aula["comedor"]
        self.obj["request"]["args"] = http_args
        if http_args.get("embed") != None:
            self.obj["template"] = "embed.html"
        self.client = client
        self.obj["today"] = client.today()

    def get_tareas(self):
        self.obj["tareas"] = list(self.client.tareas__filter(self.aula["id"]))
        self.status += 1

    def get_alumnos(self):
        self.obj["alumnos"] = list(self.client.alumnos__filter(self.aula["id"]))
        self.status += 1

    def get_comedor(self):
        self.obj["comedor"] = self.client.comedor__hoy(self.comedor_code)
        self.status += 1

    def get_comedor_reciente(self):
        self.obj["comedor_reciente"] = list(
            self.client.comedor__filter(self.comedor_code)
        )
        self.status += 1

    def get_funcs(self):
        self.obj["funcs"] = str(
            self.aula["funcs"]
        ).split()  # Split by spaces, deleting empty strings.
        self.status += 1

    def run(self):
        """Runs all requests in parallel"""
        Thread(target=self.get_tareas, name="get tareas").start()
        Thread(target=self.get_alumnos, name="get tareas").start()
        Thread(target=self.get_comedor, name="get comedor").start()
        Thread(target=self.get_comedor_reciente, name="get comedor reciente").start()
        Thread(target=self.get_funcs, name="get funcs").start()
        while self.status < 5:
            sleep(0.01)
        return self.obj


class AutoAula:
    def __init__(self, sdk: AulaSDK):
        self.sdk = sdk

    def get_year_day(self):
        return datetime.now().timetuple().tm_yday

    def get_aula_id(self, aula_code: str):
        return self.sdk.aulas__getByCode(aula_code)["0(aulas)"]["id"]

    def create_task(
        self, config: dict, alumno: str, tarea: str, fecha: str, orden: int
    ):
        id = self.get_aula_id(config["aula"])
        self.sdk.tareas__new(id, alumno, tarea, fecha, orden)

    def run_daily(self, config: dict, aula_code: str, dry_run: bool = False):
        print(f"=== Ejecutando AutoAula para {config.get('friendly_name', aula_code)}")
        self.sdk.auth()
        iT = 0
        cT = 0
        for tarea in config["tareas"]:
            i = self.get_year_day() % len(tarea["alumnos"])
            a = tarea["alumnos"][i]
            t = tarea["tarea"]
            o = tarea["orden"]
            f = datetime.now().isoformat().split("T")[0]
            iT += 1
            if not dry_run:
                self.create_task(config, a, t, f, o)
                cT += 1
        print(f"{iT} tarea(s) procesada(s), {cT} tarea(s) creada(s)")

    def run_all(self):
        enabled = [
            a
            for a in self.sdk.aulas__all()
            if "autoaula_enabled" in a["0(aulas)"]["funcs"]
        ]
        for aula in enabled:
            config = yaml.safe_load(aula["0(aulas)"]["autoaula_conf"])
            self.run_daily(config, aula["0(aulas)"]["code"])
