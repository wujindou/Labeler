import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import pandas as pd 


async def main():
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)
    data = pd.read_excel('./label_data_0613.xlsx',sheet_name=[0],engine='openpyxl')
    writer  =open('newbing_result.jsonl','a+',encoding='utf-8')
    for idx,d in enumerate(data[0].values):
        if idx<500:continue 
        json_data = {'query':d,'res':None}
        try:
            response = await bot.ask(prompt="""你是一个信息抽取的专家，会根据用户描述抽取或者总结生成出准确的字段信息。给定以下文本信息请从里面抽取出标题字段。\n
    如果原文中出现了明确的标题描述，如会议名称、事件名称、宴会要求、招投标等则抽取这些原文的日程描述字段；如果原文中未出现明确的日程描述，则以名词和短语形式描述日程事件。\n
    举例1: 输入：各分公司、部门:为提高营销员、采购员的法律意识，合理有效的规避业务合同签订中的法律风险，更好的维护公司权益，降低经营风险，我司将在“五一”节后，组织开展针对营销员、采购员关于《合同法》等法律法规知识的培训。现将相关事项通知如下:一、培训时间:2013年5月2日上午9:30-11:30 二、培训地点:公司四楼会议室 三、培训对象:建材营销分公司、工业营销分公司、幕墙销售部、外贸部全体营销员、营销内勤以及采购部全体人员。 \n输出：参加法律法规知识的培训\n
    举例2: 输入：各位组长：集团公司近期会召开“万家小年集市”为主题的联谊会，请各位组长选派一名代表于12月2日下午1点30分到工会处领取联谊会的福利，分给大家，谢谢。 \n输出：选派代表领取福利\n
    举例3: 输入: 各位积极分子：支部书记近期会专门开展关于“积极分子如何在新形势下做好日常政治生活的若干准则”的座谈会，请各位积极分子于9月10日上午9点前往党建处901会议室参加会议！\n输出:座谈会\n
    举例4: 输入： 前后端联动交流例会明天将在大会堂召开，请大家踊跃参加。\n输出： 前后端联动交流例会\n
    根据上面描述，你可以先想一下,如果明白请先回答明白。现在给定文本：{} \n 请返回你生成的标题信息。""".format(query),conversation_style=ConversationStyle.creative, simplify_response=True)
            json_data['res'] = json.dumps(response,ensure_ascii=False)
        except Exception as e:
            print(e)
        writer.write(json.dumps(json_data,ensure_ascii=False)+'\n')
        break 
    writer.close()
#         (json.dumps(response, indent=2,ensure_ascii=False)) # Returns
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
