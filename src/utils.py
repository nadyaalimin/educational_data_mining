import pickle

def dump_to_pickle(data, out_file_path):
    pickle.dump(data, open(out_file_path, 'wb'))
    
    
def get_name_of_semester(cohort, semester):
    if (semester - cohort) == 0:
        return 'sem_01'
    elif (semester - cohort) == 1:
        return 'sem_02'
    elif (semester - cohort) == 2:
        return 'sem_03'
    elif (semester - cohort) == 10:
        return 'sem_04'
    else:
        return 'sem_99'
    
    
def change_major_detector(appl_major, onboard_major):
    if appl_major == onboard_major:
        return 0
    else:
        return 1
