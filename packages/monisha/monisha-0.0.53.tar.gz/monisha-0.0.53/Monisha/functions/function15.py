import os
#=================================================================================================

class Messages:
    def __init__(self, **kwargs):
        self.filesize = kwargs.get('filesize', 0)
        self.location = kwargs.get('location', None)

#=================================================================================================

class Location:

    async def get01(flocation, exo):
        try:
            location = str(flocation)
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = str(flocation) + "." + exo
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(flocation)[0]
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(flocation)[0] + str(".mkv")
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(flocation)[0] + "." + str(exo)
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            return Messages(location=None, filesize=0)

#=================================================================================================

    async def get02(dlocation, exo, exe):
        try:
            location = str(dlocation)
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = str(dlocation) + "." + exo
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = str(dlocation) + "." + exe
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(dlocation)[0]
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(dlocation)[0] + str(".mp3")
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(dlocation)[0] + str(".mp4")
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(dlocation)[0] + str(".mkv")
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(dlocation)[0] + "." + str(exe)
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            pass
        try:
            location = os.path.splitext(dlocation)[0] + "." + str(exo)
            filesize = int(os.path.getsize(location))
            return Messages(location=location, filesize=filesize)
        except Exception:
            return Messages(location=None, filesize=0)

#=================================================================================================
