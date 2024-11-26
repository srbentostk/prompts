import os
import json
from openai import OpenAI

client = OpenAI()

# Diretório dos arquivos traduzidos
translated_dir = './arquivos_traduzidos'
# Diretório para salvar os arquivos JSON
json_output_dir = './json_outputs'
os.makedirs(json_output_dir, exist_ok=True)
# Prefixo da URL
url_prefix = 'https://github.com/srbentostk/prompts/blob/main/arquivos_traduzidos/'

# Lista de tags
tags_list = [
    'Código', 'Criação de Conteúdo', 'Software', 'Cybersegurança', 'Ciência de Dados', 'Tecnologia', 'Análise de Texto',
    'Startups', 'Twitter', 'Marketing', 'Feedback', 'Extração de Dados', 'AI', 'Checar Gramática', 'Livros',
    'Estudantes', 'Escola', 'Trends de Tech', 'Sumário', 'Entrevista de Emprego', 'Conselho de Carreira', 'Currículo',
    'Youtube', 'Proofreading', 'Escrita', 'Psicologia', 'Colaboração', 'Brainstorm', 'Produtividade', 'Procura de Emprego',
    'Filosofia', 'Auto Ajuda', 'Motivação', 'Cursos', 'Pesquisa', 'Story Telling', 'Jogos', 'Visualizações', 'Dados',
    'Engenheiros de Software', 'Empreendedor', 'LinkedIn', 'Gerente de Produto', 'Marca Pessoal', 'Roteiro de Vídeo',
    'Redes Sociais', 'Imóveis', 'Apresentação', 'Coach de Vida', 'Arte', 'Ganchos', 'Guias de Estudo', 'Dicas de Aluguel',
    'Pesquisas', 'Ética', 'Desenvolvimento de Jogos', 'Gestão de Prompts', 'Negociação', 'Música', 'Jurídico', 'Debate',
    'Pesquisa de Mercado', 'Go To Market', 'Reuniões', 'SEO', 'Citações Inspiradoras', 'Limpeza de Dados', 'Solução de Problemas',
    'TikTok', 'Ciência', 'Oratória', 'Design Gráfico', 'Podcast', 'Gerente de Produto', 'Coaching', 'Construção',
    'Compra de Imóveis', 'Instagram', 'Contratação', 'Resolução de Conflitos', 'Carreira Corporativa', 'Comunicação',
    'Gestão do Tempo', 'Pequenos Negócios', 'Blog', 'Desenvolvimento Web', 'Viagem', 'Finanças', 'Bancário',
    'Regulamentações', 'Cultura', 'Liderança', 'Treinamento', 'Trabalho Remoto', 'Receitas Culinárias', 'Filosofia Alimentar',
    'Restaurante', 'Finanças Pessoais', 'Orçamento', 'Investimento', 'Beleza', 'Desenvolvimento Pessoal', 'Geração de Leads',
    'Idiomas', 'Ensino', 'Seguros', 'Medicina', 'Saúde Mental', 'Suporte ao Cliente', 'Cuidados Infantis', 'Política',
    'Desenvolvimento de Apps', 'Freelancer', 'Saúde', 'Equilíbrio Trabalho-Vida', 'Terapia', 'Governo', 'Viagens de Luxo',
    'Dicas de Fotografia', 'Academia', 'Scrum', 'Acadêmicos', 'Gestão', 'Chatbots', 'Ecoturismo', 'ONG', 'Biodiversidade',
    'Esportes', 'Estratégia', 'Criptomoedas', 'Ações', 'Email', 'Privacidade', 'Educação', 'Vídeo', 'Apps', 'Moda',
    'E-commerce', 'Feedback de Usuário', 'Economia', 'Networking', 'História', 'Projetos DIY', 'Franquias',
    'Estratégia de Negócios', 'Idioma', 'Blockchain', 'Biologia', 'Gestão de Programas', 'Anúncios', 'Notícias',
    'Gestão de Equipes', 'Negócios', 'Automação', 'Desenvolvimento de Produto', 'Escrita Criativa',
    'Livro de Colorir', 'Mudança de Carreira', 'Família', 'Paternidade', 'Vendas', 'Renda Passiva', 'Religião', 'Dieta',
    'Impostos', 'Planejamento de Eventos', 'Agile', 'Olheiro', 'Desenvolvimento de Jogadores', 'Marketing de Rede',
    'Excel', 'Entrada de Dados', 'Bem-estar', 'Jardinagem', 'Literatura', 'Acessibilidade', 'Gestão de Reputação',
    'Engajamento de Funcionários', 'Decoração', 'Design de Interiores', 'YouTube', 'Subsídios', 'Gestão de Projetos',
    'Acadêmico', 'TDAH', 'Agendamento', 'Relacionamentos', 'Roteiro', 'Diálogo', 'Crianças', 'Resolução de Problemas',
    'Fantasy Sports', 'Gestão de Liga', 'Plano de Saúde', 'RH', 'Certificação', 'Criativo', 'Halloween', 'Projetos Criativos',
    'Outline', 'Mindfulness', 'Análise', 'Alívio do Estresse', 'Documentação', 'Comunicação com Stakeholders',
    'Processo de Encerramento', 'Contabilidade', 'Análise de Dados', 'Viagem Solo', 'Guias', 'Criatividade', 'Humor',
    'Animais', 'Previsões', 'Engajamento Comunitário', 'Divulgação Religiosa', 'Planejamento Estratégico',
    'Crescimento Pessoal', 'Fitness', 'Redação de Subsídios', 'Proposta', 'Gestão de Serviços de TI', 'Gestão de Problemas',
    'Excelência Operacional', 'Aposentadoria', 'Segurança', 'Recrutamento', 'Gestão de Talentos', 'Pinterest',
    'Consultoria', 'Trading de Opções', 'Assistência Social', 'Compliance', 'Auditoria', 'Planejamento de Lições',
    'Avaliação', 'Orientação', 'Gestão de Crédito', 'Plano de Negócios', 'Fintech', 'Sistemas de Pagamento',
    'Insights do Consumidor', 'Matemática', 'TI', 'Enfermagem', 'Marketing de Afiliados', 'API',
    'Marketing Digital', 'Redação de Propostas', 'RFP', 'Desenvolvimento de Negócios', 'MBA', 'Farmacêutica',
    'Biotecnologia', 'Contabilidade Forense', 'Análise Financeira', 'Financiamento', 'Planejamento', 'ONG',
    'Desenvolvimento Comunitário', 'Suporte Comunitário', 'Captação de Recursos', 'Assistente Virtual', 'Estatística',
    'Comunidade', 'Documentário', 'Interpretação', 'Desenvolvimento Profissional'
]

