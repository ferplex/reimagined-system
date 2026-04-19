import sys
import os
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QHBoxLayout, QWidget, QPushButton, QLabel)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QTimer, Qt

class AthenaFinal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATHENA-AXON-DEMO | FERPLEX CORPORATE")
        self.setGeometry(100, 100, 1280, 720)
        self.precio_base = 0.5245
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- PANEL LATERAL ---
        side_panel = QVBoxLayout()
        container_side = QWidget()
        container_side.setStyleSheet("background-color: #000000; border-right: 2px solid #ff00ff;")
        container_side.setFixedWidth(320)
        
        self.label_titulo = QLabel("🛡️ ATHENA-AXON\nUNIFIED SYSTEM")
        self.label_titulo.setStyleSheet("color: #ff00ff; font-weight: bold; font-size: 20px; padding: 20px;")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_precio = QLabel(f"POL/USDT\n${self.precio_base}")
        self.label_precio.setStyleSheet("color: #00ff00; font-size: 28px; font-family: monospace; background: #111; border: 1px solid #00ff00; border-radius: 5px; padding: 15px;")
        self.label_precio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_apoyo = QPushButton("⚡ APOYO PARA LA LUZ")
        btn_apoyo.setStyleSheet("background-color: #ff8c00; color: black; font-weight: bold; font-size: 16px; border-radius: 10px; height: 60px; margin: 20px;")
        btn_apoyo.clicked.connect(self.mostrar_qr)
        
        side_panel.addWidget(self.label_titulo)
        side_panel.addSpacing(20)
        side_panel.addWidget(self.label_precio)
        side_panel.addStretch()
        side_panel.addWidget(btn_apoyo)
        container_side.setLayout(side_panel)

        # --- PANEL DERECHO ---
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com")) 
        
        main_layout.addWidget(container_side)
        main_layout.addWidget(self.browser)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_mercado)
        self.timer.start(2000)

    def actualizar_mercado(self):
        self.precio_base += random.uniform(-0.001, 0.001)
        self.label_precio.setText(f"POL/USDT\n${self.precio_base:.4f}")

    def mostrar_qr(self):
        # USAMOS LA RUTA QUE VIMOS EN TU LS
        ruta_foto = "/home/luis/reimagined-system/qr_pago.png"
        
        if os.path.exists(ruta_foto):
            print(f"[OK] Desplegando: {ruta_foto}")
            # Inyectamos HTML para evitar bloqueos de seguridad de archivos locales
            html_content = f"""
            <html>
            <body style="background-color:black; margin:0; display:flex; justify-content:center; align-items:center; height:100vh;">
                <img src="file://{ruta_foto}" style="max-width:80%; border:10px solid #ff00ff; border-radius:20px;">
            </body>
            </html>
            """
            self.browser.setHtml(html_content, QUrl("file://"))
        else:
            print(f"[!] Error: No se encuentra en {ruta_foto}")
            self.browser.setUrl(QUrl("https://www.google.com/search?q=POL+Polygon+Price"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AthenaFinal()
    window.show()
    sys.exit(app.exec())
    
def mostrar_qr(self):
        import base64
        ruta_foto = "/home/luis/reimagined-system/qr_pago.png"
        
        if os.path.exists(ruta_foto):
            try:
                with open(ruta_foto, "rb") as f:
                    # Convertimos la imagen a texto para que el navegador no la bloquee
                    encoded_string = base64.b64encode(f.read()).decode()
                
                print(f"[OK] Desplegando Blindaje Maestro...")
                html_content = f"""
                <html>
                <body style="background-color:black; margin:0; display:flex; justify-content:center; align-items:center; height:100vh;">
                    <img src="data:image/png;base64,{encoded_string}" 
                         style="max-width:85%; border:5px solid #ff00ff; border-radius:15px; box-shadow: 0 0 20px #ff00ff;">
                </body>
                </html>
                """
                self.browser.setHtml(html_content)
            except Exception as e:
                print(f"[!] Error al leer la imagen: {e}")
        else:
            print(f"[!] Error: No se encuentra en {ruta_qr}")
            self.browser.setUrl(QUrl("https://www.google.com"))
