import requests
from datetime import datetime

def consultar_radiacao(latitude, longitude):
    """
    Consulta a média diária de radiação solar (kWh/m²/dia) na posição geográfica fornecida,
    utilizando a NASA POWER API.
    
    Args:
        latitude (float): Latitude da localização.
        longitude (float): Longitude da localização.
    
    Returns:
        float | None: Média da radiação solar ou None em caso de erro.
    """
    hoje = datetime.utcnow().strftime("%Y%m%d")
    
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"

    params = {
        "parameters": "ALLSKY_SFC_SW_DWN",  # Radiação solar incidente na superfície
        "community": "RE",  # Renewable Energy
        "longitude": longitude,
        "latitude": latitude,
        "start": "20230101",
        "end": hoje,
        "format": "JSON"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        dados = response.json()
        valores = [
            v for v in dados["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].values()
            if isinstance(v, (int, float)) and v > 0
        ]
        media = sum(valores) / len(valores) if valores else 0
        return round(media, 2)
    except Exception as e:
        print(f"Erro ao consultar a API da NASA: {e}")
        return None
