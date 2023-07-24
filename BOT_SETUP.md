
# Prerequisites:

Before you start, ensure you have the following:

    A Discord account: You'll need a Discord account to log in to the Discord Developer Portal.

    A server to invite your bot: You should have a Discord server where you can invite and test your bot.

# Step 1: Creating a New Application
    1. Go to the Discord Developer Portal.
    2. Click on the "New Application" button to create a new application.
    3. Give your application a name. This will be the name of your bot. 4. You can also add an optional description and profile picture.
    5. Click the "Save Changes" button to create the application.

# Step 2: Adding a Bot to Your Application
    1. Once your application is created, navigate to the "Bot" tab in the left-hand sidebar.
    2. Click on the "Add Bot" button to create a bot for your application.
    3. A confirmation popup will appear. Click "Yes, do it!" to proceed.

# Step 3: Obtaining the Bot Token
    In the "Bot" tab, you will see a "Token" section. Click on the "Copy" button to copy the bot token to your clipboard. Keep this token secure and never share it with anyone. It grants access to your bot and should be treated like a password.

# Step 4: Inviting Your Bot to a Server
    1. Go to the "OAuth2" tab in the left-hand sidebar.
    Under the "OAuth2 URL Generator" section, select "bot" from the "Scopes" list.
    2. In the "Bot Permissions" section, choose the permissions your bot requires. For most basic bots, "Read Messages" and "Send Messages" are sufficient.
    3. Copy the generated URL from the "Scopes" section.
    4. Open the URL in your web browser, select the server where you want to invite the bot, and click "Authorize."

# Step 5: Coding and Running the Bot
    Go to DiscodBot.py and then enter the token to the variable `BOT_TOKEN`

    ```python
    BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
    ```