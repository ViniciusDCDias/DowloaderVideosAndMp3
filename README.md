# 🚧 Baixador de Vídeos Online (Branch `dev`)

> **Atenção:** Esta é a branch de desenvolvimento do projeto. Alterações podem estar incompletas, conter bugs ou sofrer mudanças sem aviso.

---

## 📖 Sobre

Este projeto consiste em uma aplicação desktop desenvolvida em **Python** para download de vídeos e áudios utilizando a biblioteca **yt-dlp**.

A branch `dev` concentra todas as funcionalidades em desenvolvimento antes de serem publicadas na `main`.

---

## ✨ Funcionalidades Atuais

* Download de vídeos em MP4
* Download de áudio em MP3
* Interface gráfica desenvolvida com **CustomTkinter**
* Download para a pasta `downloads/`
* Tratamento básico de erros

---

## 🚀 Próximas Funcionalidades

* Barra de progresso durante o download
* Interface mais moderna
* Download em segundo plano (sem travar a janela)
* Escolha de qualidade do vídeo
* Melhor tratamento de erros
* Suporte aprimorado para outras plataformas compatíveis com `yt-dlp`

---

## 🛠 Tecnologias

* Python 3
* CustomTkinter
* yt-dlp
* FFmpeg

---

## ⚙️ Como executar

### Clone a branch de desenvolvimento

```bash
git clone -b dev https://github.com/ViniciusDCDias/baixador-de-videos.git
```

Ou, caso já tenha o projeto:

```bash
git checkout dev
git pull origin dev
```

---

### Instale as dependências

Se existir um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Caso contrário:

```bash
pip install customtkinter yt-dlp
```

> Para conversão para MP3 é necessário ter o **FFmpeg** instalado e configurado no `PATH` do sistema.

---

## 📂 Estrutura do Projeto

```text
baixador-de-videos/
│
├── script.py
├── downloads/
├── README.md
└── requirements.txt (opcional)
```

---

## 🤝 Contribuindo

Caso queira contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature.

```bash
git checkout -b minha-feature
```

3. Faça suas alterações.
4. Envie um Pull Request para a branch `dev`.

---

## ⚠️ Aviso

A branch `dev` pode conter funcionalidades experimentais e instáveis. Para uma versão mais estável, utilize a branch `main`.
