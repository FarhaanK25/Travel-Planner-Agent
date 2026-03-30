from tools import web_search
from llm import ask_llm


def run_travel_agent(user_goal):

    reasoning_log = []

    # STEP 1 – Understand user goal
    reasoning_log.append("Step 1: Understanding the travel goal")

    # STEP 2 – Search travel information
    reasoning_log.append("Step 2: Searching travel information from web")
    search_results = web_search(user_goal)

    # STEP 3 – Generate travel plan using LLM
    reasoning_log.append("Step 3: Generating detailed travel itinerary")

    prompt = f"""
You are a professional AI Travel Planner.

User Request:
{user_goal}

Travel Information:
{search_results}

Your task is to create a COMPLETE PROFESSIONAL TRAVEL PLAN.

IMPORTANT RULES:

1. If user DOES NOT give a budget, estimate a realistic budget.
2. Suggest REAL hotels with approximate price per night.
3. Provide day-wise itinerary.
4. Provide detailed cost breakdown for EACH day.
5. Suggest restaurants and activities.

Your response must follow this structure:

------------------------------------------------

TRIP OVERVIEW
Destination summary
Best time to visit

------------------------------------------------

RECOMMENDED HOTELS
Hotel Name
Price per night
Short description

Give 3 hotel options:
Luxury
Mid-range
Budget

------------------------------------------------

DAY-WISE TRAVEL PLAN

Day 1
Places to visit
Activities
Restaurants

Estimated Costs
Hotel:
Food:
Activities:
Transport:
Misc:

Total for Day 1

Repeat for all days.

------------------------------------------------

TOTAL TRIP COST ESTIMATE

Hotel Total
Food Total
Activities Total
Transport Total
Miscellaneous

Grand Total Estimated Budget

------------------------------------------------

TRAVEL TIPS

Local transport advice
Best areas to stay
Safety tips
"""

    result = ask_llm(prompt)

    reasoning = "\n".join(reasoning_log)

    final_output = f"""
AGENT REASONING
----------------
{reasoning}

==============================

{result}
"""

    return final_output