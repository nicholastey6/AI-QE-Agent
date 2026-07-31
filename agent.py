
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

from tools.database_tool import search_failure


def database_search(text):

    result = search_failure(text)

    return str(result)



tools = [

Tool(
    name="Failure Database Search",
    func=database_search,
    description=
    """
    Search previous semiconductor failures
    and return similar cases.
    """
)

]


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)


def ask_agent(question):

    return agent.run(question)
