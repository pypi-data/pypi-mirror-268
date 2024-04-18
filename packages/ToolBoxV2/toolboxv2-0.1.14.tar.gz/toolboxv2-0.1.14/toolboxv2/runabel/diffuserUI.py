import socket

NAME = "diffuserUI"
#  for windows pip install https://huggingface.co/r4ziel/xformers_pre_built/resolve/main/triton-2.0.0-cp310-cp310-win_amd64.whl
def get_local_ip():
    try:
        # Erstellt einen Socket, um eine Verbindung mit einem öffentlichen DNS-Server zu simulieren
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Verwendet Google's öffentlichen DNS-Server als Ziel, ohne tatsächlich eine Verbindung herzustellen
            s.connect(("8.8.8.8", 80))
            # Ermittelt die lokale IP-Adresse, die für die Verbindung verwendet würde
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception as e:
        print(f"Fehler beim Ermitteln der lokalen IP-Adresse: {e}")
        return "localhost"

def run(_, _0):
    from toolboxv2 import tbef
    import qrcode

    qr = qrcode.main.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=1,
        border=2,
    )
    qr.add_data(f'http://{get_local_ip()}:8501')
    qr.make(fit=True)

    qr.print_ascii(invert=True)

    _.run_any(tbef.DIFFUSER.START_UI)
    return

