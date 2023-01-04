import os

from flask import Flask, abort, request
from command_engine import CommandEnginge
from typing import Dict, Any, Optional

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> Dict[str, Any]:
    try:
        params = request.json
        engine = CommandEnginge(params)
        result = engine.execute()
    except Exception:
        abort(400, "Cant parse request")

    return {"status": 'ok', "result": result}


if __name__ == '__main__':
    app.run()
