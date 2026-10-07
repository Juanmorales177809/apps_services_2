"""Consumidor MQTT de ejemplo para el taller.

Este archivo solo demuestra cómo conectarse, suscribirse y visualizar mensajes.
No implementa las validaciones Pydantic, la persistencia en PostgreSQL ni la
lógica completa exigida por el taller.
"""

import json
import os
from datetime import datetime, timezone

import paho.mqtt.client as mqtt
from dotenv import load_dotenv


load_dotenv()

BROKER = os.getenv("MQTT_BROKER")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "iot/sensors/TEST-001/data")
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")
KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", "60"))


def on_connect(client, userdata, flags, reason_code, properties=None):
    """Se ejecuta cuando el cliente se conecta al broker."""
    if reason_code != 0:
        print(f"Error de conexión MQTT: {reason_code}")
        return

    print(f"Conectado al broker {BROKER}:{PORT}")
    result, _ = client.subscribe(TOPIC)
    if result != mqtt.MQTT_ERR_SUCCESS:
        print(f"No fue posible suscribirse a {TOPIC}: código {result}")
        return

    print(f"Suscrito al tópico: {TOPIC}")
    print("Esperando mensajes... Presiona Ctrl+C para finalizar.")


def on_message(client, userdata, message):
    """Se ejecuta cada vez que llega un mensaje al tópico suscrito."""
    received_at = datetime.now(timezone.utc).isoformat()

    try:
        payload = json.loads(message.payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        print(f"[{received_at}] Payload inválido en {message.topic}: {error}")
        return

    print(f"\n[{received_at}] Mensaje recibido")
    print(f"Tópico: {message.topic}")
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main():
    if not BROKER:
        raise RuntimeError(
            "Falta MQTT_BROKER. Configúralo en el archivo .env antes de ejecutar."
        )

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    if USERNAME:
        client.username_pw_set(USERNAME, PASSWORD or "")

    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Conectando a {BROKER}:{PORT}...")
    client.connect(BROKER, PORT, KEEPALIVE)
    client.loop_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nConsumidor detenido por el usuario.")
