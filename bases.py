import base64
import base58
import base45
import re

input_str = input('Digite a string codificada: ')

decodings = []

# Funções de decodificação de diferentes bases
def try_decode_base16(s):
    try:
        decoded_bytes = base64.b16decode(s.upper(), casefold=True)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def try_decode_base32(s):
    try:
        decoded_bytes = base64.b32decode(s.upper(), casefold=True)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def try_decode_base64(s):
    try:
        decoded_bytes = base64.b64decode(s)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def try_decode_base85(s):
    try:
        decoded_bytes = base64.b85decode(s)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def try_decode_base58(s):
    try:
        decoded_bytes = base58.b58decode(s)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def try_decode_base45(s):
    try:
        decoded_bytes = base45.b45decode(s)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

# Define um dicionário de bases com funções de decodificação e regex para encontrar padrões válidos
bases = [
    ('Base16', try_decode_base16, r'[A-Fa-f0-9]+'),
    ('Base32', try_decode_base32, r'[A-Z2-7]+=*'),
    ('Base45', try_decode_base45, r'[A-Z0-9 $%*+-./:]+'),
    ('Base58', try_decode_base58, r'[1-9A-HJ-NP-Za-km-z]+'),
    ('Base64', try_decode_base64, r'[A-Za-z0-9+/]+=*'),
    ('Base85', try_decode_base85, r'[!-u]+'),
]

# Detecta e decodifica substrings em cada base
for base_name, decode_func, pattern in bases:
    for match in re.finditer(pattern, input_str):
        substring = match.group(0)
        decoded_str = decode_func(substring)
        if decoded_str:
            decodings.append((base_name, substring, decoded_str))

# Exibe resultados
if decodings:
    print(f'Entrada: {input_str}')
    for base_name, substring, decoded_str in decodings:
        print(f'Base Detectada: {base_name}')
        print(f'Substring Codificada: {substring}')
        print(f'Frase Decodificada: {decoded_str}')
else:
    print('Não foi possível decodificar substrings válidas com as bases especificadas.')
