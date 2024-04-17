<p align="center">
 📦 <a href="https://pypi.org/project/utubes" style="text-decoration:none;">YOUTUBE EXTENSIONS</a>
</p>


## USAGE
```python
async def main():
    downloader = UDownloader()

    # EXAMPLE USAGE OF METHODS
    filelink = "YOUR_VIDEO_LINK"
    progress = None  # YOUR PROGRESS HOOK FUNCTION
    commands = {}    # YOUR COMMAND OPTIONS FOR YOUTUBEDL

    # CALL METHODS USING AWAIT
    metadata_result = await downloader.metadata(filelink, commands)
    extinfos_result = await downloader.extracts(filelink, commands)
    filename_result = await downloader.filename(filelink, commands)
    download_result = await downloader.download(filelink, commands, progress)
    # DO SOMETHING WITH THE RESULTS

asyncio.run(main())
```
