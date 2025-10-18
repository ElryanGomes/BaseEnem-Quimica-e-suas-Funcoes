from flask import Flask, render_template, url_for, jsonify, request
import google.generativeai as genai
from google.generativeai.types import GenerationConfig
import json
import os
import base64
import httpx
from dotenv import load_dotenv
from datetime import datetime

load_dotenv() 

app = Flask(__name__)

@app.route("/")
@app.route("/Sobre-Quimica")
def Site():
    #textos crie sua variavel e coise o negocio
    base = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown ."
    quimiquia = "Explore como as IAs estão revolucionando a Química Computacional, acelerando descobertas de novos materiais e impulsionando a criação de medicamentos."
    ciencitecno = "A ciência fornece os fundamentos teóricos necessários para a inovação tecnológica, enquanto a tecnologia possibilita avanços na pesquisa científica, fornecendo novas ferramentas e métodos \n de investigação."
    enem = f"Pratique questóes de quimica do ENEM dos anos de 2009 a {datetime.now().year}!"
    afonsinha = "As energias renováveis são fontes de energia naturais e inesgotáveis. Elas são mais sustentáveis e têm menor impacto ambiental em comparação com os combustíveis fósseis."
    QuimicaSociedade = "Química na sociedade tem como objetivo o desenvolvimento e consolidação de suas importantes relações e aplicações para o desenvolvimento do mundo e para a melhoria da qualidade de vida das pessoas."
    ambiente = "A química estuda as substâncias e suas reações, ajudando a desenvolver soluções para problemas ambientais, como a redução da poluição e o uso sustentável dos recursos."

    cards = [
        #Felipe e Maria
        {"refe": "IA-Quimica", "imge": "img/IA-Quimica/FotoCard.jpg", "titu": "IA e Química Computacional", "text": quimiquia, },
        
        #Elryan, Arthur e Gabriel
        {"refe": "CienciaTecnologia", "imge": "img/CienciaTecnologia/FotoCard.webp", "titu": "Ciência e Tecnologia", "text": ciencitecno, },

        #Ravel, Rafaelson e Vinicius
        {"refe": "EnemQuestoes", "imge": "img/EnemQuestoes/FotoCard.jpg", "titu": "Questões Enem-Química", "text": enem, },

        #Dielson, Bezinha e João Victor
        {"refe": "Energias", "imge": "img/Energias/FotoCard.avif", "titu": "Energias sustentaveis", "text": afonsinha, },

        #Carla, Isabely e Matheus
         {"refe": "QuimicaSociedade", "imge": "img/QuimicaSociedade/FotoCard.jpg", "titu": "Quimica e Sociedade", "text": QuimicaSociedade, },

        #Jéssica, Clara e Jamine
        {"refe": "QuimicaAmbiental", "imge": "img/QuimicaAmbiente/FotoCard.jpg", "titu": "Química e Meio Ambiente", "text": ambiente, },
    ]
    return render_template('SiteP.I.html', cards=cards)

@app.route("/Sobre")
def Sobre():
    return render_template('Sobre.html')

