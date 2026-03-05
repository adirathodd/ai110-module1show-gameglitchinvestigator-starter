# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  It was a simple number guessing game which is supposed to be from 1 to 100. There is also a developer debug section which also shows some of the internal metrics of the app.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  - If the number guessed is higher than the secret, then the hint actually says to go lower and vice versa.
  - After you guess the number, you cannot restart by clicking New Game and it keeps showing the 
  "You already Won. Start a new game to play again." message.
  - The history does not update right away when the user clicks submit guess.
  - The history does not reset when the user clicks New Game.
  - Attempts counter starts at 1 when it should be starting at 0
  - The website says I am out of attempts when I have 1 attempt left

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Copilot.


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It successfully created the test cases for checking the 'check_guess' function. I verified by making sure the results actually make sense.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The way it created the 'check_guess' function was wrong because of its output. If the result was "Too high", then the message would be "Go HIGHER" when it should be "Go LOWER" and vice versa.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - For the 'check_guess' function, I fixed the function and then went on the game to verify the hint.
    If the hint was right for my guess and the secret, then I was satisfied.
  - For the attempts counter, I made sure the starting number was 0 instead of 1 to give the user 8 tries and I verified it by seeing the number on the website.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I ran the test to verify the correct message for a guess and secret. I realized the output of the function is a tuple and not a singular message.

- Did AI help you design or understand any tests? How?

  AI helped me design the tests for when the inputs to the 'check_guess' function are strings instead of integers by creating edge cases for me.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  The original app didn't use Streamlit's session state to store the secret number. Every time the page reran (which happens whenever you interact with a button or input field), the code would re-execute from top to bottom, generating a new random number without checking if one already existed. This meant the secret changed with every click.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit reruns mean that every time a user interacts with the app (clicking buttons, typing in boxes), the entire script executes from top to bottom again. Without session state, variables reset. Session state is like a persistent memory that survives these reruns—it's a dictionary (`st.session_state`) that keeps data alive across multiple script executions. By checking if a variable exists in session state before setting it, you can ensure it's only created once and then reused.

- What change did you make that finally gave the game a stable secret number?

  I added a check: `if "secret" not in st.session_state:` before generating the random number. This ensures that the secret is only generated once when the game starts, and on every subsequent rerun, the existing secret is used instead of creating a new one. This pattern was applied to all persistent game state (attempts, score, status, history).

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I want to build a habit of writing tests early and running them frequently, especially after refactoring code. Creating test cases for edge cases (like when inputs are strings vs. integers) helped me catch the root cause of the bug quickly. I'll apply this practice to future projects by defining test cases before fixing bugs, which forces me to think about what the correct behavior should be.

- What is one thing you would do differently next time you work with AI on a coding task?

  I would be more skeptical of AI-generated code, especially when it involves logic or comparisons. Even though the code looked reasonable at first glance, it had a subtle but critical bug where it mixed string and numeric comparisons. Next time, I'll ask the AI to walk me through the logic step-by-step, or I'll manually trace through the code with concrete examples before trusting it to work correctly.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI-generated code can be deceptively wrong—it can run without errors but produce incorrect results due to subtle logic errors. This taught me that AI is a useful starting point, not a finished product, and that thorough testing and critical review are essential before shipping any AI-generated code to production.
