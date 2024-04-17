import asyncio
from ..scripts.eo import Okeys
from yt_dlp import YoutubeDL, DownloadError
#=================================================================================================

class UDMessages:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', True)
        self.errors = kwargs.get('errors', None)
        self.finame = kwargs.get('finame', None)
        self.result = kwargs.get('result', None)

#=================================================================================================

class UDownloader:

    def __init__(self):
        self.finame = None
        self.result = None
        self.errors = None
        self.status = True
        self.downdl = Okeys.DATA01

#=================================================================================================
    
    async def download(self, link, command, progress):
        loop = asyncio.get_event_loop()
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)   
                await loop.run_in_executor(None, ydl.download, filelink)
                return self.status
            except DownloadError as errors:
                self.errors = errors
                self.status = False
                return self.status
            except Exception as errors:
                self.errors = errors
                self.status = False
                return self.status

#=================================================================================================

    async def metadata(self, link, command):
        with YoutubeDL(command) as ydl:
            self.result = ydl.extract_info(link, download=False)
            return self.result

#=================================================================================================

    async def extinfos(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                self.result = ydl.extract_info(link, download=False)
                return UDMessages(result=self.result)
            except Exception as errors:
                self.errors = errors
                return UDMessages(errors=self.errors)

#=================================================================================================

    async def filename(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                masteredata = await self.metadata(link, command)
                self.finame = ydl.prepare_filename(masteredata, outtmpl=self.downdl)
                return UDMessages(finame=self.finame)
            except Exception as errors:
                self.errors = errors
                return UDMessages(errors=self.errors)

#=================================================================================================

    async def start(self, link, command, progress):
        mainou = await self.download(link, command, progress)
        return UDMessages(status=mainou, errors=self.errors)

#=================================================================================================
