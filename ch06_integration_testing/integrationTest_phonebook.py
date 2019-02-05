# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:14:29 2019

@author: Kate Sorotos
"""

"""ch08_integration_testing"""

from test_phonebook_database import *

def search_by_person(): 
    checked = getdb()
    if checked:
        user_location_coordinates = search_by_location()
        if user_location_coordinates:
            merge_tables, person_name =    
            if merge_tables and person_name:
                person_filtered_list_with_distance=calculate_distance_of_person_from_inputed_location(merge_tables, person_name, user_location_coordinates) 
                if person_filtered_list_with_distance:
                    sort_business_by_distance_from_user(person_filtered_list_with_distance, person_name)
                else:
                            print("calculate_distance_of_person_from_inputed_location function failed")
            else:
                    print("retrieve_person_name function failed")
        else:
            print("search location function failed.")
    else:
        print("cannot connect")

   
search_by_person()   