from src import gerar_poema

def main():
  print()
  palavra = input("Digite uma palavra ou frase: ")
  poema = gerar_poema(palavra)
  print(f"\nPoema Gerado:\n\n{poema}")

if __name__ == "__main__":
  main()
