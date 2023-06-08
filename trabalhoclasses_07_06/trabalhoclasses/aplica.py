from classes.MenuGerenciadorS3 import MenuGerenciadorS3
nome_bucket = "aulanoitethallyssonn"  # Substitua pelo nome do seu bucket
menu = MenuGerenciadorS3(nome_bucket)
menu.executar()