@app.route("/Contatos")
def contatos():
    # base
    baseFtFundo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScBSCxDiRbNZMWk1dB7Sai1M5y9qUgvw5Ymb_WXZBXve_awClF_khZ1QN7FC4smv12I7c&usqp=CAU"
    baseFtPerfil = "https://img.freepik.com/vetores-premium/ilustracao-de-avatar-de-estudante-icone-de-perfil-de-usuario-avatar-de-jovem_118339-4402.jpg"

    # IA QUIMICA
    fotoFundoFelipe = "https://i.pinimg.com/736x/25/ab/e4/25abe442a4694a135bad24019d951c54.jpg"
    fotoFundoMaria = "../static/img/IA-quimica/FotoFundoMaria.gif"
    
    # CIENCIA E TECNOLOGIA
    fotoFundoElryan = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy_jxD7XS0C2V2FBbf6IFE4NsC-WNFkmTEhA&s"
    fotoFundoArthur = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy_jxD7XS0C2V2FBbf6IFE4NsC-WNFkmTEhA&s"
    fotoFundoGabriel = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy_jxD7XS0C2V2FBbf6IFE4NsC-WNFkmTEhA&s"
    
    # QUESTOES ENEM
    fotoFundoRavel = "https://w0.peakpx.com/wallpaper/144/752/HD-wallpaper-sunset-clouds-sky-horizon.jpg"
    fotoFundoRafaelson = "https://cdn.steamstatic.com/steamcommunity/public/images/items/224420/1cee148dbe320a9367bcdf5211ae077e695a4cfe.jpg"
    fotoFundoVinicius = "https://w0.peakpx.com/wallpaper/144/752/HD-wallpaper-sunset-clouds-sky-horizon.jpg"

    # ENERGIAS SUSTENTAVEIS
    fotoFundoBezinha = "https://wallpaperaccess.com/full/3061192.jpg"
    fotoFundoDielson = "https://wallpaperaccess.com/full/3061192.jpg"
    fotoFundoJoao = "https://wallpaperaccess.com/full/3061192.jpg"

    #QUÍMICA E SOCIEDADE
    fotoFundoIsabel = "https://img.freepik.com/fotos-premium/papel-de-parede-de-fundo-preto-para-telefone_764067-141.jpg?w=360"
    fotoFundoCarla = "https://img.freepik.com/fotos-premium/papel-de-parede-de-fundo-preto-para-telefone_764067-141.jpg?w=360"
    fotoFundoMatheus = "https://img.freepik.com/fotos-premium/papel-de-parede-de-fundo-preto-para-telefone_764067-141.jpg?w=360"

    # QUIMICA E AMBIENTE
    fotoFundoJessica = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfLcyFeffAKXoBS2aR4rJYlEuuWjWIQ9BBtRe4wpekhdTO5lMKgHwJJhIb7c3zvnLTmzw&usqp=CAU"
    fotoFundoClara = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfLcyFeffAKXoBS2aR4rJYlEuuWjWIQ9BBtRe4wpekhdTO5lMKgHwJJhIb7c3zvnLTmzw&usqp=CAU"
    fotoFundoJamine = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfLcyFeffAKXoBS2aR4rJYlEuuWjWIQ9BBtRe4wpekhdTO5lMKgHwJJhIb7c3zvnLTmzw&usqp=CAU"

    grupio = [

        #FEZ O LAYOUT
        {"fez": "Desenvolvedores do layout", 
        "Nome": "Elryan", "NomeS": "Gomes", "FtFundo1": fotoFundoElryan, "FtPerfil1": "img/CienciaTecnologia/fotoPerfilElryan.jpg", "Insta1": "https://www.instagram.com/elryan_gomez/", "git": "https://github.com/ElryanGomes", "link": "https://www.linkedin.com/in/elryan-gomes/", "email1": "elryangomes@gmail.com",
        "Nome2": "Arthur", "Nome2S": "Dias", "FtFundo2": fotoFundoElryan, "FtPerfil2": "img/CienciaTecnologia/fotoPerfilArthur.jpg", "Insta2": "https://www.instagram.com/arthurdias______/", "git2": "https://github.com/Arthur-D-X", "link2": "sem", "email2": " arthur2007dx@gmail.com ",  
        "Nome3": "João", "Nome3S": "Gabriel", "FtFundo3": fotoFundoGabriel, "FtPerfil3": "img/CienciaTecnologia/fotoPerfilGabriel.jpg", "Insta3": "https://www.instagram.com/mlksz.s/", "git3": "https://github.com/mlksz", "link3": "https://www.linkedin.com/in/mlksz/", "email3": "twgabe@gmail.com"},
        
        #IA QUIMICA
        {"fez": "IA Química", 
        "Nome": "Felipe", "NomeS": "Silva", "FtFundo1": fotoFundoFelipe, "FtPerfil1": "img/IA-Quimica/fotoPerfilFelipe.jpg", "Insta1": "https://www.instagram.com/felype.p7/", "git": "https://github.com/Felipe-Silva7", "link": "https://www.linkedin.com/in/felipe-silva-313a27337/", "email1": "fs0987145@gmail.com", 
        "Nome3": "seila",
        "Nome2": "Maria", "Nome2S": "Duarte", "FtFundo2": fotoFundoMaria, "FtPerfil2": "img/IA-Quimica/fotoPerfilMaria.jpg", "Insta2": "sem", "git2": "sem", "link2": "sem", "email2": "mariazyyn1@gmail.com",},
        
        #CIENCIA E TECNOLOGIA
        {"fez": "Ciência e Tecnologia", 
        "Nome": "Elryan", "NomeS": "Gomes", "FtFundo1": fotoFundoElryan, "FtPerfil1": "img/CienciaTecnologia/fotoPerfilElryan.jpg", "Insta1": "https://www.instagram.com/elryan_gomez/", "git": "https://github.com/ElryanGomes", "link": "https://www.linkedin.com/in/elryan-gomes/", "email1": "elryangomes@gmail.com",
        "Nome2": "Arthur", "Nome2S": "Dias", "FtFundo2": fotoFundoArthur, "FtPerfil2": "img/CienciaTecnologia/fotoPerfilArthur.jpg", "Insta2": "https://www.instagram.com/arthurdias______/",  "git2": "https://github.com/Arthur-D-X", "link2": "sem", "email2": " arthur2007dx@gmail.com ",  
        "Nome3": "João", "Nome3S": "Gabriel", "FtFundo3": fotoFundoGabriel, "FtPerfil3": "img/CienciaTecnologia/fotoPerfilGabriel.jpg", "Insta3": "https://www.instagram.com/mlksz.s/", "git3": "https://github.com/mlksz", "link3": "https://www.linkedin.com/in/mlksz/", "email3": "twgabe@gmail.com"},
        
        #QUESTOES ENEM
        {"fez": "Questões ENEM-Química", 
        "Nome": "Victor", "NomeS": "Ravel", "FtFundo1": fotoFundoRavel, "FtPerfil1": "img/EnemQuestoes/fotoPerfilRavel.png", "Insta1": "https://www.instagram.com/vict0rrrrr__/", "git": "https://github.com/vit0rr05", "link": "sem", "email1": "ravelvictor3619@gmail.com",
        "Nome2": "Rafaelson", "Nome2S": "Rodrigues", "FtFundo2": fotoFundoRafaelson, "FtPerfil2": "img/EnemQuestoes/fotoPerfilRafaelson.jpg", "Insta2": "https://www.instagram.com/rafaelson_76/", "git2": "https://github.com/RafaelsonRodrigues", "link2": "https://www.linkedin.com/in/rafaelson-rodrigues-2844bb31b/", "email2": "rafaelsonrodrigues03@gmail.com",
        "Nome3": "Arthur", "Nome3S": "Vinícius", "FtFundo3": fotoFundoVinicius, "FtPerfil3": "img/EnemQuestoes/fotoPerfilVinicius.jpg" , "Insta3": "https://www.instagram.com/__arthur.vinicius__/", "git3": "https://github.com/ArthurV1nicius", "link3": "sem", "email3": "capir.2023116isinf0024@aluno.ifpi.edu.br"},

        #ENERGIAS SUSTENTAVEIS
        {"fez": "Energias Sustentáveis", 
        "Nome": "Francislane", "NomeS": "Santos", "FtFundo1": fotoFundoBezinha, "FtPerfil1": "img/Energias/fotoPerfiBezinha.jpeg", "Insta1": "https://www.instagram.com","git": "sem", "link": "sem", "email1": "@gmail.com",
        "Nome2": "Dielson", "Nome2S": "Cordeiro", "FtFundo2": fotoFundoDielson, "FtPerfil2": "img/Energias/fotoPerfiDielson.jpeg", "Insta2": "https://www.instagram.com/dissh_xz?igsh=b2t0cHhvODV0c2R0","git2": "https://github.com/Disshxz", "link2": "https://www.linkedin.com/in/dielson-cordeiro-970369316?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app", "email2": "cordeirosilva2@icloud.com",
        "Nome3": "João", "Nome3S": "Victor", "FtFundo3": fotoFundoJoao, "FtPerfil3": "img/Energias/fotoPerfiJoao.jpeg", "Insta3": "https://www.instagram.com","git3": "sem", "link3": "sem", "email3": "@gmail.com"},

        #QUÍMICA E SOCIEDADE
        {"fez": "Química e Sociedade", 
        "Nome": "Antonia", "NomeS": "Isabely", "FtFundo1": fotoFundoIsabel, "FtPerfil1": "img/QuimicaSociedade/fotoPerfilIsabel.jpg", "Insta1": "https://www.instagram.com/isabely651?igsh=OW5ucnNqaHJsaDE= ","git": "sem", "link": "sem", "email1": "isabellysanto0000@gmail.com",
        "Nome2": "Carla", "Nome2S": "Vilena", "FtFundo2": fotoFundoCarla, "FtPerfil2": "img/QuimicaSociedade/fotoPerfilVilena.jpg", "Insta2": "https://www.instagram.com/vilena_carvalho006?igsh=MWI1djU0bHMydnpsbA==","git2": "sem", "link2": "sem", "email2": "carlavilenacarvalhocosta@gmail.com",
        "Nome3": "Matheus", "Nome3S": "Rodrigues", "FtFundo3": fotoFundoMatheus, "FtPerfil3": "img/QuimicaSociedade/fotoPerfilMatheus.jpg", "Insta3": "https://www.instagram.com/7coemt?igsh=bmZzNmhnMG9lYWJl ","git3": "sem", "link3": "sem", "email3": "matheusrodrigues4037@gmail.com"},

         # QUIMICA E AMBIENTE
         {"fez": "Química e Ambiente", 
        "Nome": "Jéssica", "NomeS": "Almeida", "FtFundo1": fotoFundoJessica, "FtPerfil1": "img/QuimicaAmbiente/fotoPerfilJessica.jpg", "Insta1": "https://www.instagram.com/jessicalmda_?igsh=MWQzamhpMTBtb2JyNg%3D%3D&utm_source=qr","git": "sem", "link": "sem", "email1": "jessicaousah202@gmail.com",
        "Nome2": "Maria", "Nome2S": "Clara", "FtFundo2": fotoFundoClara, "FtPerfil2": "img/QuimicaAmbiente/fotoPerfilClara.jpg", "Insta2": "sem","git2": "sem", "link2": "sem", "email2": "carvalhomariacrv@gmail.com",
        "Nome3": "Jamine", "Nome3S": "Nascimento", "FtFundo3": fotoFundoJamine, "FtPerfil3": "img/QuimicaAmbiente/fotoPerfilJamine.jpg", "Insta3": "https://www.instagram.com/j4miine._?igsh=eXlzYWI2Nmp2NGIz","git3": "sem", "link3": "sem", "email3": "jaminea42@gmail.com"},
        
    ]
    return render_template('Contatos.html', grupio=grupio)


