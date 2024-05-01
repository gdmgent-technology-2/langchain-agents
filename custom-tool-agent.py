import os
from dotenv import load_dotenv

# Custom tools
from tools.system_time_tool import check_system_time

# Custom templates
from templates.react_template import get_react_prompt_template

# LangChain
from langchain import hub

# LangChain OpenAI
from langchain_openai import ChatOpenAI

# Agents
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor

# Set the OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Choose the LLM to use
llm = ChatOpenAI()

# set my message
query = "What's the current time in New York, based on my current time. Just show the time in New York and not the date?"

# set the tools
tools = [check_system_time]

# Get the react prompt template
prompt_template = get_react_prompt_template()

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke
result = agent_executor.invoke({"input": query})

# Print the result
print(result)
