import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def main():
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt="Hello world", conversation_style=ConversationStyle.creative, simplify_response=True)
    print(json.dumps(response, indent=2)) # Returns
    """
    {
        "text": str
        "author": str
        "sources": list[dict]
        "sources_text": str
        "suggestions": list[str]
        "messages_left": int
    }
    """
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
