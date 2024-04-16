from cryptography.fernet import Fernet


class DataHandler:
    encrypt_key = "vuK4GTj-6ZVFZ4HON52Oty5Qnovh0oikWhGF500_SkQ="

    @classmethod
    def _encrypt_it(cls, decrypted_val: str) -> str:
        try:
            fernet = Fernet(cls.encrypt_key)
            encrypted_val = fernet.encrypt(decrypted_val.encode('utf-8'))
        except Exception as e:
            assert False, 'Exception during decryption ' + str(type(e))

        return encrypted_val.decode()

    @classmethod
    def decrypt_it(cls, encrypted_val: str) -> str:
        try:
            fernet = Fernet(cls.encrypt_key)
            decrypted_val = fernet.decrypt(encrypted_val).decode()
        except Exception as e:
            assert False, 'Exception during decryption ' + str(type(e))

        return decrypted_val


# var = DataHandler._encrypt_it('ABC123')
# print(var)
# var = DataHandler.decrypt_it(var)
# print(var)
