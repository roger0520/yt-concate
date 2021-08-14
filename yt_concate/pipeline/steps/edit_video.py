from .step import Step

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            print(found.time)
            # print(self.parse_caption_time(found.time))
            start, end = self.parse_caption_time(found.time)        # 這邊是tuple的資料結構
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end) # subclip要用tuple投
            clips.append(video)
            if len(clips) >= inputs['limit']:   # 處理超過20個video就離開
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs('search_word'))
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end) #這會用tuple裝起來

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000 #這會用tuple把它裝起來
