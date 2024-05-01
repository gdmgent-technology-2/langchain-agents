import os
from dotenv import load_dotenv

# Langchain
from langchain import hub
from langchain.schema import HumanMessage, SystemMessage

# Langchain OpenAI
from langchain_openai import ChatOpenAI

# Langchain Community
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

# Agents
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# Set the OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create a chat instance that uses the OpenAI API
llm = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

# Create the messages
message = [
  SystemMessage(content="A user will input in a year and you will get 5 events that happend in that year"),
  HumanMessage(content="2023")
]

# Invoke the large language model (this raises the problem)
# result = llm.invoke(message)
# print(result)

# Create a prompt
prompt = hub.pull("hwchase17/openai-functions-agent")

# Init the wikipedia tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wikitool = WikipediaQueryRun(api_wrapper=api_wrapper)
# print(wikitool.run("HUNTER X HUNTER"))

# Create the tools
tools = [wikitool]

# Init the agent
agent = create_openai_functions_agent(llm, tools, prompt)

# Execute the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke the agent
result  = agent_executor.invoke({ "input": "Name a random event that happened in 2023. Look it up." })

# Outptut the result
print(result)