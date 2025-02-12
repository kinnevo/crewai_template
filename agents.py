from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = OpenAI(model="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = OpenAI(model="gpt-4", temperature=0.7)

    def agent_1_name(self, topic, industry):
        return Agent(
            role=dedent(f"Research Analyst in the industry of {topic} "),
            backstory=dedent(f"""You have been 10 years in the industry of {industry} and you are an expert in the field"""),
            goal=dedent(f"""Find 10 problems related to {topic} in the industry of {industry} """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_2_name(self, topic, industry):
        return Agent(
            role="""Value Chain Analyst in the industry of {topic}""",
            backstory=dedent(f"""You have been 10 years as a buyer expert in the industry of {industry}"""),
            goal=dedent(f"""Provide your point of view of the limitations of the value chain of {topic} in the industry of {industry}"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
