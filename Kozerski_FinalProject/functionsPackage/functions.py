# Name: Keegan Smith, Jack Smith, Noah Gruber, Logan Schuster
# email: smith6kg@mail.uc.edu, smit4jk@mail.uc.edu, grubernw@mail.uc.edu, schustlt@mail.uc.edu 
# Assignment Title: Final Project
# Due Date: 12/07/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates we can decrypt AES, navigate UC campus, and use Pillow
# Citations: 
# Anything else that's relevant: 

import json
from cryptography.fernet import Fernet
from PIL import Image

'''
we need to decrypt the location data
@param encrypted_data: the encryption data (TeamsAndEncryptedMessages.json)
@param: english_file_path: the english txt file (english-2.txt)
@returns: the decrypted locations, as a dictionary.
'''
def decrypt_location_data(encrypted_data, english_file_path):
    #open and read the english-2.txt
    with open(english_file_path, 'r', encoding='utf-8') as english_file:
        english_text = english_file.readlines()

    #match up indices, store in a dictionary (decrypted_location{})
    decrypted_location = {}
    #add error handling in case one doesn't work
    for team_member, indices in encrypted_data.items():
        try:
            decrypted_words = [english_text[int(index)].strip() for index in indices]
            decrypted_location[team_member] = decrypted_words
        except IndexError:
            decrypted_location[team_member] = f"Error decrypting indices for {team_member}"

    return decrypted_location
