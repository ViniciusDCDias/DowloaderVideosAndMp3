# 📥 App para Baixar Vídeos Online

Projeto desenvolvido para fins de estudo e prática com Python. O aplicativo permite baixar vídeos ou extrair o áudio (MP3) a partir de uma URL utilizando a biblioteca **yt-dlp**.

---

## 🧪 Objetivo

Este projeto tem como objetivo explorar:

* Integração com bibliotecas de terceiros;
* Manipulação de mídias;
* Desenvolvimento de interfaces gráficas em Python;
* Boas práticas de organização de código.

---

## 🚀 Funcionalidades

* Download de vídeos em MP4;
* Download de áudio em MP3;
* Interface gráfica simples;
* Compatível com plataformas suportadas pelo `yt-dlp` (como YouTube e outras).

---

## 🛠 Tecnologias Utilizadas

* **Python**
* **CustomTkinter** (Interface gráfica)
* **yt-dlp** (Download de mídia)
* **FFmpeg** (Conversão para MP3)

---

## ⚙️ Como Executar

### 1. Clone a branch `dev`

As novas funcionalidades são desenvolvidas na branch `dev`. Para obter a versão mais recente do projeto, execute:

```bash
git clone -b dev https://github.com/ViniciusDCDias/baixador-de-videos.git
```

ou, caso já tenha clonado o repositório:

```bash
git checkout dev
git pull origin dev
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Caso ainda não exista um `requirements.txt`, instale manualmente:

```bash
pip install yt-dlp customtkinter
```

Para utilizar o download em MP3, também é necessário ter o **FFmpeg** instalado e configurado no `PATH`.

---

## 📂 Estrutura

```text
baixador-de-videos/
│
├── script.py
├── downloads/
└── README.md
```

---

## 📌 Observações

Este projeto está em desenvolvimento e novas funcionalidades serão adicionadas na branch `dev` antes de serem publicadas na `main`.
