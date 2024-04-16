#============================================================================================================================

class Rawexo(object):

    DATA06 = (".TXT", ".PDF", ".APK", ".EXE", ".ZIP", ".RAR", ".TAR", ".ISO")

    DATA01 = ['audio/mpeg', 'audio/x-flac', 'audio/x-wav', 'audio/m4a', 'audio/ogg']

    DATA03 = (".MKV", ".MP4", ".MOV", ".WMV", ".3GP", ".MPG", ".WEBM", ".AVI", ".FLV", ".M4V", ".GIF")

    DATA04 = (".MP3", ".M4A", ".M4B", ".FLAC", ".WAV", ".AIF", ".OGG", ".AAC", ".DTS", ".MID", ".AMR", ".MKA")

    DATA05 = (".JPG", ".JPX", ".PNG", ".WEBP", ".CR2", ".TIF", ".BMP", ".JXR", ".PSD", ".ICO", ".HEIC", ".JPEG")

    DATA00 = ("audio", "document", "photo", "sticker", "animation", "video", "voice", "video_note", "new_chat_photo")

    DATA02 = ['video/3gpp', 'video/mp4', 'video/x-matroska', 'video/webm', 'video/mpeg', 'video/x-flv', 'video/x-msvideo']

#============================================================================================================================

class Extions(object):

    DATA01 = Rawexo.DATA03 + Rawexo.DATA04 + Rawexo.DATA05 + Rawexo.DATA06

#============================================================================================================================
