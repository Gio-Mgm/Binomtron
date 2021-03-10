class Group:
    def __init__(self, isBySize, number, randomParam):
        """
            Group object initialization

            params:
            self : self
            isBySize(bool) : true : size , false : nb of group
            number(int) : number for size or number of group
            randomParam(str) : heterogeneous, homogeneous, random

            returns: (object)

        """
        self.isBySize = isBySize
        self.number = number
        self.randomParam = randomParam

    def getListCopy():
        """
            Get list of students

            returns: (list)

        """
        return students.copy()

    def distrib():
        """
            Get distribution type

            returns: (string)

        """
        print("Quel type de distribution voulez-vous ?\n1) Aléatoire\n2) Par compétence")
        x = input().lower()
        choice = ""
        if x == '1':
            choice ='random'
        elif x == "2":
            choice = Group.distribHH()
        else:
            print("Veuillez saisir 1 ou 2")
            Group.distrib()

        return choice

    def distribHH():
        """
            Get distribution type if not "random" ("homogeneous" or "heterogeneous")

            returns: (string)

        """
        print("Quelle répartition spécifique voulez-vous ?\n1) Hétérogène\n2) Homogène")
        x = input()
        choice =""
        if x == '1':
            choice = 'heterogeneous'
        elif x == '2':
            choice =  'homogeneous'
        else:
            print(" Veuillez saisir 1 ou 2 ")
            Group.distribHH()

        return choice

    def sortType():
        """
            Get sort type

            returns: (boolean)

        """

        print("Quelle méthode de tri?\n1) Tri par nombre de groupes\n2) Tri par nombre d'apprenants par groupe")
        sort_type = input()

        if sort_type == '1':
            return False
        elif sort_type == '2':
            return True
        else:
            print("Veuillez saisir 1 ou 2\n")
            Group.sortType()

    def groupValue():
        """
            Get numeric value of input for size of group or number of groups

            returns: (int)

        """
        print('Quelle nombre voulez-vous ?')
        group_value=input()
        if group_value.isdigit():
            return int(group_value)
        else:
            Group.groupValue()

    def sortBySkill(listToSort) :
        """
            Sort list of groups by skill level

            returns: (list)
        """
        def skill(s) :
            return s[1]

        return sorted(listToSort, key=skill)

    def format_output(groups):

        for i, group in enumerate(groups):
            print("Groupe n°{} :\n".format(i+1))
            for x, student in enumerate(group):
                print("({1}) {0}".format(student[0], student[1]))
            print("\n")

    def generateGroup():
        """
           Generate groups from object Group,
           which contains parameters

           returns: (list)
        """

        print("\n\033[4mGénérateur de groupe\033[0m\n")
        # Initialisation objet Group
        s = Group(Group.sortType(), Group.groupValue(), Group.distrib())
        print('Fin de la sélection des paramètres\n')
        pool = []
        pool_r= []
        groups = []
        nbGroups = s.number
        # Si la répartition est aléatoire, on récupère une copie de la liste des apprenants
        if s.randomParam == "random":
            pool = Group.getListCopy()
        # Sinon on récupère une version triée par compétences de la liste
        else:
            pool = Group.sortBySkill(students)
        # initialisation du nombre de groupes
        if s.isBySize:
            nbGroups = len(pool) // s.number
        for i in range (len(pool)):
            if s.randomParam == "random" :
                # choix aléatoire dans la liste
                r = random.choice(pool)
            else:
                # ou choix ordonné
                r = pool[0]

            pool_r.append(r)
            pool.remove(r)

        # si groupe homogène
        if s.randomParam == "homogeneous":
            size = len(pool_r) // nbGroups
            group = []
            for i in range(len(pool_r)):
                group.append(pool_r[i])
                if (i+1) % size == 0:
                    groups.append(group)
                    group = []

            # Si les groupes ne sont pas de même taille
            # Répartir les personnes restantes dans les groupes existants
            # ie : groupe de 3 personnes ->
            #      5 groupes de 3 personnes + 1 groupe de 1 personne

            if len(pool_r) % nbGroups != 0:
                i = 0
                while i < len(pool_r) % nbGroups :
                    groups[i].append(pool_r[-i])
                    i += 1
        # si groupe hétérogène
        else:
            for i in range(nbGroups):
                groups.append([])
            for i in range(len(pool_r)):
                groups[(i%len(groups))].append(pool_r[i])
        print('Affichage des résultats\n')
        Group.format_output(groups)
