from highrise.__main__ import *
import time

"""Bot Settings"""
room_id = "629883d1af4572026d275f3b"
bot_token = "2796ff6037fa4e8f1361092c1f3147b277ebe4a5f3e8f42a38f94bbc31ebb5d4"
bot_file = "main"
bot_class = "MyBot"

if __name__ == "__main__":
  definitions = [
    BotDefinition(
      getattr(import_module(bot_file), bot_class)(),
      room_id, 
      bot_token)]  # More BotDefinition classes can be added to the definitions list
  while True:
    try:
      arun(main(definitions))
    except Exception as e:
      # Print the full traceback for the exception
      import traceback
      print("Caught an exception:")
      traceback.print_exc()  # This will print the full traceback       
      time.sleep(1)       
      continue
