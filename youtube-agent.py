import os
from dotenv import load_dotenv

# Langchain
from langchain import hub

# Langchain OpenAI
from langchain_openai import ChatOpenAI

# Langchain Community
from langchain_community.tools import YouTubeSearchTool
from langchain_community.document_loaders import YoutubeLoader

# Agents
from langchain.agents import Tool
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# Set the OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create a chat instance that uses the OpenAI API
llm = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

# Create a prompt
prompt = hub.pull("hwchase17/openai-functions-agent")

# Init the YouTube tool
youtube_search_tool = YouTubeSearchTool()

# Create the tools
tools = [youtube_search_tool]

# Init the agent
agent = create_openai_functions_agent(llm, tools, prompt)

# Execute the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke the agent
result  = agent_executor.invoke({ "input": "Find some YouTube videos about AC/DC and get the description of the first encountered video." })

# Outptut the result
print(result)