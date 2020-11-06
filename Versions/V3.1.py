from random import *

##### Description ####
#                    #
######################


''' Fonctions '''
def func_ini_matrice_parent(par_matrice_parent, par_nb_parent, par_nb_plage):
    for num_parent in range(par_nb_parent):
        if num_parent != 0:
            for num_plage in range(par_nb_plage):
                par_matrice_parent[num_parent][num_plage] = randint(0,1)

    par_matrice_parent[2][0] = 1




def func_ini_tab_corres(par_tab_corres_plage_heure, par_nb_plage, par_heure_debut):
    for num_plage in range(par_nb_plage):
        if num_plage == 0:
            heure_de_debut = par_heure_debut

        else:
            heure_de_debut = heure_de_fin

        #definit l'heure de fin du rdv selon heure_de_debut
        heures = int(heure_de_debut[0:2])
        minutes = int(heure_de_debut[3:4])
        if minutes == 0:
            minutes = 30
        else:
            heures += 1
            minutes = 0

        if minutes == 0:
            heure_de_fin = str(heures) + "H" + "00"
        else:
            heure_de_fin = str(heures) + "H" + str(minutes)

        par_tab_corres_plage_heure[num_plage] = heure_de_debut + " - " + heure_de_fin

def func_premiere_dispo_prof(par_matrice_prof, par_nb_plage): # renvoie le premier créneau disponible du prof
    ''' pour plus tard
    for num_prof in range(par_nb_prof):
        for num_plage in range(par_nb_plage):
            if par_matrice_prof[num_prof][num_plage] == -1:
                return
    '''

    for num_plage in range(par_nb_plage):
        if par_matrice_prof[0][num_plage] == -1:
            return num_plage

    return (-1)

def func_premier_parent_dispo(par_matrice_parent, par_nb_parent, par_plage, par_tab_pris, par_num_prof, par_ordre): # renvoie le premier parent dispo pour la plage et le prof donnés
    for num_parent in (par_ordre):
        if par_tab_pris[par_num_prof][num_parent] == 1 and par_matrice_parent[num_parent][par_plage] == 1:
            return num_parent

    return (-1)

def func_main(par_matrice_prof, par_matrice_parent, par_nb_plage, par_nb_parent, par_tab_pris, par_nb_prof, par_ordre):
    for num_plage in range(par_nb_plage):
        #Plage_dispo_prof = func_premiere_dispo_prof(Matrice_prof, nb_plage)
        for num_prof in range(par_nb_prof):
            if par_matrice_prof[num_prof][num_plage] == -1:
                Parent_dispo_meme_plage = func_premier_parent_dispo(par_matrice_parent, par_nb_parent, num_plage, par_tab_pris,num_prof, par_ordre)

                if Parent_dispo_meme_plage != -1 :
                    Matrice_prof[num_prof][num_plage] = Parent_dispo_meme_plage
                    par_tab_pris[num_prof][Parent_dispo_meme_plage] = 0
                    par_matrice_parent[Parent_dispo_meme_plage][num_plage] = 0

def func_affichage_rdv(par_nb_plage, par_tab_corres_plage_heure, par_matrice_prof, par_nb_prof):
    compteur = 0
    for num_prof in range (par_nb_prof):
        print(num_prof)
        for num_plage in range(par_nb_plage):
            #afficher l'horaire du créneau
            creneau = par_tab_corres_plage_heure[num_plage]
            parent_pour_creneau = str(par_matrice_prof[num_prof][num_plage])

            if parent_pour_creneau != "-1":
                print(creneau, ": parent", parent_pour_creneau)
                compteur += 1

    return compteur

def func_affichage_rdv_test(par_nb_plage, par_tab_corres_plage_heure, par_matrice_prof, par_nb_prof):
    compteur = 0
    for num_prof in range (par_nb_prof):
        #print(num_prof)
        for num_plage in range(par_nb_plage):
            #afficher l'horaire du créneau
            creneau = par_tab_corres_plage_heure[num_plage]
            parent_pour_creneau = str(par_matrice_prof[num_prof][num_plage])

            if parent_pour_creneau != "-1":
                #print(creneau, ": parent", parent_pour_creneau)
                compteur += 1

    return compteur

def func_affiche_edt(par_matrice, par_nb_personnes, par_type_personne):
    print("Emploi du temps :", par_type_personne)
    for num_personne in range(par_nb_personnes):
        print(par_type_personne, num_personne, ":", par_matrice[num_personne])

def func_ini_tab_tri(par_matrice_parent, par_nb_parent, par_tab_tri):
    for num_parent in range(nb_parent):
        par_tab_tri[num_parent][0] = num_parent
        par_tab_tri[num_parent][1] = par_matrice_parent[num_parent].count(1)




'''tri fusion'''

