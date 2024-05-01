import os
from dotenv import load_dotenv

# Langchain
from langchain import hub
from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import LLMMathChain

# Langchain OpenAI
from langchain_openai import ChatOpenAI

# Langchain Community
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun

# Agents
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.agents import Tool

# Set the OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create a chat instance that uses the OpenAI API
llm = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

# Create a prompt
prompt = hub.pull("hwchase17/openai-functions-agent")

# Multiple Tools

# Math tool
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
math_tool = Tool.from_function(
  func=llm_math_chain.run,
  name="Calculator",
  description="Useful for answering math questions. Only math questions and nothing else. Only input math expressions."
)

# Duck Duck Go Tool
search = DuckDuckGoSearchRun()

# Combine tools
tools = [math_tool, search]

# Init the agent
agent = create_openai_functions_agent(llm, tools, prompt=prompt)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke the agent
result = agent_executor.invoke({ "input": "Who was the band behind the track Back in Black and how many years have been passed from 2024 since it's release?" })

# Output the result
print(result)