@app.route("/CienciaTecnologia")
def CieTec():
    return render_template('CienciaTecnologia.html')

# Felipe e Maria

@app.route("/IA-Quimica")
def IAQui():
    return render_template('IA-Quimica.html')

secoes = {
    "O que é Inteligência Artificial e Química Computacional?": """
        A Inteligência Artificial (IA) e a Química Computacional estão transformando a forma como os cientistas abordam problemas complexos. 
        Elas permitem realizar previsões mais rápidas e precisas, descobrir novos materiais e medicamentos, e otimizar processos industriais de forma eficiente. 
        Essas tecnologias têm aplicações que abrangem desde o design de novos compostos químicos até o avanço em tratamentos personalizados para doenças. 
        A Química Computacional usa modelos matemáticos e simulações computacionais para estudar e prever o comportamento de moléculas e materiais. 
        Quando combinada com a IA, a computação avança ainda mais, oferecendo novas abordagens para a pesquisa e inovação.
    """,
    "Simulações de Moléculas e Materiais": """
        A modelagem computacional de moléculas e materiais é uma ferramenta essencial na química moderna. Com a ajuda da IA, é possível realizar simulações de novos compostos e prever suas propriedades, como reatividade, estabilidade e capacidade de interação com outras moléculas.
        Principais Métodos de Química Computacional:
        - **Mecânica Quântica**: Base para descrever as interações atômicas e moleculares.
        - **Dinâmica Molecular**: Simula o movimento dos átomos em uma molécula ao longo do tempo.
        - **Simulação de Monte Carlo**: Método estatístico utilizado para prever o comportamento de materiais.
        Exemplo prático: A IA foi usada para prever a estrutura de novos compostos para baterias de lítio, acelerando o desenvolvimento de baterias com maior capacidade e durabilidade.
    """,
    "Análise de Dados com IA": """
        A química experimental gera grandes volumes de dados, desde espectros de RMN até resultados de simulações complexas. 
        A IA permite analisar esses dados de forma eficiente, identificando padrões que podem passar despercebidos por métodos tradicionais.
        Exemplos de Aplicações:
        - **Design de Materiais Assistido por Computador (CAMD)**: IA pode analisar grandes bases de dados de materiais e sugerir novos compostos com propriedades desejáveis.
        - **Análise de Dados Espectroscópicos**: Algoritmos de IA são usados para interpretar dados de espectrometria e RMN de forma mais rápida e precisa.
        Exemplo Real: A IA ajudou a identificar novos materiais para células solares de perovskita, com maior eficiência na conversão de energia.
    """,
    "IA e Machine Learning no Desenvolvimento de Medicamentos": """
        A descoberta de medicamentos é uma das áreas mais promissoras para a aplicação de IA. A combinação de IA e Química Computacional pode reduzir significativamente o tempo e o custo do desenvolvimento de novos fármacos, além de melhorar a precisão dos resultados.
        Como a IA Acelera o Desenvolvimento de Medicamentos:
        - **Triagem Virtual**: A IA pode avaliar rapidamente grandes bibliotecas de compostos.
        - **Desenho de Fármacos de Novo**: Algoritmos de IA podem ser usados para projetar novos compostos químicos.
        - **Previsão de Toxidade**: IA pode prever a toxicidade de novos compostos antes de serem sintetizados.
        Exemplo prático: A IA foi usada para acelerar a descoberta de novos antibióticos, encontrando compostos que eram previamente desconhecidos.
    """,
    "Desafios e Oportunidades": """
        Embora a combinação de IA e Química Computacional tenha um enorme potencial, também existem desafios significativos. A precisão dos modelos de IA depende da qualidade dos dados de treinamento, e a interpretação dos resultados pode ser complexa.
        Principais Desafios:
        - **Qualidade dos Dados**: Dados imprecisos ou incompletos podem levar a previsões incorretas.
        - **Interpretação dos Resultados**: Modelos de IA muitas vezes são "caixas pretas".
        - **Capacidade Computacional**: Modelos avançados exigem grande poder de processamento.
    """,
    "Exemplos Práticos de IA na Química Computacional": """
        Diversos exemplos de sucesso mostram como a IA tem sido aplicada de forma prática em áreas como a previsão de propriedades de materiais, design de fármacos e otimização de processos químicos.
        Exemplos Notáveis:
        - **Novos Materiais para Eletrônica**: IA ajudou a identificar materiais com propriedades ótimas para dispositivos eletrônicos flexíveis.
        - **Desenvolvimento de Fármacos**: IA acelerou a identificação de novos compostos para tratamentos contra o câncer.
    """
}

