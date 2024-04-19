import os, asyncio
from ..scripts.eo import Okeys
from yt_dlp import YoutubeDL, DownloadError
#==========================================================================

class UDMessages:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', True)
        self.errors = kwargs.get('errors', None)
        self.result = kwargs.get('result', None)
        self.extension = kwargs.get('extension', None)
        self.completed = kwargs.get('completed', True)

#==========================================================================

class DownloadER:

    async def namesexe(reames, filename):
        if reames == None and filename == None:
            return UDMessages(result=reames, extension="tmp")
        else:
            nameas = str(reames.result)
            exeson = nameas.split('.')[-1]
            cnames = os.path.splitext(nameas)[0]
            moonus = filename if filename else cnames
            return UDMessages(result=moonus, extension=exeson)

#==========================================================================

    async def metadata(link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#==========================================================================

    async def extracts(link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(errors=errors)

#==========================================================================

    async def filename(link, command):
        with YoutubeDL(command) as ydl:
            try:
                mainos = Okeys.DATA01
                metase = ydl.extract_info(link, download=False)
                moonus = ydl.prepare_filename(metase, outtmpl=mainos)
                return UDMessages(result=moonus)
            except Exception as errors:
                return UDMessages(result="Unknown", errors=errors)

#==========================================================================

    async def download(link, command, progress):
        loop = asyncio.get_event_loop()
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)   
                await loop.run_in_executor(None, ydl.download, filelink)
                return UDMessages(completed=True)
            except DownloadError as errors:
                return UDMessages(completed=False, errors=errors)
            except Exception as errors:
                return UDMessages(completed=False, errors=errors)

#==========================================================================
