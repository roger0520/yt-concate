from .step import Step

from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # set()會把重複的清單淘汰掉
        print(f'videos to download= {len(yt_set)}')

        for yt in yt_set:
            url = yt.url

            if utils.viedo_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print(f'downloading:{url}')
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        return data
