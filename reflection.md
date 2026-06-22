# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The UI/UX was friendly and the instructions. The title displayed immediately gave an idea of what the game was about. The hints were inconsistent and often told me to "Go lower" when I actually needed to guess higher.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hint direction was backwards/inconsistent ("Go lower" when the guess was too low).
  2. The New Game button did not clear old input/history state.
  3. The game score did not reset with each new game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 20    | Go Higher         | Hint said "Go Lower" (wrong direction) | "none" |  
| 15    | Go Higher         | Hint said "Go Lower" (wrong direction) | "none" | 
| 5     | Go Higher         | Hint said "Go Lower" (wrong direction) | "none" | 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
