from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

# 1. Metadados da API para uma documentação (Swagger) mais profissional
app = FastAPI(
    title="Minha API Profissional",
    description="Uma API robusta para gerenciamento de itens.",
    version="1.1.0",
)

# 2. Modelo com validações e exemplos
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Cadeira Gamer")
    price: float = Field(..., gt=0, description="O preço deve ser maior que zero", example=1200.50)
    description: Optional[str] = Field(None, max_length=300, example="Uma cadeira muito confortável")

# 3. Endpoints organizados por Tags
@app.get("/", tags=["Monitoramento"])
async def root():
    """Retorna o status básico da API."""
    return {"status": "ok", "message": "API rodando com sucesso!"}

@app.get("/health", tags=["Monitoramento"], status_code=status.HTTP_200_OK)
async def health():
    """Endpoint para verificações de integridade (Health Check)."""
    return {"status": "healthy", "version": "1.1.0"}

@app.post(
    "/items", 
    tags=["Itens"], 
    status_code=status.HTTP_201_CREATED,
    response_model=Item
)
async def create_item(item: Item):
    """
    Cria um novo item no sistema.
    - **name**: Nome do item
    - **price**: Preço unitário (deve ser positivo)
    - **description**: Descrição opcional
    """
    # Aqui entraria a lógica de banco de dados
    return item
