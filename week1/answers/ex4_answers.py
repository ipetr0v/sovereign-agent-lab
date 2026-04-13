"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = [
    "search_venues",
    "get_venue_details"
]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "It seems there are no Edinburgh venues currently available that can accommodate 300 guests with vegan options. Would you like to:\n1. Try reducing the minimum capacity requirement?\n2. Check for venues with vegan options that have lower capacity?\n3. Search for venues without the vegan requirement?\n\nLet me know how you'd like to adjust the criteria!"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changed The Albanach's status to "full" in mcp_venue_server.py and reran the client.
Query 1 returned only The Haymarket Vaults instead of both venues.
The client code (exercise4_mcp_client.py) didn't need any changes at all.
Only the server data changed, and the client picked it up automatically via MCP discovery.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 226   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 50    # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP gives you runtime discovery.
The client doesn't know what tools exist until it connects.
You can add, remove or change tools on the server without touching the client at all.
Also multiple different clients (LangGraph, Rasa and anything that speaks MCP) can share the same server.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Planner sits at the top and breaks down Rod's big WhatsApp request into small steps like "find venue" or "make flyer".
- The Executor is just the ReAct loop we built. It takes those small steps and actually runs the tools until it gets an answer.
- The Shared MCP Server is the server we just tested. Both the loop and the Rasa agent connect to it to share tools.
- The Handoff Bridge is the glue between them. If the loop needs to talk to a human, it hands off to Rasa. If Rasa needs research, it hands back.
- The Rasa CALM Agent handles the phone call with the pub manager using strict rules so it doesn't mess up.
- Persistent Memory lets the agent remember what it did before so it doesn't ask the same questions twice.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
I'd use LangGraph for the research and Rasa for the call.
In Exercise 2, LangGraph figured out on its own which venues to check and skip.
In Exercise 3, Rasa just collected three specific answers and followed business rules.
Swapping them is a bad idea. LangGraph might just improvise and accept a bad deposit because it "thinks" it is okay.
And you can't write a Rasa flow for every possible search query you might make.
"""
