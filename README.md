Download the source code and open in IDE/Console of your choice. You just need to eventually be able to run it and start the server.

Head over to https://discord.com/developers/applications and create a new application. Copy the unique secret token (don't share this) when you have it. There is a place at the bottom of the source code where you'll add that -- that should be the only change you need to make to the code to at least get it up and running.

Once your application is created make sure all of the privileged gateway intents are enabled. You really should only need 'Server Members Intent' and 'Message Content Intent' but just enable all - it doesn't hurt anything.
![image](https://github.com/doranmaul/discord-export-members-bot/assets/144544434/b44a6ce5-c72b-45b7-a701-2196bf82aa27)

Next head over to OAuth2 > General and add the following redirect uri: "http://localhost". 
![image](https://github.com/doranmaul/discord-export-members-bot/assets/144544434/6b91be92-8418-40d1-9166-817100e8c05e)

Then head to OAuth2 > URL Generator and select the following: 
![image](https://github.com/doranmaul/discord-export-members-bot/assets/144544434/c7ee26b7-e1f2-4b1c-9a8e-ed259ab12c58)

Now, copy the URL at the bottom and paste it in your browser. Follow the directions to add the bot to the desired server. Once complete you should see the bot join.

The bot can respond to !greet, !list_command, !functions, and most importantly !export_members.

Go ahead and give it a try. The CSV should save in the root path of the code/project. 
Careful, it will overwrite itself if you export again and dont move the initial CSV or change the name.

GLHF
