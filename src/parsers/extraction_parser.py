from typing import Dict, List, Any
import re
from models.entities import Entity, Relationship, ExtractedData

class ExtractionParser:
    """Parser for LLM extraction output."""
    
    @staticmethod
    def parse_response(response: str) -> ExtractedData:
        """
        Parse LLM response into structured data.
        
        Args:
            response: Raw LLM response text
            
        Returns:
            ExtractedData object containing entities and relationships
        """
        entities = []
        relationships = []
        
        # Clean and split response, filtering out empty strings and whitespace
        entries = [entry.strip() for entry in response.split("<<<>>>") if entry.strip()]
        
        for entry in entries:
            # Remove quotes and split by delimiter, strip each part
            parts = [part.strip() for part in entry.replace('"', '').split("|||")]
            
            # Skip if we don't have enough parts
            if len(parts) < 4:
                continue
                
            if parts[0] == "entity":
                entities.append(Entity(
                    name=parts[1],
                    type=parts[2],
                    description=parts[3]
                ))
            elif parts[0] == "relationship":
                # Only process relationship if we have all required parts
                if len(parts) >= 5:
                    try:
                        relationships.append(Relationship(
                            source=parts[1],
                            target=parts[2],
                            description=parts[3],
                            strength=int(parts[4])
                        ))
                    except ValueError:
                        # Handle case where strength isn't a valid integer
                        continue
        
        return ExtractedData(
            entities=entities,
            relationships=relationships
        ) 