import os
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

def get_response_text(response):
    """Extrai texto da resposta do Gemini com segurança e logs para debug."""
    print("==== DEBUG GEMINI RAW RESPONSE ====")
    print(response)
    print("===================================")

    try:
        if response and response.candidates:
            parts = response.candidates[0].content.parts
            if parts:
                texto = "".join([p.text for p in parts if hasattr(p, "text")]).strip()
                if texto:
                    return texto
        finish_reason = response.candidates[0].finish_reason if response.candidates else None
        return f"Não foi possível gerar uma resposta. (finish_reason={finish_reason})"
    except Exception as e:
        return f"Erro ao interpretar resposta: {e}"


def gerar_resposta(prompt):
    """Executa o Gemini com configuração segura."""
    try:
        api_key = os.getenv("API_KEY_FE")
        if not api_key:
            return "Erro: variável de ambiente API_KEY_FE não definida."

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-2.0-flash")

        response = model.generate_content(
            prompt,
            generation_config=GenerationConfig(
                temperature=0.7,
                max_output_tokens=2048  # ↑ antes era 500
            )
        )
        return get_response_text(response)

    except Exception as e:
        return f"Erro ao gerar resposta: {e}"


def reformular_explicacao(titulo_topico, texto_original):
    prompt = (
        f"O usuário não entendeu o tópico '{titulo_topico}'. "
        f"Aqui está a explicação original: {texto_original}. "
        f"Reformule de forma simples, curta e com exemplos claros. "
        f"NÃO COLOQUE ASTERISCOS '**'. "
        f"Use '<br>' para cada parágrafo e '<b>' para destacar trechos importantes. "
        f"Comece a resposta imediatamente com a explicação reformulada, sem introdução."
    )
    return gerar_resposta(prompt)


