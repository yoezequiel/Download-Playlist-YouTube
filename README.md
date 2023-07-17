# Descargador de YouTube Playlist

Este es un script de Python que te permite descargar videos y audio de una playlist de YouTube utilizando la biblioteca `pytube` y `moviepy`. Puedes ingresar la URL de la playlist y elegir entre descargar toda la playlist o seleccionar una cantidad específica de videos para descargar.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar el script:

- `pytube`: Permite acceder a los datos de los videos de YouTube y descargarlos.
- `moviepy`: Proporciona herramientas para trabajar con archivos de video.

Puedes instalar estas bibliotecas usando el siguiente comando:

```
pip install pytube moviepy
```

## Uso

1. Ejecuta el script desde la línea de comandos: `python youtube_playlist_downloader.py`.

2. Ingresa la URL de la playlist de YouTube cuando se solicite.

3. Se mostrará el número de videos encontrados en la playlist.

4. Ingresa el nombre de la carpeta donde deseas guardar la playlist. Si la carpeta no existe, se creará automáticamente en la ubicación actual.

5. Elige si deseas descargar toda la playlist o seleccionar videos específicos.

    - Si eliges descargar toda la playlist, se te pedirá que elijas entre descargar el video (v) o solo el audio (a). Luego, se te pedirá que ingreses la calidad de descarga del video (por ejemplo, 1080p, 720p, 480p, 360p).
    
    - Si eliges descargar videos específicos, se te pedirá que ingreses el número de videos que deseas descargar. Luego, se te pedirá que elijas entre descargar el video (v) o solo el audio (a). Se descargarán los videos seleccionados de la playlist.

6. La descarga comenzará y se mostrará el progreso en la consola. Una vez completada la descarga, los archivos se guardarán en la carpeta especificada.

## Notas

- El título de cada video se utilizará como nombre de archivo después de limpiarlo de caracteres no válidos.

- Si la calidad de video especificada no está disponible, se mostrará un mensaje de error.

- Si ocurre algún error durante la descarga, se mostrará un mensaje de error correspondiente.

¡Disfruta descargando videos y audio de tus playlists de YouTube! Si tienes alguna pregunta o encuentras algún problema, no dudes en abrir un problema en este repositorio de GitHub.

**¡Recuerda!**
Asegúrate de cumplir con las políticas de YouTube y los derechos de autor al descargar videos y audio de YouTube.
