# telegram-bot
Created a telegram bot that sends me a reminder to solve a leetcode problem daily

## Requirements
1. A telegram goup and its id
2. A telegram bot

### Steps to create a telegram bot
1. Search for BotFather in your telegram app.
2. Send 'hi', BotFather then replies with a list of commands to create, edit, and change bot settings.
3. To create a new bot, type '/newbot', BotFather will then ask you to provide a name to the newly created bot. (for example: reminderbot)
4. BotFather will then ask you to provide a username to the bot. (for example: reminder_bot)
5. BotFather will now create the bot and provide you with a token.

## Execution steps
1. Add the telegram bot to the telegram group.
2. To fetch the chat id:
   1. send `/my_id <bot_username>` in the telegram group(for example:`/my_id remind aer_bot`)
   2. Hit `https://api.telegram.org/bot<add_token>/getUpdates` URL in the browser, you will receive a json reaponse which will include chat details:
      for example: `"chat":{"id": <chat_id>, "title":<group_name>,..}`

      
