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

  I decided a bug was really fixed by checking it in two ways: first with a focused test, and then by running the actual Streamlit game again. I did not want to only trust that the code “looked right,” because some of the bugs only showed up when the game reran or when a certain type of guess was entered. My goal was to confirm that the fixed behavior matched what a player would expect.

  One test I ran was for the high/low hint logic. For example, when the secret number was 50 and the guess was 60, the game should return “Too High.” When the guess was 40, it should return “Too Low.” This helped prove that the comparison logic was no longer reversed. I also manually tested the game in Streamlit by entering guesses above, below, and equal to the secret number to make sure the live game matched the test results.

  I also checked the state-related bugs by playing more than one round and watching whether the score, guesses, and game messages stayed consistent after each input. Since Streamlit reruns the script after interaction, I had to make sure important values were stored in st.session_state instead of being reset every time the page refreshed.

  AI helped me design and understand the tests by suggesting simple pytest cases that targeted one bug at a time. Instead of testing the entire game at once, the AI helped me focus on small pieces of logic, like checking a guess or parsing input. I still reviewed the suggestions myself and verified them by running pytest and then testing the Streamlit app manually.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I learned that Streamlit works differently from a normal program that just runs once from top to bottom. In Streamlit, the whole script reruns whenever the user interacts with the app, such as pressing a button or submitting a guess. I would explain it to a friend like this: Streamlit rebuilds the page every time something happens, so if you do not save important information somewhere, the app can “forget” it.

  That is why st.session_state is important. It acts like the app’s memory between reruns. Values like the secret number, score, number of guesses, game status, and messages need to be stored in session state so they do not disappear every time Streamlit reloads the script.

  Before this project, I thought a variable would automatically keep its value while the app was running. Now I understand that regular variables can reset during a rerun, but session state keeps track of the data that should survive between user actions. This helped me understand why some bugs were not just logic bugs, but state management bugs.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
