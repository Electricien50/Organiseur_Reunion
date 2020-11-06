from random import *

##### Description ####
#                    #
######################


''' Fonctions '''
def func_ini_matrice_parent(par_matrice_parent, par_nb_parent, par_nb_plage):
    for num_parent in range(par_nb_parent):
        for num_plage in range(par_nb_plage):
            par_matrice_parent[num_parent][num_plage] = randint(0,1)

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

def func_premier_parent_dispo(par_matrice_parent, par_nb_parent, par_plage, par_tab_pris, par_num_prof): # renvoie le premier parent dispo pour la plage et le prof donnés  
    for num_parent in range(par_nb_parent):
        if par_tab_pris[par_num_prof][num_parent] == 1 and par_matrice_parent[num_parent][par_plage] == 1:
            return num_parent

    return (-1)

def func_main(par_matrice_prof, par_matrice_parent, par_nb_plage, par_nb_parent, par_tab_pris, par_nb_prof):
    for num_plage in range(par_nb_plage):
        #Plage_dispo_prof = func_premiere_dispo_prof(Matrice_prof, nb_plage)
        for num_prof in range(par_nb_prof):
            if par_matrice_prof[num_prof][num_plage] == -1:
                Parent_dispo_meme_plage = func_premier_parent_dispo(par_matrice_parent, par_nb_parent, num_plage, par_tab_pris,num_prof)

                if Parent_dispo_meme_plage != -1 :
                    Matrice_prof[num_prof][num_plage] = Parent_dispo_meme_plage
                    par_tab_pris[num_prof][Parent_dispo_meme_plage] = 0
                    par_matrice_parent[Parent_dispo_meme_plage][num_plage] = 0

def func_affichage_rdv(par_nb_plage, par_tab_corres_plage_heure, par_matrice_prof, par_nb_prof):
    for num_prof in range (par_nb_prof):
        print(num_prof)
        for num_plage in range(par_nb_plage):
            #afficher l'horaire du créneau
            creneau = par_tab_corres_plage_heure[num_plage]
            parent_pour_creneau = str(par_matrice_prof[num_prof][num_plage])

            if parent_pour_creneau != "-1":
                print(creneau, ": parent", parent_pour_creneau)

def func_affiche_edt(par_matrice, par_nb_personnes, par_type_personne):
    print("Emploi du temps :", par_type_personne)
    for num_personne in range(par_nb_personnes):
        print(par_type_personne, num_personne, ":", par_matrice[num_personne])



''' Variables '''
nb_prof = 4
nb_parent = 4
duree_rdv = 30 # en min
nb_heure_dispo = 4 * 60
nb_plage = int(nb_heure_dispo / duree_rdv)
Matrice_prof = [[-1]*nb_plage for j in range(nb_prof)]     # -1 -> le prof n'a pas de rdv / chiffre -> le num de parent avec qui le prof a rdv
Matrice_parent = [[0]*nb_plage for j in range(nb_parent)] # 0  -> le parent n'est pas dispo / 1 -> le parent est dispo 
Tab_pris = [[1]*nb_parent for j in range(nb_prof)]   # 0 -> le parent n'est pas dispo / 1 -> le parent est dispo 
Tab_corres_plage_heure = [""] * nb_plage
Heure_de_debut = "12H00"

''' Code '''
# Creation d'un exemple de matrice de parents
func_ini_matrice_parent(Matrice_parent, nb_parent, nb_plage)
func_ini_tab_corres(Tab_corres_plage_heure, nb_plage, Heure_de_debut)

func_affiche_edt(Matrice_prof, nb_prof,"prof")

print("")

func_affiche_edt(Matrice_parent, nb_parent, "parent")

func_main(Matrice_prof, list(Matrice_parent), nb_plage, nb_parent, Tab_pris, nb_prof)

print("")

func_affichage_rdv(nb_plage, Tab_corres_plage_heure, Matrice_prof, nb_prof)





