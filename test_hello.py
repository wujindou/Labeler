import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def main():
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt="你是一个信息抽取的专家，会根据用户描述抽取或者总结生成出准确的字段信息。给定以下文本信息请从里面抽取出
标题、开始日期、开始时间、开始相对时间、结束日期、结束时间、持续时间、重复周期、重复周期截止时间、提醒时间、提醒相对时间、地点、召集人、参与人字段。其中标题字段可以总结生成，抽取完成后，请按顺序返回结果如果没有对应字段填充为no，字段间请用\t分隔。比如输入文本：各位积极分子：支部书记近期会专门开展关于“积极分子如何在新形势下做好日常政治生活的若干准则”的座谈会，请各位积极分子于9月10日上午9点前往党建处901会议室参加会议！返回：座谈会	9月10日	上午9点	no	no	no	no	no	no	no	no	党建处901会议室	支部书记	积极分子。给定文本：各位领导，全国高血压宣传日的海报和宣传折页已到。请9月30日前抽空来慢病科领取。另外之前三减三健宣传折页和自我管理小组物品没拿的，抓紧时间来领取。请返回你的抽取结果。", conversation_style=ConversationStyle.creative, simplify_response=True)
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
