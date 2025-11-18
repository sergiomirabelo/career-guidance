# src/models.py
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Competencia:
    nome: str
    tipo: str  # 'tecnica' ou 'comportamental'
    peso: float = 1.0

@dataclass
class Perfil:
    nome: str
    competencias: Dict[str, int] = field(default_factory=dict)

    def adicionar_competencia(self, nome: str, nivel: int):
        nivel = max(0, min(10, int(nivel)))
        self.competencias[nome] = nivel

    def obter_media(self) -> float:
        if not self.competencias:
            return 0.0
        return sum(self.competencias.values()) / len(self.competencias)

@dataclass
class Carreira:
    nome: str
    descricao: str
    requisitos: Dict[str, int] = field(default_factory=dict)

    def combinar_score(self, perfil: Perfil) -> float:
        """Calcula score de 0 a 100 comparando requisitos com o perfil."""
        if not self.requisitos:
            return 0.0
        total = 0.0
        peso_total = 0.0
        for comp, nivel_req in self.requisitos.items():
            peso_total += 1.0
            nivel_perfil = perfil.competencias.get(comp, 0)
            # Quanto mais próximos, maior a contribuição (0 a 1)
            contrib = max(0, 1 - abs(nivel_req - nivel_perfil) / 10)
            total += contrib
        score = (total / peso_total) * 100
        return round(score, 2)
