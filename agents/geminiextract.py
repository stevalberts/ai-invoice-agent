import os
import httpx
from typing import List, Union
from pydantic_ai import Agent, BinaryContent
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv

from docling.document_converter import DocumentConverter

class GeminiDocumentProcessor:
    """
    A class to process images and PDFs from URLs or local files using the Google Gemini API.
    
    - For image files, it reads them directly.
    - For PDF files, it converts them into images (one per page) before processing.
    """
    
    def __init__(
        self,
        gemini_model: str = "gemini-2.0-flash",
        system_prompt: str = (
            "You are an AI that describes images and documents. "
            "Analyze the given images and PDFs and provide detailed descriptions."
        ),
    ):
        # Load environment variables from .env file
        load_dotenv()
        
        # Load API key from environment variables
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Google API Key is missing! Set it as an environment variable.")
        
        # Configure the Gemini API model
        self.model = GeminiModel(gemini_model, api_key=self.api_key)
        
        # Initialize the AI agent
        self.agent = Agent(
            model=self.model,
            result_type=str,
            system_prompt=system_prompt,
        )

    def is_pdf(self, file_bytes: bytes, content_type: str = "") -> bool:
        """
        Detects whether a file is a PDF based on its content type or file signature.
        """
        return content_type.startswith("application/pdf") or file_bytes.startswith(b"%PDF-")
    
    def process_files(self, files: List[Union[str, bytes]]) -> str:
        """
        Processes a list of files (URLs or local files) and returns the AI-generated description.
        
        Args:
            files (List[Union[str, bytes]]): List of file URLs or local file paths.
            
        Returns:
            str: AI-generated description of the files.
        """        
        converter = DocumentConverter()
        
        conv_results = converter.convert_all(files)

        for res in conv_results:
            print(f"Document {res.input.file.name} converted.")
            # print(res.document.export_to_markdown())
            print("\n")
            

def simple_check_file_type(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()
    
    if extension == '.pdf':
        return "PDF"
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    if extension in image_extensions:
        return "Image"
    
    return "Unknown"

# Example Usage:
if __name__ == "__main__":
    files = [
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/120.jpg",  # Image URL
        '/Users/stevenogwal/development/openlyne/data/img/110.jpg',  # Local image file
        '/Users/stevenogwal/development/openlyne/data/docs/invoice_1.pdf',
        '/Users/stevenogwal/development/openlyne/data/docs/invoice_2.pdf',
        # "https://example.com/sample.pdf"  # Remote PDF
    ]
    
    ftp = simple_check_file_type(files[0])
    ftp1 = simple_check_file_type(files[1])
    ftp2 = simple_check_file_type(files[2])
    ftp3 = simple_check_file_type(files[3])
    
    print(ftp)
    print(ftp1)
    print(ftp2)
    print(ftp3)
    
    processor = GeminiDocumentProcessor()
    description = processor.process_files(files)
    print(description)
