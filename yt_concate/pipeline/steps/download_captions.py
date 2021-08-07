import os
import time

from pytube import YouTube  # download the package by:  pip install pytube

from .step import Step
from .step import StepException




class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print(f'downloading caption for {yt.id}')
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError): #AttributeError 是要處理跳過本身影片沒有自動產生字幕
                print(f'Error when downloading caption for {yt.url}')
                continue
            #print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print(f'took,{end} - {start}, seconds')

        return data