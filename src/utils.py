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
    

def major_diff_comparator(first_col, second_col):
    if first_col == second_col:
        return 0
    
    elif ((first_col.lower() == 'pendidikan dokter') and (second_col.lower() == 'kedokteran')):
        return 0
    
    else:
        list_1 = first_col.lower().split()
        list_2 = second_col.lower().split()
        
        for item in list_2:
            if item in list_1:
                return 0
            
        return 1 