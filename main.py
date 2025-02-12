import os
from crewai import Agent, Task, Crew, Process
# from langchain_openai import ChatOpenAI
from langchain_community.llms import OpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

# from langchain.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()


os.environ["OPENAI_API_KEY"] = str(config("OPENAI_API_KEY"))
os.environ["OPENAI_ORGANIZATION"] = str(config("OPENAI_ORGANIZATION_ID"))

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, topic, industry):
        self.topic = topic
        self.industry = industry

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.agent_1_name(self.topic, self.industry)
        custom_agent_2 = agents.agent_2_name(self.topic, self.industry)

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.topic,
            self.industry,
        )

        custom_task_2 = tasks.task_2_name(
            custom_agent_2,
            self.topic,
            self.industry,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("Explore what is an issue in the industry of your choice")
    print("-------------------------------")
    topic = input(dedent("""Enter topic: """))
    industry = input(dedent("""Enter industry: """))

    custom_crew = CustomCrew(topic, industry)
    result = custom_crew.run()
    print("\n\n########################")
    print("## These are the results of the research done by your crew:")
    print("########################\n")
    print(result)
