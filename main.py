import yt_dlp

def main():

    def baixar_video(url):
        opcoes = {
            'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo com base no título do vídeo
            'format': 'bestvideo+bestaudio/best',  # Melhor qualidade disponível
            'merge_output_format': 'mp4',  # Formato de saída
        }

        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

    # Exemplo de uso
    url_video = input("Cole a URL do vídeo do YouTube: ")
    baixar_video(url_video)


if __name__ == "__main__":
    main()
