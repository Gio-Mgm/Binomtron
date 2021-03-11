from settings import students
from classes.Group import Group

class Student:
    def __init__(self, name, comp):
        """
            Student object initialization
        """
        self.name = name
        self.comp = comp


    def add():
        """
            add a student to the students list
        """
        Student.display_list()
        print("Entrez le nom de l'apprenant à ajouter à la liste :")
        new = input()
        if new:
            newstudent = [new, 0]
            students.append(newstudent)
        else:
            print("Erreur ! Saisie incorrecte !")
            print("Retour au menu :\n")
        Student.edit_list()

    def remove():
        """
            remove a student from the students list
        """
        Student.display_list()
        print("Entrez le numéro de l'apprenant à retirer de la liste :")
        x = input()
        if not x.isdigit() or int(x) < 0 or int(x) > len(students) - 1:
            print("Erreur ! Saisie incorrecte !")
            print("Retour au menu :\n")
            Student.edit_list()
        students.pop(int(x))
        Student.edit_list()

    def update():
        """
            update a student in the students list
        """
        Student.display_list()
        print("Entrez le numéro de l'apprenant à éditer :")
        x = input()
        if not x.isdigit() or int(x) < 0 or int(x) > len(students) - 1:
            print("Erreur ! Saisie incorrecte !")
            print("Retour au menu :\n")
            Student.edit_list()
        toEdit = int(x)
        print("Vous voulez éditer: {}".format(students[toEdit]))
        print("Entrez le nouveau nom")
        newName = input()
        if not newName:
            newName = students[toEdit][0]

        print("Entrez le niveau de compétences entre 0 et 3 :")
        newComp = input()
        if not newComp:
            newComp = students[toEdit][1]
        else:
            students[toEdit] = [newName, newComp]
        Student.edit_list()

    def edit_list():


        print("\n\033[4mGestion des apprenants\033[0m")
        print("\n1) Ajouter un apprenant,\n2) Supprimer un apprenant, \n3) Modifier un apprenant.\n0) Revenir au menu Principal")
        user_input = input()
        while user_input not in ["0","1", "2", "3"]:
            print("Merci d'entrer un chiffre compris entre 1 et 3,\nou 0 pour revenir au menu Principal : ")
            user_input = input()


        if user_input == "1":
            return Student.add()
        elif user_input == "2":
            return Student.remove()
        elif user_input == "3":
            return Student.update()
        else:
            Student.menu()

    def display_list():
        for i in range(len(students)):
            print("N°{} : {} ({})".format(i, students[i][0], students[i][1]))

    def menu():
        print("\nSuper-Binomtron à votre service !")
        print("\n\033[4mMenu principal\033[0m\n")
        print("1) Gérer la liste des apprenants\n2) Générer un groupe\n0) Quitter")
        user_input = input()
        while user_input not in ["0","1", "2"]:
            print("Merci de saisir 1 ou 2 , ou 0 pour quitter : ")
            user_input = input()
        if user_input == "1":
            Student.edit_list()
        elif user_input == "2":
            return Group.generateGroup()
        else:
            print("Au revoir")
