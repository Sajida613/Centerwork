import os
import msvcrt

character_array_Fsetpin=[]
character_array_fCreatepin=[]

def    set_pin():
       print("\n\n\n\n\n\n\n\n\n\nplease create /Enter your 4 digits PIN:")
       print('\t\t\t\t', end ='')
       get_character_setpin() 
       get_character_setpin() 
       get_character_setpin() 
       get_character_setpin()



def     get_character_setpin():
        character=msvcrt.getch()
        character_array_Fsetpin.append(character)
        print('*',end= '',flush=True)

 
def    get_character_userpin():
       character=msvcrt.getch()
       character_array_fCreatepin.append(character)
       print('*', end= '',flush=True)


def    user_pin():
       print("\n\n\n\n\n\n\n\n\n\nEnter your 4 digits PIN:")
       print('\t\t\t\t', end ='')
       get_character_userpin() 
       get_character_userpin() 
       get_character_userpin() 
       get_character_userpin()

set_pin()
os.system("cls")
user_pin()