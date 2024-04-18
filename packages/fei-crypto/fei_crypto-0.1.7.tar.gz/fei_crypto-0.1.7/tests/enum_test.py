from enum import Enum


class TestType(Enum):
    AUDIO = "audio"
    GIF = "gif"
    VIDEO = "video"
    VIDEO_NOTE = "video_note"
    STICKER = "sticker"
    CONTACT = "contact"
    PHOTO = "photo"
    DOCUMENT = "document"
    NOFILE = "nofile"


if __name__ == '__main__':
    for f in TestType:
        print(f)
        print(f.value)
        print(type(f.value))
        # if f == TestType.NOFILE:
        #     print(TestType.NOFILE)
