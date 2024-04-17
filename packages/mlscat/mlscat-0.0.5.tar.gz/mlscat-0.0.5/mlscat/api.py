from . import utils

def get_sbox(algorithm='AES'):
    if algorithm == 'AES':
        return utils.AES_Sbox
    else:
        return "Can not search this algorithm's sbox"