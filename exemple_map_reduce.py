def calc_nb_mots(mots):
    dict_mot = {}
    for mot in mots:
        if mot in dict_mot:
            dict_mot[mot] += 1
        else:
            dict_mot[mot] = 1
    return dict_mot


if __name__ == "__main__":
    enter_file = "a b a c"
    mots = enter_file.split()
    dict_mot = calc_nb_mots(mots)
    print(dict_mot)
