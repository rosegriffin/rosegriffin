import os

def require_env(name):
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(f'Missing environment variable: {name}')

    return value

APP_SECRET_KEY = require_env("APP_SECRET_KEY")

MODEL_CONFIG = {
    "amer_dialect_id": {
        "lr.pkl": require_env("LR_URL"),
        "wav2vec_scaler.pkl": require_env("WAV2VEC_SCALER_URL"),
    }
}
