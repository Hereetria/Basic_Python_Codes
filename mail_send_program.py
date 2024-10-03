import sys
from PyQt5.QtWidgets import QWidget,QSpinBox,QLabel,QApplication,qApp,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QTextEdit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
class Mail_Programi(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.gonderici = QLabel("Gönderen:")
        self.sifre = QLabel("Şifre:")
        self.alici = QLabel("Alıcı:")
        self.mesaj_sayisi = QLabel("Mesaj Sayısı:")
        self.baslik = QLabel("başlık")
        self.yazi = QLabel("Konu:")
        self.gonderici_gir = QLineEdit()
        self.sifre_gir = QLineEdit()
        self.sifre_gir.setEchoMode(QLineEdit.Password)
        self.alici_gir = QLineEdit()
        self.yazi_gir = QTextEdit()
        self.durum = QLabel("")
        self.mesaj_sayisi_gir = QSpinBox()
        self.mesaj_sayisi_gir.setMinimum(1)
        self.mesaj_sayisi_gir.setMaximum(100)
        self.baslik_gir = QLineEdit()
        self.button1 = QPushButton("Gönder (Ctrl+G)")
        self.button2 = QPushButton("Temizle (Ctrl+T)")
        self.button3 = QPushButton("Programı Kapat (Ctrl+Q)")

        h_box = QHBoxLayout()
        h_box.addWidget(self.button1)
        h_box.addWidget(self.button2)
        h_box.addWidget(self.button3)

        v_box = QVBoxLayout()
        v_box.addWidget(self.gonderici)
        v_box.addWidget(self.gonderici_gir)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.sifre_gir)
        v_box.addWidget(self.alici)
        v_box.addWidget(self.alici_gir)
        v_box.addWidget(self.baslik)
        v_box.addWidget(self.baslik_gir)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.yazi_gir)
        v_box.addWidget(self.mesaj_sayisi)
        v_box.addWidget(self.mesaj_sayisi_gir)
        v_box.addWidget(self.durum)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setGeometry(470,140,400,500)
        self.setWindowTitle("Mail Gönderme Programı")

        self.button1.clicked.connect(self.mail_gonder)
        self.button2.clicked.connect(self.temizle)
        self.button3.clicked.connect(self.cikis)

        self.button1.setShortcut("Ctrl+G")
        self.button2.setShortcut("Ctrl+T")
        self.button3.setShortcut("Ctrl+Q")

        self.show()

    def mail_gonder(self):
        mesaj = MIMEMultipart()
        mesaj["From"] = self.gonderici_gir.text()
        mesaj["To"] = self.alici_gir.text()
        mesaj["Subject"] = self.baslik_gir.text()
        yazi = self.yazi_gir.toPlainText()
        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()

            app_parola = self.sifre_gir.text()
            mail.login(self.gonderici_gir.text(),app_parola)

            mesaj_sayisi = self.mesaj_sayisi_gir.value()
            basarili_mesajlar = 0

            for _ in range(mesaj_sayisi):
                try:
                    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                    basarili_mesajlar += 1
                except:
                    self.durum.setText(f"Mail Gönderme Başarısız: {basarili_mesajlar}/{mesaj_sayisi}")

            if mesaj_sayisi == basarili_mesajlar:
                self.durum.setText("Mail Gönderme Başarılı")
        
        except:
            self.durum.setText("Bir sorun oluştu")
            sys.stderr.flush()
        finally:
            mail.quit()

    def temizle(self):
        self.gonderici_gir.clear()
        self.alici_gir.clear()
        self.sifre_gir.clear()
        self.baslik_gir.clear()
        self.mesaj_sayisi_gir.clear()
        self.yazi_gir.clear()
        self.durum.setText("")

    def cikis(self):
        qApp.quit()

app = QApplication(sys.argv)
mail_programi = Mail_Programi()
sys.exit(app.exec_())
