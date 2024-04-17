import asyncio
import json
import re

import datetime
from typing import Dict
from openfinance.config import Config

from openfinance.datacenter.database.source.event.cailianshe import get_cailianshe_news

from openfinance.datacenter.database.base import DataBaseManager
from openfinance.searchhub.recall.base import IndexManager
from openfinance.utils.embeddings.embedding_manager import EmbeddingManager

from openfinance.robot.wechat.base import Wechat
from openfinance.service.base import wrapper_return

from openfinance.searchhub.task.percept.percept_task import PerceptTask

db = DataBaseManager(Config()).get("db")

class OnlinePerceptTask(PerceptTask):
    name = "online_percept"
    async def aexecute(
        self, 
        text, 
        **kwargs
    ) -> Dict[str, str]:
        print("text", text)
        websocket = kwargs.get("websocket", None)
        wechat = kwargs.get("wechat", None)

        if websocket:
            if websocket.open:
                await websocket.send(wrapper_return("\n开始分析新闻...\n"))
            else:
                raise f"websocket lost"
        save_db = kwargs.get("save_db", False)
        infile = open("openfinance/datacenter/knowledge/entity_graph/files/graph.txt", "a+")

        sleep_duration = 5 * 60
        docs = list()
        max_len = 15

        while True:
            try:
                jsondata = get_cailianshe_news()
                for d in jsondata["data"]["roll_data"]:
                    if d["id"] in docs:
                        continue
                    if len(docs) == max_len:
                        docs.pop(0)

                    docs.append(d["id"])

                    # delete summary docs
                    ##################################
                    if re.search(r".*（.*）.*", d["title"]):
                        continue

                    if d["subjects"]:
                        flag = False
                        for sd in d["subjects"]:
                            if "天气" in sd["subject_name"]:
                                flag = True
                        if flag:
                            continue

                    if "早间新闻" in d['content'] or "要闻" in d["content"]:
                        continue
                    ##################################

                    content = d["content"]
                    percept_data = await self.percept.acall(**{
                        "content": content
                    })

                    match_result = await self.match.acall(**{
                        "content": percept_data["output"],
                        "channel": self.name,         
                    })
                    match = match_result['output']
                    if not match["main_entity"]:
                        continue
                    if save_db:
                        db.insert(
                            "t_news_percept",
                            {
                                "entity": match["main_entity"],
                                "entity_type": match["level"],
                                "indicator": match["indicator"],
                                "effect": match["sentiment"],
                                "src": match["event"],
                                "sid": str(d["id"])
                            }
                        )
                    if websocket:
                        if websocket.open:
                            await websocket.send(wrapper_return(
                                output = str(news)
                            ))                            
                            await websocket.send(wrapper_return(
                                output = str(match)
                            ))
                        else:
                            raise f"websocket lost" 
                    if wechat:
                        #msg = "新闻: " + d["title"] + "\n"
                        msg = ""
                        msg += "主体: " + match["main_entity"] + "\n"
                        msg += "事件: " + match["event"] + "\n"
                        msg += "指标: " + match["indicator"] + "\n"
                        msg += "情绪: " + match["sentiment"] + "\n"
                        #Wechat.self_push(msg, name="港美缅股交流", isRoom=True)
                        msg += "来源: https://api3.cls.cn/a/" + str(d["id"])
                        Wechat.self_push(msg, name="实时热点财经新闻同步群5", isRoom=True)
                        if d["subjects"]:
                            for sd in d["subjects"]:
                                if "美股动态" == sd["subject_name"] or "港股动态" == sd["subject_name"]:
                                    Wechat.self_push(msg, name="港美缅股交流", isRoom=True)
                    if True:
                        infile.write(str(d["id"]) + "\t" + str(datetime.date.today()) + "\t")
                        if d["subjects"]:
                            for sd in d["subjects"]:
                                infile.write(sd["subject_name"] + "|")
                        infile.write("\t" + content.replace("\n", "@line@") + "\t")                                
                        infile.write(str(match) + "\n")
                        infile.flush()                                              
                await asyncio.sleep(sleep_duration)
            except Exception as e:
                print("Exception:", e)
        return {self.output: "finish detect!"}

if __name__ == '__main__':
    task = OnlinePerceptTask() 
    result = asyncio.run(task.aexecute("开始", save_db=True, wechat=False))
    print(result)