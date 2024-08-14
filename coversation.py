 # Conversation Tool Program

# Dictionary of responses
responses = {
  "hello": "Hi! How are you?",
  "hi": "Hello! What's up?",
  "how are you": "I'm good, thanks. How about you?",
  "what's up": "Not much. Just chatting.",
  "bye": "See you later!"
}

# Main program
while True:
  user_input = input("You: ").lower()
  if user_input in responses:
    print("Bot:", responses[user_input])
  else:
    print("Bot: Sorry, I didn't understand that.")
  if user_input == "bye":
    break





#You: hello
#Bot: Hi! How are you?
#You: how are you
#Bot: I'm good, thanks. How about you?
#You: what's up
#Bot: Not much. Just chatting.
#You: bye
#Bot: See you later!


