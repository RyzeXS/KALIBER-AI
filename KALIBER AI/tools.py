
from toolkit.file_writer_tool import FileWriterTool
import os
import dotenv
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

file_writer_tool = FileWriterTool()
search_tool = SerperDevTool(serper_key= os.getenv("SERPER_API_KEY"))
scrape = ScrapeWebsiteTool()