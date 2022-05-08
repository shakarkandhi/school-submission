from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
import qrcode
import plyer
from cryptography.fernet import Fernet
from PIL import Image
from pyzbar.pyzbar import decode
key1 = b'ARdWVYi6meZGpeHv-EVoev6pp8yyMSamsSILn2hVoT4='
key2 = b'Y6nRsVn_4Hek50q89OXaZnAV8hRjdBwO0bwHS9e4qmE='
fernet1 = Fernet(key1)
fernet2 = Fernet(key2)
class Function(ScreenManager):
    def generate_qr_code(self,root):
        if self.ids.link_text.text != '':
            name="temp"
            encMessage = fernet1.encrypt(self.ids.link_text.text.encode())
            encMessage = fernet2.encrypt(encMessage)
            code=qrcode.QRCode(version=1.0, box_size=15, border=4)
            code.add_data(encMessage)
            code.make(fit=True)
            img=code.make_image(fill = 'Black',back_color='White')
            img.save(f"{name}.png")
            #img.save(f"{path}/{name}.png")
            plyer.notification.notify(
                title = 'QR Code Generator',message="QR Code Generated"
            ) 
            self.ids.img_.source=f"{name}.png"
            root.current="image"
        else:
            plyer.notification.notify(
                title = 'QR Code Generator',message="Input Field is Empty"
            )
    
    def make_another(self,root):
        self.ids.link_text.text = ''
        root.current="gen"
    def read(self):
        try:
            camera = self.ids['camera']
            camera.export_to_png("temp.png")
            data=decode(Image.open('temp.png'))
            decMessage = fernet2.decrypt(data[0].data)
            decMessage = fernet1.decrypt(decMessage).decode()
            self.ids.output=decMessage
            root.current="opt"
        except:pass
        

class Main(MDApp):
    Builder.load_file('layout.kv')
    def build(self):
        self.title = 'QR Code Generator/Scanner'
        return Function()

Main().run()