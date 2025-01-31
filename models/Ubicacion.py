import json
class Ubicacion:
    def __init__(self, id: int, direccion: str, coordenadas: list[float] ):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas


    def to_json(self):
        return {"id":self.id, 
                "direccion":self.direccion,
                "coordenadas":self.coordenadas,}


    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["id"],data["direccion"],data["coordenadas"])