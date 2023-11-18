import qrcode

class MyQR:
    def __init__(self,size,padding) -> None:
        self.qr = qrcode.QRCode(box_size=size,border=padding)

    def create_gr(self,file_name,fg,bg):
        #user_input = input('insert your text: ')
        user_input = 'www.web.com'

        try:
            self.qr.add_data(user_input)
            qr_image =self.qr.make_image(fill_color=fg,back_color=bg)
            qr_image.save(file_name)
            print(f'its ok {file_name}')
        except:
            print('error e')

def main():
    myqr = MyQR(size=30,padding=2)
    myqr.create_gr('sample.png',
                   fg='black' ,bg='white')
    
main()