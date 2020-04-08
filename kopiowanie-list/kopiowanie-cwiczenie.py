import random
import copy

class Play:
    def __init__(self,path:str):
        if not isinstance(path,str):
            raise TypeError
        else:
            print("Gra muzyka")

#baza_slownik {id: [id,ścieżka,tytuł, wykonawca, liczba odsłuchań]}
#zmieniamy liczbę odsłuchań oraz dodajemy piosenkę, jeśli nie ma jej w bazie

with open("baza_piosenek.txt","r",-1,"utf-8") as file:
    base_dict={line.strip().split(";")[0]:line.strip().split(";") for line in file.readlines()}

playlist_base={
            "Różne":
                [base_dict['path2.mp3'],base_dict['path7.mp3'],base_dict['path9.mp3'],
                base_dict['path10.mp3'],base_dict['path18.mp3'],base_dict['path19.mp3']],
            "Instrumental":
                [base_dict['path3.mp3'],base_dict['path4.mp3'],base_dict['path8.mp3'],
                base_dict['path16.mp3'],base_dict['path20.mp3'],base_dict['path21.mp3']]}

def play_random(playlista,baza):
    playlista=[*playlista] #lub copy.deepcopy(playlista)
    random.shuffle(playlista)
    for song in playlista:
        song[3]=int(song[3])+1 #song[3] to liczba odsłuchań
        #kluczem w słowniku z wszystkimi piosenkami jest ścieżka dostępu, którą przechowujemy także w song[0]
        #baza[song[0]][3]=int(baza[song[0]][3])+1 jeśli użyjesz deepcopy()
        song[3]=str(song[3]) #Konwertujemy z powrotem na string
        Play(song[0]) #przekazujemy ściężkę dostępu piosenki
        print(f"Teraz gra piosenka '{song[2]}', autora {song[1]}, którą odsłuchujesz {song[3]} raz.")
        #Nadpisujemy naszą bazę w .txt
        values = [';'.join(item) for item in baza.values()]
        open('baza_piosenek.txt', 'w',-1,'utf-8').write('\n'.join(values))

print(base_dict) #przed odsłuchaniem
list_name=input("Podaj nazwę playlisty: ")
play_random(playlist_base.get(list_name, "Brak takiej playlisty"),base_dict)
print(base_dict) #po odsłuchaniu

