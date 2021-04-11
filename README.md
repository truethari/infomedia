# infomedia 🎬🎧

[![infomedia](https://github.com/truethari/infomedia/actions/workflows/infomedia.yml/badge.svg?branch=master)](https://github.com/truethari/infomedia/actions/workflows/infomedia.yml)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://badge.fury.io/py/infomedia.svg)](https://badge.fury.io/py/infomedia)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/972b3e817f6e47c2b161c5ad34d61f50)](https://www.codacy.com/gh/truethari/infomedia/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=truethari/infomedia&amp;utm_campaign=Badge_Grade)

## What is This

This is a Python application that can be used to retrieve media file information such as duration, frame rate, bit rate, etc..

## Installation

You can use pip:

```console
~$ pip3 install infomedia
```

## Usage

### Usage options

``` text
positional arguments:
    input                   path to file

optional arguments:
    -h, --help              show this help message and exit
    -i INFO, --info INFO    get information about
    -s SAVE_PATH, --save-path SAVE_PATH
                            a folder path to save the data file
    -of {json,ini,xml,csv,flat}, --output-format {json,ini,xml,csv,flat}
                            data file format
    -v, --version           infomedia version
```

### Console

``` console
~$ infomedia video.mkv
~$ infomedia c:/song.mp3

~$ infomedia c:/folder/video.mkv -i duration
~$ infomedia c:/folder/song.mp3 -i 'duration codec_name'
~$ infomedia -i 'duration codec_name' c:/folder/video.mkv

~$ infomedia c:/video.mkv -of json -s d:/folder
~$ infomedia -of csv -s d:/folder c:/song.mp3
```

### Python

Shell

``` console
>>> from infomedia import mediainfo
>>> data = mediainfo("video.mkv")
>>> data

{'streams.stream.0': {'index': 0, 'codec_name': 'h264', 'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10', 'profile': 'High', 'codec_type': 'video', 'codec_time_base': '1001/48000', 'codec_tag_string': '[0][0][0][0]', 'codec_tag': '0x0000', 'width': 1280, 'height': 720, 'coded_width': 1280, 'coded_height': 720, 'closed_captions': 0, 'has_b_frames': 2, 'sample_aspect_ratio': 'N/A', 'display_aspect_ratio': 'N/A', 'pix_fmt': 'yuv420p', 'level': 31, 'color_range': 'unknown', 'color_space': 'unknown', 'color_transfer': 'unknown', 'color_primaries': 'unknown', 'chroma_location': 'left', 'field_order': 'progressive', 'timecode': 'N/A', 'refs': 1, 'is_avc': 'true', 'nal_length_size': 4, 'id': 'N/A', 'r_frame_rate': '24000/1001', 'avg_frame_rate': '24000/1001', 'time_base': '1/1000', 'start_pts': 0, 'start_time': 0.0, 'duration_ts': 'N/A', 'duration': 'N/A', 'bit_rate': 'N/A', 'max_bit_rate': 'N/A', 'bits_per_raw_sample': 8, 'nb_frames': 'N/A', 'nb_read_frames': 'N/A', 'nb_read_packets': 'N/A'}, 'streams.stream.0.disposition': {'default': 1, 'dub': 0, 'original': 0, 'comment': 0, 'lyrics': 0, 'karaoke': 0, 'forced': 0, 'hearing_impaired': 0, 'visual_impaired': 0, 'clean_effects': 0, 'attached_pic': 0, 'timed_thumbnails': 0}, 'streams.stream.0.tags': {'handler_name': 'L-SMASH Video Handler', 'encoder': 'Lavc57.107.100 libx264', 'duration': '00\\:00\\:28.237000000'}, 'format': {'filename': '/home/user/videos/video.mkv', 'nb_streams': 1, 'nb_programs': 0, 'format_name': 'matroska,webm', 'format_long_name': 'Matroska / WebM', 'start_time': 0.0, 'duration': 28.237, 'size': 17433130, 'bit_rate': 4939088, 'probe_score': 100}, 'format.tags': {'compatible_brands': 'mp42mp41isomavc1', 'major_brand': 'mp42', 'minor_version': '0', 'encoder': 'Lavf57.83.100'}}
```

Example 1

``` python
from infomedia import mediainfo

data = mediainfo("video.mkv")
print("Duration = {}".format(data['format']['duration']))
```

Example 2

Notice: The 'streams.stream.1' is guessed as the audio data. This may change if other audio is embedded or something else. If you want to avoid such errors, check 'codec_type' before using / assign data.

``` python
from infomedia import mediainfo
import os

folder = '/home/user/Videos/'

for video in os.listdir(folder):
    data = mediainfo(os.path.join(folder, video))
    print("{}\n"
          "Duration: {}"
          "Codec type (video): {}"
          "Codec type (audio): {}"
          .format(
              os.path.join(folder, video),
              data['format']['duration'],
              data['streams.stream.0']['codec_type'],
              data['streams.stream.1']['codec_type'],
            )
          )
```

## Exporting data files

### json

``` console
~$ infomedia c:/video.mp4 -of json -s d:/folder
```

video.json

``` json
{
    "streams": [
        {
            "index": 0,
            "codec_name": "h264",
            "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
            "profile": "Main",
            "codec_type": "video",
            "codec_time_base": "125/5994",
            "codec_tag_string": "avc1",
            "codec_tag": "0x31637661",
            "width": 1280,
            "height": 720,
            "coded_width": 1280,
            "coded_height": 720,
            "closed_captions": 0,
            "has_b_frames": 2,
            "sample_aspect_ratio": "1:1",
            "display_aspect_ratio": "16:9",
            "pix_fmt": "yuv420p",
            "level": 31,
            "color_range": "tv",
            "color_space": "bt709",
            "color_transfer": "bt709",
            "color_primaries": "bt709",
            "chroma_location": "left",
            "refs": 1,
            "is_avc": "true",
            "nal_length_size": "4",
            "r_frame_rate": "2997/125",
            "avg_frame_rate": "2997/125",
            "time_base": "1/11988",
            "start_pts": 0,
            "start_time": "0.000000",
            "duration_ts": 2771000,
            "duration": "231.147814",
            "bit_rate": "1145112",
            "bits_per_raw_sample": "8",
            "nb_frames": "5542",
            "disposition": {
                "default": 1,
                "dub": 0,
                "original": 0,
                "comment": 0,
                "lyrics": 0,
                "karaoke": 0,
                "forced": 0,
                "hearing_impaired": 0,
                "visual_impaired": 0,
                "clean_effects": 0,
                "attached_pic": 0,
                "timed_thumbnails": 0
            },
            "tags": {
                "language": "und",
                "handler_name": "VideoHandler"
            }
        },
        {
            "index": 1,
            "codec_name": "aac",
            "codec_long_name": "AAC (Advanced Audio Coding)",
            "profile": "HE-AAC",
            "codec_type": "audio",
            "codec_time_base": "1/44100",
            "codec_tag_string": "mp4a",
            "codec_tag": "0x6134706d",
            "sample_fmt": "fltp",
            "sample_rate": "44100",
            "channels": 2,
            "channel_layout": "stereo",
            "bits_per_sample": 0,
            "r_frame_rate": "0/0",
            "avg_frame_rate": "0/0",
            "time_base": "1/44100",
            "start_pts": 0,
            "start_time": "0.000000",
            "duration_ts": 10204036,
            "duration": "231.384036",
            "bit_rate": "47976",
            "max_bit_rate": "603000",
            "nb_frames": "4980",
            "disposition": {
                "default": 1,
                "dub": 0,
                "original": 0,
                "comment": 0,
                "lyrics": 0,
                "karaoke": 0,
                "forced": 0,
                "hearing_impaired": 0,
                "visual_impaired": 0,
                "clean_effects": 0,
                "attached_pic": 0,
                "timed_thumbnails": 0
            },
            "tags": {
                "language": "und",
                "handler_name": "SoundHandler"
            }
        }
    ],
    "format": {
        "filename": "c:/video.mp4",
        "nb_streams": 2,
        "nb_programs": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "231.385000",
        "size": "34608911",
        "bit_rate": "1196582",
        "probe_score": 100,
        "tags": {
            "major_brand": "isom",
            "minor_version": "512",
            "compatible_brands": "isomiso2avc1mp41",
            "title": "2000172463643763",
            "encoder": "Lavf56.40.101"
        }
    }
}
```

### ini

``` console
~$ infomedia c:/video.mp4 -of ini -s d:/folder
```

video.ini

``` ini
[streams.stream.0]
index=0
codec_name=h264
codec_long_name=H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
profile=Main
codec_type=video
codec_time_base=125/5994
codec_tag_string=avc1
codec_tag=0x31637661
width=1280
height=720
coded_width=1280
coded_height=720
closed_captions=0
has_b_frames=2
sample_aspect_ratio=1\:1
display_aspect_ratio=16\:9
pix_fmt=yuv420p
level=31
color_range=tv
color_space=bt709
color_transfer=bt709
color_primaries=bt709
chroma_location=left
field_order=unknown
timecode=N/A
refs=1
is_avc=true
nal_length_size=4
id=N/A
r_frame_rate=2997/125
avg_frame_rate=2997/125
time_base=1/11988
start_pts=0
start_time=0.000000
duration_ts=2771000
duration=231.147814
bit_rate=1145112
max_bit_rate=N/A
bits_per_raw_sample=8
nb_frames=5542
nb_read_frames=N/A
nb_read_packets=N/A

[streams.stream.0.disposition]
default=1
dub=0
original=0
comment=0
lyrics=0
karaoke=0
forced=0
hearing_impaired=0
visual_impaired=0
clean_effects=0
attached_pic=0
timed_thumbnails=0

[streams.stream.0.tags]
language=und
handler_name=VideoHandler

[streams.stream.1]
index=1
codec_name=aac
codec_long_name=AAC (Advanced Audio Coding)
profile=HE-AAC
codec_type=audio
codec_time_base=1/44100
codec_tag_string=mp4a
codec_tag=0x6134706d
sample_fmt=fltp
sample_rate=44100
channels=2
channel_layout=stereo
bits_per_sample=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/44100
start_pts=0
start_time=0.000000
duration_ts=10204036
duration=231.384036
bit_rate=47976
max_bit_rate=603000
bits_per_raw_sample=N/A
nb_frames=4980
nb_read_frames=N/A
nb_read_packets=N/A

[streams.stream.1.disposition]
default=1
dub=0
original=0
comment=0
lyrics=0
karaoke=0
forced=0
hearing_impaired=0
visual_impaired=0
clean_effects=0
attached_pic=0
timed_thumbnails=0

[streams.stream.1.tags]
language=und
handler_name=SoundHandler

[format]
filename=c:/video.mp4
nb_streams=2
nb_programs=0
format_name=mov,mp4,m4a,3gp,3g2,mj2
format_long_name=QuickTime / MOV
start_time=0.000000
duration=231.385000
size=34608911
bit_rate=1196582
probe_score=100

[format.tags]
major_brand=isom
minor_version=512
compatible_brands=isomiso2avc1mp41
title=2000172463643763
encoder=Lavf56.40.101
```

### xml

``` console
~$ infomedia c:/video.mp4 -of xml -s d:/folder
```

video.xml

``` xml
<streams>
    <stream index="0" codec_name="h264" codec_long_name="H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10" profile="Main" codec_type="video" codec_time_base="125/5994" codec_tag_string="avc1" codec_tag="0x31637661" width="1280" height="720" coded_width="1280" coded_height="720" closed_captions="0" has_b_frames="2" sample_aspect_ratio="1:1" display_aspect_ratio="16:9" pix_fmt="yuv420p" level="31" color_range="tv" color_space="bt709" color_transfer="bt709" color_primaries="bt709" chroma_location="left" refs="1" is_avc="true" nal_length_size="4" r_frame_rate="2997/125" avg_frame_rate="2997/125" time_base="1/11988" start_pts="0" start_time="0.000000" duration_ts="2771000" duration="231.147814" bit_rate="1145112" bits_per_raw_sample="8" nb_frames="5542">
        <disposition default="1" dub="0" original="0" comment="0" lyrics="0" karaoke="0" forced="0" hearing_impaired="0" visual_impaired="0" clean_effects="0" attached_pic="0" timed_thumbnails="0"/>
        <tag key="language" value="und"/>
        <tag key="handler_name" value="VideoHandler"/>
    </stream>
    <stream index="1" codec_name="aac" codec_long_name="AAC (Advanced Audio Coding)" profile="HE-AAC" codec_type="audio" codec_time_base="1/44100" codec_tag_string="mp4a" codec_tag="0x6134706d" sample_fmt="fltp" sample_rate="44100" channels="2" channel_layout="stereo" bits_per_sample="0" r_frame_rate="0/0" avg_frame_rate="0/0" time_base="1/44100" start_pts="0" start_time="0.000000" duration_ts="10204036" duration="231.384036" bit_rate="47976" max_bit_rate="603000" nb_frames="4980">
        <disposition default="1" dub="0" original="0" comment="0" lyrics="0" karaoke="0" forced="0" hearing_impaired="0" visual_impaired="0" clean_effects="0" attached_pic="0" timed_thumbnails="0"/>
        <tag key="language" value="und"/>
        <tag key="handler_name" value="SoundHandler"/>
    </stream>
</streams>
<format filename="c:/video.mp4" nb_streams="2" nb_programs="0" format_name="mov,mp4,m4a,3gp,3g2,mj2" format_long_name="QuickTime / MOV" start_time="0.000000" duration="231.385000" size="34608911" bit_rate="1196582" probe_score="100">
    <tag key="major_brand" value="isom"/>
    <tag key="minor_version" value="512"/>
    <tag key="compatible_brands" value="isomiso2avc1mp41"/>
    <tag key="title" value="2000172463643763"/>
    <tag key="encoder" value="Lavf56.40.101"/>
</format>
</ffprobe>
```

### csv

``` console
~$ infomedia c:/video.mp4 -of csv -s d:/folder
```

video.csv

| A      | B            | C    | D                                         | E                       | FGH |
|--------|--------------|------|-------------------------------------------|-------------------------|-----|
| stream | 0            | h264 | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 | Main                    | ~~~ |
| stream | 1            | aac  | AAC (Advanced Audio Coding)               | HE-AAC                  | ~~~ |
| Format | c:/video.mp4 | 2    | 0                                         | mov,mp4,m4a,3gp,3g2,mj2 | ~~~ |

### flat

``` console
~$ infomedia c:/video.mp4 -of flat -s d:/folder
```

video.flat

``` flat
streams.stream.0.index=0
streams.stream.0.codec_name="h264"
streams.stream.0.codec_long_name="H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10"
streams.stream.0.profile="Main"
streams.stream.0.codec_type="video"
streams.stream.0.codec_time_base="125/5994"
streams.stream.0.codec_tag_string="avc1"
streams.stream.0.codec_tag="0x31637661"
streams.stream.0.width=1280
streams.stream.0.height=720
streams.stream.0.coded_width=1280
streams.stream.0.coded_height=720
streams.stream.0.closed_captions=0
streams.stream.0.has_b_frames=2
streams.stream.0.sample_aspect_ratio="1:1"
streams.stream.0.display_aspect_ratio="16:9"
streams.stream.0.pix_fmt="yuv420p"
streams.stream.0.level=31
streams.stream.0.color_range="tv"
streams.stream.0.color_space="bt709"
streams.stream.0.color_transfer="bt709"
streams.stream.0.color_primaries="bt709"
streams.stream.0.chroma_location="left"
streams.stream.0.field_order="unknown"
streams.stream.0.timecode="N/A"
streams.stream.0.refs=1
streams.stream.0.is_avc="true"
streams.stream.0.nal_length_size="4"
streams.stream.0.id="N/A"
streams.stream.0.r_frame_rate="2997/125"
streams.stream.0.avg_frame_rate="2997/125"
streams.stream.0.time_base="1/11988"
streams.stream.0.start_pts=0
streams.stream.0.start_time="0.000000"
streams.stream.0.duration_ts=2771000
streams.stream.0.duration="231.147814"
streams.stream.0.bit_rate="1145112"
streams.stream.0.max_bit_rate="N/A"
streams.stream.0.bits_per_raw_sample="8"
streams.stream.0.nb_frames="5542"
streams.stream.0.nb_read_frames="N/A"
streams.stream.0.nb_read_packets="N/A"
streams.stream.0.disposition.default=1
streams.stream.0.disposition.dub=0
streams.stream.0.disposition.original=0
streams.stream.0.disposition.comment=0
streams.stream.0.disposition.lyrics=0
streams.stream.0.disposition.karaoke=0
streams.stream.0.disposition.forced=0
streams.stream.0.disposition.hearing_impaired=0
streams.stream.0.disposition.visual_impaired=0
streams.stream.0.disposition.clean_effects=0
streams.stream.0.disposition.attached_pic=0
streams.stream.0.disposition.timed_thumbnails=0
streams.stream.0.tags.language="und"
streams.stream.0.tags.handler_name="VideoHandler"
streams.stream.1.index=1
streams.stream.1.codec_name="aac"
streams.stream.1.codec_long_name="AAC (Advanced Audio Coding)"
streams.stream.1.profile="HE-AAC"
streams.stream.1.codec_type="audio"
streams.stream.1.codec_time_base="1/44100"
streams.stream.1.codec_tag_string="mp4a"
streams.stream.1.codec_tag="0x6134706d"
streams.stream.1.sample_fmt="fltp"
streams.stream.1.sample_rate="44100"
streams.stream.1.channels=2
streams.stream.1.channel_layout="stereo"
streams.stream.1.bits_per_sample=0
streams.stream.1.id="N/A"
streams.stream.1.r_frame_rate="0/0"
streams.stream.1.avg_frame_rate="0/0"
streams.stream.1.time_base="1/44100"
streams.stream.1.start_pts=0
streams.stream.1.start_time="0.000000"
streams.stream.1.duration_ts=10204036
streams.stream.1.duration="231.384036"
streams.stream.1.bit_rate="47976"
streams.stream.1.max_bit_rate="603000"
streams.stream.1.bits_per_raw_sample="N/A"
streams.stream.1.nb_frames="4980"
streams.stream.1.nb_read_frames="N/A"
streams.stream.1.nb_read_packets="N/A"
streams.stream.1.disposition.default=1
streams.stream.1.disposition.dub=0
streams.stream.1.disposition.original=0
streams.stream.1.disposition.comment=0
streams.stream.1.disposition.lyrics=0
streams.stream.1.disposition.karaoke=0
streams.stream.1.disposition.forced=0
streams.stream.1.disposition.hearing_impaired=0
streams.stream.1.disposition.visual_impaired=0
streams.stream.1.disposition.clean_effects=0
streams.stream.1.disposition.attached_pic=0
streams.stream.1.disposition.timed_thumbnails=0
streams.stream.1.tags.language="und"
streams.stream.1.tags.handler_name="SoundHandler"
format.filename="c:/video.mp4"
format.nb_streams=2
format.nb_programs=0
format.format_name="mov,mp4,m4a,3gp,3g2,mj2"
format.format_long_name="QuickTime / MOV"
format.start_time="0.000000"
format.duration="231.385000"
format.size="34608911"
format.bit_rate="1196582"
format.probe_score=100
format.tags.major_brand="isom"
format.tags.minor_version="512"
format.tags.compatible_brands="isomiso2avc1mp41"
format.tags.title="2000172463643763"
format.tags.encoder="Lavf56.40.101"
```
