from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int


biblioteca: List[Livro] = []

@app.post("/livros", status_code=201)
async def adicionar_livro(livro: Livro):
    for l in biblioteca:
        if l.id == livro.id:
            raise HTTPException(status_code=404, detail="ID já registrado em outro livro.")
    biblioteca.append(livro)
    return {"message": "Livro registrado com sucesso", "Livro": livro}

@app.get("/livros/")
async def registros_livros():
    return{"Livro": biblioteca}

@app.put("/livros/{id_livro}")
async def livro_atu(id_livro: int, livro_atualizado: Livro):
    for i, livro in enumerate(biblioteca):
        if livro.id == id_livro:
            biblioteca[i] = livro_atualizado
            return {"message": "Livro atualizado com sucesso", "Livro": livro_atualizado}
    
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{id_livros}")
async def deletar_livro(id_livros: int):
    for livro in biblioteca:
        if livro.id == id_livros:
            biblioteca.remove(livro)
            return {"message": "Livro removido com sucesso!"}
        
    raise HTTPException(status_code=404, detail="Livro não encontrado")
