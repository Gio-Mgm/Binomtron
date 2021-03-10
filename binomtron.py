#! /usr/bin/env python3
# coding: utf-8


from classes.Group import Group as G
from classes.Student import Student as S
import random

def menu():
    print("\nSuper-Binomtron à votre service !")
    print("\n\033[4mMenu principal\033[0m\n")
    print("1) Gérer la liste des apprenants\n2) Générer un groupe\n0) Quitter")
    user_input = input()
    while user_input not in ["0","1", "2"]:
        print("Merci de saisir 1 ou 2 , ou 0 pour quitter : ")
        user_input = input()
    if user_input == "1":
        S.edit_list()
    elif user_input == "2":
        return G.Group.generateGroup()
    else:
        print("Au revoir")


if __name__ == '__main__':
    menu()
