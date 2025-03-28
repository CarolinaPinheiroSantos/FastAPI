from fastapi import FastAPI, HTTPException, status, Response, Depends
from typing import Optional, Any
from model import Cinema

app = FastAPI(title="API de Cinema", description="API programação do cinema")

cinema = {
    1: {
        "filme": "Avatar",
        "classificacao": 14,
        "genero": "aventura",
        "sobre": "No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que parecem ser primitivos, mas são altamente evoluídos. Como o ambiente do planeta é tóxico, foram criados os avatares, corpos biológicos controlados pela mente humana que se movimentam livremente em Pandora",
        "capa": "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
        "data_horario": "05/10/2024 14:30:00"
    },
    2: {
        "filme": "Crepusculo",
        "classificacao": 16,
        "genero": "romance",
        "sobre": "A estudante Bella Swan conhece Edward Cullen, um belo mas misterioso adolescente. Edward é um vampiro, cuja família não bebe sangue, e Bella, longe de ficar assustada, se envolve em um romance perigoso com sua alma gêmea imortal.",
        "capa": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUxE0ap_ktC_9N3lczwiSiOdd1BQ465xAXWQ&s",
        "data_horario": "29/03/2024 14:00:00"
    }
}

@app.get("/", description="Retorna todo em cartaz do cinema")
async def todo_cinema():
    return cinema

@app.get("/cinema/{cinema_id}", description="Retorna a partir do id filme em cartaz do cinema")
async def cada_cinema(cinema_id:int):
    try:
        cinemas = cinema[cinema_id]
        return cinemas
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe nada em cartaz com o {cinema_id}")

@app.post("/cinema/criar", description="Cria filme em cartaz do cinema")
async def criar_cinema(cinema: Optional[Cinema]= None):
    increment_id = len(Cinema) + 1
    cinema[increment_id] = cinema
    del cinema.id
    return cinema
