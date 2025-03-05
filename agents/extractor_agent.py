import json
import os
import sys
import httpx
from pydantic_ai import Agent, BinaryContent
from pydantic_ai.models.gemini import GeminiModel
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Add the parent directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from models.invoice_model import Invoice  # Import Invoice model

class InvoiceItem(BaseModel):
    desc: str
    qty: int
    unitprice: float
    price: float

class Invoice(BaseModel):
    invoice_no: str
    invoice_datetime: datetime
    store_name: str
    store_address: str
    customer_name: Optional[str]
    customer_info: Optional[str] = None #customer info is optional
    currency: str
    items: List[InvoiceItem]
    tax: float
    total: float
    discount: Optional[float] = None #discount is optional
    type: str #invoice type
    confidence: float # confidence rating


class AgentImageProcessor:
    """
    A class to process images using the Google Gemini API.
    
    Attributes:
        model: An instance of the GeminiModel.
        agent: An instance of the Pydantic AI Agent.
    """
    
    def __init__(
        self,
        gemini_model: str = "gemini-2.0-flash",
        system_prompt: str = (
            "You are an AI that describes images. Analyze the given receipt images giving a confidence rating (0-1). Be concise."
        ),
    ):
        # Load API key from environment variables
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Google API Key is missing! Set it as an environment variable.")
        
        # Configure Gemini API model
        self.model = GeminiModel(gemini_model, api_key=self.api_key)
        
        # Initialize the AI agent
        self.agent = Agent(
            model=self.model,
            # result_type=str,  # Expected output is a text description
            system_prompt=system_prompt,
            result_type=List[Invoice],
        )
    
    def process_images(self, image_urls: List[str]) -> str:
        """
        Processes a list of image URLs and returns the agent's description.
        
        Args:
            image_urls: A list of image URLs to process.
            
        Returns:
            A string with the agent's detailed description of the images.
        """
        # Fetch images and create BinaryContent objects
        image_contents = [
            BinaryContent(data=httpx.get(url).content, media_type="image/png")
            for url in image_urls
        ]
        
         # Prepare AI prompt
        prompt = (
            "Extract details (invoice_no*,invoice_datetime,store_name,store_address,"
            "customer_name,customer_info,currency,items[desc,qty,unitprice,price],"
            "tax,total,discount,type,category,confidence) from these receipts in json. Be concise"
        )
        
        # Run the agent synchronously with the list of images
        result = self.agent.run_sync([prompt] + image_contents)
        return result.data

# Example usage:
if __name__ == "__main__":
    # List of image URLs
    image_urls = [
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/110.jpg",
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/121.jpg",
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/132.jpg",
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/142.jpg",
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/102.jpg",
        "https://raw.githubusercontent.com/zzzDavid/ICDAR-2019-SROIE/refs/heads/master/data/img/182.jpg",
    ]
    
    agent = AgentImageProcessor()
    response = agent.process_images(image_urls)
    print(response)
    print(len(response))
    # json
    # print(response.model_dump_json())
    print(response[1].model_dump_json())

