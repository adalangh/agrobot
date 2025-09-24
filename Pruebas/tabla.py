from bs4 import BeautifulSoup
import json

# Cargar el HTML
with open("Intents.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = soup.find_all("tr")[1:]  # ignorar encabezado
with open("salida.jsonl", "w", encoding="utf-8") as f:
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        obj = {
            "uri": cols[0],
            "before": cols[1],
            "after": cols[2],
            "feedback": cols[3],
            "learning": cols[4],
            "iterationId": cols[5]
        }
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