def responder_duvida_especifica(pergunta):
    prompt = (
        f"Responda de forma clara, objetiva e explicativa a seguinte pergunta: {pergunta}. "
        f"A resposta deve estar relacionada à <b>química</b>, <b>química computacional</b> ou <b>IA aplicada à química</b>. "
        f"Se a pergunta não estiver relacionada a esses temas, diga apenas: 'Essa pergunta não está relacionada à química ou IA aplicada à química.' "
        f"NÃO COLOQUE ASTERISCOS '**'. "
        f"Use '<br>' para cada parágrafo e '<b>' para destacar trechos importantes. "
        f"Comece direto com a explicação, sem repetições do enunciado."
    )
    return gerar_resposta(prompt)
   
@app.route('/explicar', methods=['POST'])
def explicar():
    dados = request.json
    topico = dados.get("topico")
    duvida = dados.get("duvida")

    # Verificar se o tópico foi selecionado e é válido
    if topico and topico not in secoes:
        return jsonify({"resposta": "Desculpe, o tópico selecionado não é válido."})

    # Se um tópico foi selecionado, forneça uma reformulação do texto original
    if topico:
        texto_original = secoes.get(topico)
        if texto_original:
            resposta = reformular_explicacao(topico, texto_original)
            return jsonify({"resposta": resposta})

    # Caso contrário, responde com uma explicação direta para a dúvida
    if duvida:
        resposta = responder_duvida_especifica(duvida)
        return jsonify({"resposta": resposta})

    return jsonify({"resposta": "Por favor, selecione um tópico ou escreva uma dúvida."})

