"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Everything was correct, but interestingly enough different representations gave a different answer.
Plain one was the `Haymarket Vaults`.
Haymarket Vaults has the exact capacity.
Maybe attention just triggered at 160 both in the question and in the list (i.e. just a pattern match).
Since checking that 180 is bigger than 160 would require reasoning (though a very minimal one).
And XML and sandwich gave `The Albanach`, which is the first one in the list.
Llama-3.3-70B is not a reasoning model, but I assume that when it encounters structured data, it's easier for it to reason that 180 is more than 160.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The result is exactly the same as in Part A.
This means that the distraction is not strong enough for this kind of model.
Though the answers are not the same again (and exactly as in the previous part).
This means that the model reasoning process (i.e. structured vs plain) stays the same even with distractions.

The hardest distractor should be The Holyrood Arms, because it satisfies both capacity and vegan, but doesn't have the correct status.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Now the model returned `The Haymarket Vaults` regardless of the structure.
But we used a different model, which means that it has a different internal reasoning.
And it triggered at the number 160 in all of the cases.
This means the structuring effect we had on the bigger model disappeared completely.
And the model just pattern-matched 160 in all cases.
But even with this pattern-match it was able to discard the `The Holyrood Arms` distractor, even though it was earlier and also had 160.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when (at least should matter when) the model is weaker or the signal-to-noise ratio is lower.
But in this experiment we didn't see failures, which means that this effect is very task dependent (or these specific examples were too easy for these models).
"""
