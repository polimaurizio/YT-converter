
try:
    from pytube import YouTube
except ImportError:
    print("Errore: Pytube non installato. Esegui lo script di installazione delle dipendenze.")
    exit(1)

import os 

# user yt url  
yt = YouTube( 
    str(input("URL da convertire: \n>> "))) 

video = yt.streams.filter(only_audio=True).first()
  
# add path for saving the file
print("Percorso cartella (lasciare vuoto per salvare nella cartella corrente): ") 
destination = str(input(">> ")) or '.'
  
# download audio track
out_file = video.download(output_path=destination) 
  
# save file 
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 
  
# print result
print(yt.title + " è stato convertito con successo")