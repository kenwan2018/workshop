from numpy import *
import random


def load_training_data(file_path_train, file_path_test):
    """
    load movie lens 100k ratings from original rating file.
    need to download and put rating data in /data folder first.
    Source: http://www.grouplens.org/
    """
    prefer = []
    userid_string_to_int = []
    movieid_string_to_int = []

        
    for line in open(file_path_test, 'r'):  
        (userid, movieid) = line.split()    
        uid_tmp = str(userid)
        mid_tmp = str(movieid)
        rat = 0
        if uid_tmp in userid_string_to_int:
            userid2 = userid_string_to_int.index(uid_tmp) + 1
        else:
            userid_string_to_int.append(uid_tmp)
            userid2 = len(userid_string_to_int)

        if mid_tmp in movieid_string_to_int:
            movieid2 = movieid_string_to_int.index(mid_tmp) + 1
        else:
            movieid_string_to_int.append(mid_tmp)
            movieid2 = len(movieid_string_to_int)
        uid = int(userid2)
        mid = int(movieid2)
        prefer.append([uid, mid, rat])
        
    for line in open(file_path_train, 'r'):  
        (userid, movieid, rating) = line.split()    
        uid_tmp = str(userid)
        mid_tmp = str(movieid)
        rat = float(rating)
        if uid_tmp in userid_string_to_int:
            userid2 = userid_string_to_int.index(uid_tmp) + 1
        else:
            userid_string_to_int.append(uid_tmp)
            userid2 = len(userid_string_to_int)

        if mid_tmp in movieid_string_to_int:
            movieid2 = movieid_string_to_int.index(mid_tmp) + 1
        else:
            movieid_string_to_int.append(mid_tmp)
            movieid2 = len(movieid_string_to_int)
        uid = int(userid2)
        mid = int(movieid2)
        prefer.append([uid, mid, rat])
        
    data = array(prefer)
    return data

def load_testing_data(file_path_test):

    prefer = []
    userid_string_to_int = []
    movieid_string_to_int = []
    
    for line in open(file_path_test, 'r'):  
        (userid, movieid) = line.split()    
        uid_tmp = str(userid)
        mid_tmp = str(movieid)
        rat = 0
        if uid_tmp in userid_string_to_int:
            userid2 = userid_string_to_int.index(uid_tmp) + 1
        else:
            userid_string_to_int.append(uid_tmp)
            userid2 = len(userid_string_to_int)

        if mid_tmp in movieid_string_to_int:
            movieid2 = movieid_string_to_int.index(mid_tmp) + 1
        else:
            movieid_string_to_int.append(mid_tmp)
            movieid2 = len(movieid_string_to_int)
        uid = int(userid2)
        mid = int(movieid2)
        prefer.append([uid, mid, rat])
    data = array(prefer)
    return data

