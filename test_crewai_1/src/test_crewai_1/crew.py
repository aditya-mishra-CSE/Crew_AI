from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, FileWriterTool

@CrewBase
class ResumeBuilderCrew():
    """ResumeBuildercrew"""

    agents: List[BaseAgent]
    tasks: List[Task]

      # Define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def resumebuilder(self) -> Agent:
        return Agent(
            config=self.agents_config['resumebuilder'], # type: ignore[index]
            verbose=True,
            tools=[FileWriterTool()]
        )

    @agent
    def resumereviewandreconstruct(self) -> Agent:
        return Agent(
            config=self.agents_config['resumereviewandreconstruct'], # type: ignore[index]
            verbose=True,
            tools=[FileWriterTool()]
        )

 
    @task
    def resumebuilder_task(self) -> Task:
        return Task(
            config=self.tasks_config['resumebuilder_task'], # type: ignore[index]
        )

    @task
    def resumereviewandreconstruct_task(self) -> Task:
        return Task(
            config=self.tasks_config['resumereviewandreconstruct_task'], # type: ignore[index]
            output_file='output/resume.txt'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeBuildercrew"""
        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
