import os

from crewai import Agent, Task, Crew
from langchain_core import ChatGroq
from crewai_tools import ServerDevTool
from dotenv import load_dotenv
from litellm import completion

#load_dotenv('/content/drive/MyDriver/Colab Notebooks/IA/.env')
load_dotenv('.env')

#from pyexpat.errors import messages

response = completion(
    model="groq/llama3-8b-8192",
    messages=[
        {"role": "user", "content": "hello"}
    ]
)
print(response)

#base_url: "https://localhost:8080/"

#Definição do Agente "Pesquisador de Mercado"
market_researcher = Agent(
	#função do agente"
	#histórico do agente - backstory
	#permissão para delegar tarefas - allow_delegation
	#exibir detalhes do agente - verbose
	#modelo de linguagem usado pelo agente - llm
	role="Pesquisador de Mercado Sênior",
	goal="Garanta que o negócio {ideia} seja respaldado por pesquisas e dados sólidos. Realize uma pesquisa abrangente e realista para a ideia de negocio",
	backstory="Você é um especialista de mercado habilitado para pesquisas de mercado e muito habilidoso em validar ideias de negócios. Você trabalhou com várias empresas estabelecidas." ,
	allow_delegation=False,
	verbose=True,
	llm="groq/llama3-8b-8192"
)

#Definição do agente "Empreendedor"
enterpreneur_agent = Agent(
	#função do agente" - role
	#histórico do agente - backstory
	#permissão para delegar tarefas - allow_delegation
	#exibir detalhes do agente - verbose
	#modelo de linguagem usado pelo agente - llm
	role="Empreendedor experiente",
	goal="Criar um plano de marketing e um plano de negócios para {ideia}",
	backstory="Você construiu empresas de sucesso. Você tem habilidade de criar novas ideias de negócios e de planos de marketing." ,
	allow_delegation=False,
	verbose=True,
	llm="groq/llama3-8b-8192"
)

#Importação da ferramenta para buscas na web
tool = ServerDevTool()

#Definir as tarefas para o pesquisador de mercado
task_market_researcher = Task(
	description="Analise os pontos fortes, fracos, oportunidades e ameaças da ideia de negócio {ideia}. Estimar o tamanho do mercado para essa ideia. Avalie a viabilidade do modelo de negócios. Avalie a existência de outras empresas com a mesma ideia no mercado. Força insigts para a criação do plano de negócios", #tarefa a ser relaizada
	expected_output=(
		"Um relatório detalhado de pesquisa de mercado para a ideia mencionada {ideia}. Inclua as referências a dados externos para análise de mercado."
), #saida esperada
	tools=[tool], #ferramenta a ser utilizada
	agent=market_researcher,
)

#Definir as tarefas para o empreendedor
task_enterpreneur = Task(
	description="Crie o plano de marketing e o plano de negócios para a {ideia} Garanta que não haja discrepância entre os planos gerados. Verifique se todos os conceitos importantes de planos de negócios e de marketing foram cobertos", #tarefa a ser relaizada
	expected_output=(
		"A saída deve conter duas partes: um plano de negócio final para a {ideia} E um plano de marketing final para a {ideia}"
		), #saida esperada
	tools=[tool], #ferramenta a ser utilizada
	agent=enterpreneur_agent,
	output_file="analise.md"
)

#Criação do grupo de agentes
crew = Crew(
	agents=[market_researcher, enterpreneur_agent],
	task=[task_market_researcher, task_enterpreneur],
	verbose=True,
	max_rpm=25
)

result = crew.kickoff(
	input={"ideia": ""}
)