# Inicializa lista para armazenar os dados
data_list = []

# Configurar API Key
#openai.api_key = os.getenv("OPENAI_API_KEY")

# Lista de arquivos no diretório
files = [f for f in os.listdir(translated_dir) if f.endswith('.md')]

for filename in files:
    file_path = os.path.join(translated_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Preparar mensagens para a API
    messages = [
        {
            "role": "system",
            "content": "Você é um assistente que ajuda a extrair informações de arquivos."
        },
        {
            "role": "user",
            "content": f"""
A partir do nome do arquivo e do conteúdo do arquivo Markdown, você deve fornecer as seguintes informações:

1. Tradução do nome do arquivo para o português brasileiro, sem a extensão. Exemplo: 'recommend_artists.md' -> 'Recomendar Artistas'.

2. Uma breve descrição (até 400 caracteres) da intenção do prompt contido no arquivo. A descrição deve ser em português brasileiro.

3. Até três tags relevantes ao conteúdo do prompt, escolhidas da seguinte lista:
{', '.join(tags_list)}

Por favor, forneça as informações no seguinte formato:

Nome traduzido: [nome traduzido]
Descrição: [descrição]
Tags: [tag1], [tag2], [tag3]

Agora, aqui estão o nome do arquivo e o conteúdo:

Nome do arquivo: {filename}
Conteúdo do arquivo:
{content}
"""
        }
    ]

    # Chamada à API OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            top_p=1
        )
        output = response.choices[0].message.content.strip()
        print(f"Output for {filename}: {output}")
        # Extrair as informações do output
        nome_traduzido = ''
        descricao = ''
        tags = []

        lines = output.split('\n')
        for line in lines:
            if line.startswith('Nome traduzido:'):
                nome_traduzido = line[len('Nome traduzido:'):].strip()
            elif line.startswith('Descrição:'):
                descricao = line[len('Descrição:'):].strip()
            elif line.startswith('Tags:'):
                tags_line = line[len('Tags:'):].strip()
                tags = [tag.strip() for tag in tags_line.split(',') if tag.strip() in tags_list][:3]
        
        # Se não conseguiu extrair, usar valores padrão
        if not nome_traduzido:
            nome_traduzido = os.path.splitext(filename)[0].replace('_', ' ').title()
        if not descricao:
            descricao = 'Descrição não disponível.'
        if not tags:
            tags = []

        # Construir URL
        url = url_prefix + filename
        print(f"Processando {filename}... URL: {url} - Nome: {nome_traduzido} - Tags: {tags} - Descricao: {descricao}")
        # Adicionar ao data_list
        data ={
            "filename": filename,
            "nome": nome_traduzido,
            "url": url,
            "descricao": descricao[:400],
            "tags": tags
        }
        data_list.append(data)
        # Definir o caminho do arquivo JSON de saída
        json_output_path = os.path.join(json_output_dir, f"{os.path.splitext(filename)[0]}.json")
        # Salvar o resultado em um arquivo JSON individual
        with open(json_output_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            print(f"Arquivo JSON criado com sucesso: {json_output_path}")

    except Exception as e:
        print(f"Erro ao processar {filename}: {e}")
    

# Salvar o resultado em um arquivo JSON
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)
    print("Arquivo JSON criado com sucesso.")
