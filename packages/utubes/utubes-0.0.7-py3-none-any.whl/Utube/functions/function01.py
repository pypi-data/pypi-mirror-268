import asyncio
from ..scripts.eo import Okeys
from yt_dlp import YoutubeDL, DownloadError
#=================================================================================================

class UDMessages:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', True)
        self.errors = kwargs.get('errors', None)
        self.fileid = kwargs.get('fileid', None)
        self.result = kwargs.get('result', None)

#=================================================================================================

class UDownloader:

    async def metadata(link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#=================================================================================================

    async def extracts(link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#=================================================================================================

    async def filename(link, command):
        with YoutubeDL(command) as ydl:
            try:
                downoums = Okeys.DATA01
                metadota = ydl.extract_info(link, download=False)
                filenamo = ydl.prepare_filename(metadota, outtmpl=downoums)
                return UDMessages(fileid=filenamo)
            except Exception as errors:
                return UDMessages(errors=errors)

#=================================================================================================

    async def download(link, command, progress):
        loop = asyncio.get_event_loop()
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)   
                await loop.run_in_executor(None, ydl.download, filelink)
                return UDMessages(status=True, errors=None)
            except DownloadError as errors:
                return UDMessages(status=False, errors=errors)
            except Exception as errors:
                return UDMessages(status=False, errors=errors)

#=================================================================================================
