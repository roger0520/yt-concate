import os

from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {} #每個字幕的檔名是'key', 字幕是'value'
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {} #每個字幕是'key', 時間是'value'
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line()
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions
        pprint(data)
        return data