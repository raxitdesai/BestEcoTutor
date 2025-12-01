from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.apps import AdkApp
from google.adk.sessions import InMemorySessionService

from tools.footprint_tools import calculate_footprint, simulate_reduction
from tools.goal_tools import store_goal

# Sub-agents
intake_agent = Agent(
    name="intake_agent",
    model="gemini-2.5-flash",
    description="Collects sustainability usage data",
)

footprint_agent = Agent(
    name="footprint_agent",
    model="gemini-2.5-flash",
    description="Calculates carbon use and reduction plans",
    tools=[calculate_footprint, simulate_reduction],
)

coach_agent = Agent(
    name="coach_agent",
    model="gemini-2.5-flash",
    description="Creates personalized plans and educational content",
    tools=[store_goal],
)

root_agent = Agent(
    name="eco_tutor_root",
    model="gemini-2.5-flash",
    description="EcoTutor root orchestrator",
    sub_agents=[intake_agent, footprint_agent, coach_agent],
)

session_service = InMemorySessionService()

eco_app = AdkApp(root_agent=root_agent, session_service=session_service)

runner = Runner(app=eco_app)
