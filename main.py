from fastapi import FastAPI, Query, Request, HTTPException
from fastapi.responses import StreamingResponse
from TTS.api import TTS
import io
import os

app = FastAPI()

# Carrega o modelo em português
tts = TTS(model_name="tts_models/pt/cv/vits", progress_bar=False, gpu=False)

# Token de autenticação
API_TOKEN = os.getenv("API_TOKEN")

@app.get("/speak")
def speak(request: Request, text: str = Query(..., min_length=1)):
    auth = request.headers.get("authorization")

    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid")

    token = auth.replace("Bearer ", "").strip()
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API token")

    # Gera o áudio em memória
    waveform = tts.tts(text)
    wav_bytes = tts.save_wav(waveform, None, return_bytes=True)

    return StreamingResponse(io.BytesIO(wav_bytes), media_type="audio/wav")
