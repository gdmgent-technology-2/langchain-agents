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
from langchain.agents import load_tools
from langchain.agents import AgentExecutor

# Set the serp api key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
serpai_api_key = os.getenv("SERPAPI_API_KEY")

# Create a chat instance that uses the OpenAI API
llm = ChatOpenAI(
  temperature=0.5,
  openai_api_base="http://localhost:1234/v1",
  openai_api_key="not needed"
  #openai_api_key=openai_api_key
)

# Create the messages
message = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="What is Britney Spears recently doing?")
]

#Invoke the large language model (this raises the problem)
result = llm.invoke(message)
print(result)

# Create a prompt
prompt = hub.pull("hwchase17/openai-functions-agent")

# Init the toolkit
tools = load_tools(["serpapi"], llm=llm, serpapi_api_key=serpai_api_key)

# # Init the agent
agent = create_openai_functions_agent(llm, tools, prompt)

# # Execute the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# # Invoke the agent
result  = agent_executor.invoke({ "input": "How much did Trump needed to pay for court recently?" })

# # Outptut the result
print(result)