import os
import re
from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip
import string

def clean_filename(filename):
    valid_chars = "-_.() {}{}".format(string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars).strip()

def download_playlist(url):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print("Se encontraron {} videos en la playlist.".format(len(playlist.video_urls)))

    folder_name = input("Ingresa el nombre de la carpeta para guardar la playlist: ")
    folder_path = os.path.join(os.getcwd(), "playlists", folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print("La carpeta de destino para la descarga es: {}".format(folder_path))

    download_choice = input("¿Deseas descargar toda la playlist? (s/n): ")

    if download_choice.lower() == "s":
        choice = input("¿Deseas descargar el video (v) o solo el audio (a)? ")
        quality = None
        if choice.lower() == "v":
            quality = input("Ingresa la calidad de descarga de video (1080p, 720p, 480p, 360p): ")
        download_all_videos(playlist, folder_path, choice, quality)
    elif download_choice.lower() == "n":
        download_selected_videos(playlist, folder_path)
    else:
        print("Opción no válida. Saliendo.")

def download_all_videos(playlist, folder_path, choice, quality):
    for url in playlist.video_urls:
        download_media(url, folder_path, choice, quality)

def download_selected_videos(playlist, folder_path):
    num_videos = input("Ingresa el número de videos que deseas descargar: ")

    try:
        num_videos = int(num_videos)
    except ValueError:
        print("El valor ingresado no es válido.")
        return

    if num_videos <= 0 or num_videos > len(playlist.video_urls):
        print("El número de videos a descargar es inválido.")
        return

    selected_videos = playlist.video_urls[:num_videos]

    choice = input("¿Deseas descargar el video (v) o solo el audio (a)? ")
    quality = None
    if choice.lower() == "v":
        quality = input("Ingresa la calidad de descarga de video (1080p, 720p, 480p, 360p): ")
    for url in selected_videos:
        download_media(url, folder_path, choice, quality)

def download_media(url, folder_path, choice, quality):
    try:
        youtube = YouTube(url)

        if youtube:
            title = youtube.title
            cleaned_title = clean_filename(title)  # Limpiar el título del video

            if choice.lower() == "v":
                stream = youtube.streams.get_by_resolution(quality)
                if stream:
                    stream.download(output_path=folder_path, filename=cleaned_title + ".mp4")
                    video_path = os.path.join(folder_path, cleaned_title + ".mp4")
                    print("Descarga del video completada. Guardado en: {}".format(video_path))
                else:
                    print("No se encontró una corriente de video con la calidad especificada: {}".format(quality))
            elif choice.lower() == "a":
                stream = youtube.streams.get_audio_only()
                if stream:
                    stream.download(output_path=folder_path, filename=cleaned_title + ".mp3")
                    audio_path = os.path.join(folder_path, cleaned_title + ".mp3")
                    print("Descarga del audio completada. Guardado en: {}".format(audio_path))
            else:
                print("Opción no válida.")
        else:
            print("No se pudo obtener el objeto YouTube para la URL: {}".format(url))
    except Exception as e:
        print("Ocurrió un error al descargar el media: {}".format(str(e)))


def main():
    url = input("Ingresa la URL de la playlist de YouTube: ")
    download_playlist(url)

if __name__ == '__main__':
    main()