# end Felipe e Maria

@app.route("/EnemQuestoes")
def EnemQuimica():
    return render_template('EnemQuestoes.html')

# Dielson
@app.route("/Energias")
def energias():
    return render_template('Energias.html')

@app.route("/QuimicaSociedade")
def Sociedade():
    return render_template('QuimicaSociedade.html')

@app.route("/QuimicaAmbiental")
def quimica_hambiental():
    return render_template('QuimicaAmbiental.html')

QUESTIONS_FILE = os.path.join("static", "ArquivoJson", "questions.json")

# Configuração do gemini para responder as questões (ENEM)
API_KEY = os.getenv("API_KEY_ENEM")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/load-questions', methods=['GET'])
def load_questions():
    try:
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
            questions_data = json.load(file)
        return jsonify(questions_data)
    except Exception as e:
        return jsonify({"error": f"Erro ao carregar questões: {str(e)}"}), 500

@app.route('/ia-response', methods=['POST'])
def ia_response():
    data = request.get_json()
    question_text = data.get("question_text")
    image_url = data.get("image") 
    text2 = data.get("text2")
    options = data.get("options")
    correct_index = data.get("correct")

    if not question_text:
        return jsonify({"error": "Texto da pergunta não fornecido."}), 400

    formatted_options = ""
    images_to_send = []

    # Processar alternativas
    if options:
        for i, opt in enumerate(options):
            opt_text = opt.get('text', '')
            opt_image_url = opt.get('image', None)  # Verifica se a alternativa tem imagem
            
            formatted_options += f"{chr(65 + i)}) {opt_text}\n"

            if opt_image_url:
                try:
                    image_response = httpx.get(opt_image_url)
                    if image_response.status_code == 200:
                        image_data = base64.b64encode(image_response.content).decode('utf-8')
                        images_to_send.append({'mime_type': 'image/jpeg', 'data': image_data})
                except Exception as e:
                    print(f"Erro ao processar imagem da alternativa {chr(65 + i)}: {str(e)}")

    correct_option = f"A alternativa correta é: {chr(65 + correct_index)}" if correct_index is not None else "Nenhuma alternativa correta foi fornecida."

    full_prompt = (
        f"Responda de forma objetiva, detalhada e com palavras fáceis de entender e FORNEÇA A ALTERNATIVA CORRETA. "
        f"Se a questão envolver cálculos, explique-os detalhadamente. "
        f"NÃO COLOQUE ASTERISCOS '**'. "
        f"Use '<br>' para cada parágrafo e '<b>' para destacar trechos importantes. "
        f"Responda apenas em português Brasil.\n\n"
        f"Pergunta: {question_text}\n\n"
    )

    if text2:
        full_prompt += f"Texto adicional: {text2}\n\n"

    if formatted_options:
        full_prompt += f"Alternativas:\n{formatted_options}\n\n"

    if correct_option:
        full_prompt += f"{correct_option}\n\n"

    # Adicionar a imagem da questão principal
    if image_url:
        try:
            image_response = httpx.get(image_url)
            if image_response.status_code == 200:
                image_data = base64.b64encode(image_response.content).decode('utf-8')
                images_to_send.insert(0, {'mime_type': 'image/jpeg', 'data': image_data})  # Insere a imagem da questão no início
        except Exception as e:
            print(f"Erro ao processar imagem da questão: {str(e)}")

    # Preparar a entrada do Gemini
    input_data = images_to_send + [full_prompt]  # Primeiro as imagens, depois o texto

    try:
        response = model.generate_content(input_data)
        ai_response = response.text if response and response.text else "Não foi possível obter uma resposta no momento."
        return jsonify({"ai_response": ai_response.strip()})
    except Exception as e:
        return jsonify({"error": f"Erro ao processar a pergunta: {str(e)}"}), 500

def main():
    app.run(port=int(os.environ.get('PORT', 80)), debug=True)

if __name__ == "__main__":
    main()