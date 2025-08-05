# COQUI-TTS API

API de Text-to-Speech (TTS) baseada no **Coqui TTS** com modelo em **português**, pronta para rodar via **Docker** e integrada ao **Coolify**.

---

## **Funcionalidades**
- Conversão de texto em áudio `.wav` usando **Coqui TTS**.
- Streaming do áudio (sem salvar no disco).
- Autenticação via **Bearer Token** (`API_TOKEN`).
- Endpoint HTTP simples:  
  `GET /speak?text=Olá mundo`

---

## **Pré-requisitos**
- **Python 3.9+** (para rodar localmente)
- **Docker** (para rodar em container)
- **API_TOKEN** configurado como variável de ambiente (padrão: `bctrips2025`).

---

## **Rodando Localmente**
```bash
git clone https://github.com/obruncocaldeira23-sys/COQUI-TTS.git
cd COQUI-TTS

# Crie um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute a API
API_TOKEN=bctrips2025 uvicorn main:app --host 0.0.0.0 --port 8080
