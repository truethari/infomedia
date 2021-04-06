import os
import ntpath

from infomedia  import mediainfo, Worker

video_path = "/home/sample-mp4-file.mp4"
output_path = "/home/runner/work/infomedia/infomedia"

def test_mediainfo():
    test_mediainfo_value = mediainfo(video_path)
    assert "duration" in test_mediainfo_value["format"]

def test_Worker():
    worker = Worker(video_path, request_data='False', output_format='json', save_path=output_path)
    worker._application()
    assert os.path.isfile(os.path.join(output_path, ntpath.basename(video_path[:-4]) + ".json"))
