from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
#CHANNEL_ID = 'UCTYwP8fwemw8olg3DQ8bLLA'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps =[
        GetVideoList(),
        ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()