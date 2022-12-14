from flask import Flask, request
import requests
from pathlib import Path

from define import voice_host, voice_port, news_server_url, is_debug_mode

app = Flask(__name__)


@app.route('/', methods=['POST'])
def request_voice():
    # 這些都是文章生成所需的參數
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    # 取得生成好的文章
    respond = requests.post(news_server_url,
                            data={
                                'date': date,
                                'date_interval': date_interval,
                                'topic': topic,
                                'additional_info': additional_info
                            })
    data = respond.json

    uuid = data["uuid"]
    Path(f"./outputs/{uuid}").mkdir(parents=True, exist_ok=True)

    news = data["data"]

    f = open("./outputs/uuid/voice.text", "w")
    f.write("voicevoicevoicevoicevoice"+news+"\n")
    f.close()
    # 生成聲音
    # todo

    return f"Of course, this is your voice file. \nfrom news:\n {news}"


if __name__ == "__main__":
    app.run(debug=is_debug_mode, host=voice_host, port=voice_port)
