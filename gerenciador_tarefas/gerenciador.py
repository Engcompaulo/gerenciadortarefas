from fastapi import FastAPI

app = FastAPI()
"""
TAREFAS = [
    {
        "id": 1,
        "titulo": "titulo",
        "descricao": "descricao",
        "estado": "Finalizado"
    },
    {
        "id": 2,
        "titulo": "titulo",
        "descricao": "descricao",
        "estado": "Finalizado"
    }
]

"""
TAREFAS = []

@app.get("/tarefas")
def listar_tarefas():
    return TAREFAS