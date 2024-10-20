1. Entrar no site https://groq.com/ , criar uma conta e gerar uma chave de API
2. Entrar no site https://serper.dev/signup , criar uma conta e gerar uma chave
de API
3. Criar um arquivo .env com as chaves

```
%pip install -U -q python-dotenv
%pip install -U -q crewai
%pip install -U -q crewai_tools
%pip install -U -q langchain_groq
%pip install -U -q langchain_groq==0.1.9
```

#Definição do Agente "Pesquisador de Mercado"
market_researcher = Agent(
	role="Pesquisador de Mercado Sênior, #função do agente
	goal="Garanta que o negócio {ideia} seja respaldado por pesquisas e \
	dados sólidos. Realize uma pesquisa abrangente e realista para a ideia de negocio \
	backstory="Você é um especialista de mercado habilitado para pesquisas de mercado e \
	muito habilidoso em validar ideias de negócios. Você trabalhou com várias empresas \
	estabelecidas." #histórico do agente
	allow_delegation=False, #permissão para delegar tarefas
	verbose=True, #exibir detalhes do agente 
	llm="groq/llama3-8b-8192" #modelo de linguagem usado pelo agente 
)

enterpreneur_agent = Agent()
