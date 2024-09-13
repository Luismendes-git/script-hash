import hashlib

def calcular_hash(arquivo_txt, algoritmo='sha256'):
    
    hash_obj = hashlib.new(algoritmo)
    
    
    with open(arquivo_txt, 'rb') as f:
        
        for bloco in iter(lambda: f.read(4096), b""):
            hash_obj.update(bloco)
    
    
    return hash_obj.hexdigest()


arquivo = 'script.txt'
hash_resultado = calcular_hash(arquivo)
print(f'O hash do arquivo {arquivo} é: {hash_resultado}')
