from fastapi import FastAPI
from typing import List
from random import randint
import os
import uvicorn

# ==============================
# INITIALISATION DE L'APP
# ==============================
app = FastAPI()

# ==============================
# ROUTE RACINE
# ==============================
@app.get("/")
def home():
    return {"status": "Alerte Deals API v2 is live 🚀"}

# ==============================
# ROUTE /search - Vols flexibles (mock)
# ==============================
@app.get("/search")
def search_flexible_flights(
    origin: str,
    month: str,
    max_price: int
):
    """
    Recherche de vols flexibles (mock intelligent)
    """
    destinations = [
        "Rome",
        "Madrid",
        "Lisbonne",
        "Barcelone",
        "Berlin",
        "Athènes",
        "Istanbul"
    ]

    results = []

    for city in destinations:
        price = randint(50, max_price)

        average_price = price + randint(50, 200)
        discount = round((average_price - price) / average_price * 100)

        if discount >= 40:
            label = "🔥 Exceptionnel"
        elif discount >= 20:
            label = "✅ Bon deal"
        else:
            label = "🟡 Correct"

        results.append({
            "origin": origin,
            "destination": city,
            "month": month,
            "price": price,
            "average_price": average_price,
            "discount_percent": discount,
            "deal_label": label
        })

    return {
        "count": len(results),
        "results": results
    }

# ==============================
# LANCEMENT SERVEUR (RAILWAY)
# ==============================
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
