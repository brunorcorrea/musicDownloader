# musicDownloader

## Baixador de música criado com [Pytube](https://pypi.org/project/pytube/), e interface desenvolvida usando Tkinter

<br/>

### Para usá-lo é necessário instalar os seguintes programas

* [FFmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)

* [Python](https://www.python.org/downloads/)

## 1. Instalando Python pela Microsoft Store

* **Pesquise no menu Iniciar CMD e execute como administrador :**

  ![cmd](https://i.imgur.com/lY4b9Z5.png)

<br/>

* **Com o CMD aberto digite python :**

 ![Imgur](https://imgur.com/LBqCw0v.png)

<br/>

* **Pressione enter e então a Microsoft Store irá abrir na página de download da versão mais recente :**

  ![Imgur](https://imgur.com/1HDf03T.png)

<br/>

* **Pressione _Obter_ e depois _Instalar_ para iniciar o download:**

  ![Imgur](https://imgur.com/WsyYWWe.png)

<br/>

* **Para ter certeza que o Python foi instalado corretamente digite sem as aspas "python --version", caso ele retorne a versão do python, deu certo :**

  ![Imgur](https://imgur.com/4Vg0ZUQ.jpg)

## 2. Instalando o FFmpeg

* **Primeiro faça o download dos arquivos pelo link [FFmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z) :**

<br/>

* **Extraia os arquivos usando seu descompactador preferido :**

![Imgur](https://imgur.com/ccDtSvd.png)

<br/>

* **Renomeie a pasta extraída para _FFmpeg_ :**

![Imgur](https://imgur.com/S2oVlAZ.png)

<br/>

* **Mova a pasta extraída para o disco onde o Windows está instalado (no meu caso é o disco C) :**

![Imgur](https://imgur.com/GdVfiXh.png)

<br/>

* **Pesquise no menu Iniciar CMD e execute como administrador :**

  ![cmd](https://i.imgur.com/lY4b9Z5.png)

<br/>

* **Digite _setx /m PATH "C:\FFmpeg\bin;%PATH%"_ com as aspas :**

  ![Imgur](https://imgur.com/Z01VmIq.png)

<br/>

* **Se o CMD retornar "_ÊXITO: o valor especificado foi salvo_" deu certo:**

<br/>

* **Para testar se o FFmpeg está funcionando digite "ffmpeg -version" sem as aspas :**
