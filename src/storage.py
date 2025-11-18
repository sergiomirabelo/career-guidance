# src/storage.py
import json
from pathlib import Path
from typing import List
from .models import Carreira

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / 'sample_data'
DATA_DIR.mkdir(exist_ok=True)
CAREERS_FILE = DATA_DIR / 'careers.json'
PROFILES_FILE = DATA_DIR / 'profiles.json'

def carregar_carreiras() -> List[Carreira]:
    if not CAREERS_FILE.exists():
        default = [
            {"nome": "Engenheiro de IA", "descricao": "Desenvolve modelos de IA",
             "requisitos": {"Lógica": 8, "Matemática": 7, "Programação": 8, "Criatividade": 6}},
            {"nome": "Designer de Experiência", "descricao": "Projetar experiências digitais",
             "requisitos": {"Criatividade": 8, "Colaboração": 7, "Comunicação": 7}},
            {"nome": "Gestor de Produto", "descricao": "Orquestra produtos digitais",
             "requisitos": {"Comunicação": 8, "Liderança": 7, "Adaptabilidade": 7}},
            {"nome": "Cientista de Dados", "descricao": "Analisa dados e gera insights",
             "requisitos": {"Estatística": 8, "Programação": 7, "Lógica": 7}}
        ]
        with open(CAREERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default, f, ensure_ascii=False, indent=2)
    with open(CAREERS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    careers = [Carreira(nome=d['nome'], descricao=d.get('descricao',''), requisitos=d.get('requisitos', {})) for d in data]
    return careers

def salvar_perfil(perfil):
    all_profiles = []
    if PROFILES_FILE.exists():
        with open(PROFILES_FILE, 'r', encoding='utf-8') as f:
            all_profiles = json.load(f)
    data = {'nome': perfil.nome, 'competencias': perfil.competencias}
    all_profiles.append(data)
    with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_profiles, f, ensure_ascii=False, indent=2)
