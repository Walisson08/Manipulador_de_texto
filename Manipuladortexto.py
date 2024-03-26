frase = "Curso em Video Python"
print(frase[::2]) #Fatiamento das letras da variavel. Primeiro inicio do fatiamento, segundo final dele, terceiro criterio.
print(len(frase)) #Vai contar o zero e todos os espaços para saber o tamanho.
print(frase.count('o')) # Vai contar todas as letras da variavel acima.
print(frase.count('o',0,12)) # Vai contar as letras com criterio de inicio e criterio final.
print(frase.find('deo')) # Vai encontrar pra mim onde começou a plavra e sua posição.
print('Curso' in frase) # Booleano com true e false para localizar palavra.
print(frase.replace('Python', 'Android')) # vai trocar a palavra por outra.
print(frase.upper()) # Vai deixa todos em caixa alta
print(frase.lower()) # Vai deixar todos em caixa baixa
print(frase.capitalize()) # vai deixar todos minusculos porem a primeira letra mantem letra maiuscula ou é colocado maiusculo.
print(frase.title()) # Todas as primeiras letras e tambem nos espaços terão caixa alta.
frase1 = '   Aprenda Python  '
print(frase1.strip()) # Tira os espaços desnecessarios.
print(frase1.rstrip()) #Tira os espaços desnecessarios da direita.
print(frase1.lstrip()) #Tira os espaços desnecessarios da esquerda.
print(frase1.split(), frase.split()) # Cria em espaços uma divisão de texto.
print('_'.join(frase)) # Coloca palavras nos espaços em branco.