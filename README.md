## Endpoint Individu

### Topik: T1 | Buku

| Method | Endpoint | Status | Deskripsi |
|--------|----------|--------|-----------|
| POST | `/api/buku` | 201 Created | Tambah buku baru + header Location |
| GET | `/api/buku` | 200 OK | List buku (dukung `skip`, `limit`, `search`) |
| GET | `/api/buku/{id}` | 200 / 404 | Detail buku by ID |

### Validasi
- `isbn`: 13 digit angka
- `tahun_terbit`: 1900–2026

### Cara Menjalankan
1. `cd backend && python -m venv venv && venv\Scripts\activate`
2. `pip install -r requirements.txt`
3. `uvicorn app.main:app --reload`
4. Buka `http://localhost:8000/docs`
