# This is a simple example of a aa_ui app.

from aa_ui import AskUserMessage, Message, on_chat_start


@on_chat_start
async def main():
    res = await AskUserMessage(content="What is your name?", timeout=30).send()
    if res:
        await Message(
            content=f"Your name is: {res['output']}.\naa_ui installation is working!\nYou can now start building your own aa_ui apps!",
        ).send()
