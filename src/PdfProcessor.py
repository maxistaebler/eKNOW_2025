#  Add parent directory to Python path to import helpers
from pathlib import Path
from typing import List, Literal
from docling.document_converter import DocumentConverter
import logging

class PdfProcessor:
    """Process PDF files to markdown or text using docling."""
    
    def __init__(self, input_dir: str = "../input/pdf", output_dir: str = "../input/txt"):
        """
        Initialize PDF processor with input and output directories.
        
        Args:
            input_dir: Directory containing PDF files
            output_dir: Directory where output files will be saved
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.converter = DocumentConverter()
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        self.logger = logging.getLogger(__name__)

    def process_pdfs(self, output_format: Literal["markdown", "text"] = "markdown") -> None:
        """
        Convert all PDFs in input directory to markdown or text files.
        
        Args:
            output_format: The desired output format ("markdown" or "text")
        """
        pdf_files = list(self.input_dir.glob("*.pdf"))
        self.logger.info(f"Found {len(pdf_files)} PDF files in {self.input_dir}")
        
        for pdf_path in pdf_files:
            try:
                # Convert PDF using docling
                result = self.converter.convert(str(pdf_path))
                
                # Get content based on desired format
                if output_format == "markdown":
                    content = result.document.export_to_markdown()
                    extension = ".md"
                else:  # text format
                    content = result.document.export_to_text()
                    extension = ".txt"
                
                # Save file with appropriate extension
                output_path = self.output_dir / f"{pdf_path.stem}{extension}"
                output_path.write_text(content, encoding='utf-8')
                self.logger.info(f"Processed: {pdf_path.name} -> {output_path.name}")
                
            except Exception as e:
                self.logger.error(f"Error processing {pdf_path.name}: {str(e)}")