import uvicorn
from fastapi import FastAPI, HTTPException
from starlette import status

from game import rps_game

app = FastAPI()


@app.get("/")
def healthcheck():
    return {"message": "Healthcheck is OK"}


@app.get("/moves")
def get_moves():
    return rps_game.moves


@app.get("/{move}")
def game(move: str):
    check = rps_game.check_player_move(move)
    if not check:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid move {move}. Please choice: 'rock', 'paper', 'scissors'")
    return rps_game.play(move)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=80, log_level='info')
