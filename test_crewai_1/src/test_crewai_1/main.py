#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from test_crewai_1.crew import ResumeBuilderCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Data Engineering',
    }

    try:
        ResumeBuilderCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

