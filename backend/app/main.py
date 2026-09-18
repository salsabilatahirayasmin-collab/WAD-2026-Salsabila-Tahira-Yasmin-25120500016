from fastapi import FastAPI, HTTPException, Response, Query
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from uuid import uuid4

app = FastAPI(title="WAD 2026 - Individu API")

# ============================================================
# 1. SKEMA INPUT (tanpa id, id dibuat oleh server)
# ============================================================
class BukuInput(BaseModel):
    isbn: str = Field(..., description="13 digit angka")
    judul: str = Field(..., min_length=1)
    penulis: str = Field(..., min_length=1)
    tahun_terbit: int = Field(..., ge=1900, le=2026)

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("ISBN harus berupa angka")
        if len(v) != 13:
            raise ValueError("ISBN harus 13 digit")
        return v


# ============================================================
# 2. SKEMA OUTPUT (dengan id dari server)
# ============================================================
class BukuOutput(BaseModel):
    id: str
    isbn: str
    judul: str
    penulis: str
    tahun_terbit: int


# ============================================================
# 3. "DATABASE" SEMENTARA (in-memory)
# ============================================================
db_buku: dict[str, dict] = {}


# ============================================================
# 4. ENDPOINT POST /api/buku
#    → 201 Created + Header Location
# ============================================================
@app.post("/api/buku", response_model=BukuOutput, status_code=201)
def create_buku(payload: BukuInput, response: Response):
    new_id = str(uuid4())
    data = payload.model_dump()
    data["id"] = new_id
    db_buku[new_id] = data

    # Header Location mengarah ke URL detail resource
    response.headers["Location"] = f"/api/buku/{new_id}"
    return data


# ============================================================
# 5. ENDPOINT GET /api/buku
#    → 200 OK, dukung ?skip, ?limit, ?search
# ============================================================
@app.get("/api/buku", response_model=List[BukuOutput])
def list_buku(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
):
    items = list(db_buku.values())

    # Filter berdasarkan search (judul atau penulis)
    if search:
        keyword = search.lower()
        items = [
            b for b in items
            if keyword in b["judul"].lower() or keyword in b["penulis"].lower()
        ]

    # Pagination
    items = items[skip : skip + limit]
    return items


# ============================================================
# 6. ENDPOINT GET /api/buku/{id}
#    → 200 OK atau 404 Not Found
# ============================================================
@app.get("/api/buku/{buku_id}", response_model=BukuOutput)
def get_buku(buku_id: str):
    if buku_id not in db_buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
    return db_buku[buku_id]


# ============================================================
# 7. HEALTH CHECK (untuk memastikan server jalan)
# ============================================================
@app.get("/health")
def health_check():
    return {"status": "ok"}