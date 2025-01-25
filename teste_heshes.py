def verificar_hashes(lista_hashes):
  for hash_comparacao in lista_hashes:
    hash_calculado, hash_esperado = hash_comparacao.split(",")
    
    if hash_calculado.strip() == hash_esperado.strip():
      print("Correto")
    else:
      print("Inválido")

hashes_usuario = input()

lista_hashes = hashes_usuario.split(";")

verificar_hashes(lista_hashes)