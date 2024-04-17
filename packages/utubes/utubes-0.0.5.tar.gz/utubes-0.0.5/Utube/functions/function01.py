import asyncio
from ..scripts.eo import Okeys
from yt_dlp import YoutubeDL, DownloadError
#=================================================================================================

class UDownloader:

    def __init__(self):
        self.fnames = None
        self.result = None
        self.errors = None
        self.status = True
        self.downdl = Okeys.DATA01
        self.runnes = asyncio.get_event_loop()

#=================================================================================================
    
    def download(self, link, command, progress):
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)
                ydl.download(filelink)
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
                return self.result
            except Exception as errors:
                self.errors = errors
                return self.errors

#=================================================================================================

    async def filename(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                masteredata = await self.metadata(link, command)
                self.fnames = ydl.prepare_filename(masteredata, outtmpl=self.downdl)
                return self.fnames
            except Exception as errors:
                self.errors = errors
                return self.fnames

#=================================================================================================

    async def start(self, link, command, progress):
        mainou = await self.runnes.run_in_executor(None, self.download, link, command, progress)
        return mainou

#=================================================================================================
