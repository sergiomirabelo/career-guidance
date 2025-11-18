# src/recommender.py
from typing import List, Tuple
from .models import Perfil, Carreira

class Recommender:
    def __init__(self, careers: List[Carreira]):
        self.careers = careers

    def avaliar(self, perfil: Perfil) -> List[Tuple[Carreira, float]]:
        resultados = []
        for c in self.careers:
            score = c.combinar_score(perfil)
            resultados.append((c, score))
        resultados.sort(key=lambda x: x[1], reverse=True)
        return resultados

    def gerar_trilhas(self, perfil: Perfil, top_n: int = 3) -> List[dict]:
        avaliacao = self.avaliar(perfil)
        trilhas = []
        for carreira, score in avaliacao[:top_n]:
            gaps = []
            for req, nivel in carreira.requisitos.items():
                nivel_perfil = perfil.competencias.get(req, 0)
                if nivel_perfil < nivel:
                    gaps.append({'competencia': req, 'atual': nivel_perfil, 'desejado': nivel})
            sugestoes = [f"Estude {g['competencia']} com cursos e projetos práticos" for g in gaps]
            trilhas.append({
                'carreira': carreira.nome,
                'score': score,
                'gaps': gaps,
                'sugestoes': sugestoes
            })
        return trilhas

    def areas_aprimoramento(self, perfil: Perfil, top_k: int = 5):
        itens = sorted(perfil.competencias.items(), key=lambda x: x[1])
        return itens[:top_k]
