# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "Here we are seeking for most common problems"

    def task_1_name(self, agent, topic, industry):
        return Task(
            description=dedent(
                f"""
            List the identified problems related to {topic} in the industry of {industry}
            
            {self.__tip_section()}
    
            Search in Internet for more information about {topic} in the industry of {industry}
            
        """
            ),
            expected_output=dedent(f"""Create a bullet list of the problems related to {topic} in the industry of {industry}"""),
            agent=agent,
        )

    def task_2_name(self, agent, topic, industry):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and search for each different subject related to the value chain of {topic}.
                                       
            Explore for the best locations to grow {topic}.
        """
            ),
            expected_output=dedent(f"""elaborate a summary of the most common problems related to the value chain of {topic} in the industry of {industry}"""),
            agent=agent,
        )
