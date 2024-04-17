import asyncio
from ..scripts.eo import Okeys
from yt_dlp import YoutubeDL, DownloadError
#==========================================================================

class UDMessages:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', True)
        self.errors = kwargs.get('errors', None)
        self.result = kwargs.get('result', None)

#=====================================================================================================

class UDownloader:
    def __inti__(self):
        self.foold = Okeys.DATA01
        self.looad = asyncio.get_event_loop()

#=====================================================================================================

    def start(self, link, command, progress):
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)
                ydl.download(filelink)
                return True, None
            except DownloadError as errors:
                return False, errors
            except Exception as errors:
                return False, errors

#=====================================================================================================
    
    async def metadata(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#=====================================================================================================

    async def extracts(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#=====================================================================================================

    async def filename(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                metase = ydl.extract_info(link, download=False)
                moonus = ydl.prepare_filename(metase, outtmpl=self.foold)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#=====================================================================================================

    async def download(self, link, command, progress):
        om, em = await self.looad.run_in_executor(None, self.start, link, command, progress)
        return UDMessages(status=om, errors=em)

#=====================================================================================================
