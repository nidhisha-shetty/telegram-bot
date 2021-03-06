# telegram-bot
Created a telegram bot that sends me a reminder to solve a leetcode problem daily

## Requirements
1. A telegram group and chat id
2. A telegram bot

### Steps to create a telegram bot
1. Search for BotFather in your telegram app.
2. Send `hi`, BotFather then replies with a list of commands to create, edit, and change bot settings.
3. To create a new bot, type `/newbot`, BotFather will then ask you to provide a name to the newly created bot. (for example: `reminderbot`)
4. BotFather will then ask you to provide a username to the bot. (for example: `reminder_bot`)
5. BotFather will now create the bot and provide you with a `token`.

## Execution steps
1. Add the telegram bot to the telegram group.
2. To fetch the chat id from the group:
   1. send `/my_id <bot_username>` in the telegram group(for example:`/my_id reminder_bot`)
   2. Hit `https://api.telegram.org/bot<add_token>/getUpdates` URL in the browser, you will receive a json response which will include chat details:
      for example: `"chat":{"id": <chat_id>, "title":<group_name>,..}`
3. Add this chat id in the below URL:
`base_url="https://api.telegram.org/bot<add_token>/sendMessage?chat_id=<chat_id>&text=\"{}\"".format(message)`
4. Executing the script will give you a reminder on your telegram app to solve a leetcode problem, however in this case you get the reminder on manually executing the script.
5. Inorder, to automate the execution of the python script daily,you can add a cron job.

## Steps to create a cron job
1. Execute **crontab -e** command to select an editor (select 2 for default nano editor).
2. Now, to create the job and exexute it at a specific time, enter the time of job execution in **minute hour days-in-month months days-of-week** format. <br><br>
   For example: `45 5 * * *`
   This indicates the job will execute at 5:45 all-days-in-a-month every-month all-days-of-week <br><br> 
   That is, the job will execute daily at 5:45 <br><br>
**Note:** Execute **cat /etc/crontab** command to know more about cron job creation commands.