def func_fusion_copierTab(par_tab_source, par_indice_source, par_tab_dest, par_indice_dest):
    '''
    * Copie une partie du tableau dans un autre tableau
    * par_tab_tri : tableau source des valeurs à copier
    * par_indice_source : indice de départ de la copie dans la source
    * par_tab_dest : est tableau recevant les valeurs
    * par_indice_dest : indice de départ de la copie dans la destination
    '''
    while (par_indice_source < len(par_tab_source)):
        par_tab_dest[par_indice_dest] = par_tab_source[par_indice_source]
        par_indice_source = par_indice_source + 1
        par_indice_dest = par_indice_dest + 1

def func_fusion_fusionnerTab(par_tab1, par_tab2):
    '''
    * Fusionne deux tableau trié en un tableau trié
    * par_tab1 : tableau trié d’entiers
    * par_tab2 : tableau trié d’entiers
    * @return un tableau trié d’entiers contenant les valeurs des deux passés en paramètre
    '''
    tab = [0]* (len(par_tab1)+ len(par_tab2))
    i = 0
    i1 = 0
    i2 = 0
    while (i1 < len(par_tab1) and i2 < len(par_tab2)):
        if (par_tab1[i1][1] > par_tab2[i2][1]):
            tab[i] = par_tab2[i2]
            i2 = i2 + 1
        else:
            tab[i] = par_tab1[i1]
            i1 = i1 + 1

        i += 1

    if (i1 >= len(par_tab1)):
        func_fusion_copierTab(par_tab2, i2, tab, i)
    else:
        func_fusion_copierTab(par_tab1, i1, tab, i)

    return tab

def func_fusion_triFusionInterne(par_tab, par_debut, par_fin):
    '''
    * trie par fusion un tableau d’entiers
    * @param tab tableau d’entiers
    * @param d indice de debut du tableau
    * @param f indice de fin du tableau
    '''
    t = [[]]
    if (par_debut == par_fin):
        t[0] = par_tab[par_debut]
    else:
        milieu = int((par_debut + par_fin) / 2)
        t1 = func_fusion_triFusionInterne (par_tab, par_debut, milieu)
        t2 = func_fusion_triFusionInterne (par_tab, milieu + 1, par_fin)
        t = func_fusion_fusionnerTab (t1, t2)

    return t

def func_fusion_triFusion(par_tab):
    t = func_fusion_triFusionInterne(par_tab, 0, len(par_tab) - 1)
    func_fusion_copierTab(t, 0, par_tab, 0)

def func_creation_ordre(par_tab, par_nb_parent, par_ordre):
    for i in range(par_nb_parent):
        par_ordre[i] = par_tab[i][0]



''' Variables '''
nb_prof = 5
nb_parent = 3
duree_rdv = 30 # en min
nb_heure_dispo = 1 * 60
nb_plage = int(nb_heure_dispo / duree_rdv)
Matrice_prof = [[-1]*nb_plage for j in range(nb_prof)]     # -1 -> le prof n'a pas de rdv / chiffre -> le num de parent avec qui le prof a rdv
Matrice_parent = [[0]*nb_plage for j in range(nb_parent)] # 0  -> le parent n'est pas dispo / 1 -> le parent est dispo
Tab_pris = [[1]*nb_parent for j in range(nb_prof)]   # 0 -> le parent n'est pas dispo / 1 -> le parent est dispo
Tab_corres_plage_heure = [""] * nb_plage
Heure_de_debut = "12H00"
tab_tri = [[0]*2 for j in range(nb_parent)]
Matrice_parent_trier = [[0]*nb_plage for j in range(nb_parent)]
Tab_Ordre = [0]*nb_parent
nb_rdv = 0

''' Code '''

for nb_de_fois in range(10000):
    # Creation d'un exemple de matrice de parents
    func_ini_matrice_parent(Matrice_parent, nb_parent, nb_plage)


    func_ini_tab_tri(Matrice_parent, nb_parent, tab_tri)
    '''
    for i in range(nb_parent):
        print(tab_tri[i])
    '''
    #print("")

    func_fusion_triFusion(tab_tri)

    '''
    for i in range(nb_parent):
        print(tab_tri[i])
    '''

    #print("")

    func_creation_ordre(tab_tri, nb_parent, Tab_Ordre)

    #print(Tab_Ordre)

    func_ini_tab_corres(Tab_corres_plage_heure, nb_plage, Heure_de_debut)

    #func_affiche_edt(Matrice_prof, nb_prof,"prof")

    #print("")

    #func_affiche_edt(Matrice_parent, nb_parent, "parent")

    func_main(Matrice_prof, list(Matrice_parent), nb_plage, nb_parent, Tab_pris, nb_prof, Tab_Ordre)

    #print("")

    nb_rdv = nb_rdv + func_affichage_rdv_test(nb_plage, Tab_corres_plage_heure, Matrice_prof, nb_prof)

print("moyenne du nombre de  rdv :", nb_rdv/10000)
