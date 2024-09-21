import random
import base64

def generate_captcha():
    random_number = random.randint(100000, 999999)

    encoded_bytes = base64.b64encode(str(random_number).encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    
    captcha_code = encoded_str[:10]
    
    return captcha_code

if __name__ == "__main__":
    print("=== Login Form ===")
    
    captcha = generate_captcha()
    print(f"Captcha: {captcha}")
    
    user_input = input("Masukkan Captcha: ")
    
    if user_input == captcha:
        print("Captcha valid. Login berhasil.")
    else:
        print("Captcha tidak valid. Login gagal.")
