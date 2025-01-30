from arango import ArangoClient
from typing import List, Union, Dict, Any

def get_communities_by_human_readable_ids(human_readable_ids: List[int], db) -> List[Dict[str, Any]]:
    """
    Retrieve community entries with specific human_readable_ids
    
    Args:
        human_readable_ids (List[Union[str, int]]): List of human_readable_ids to search for
        db: ArangoDB database instance
    
    Returns:
        List[Dict[str, Any]]: List of community documents with human_readable_id and id
        
    Raises:
        ValueError: If human_readable_ids is empty
        TypeError: If human_readable_ids is not a list
    """
    # Input validation
    if not isinstance(human_readable_ids, list):
        raise TypeError("human_readable_ids must be a list")
    
    if not human_readable_ids:
        raise ValueError("human_readable_ids list cannot be empty")
    
    try:
        aql_query = """
        FOR c IN communities
            FILTER c.human_readable_id IN @human_readable_ids
            RETURN {
                human_readable_id: c.human_readable_id,
                id: c.id
            }
        """
        
        # Bind parameters
        bind_vars = {
            "human_readable_ids": human_readable_ids
        }
        
        # Execute the query
        cursor = db.aql.execute(aql_query, bind_vars=bind_vars)
        
        # Get all results
        results = [doc for doc in cursor]
        
        return results
        
    except Exception as e:
        print(f"Error executing query: {str(e)}")
        raise

from arango import ArangoClient
from typing import List, Union, Dict, Any, Literal

CollectionType = Literal['communities', 'relationships', 'entities', 'chunks']

def get_documents_by_human_readable_ids(
    human_readable_ids: List[Union[str, int]],
    collection_name: CollectionType,
    db
) -> List[Dict[str, Any]]:
    """
    Retrieve documents with specific human_readable_ids from a given collection
    
    Args:
        human_readable_ids (List[Union[str, int]]): List of human_readable_ids to search for
        collection_name (str): Name of the collection to query
        db: ArangoDB database instance
    
    Returns:
        List[Dict[str, Any]]: List of documents with human_readable_id and id
        
    Raises:
        ValueError: If human_readable_ids is empty
        TypeError: If human_readable_ids is not a list
    """
    # Input validation
    if not isinstance(human_readable_ids, list):
        raise TypeError("human_readable_ids must be a list")
    
    if not human_readable_ids:
        raise ValueError("human_readable_ids list cannot be empty")
    
    if collection_name not in ['communities', 'relationships', 'entities', 'chunks']:
        raise ValueError("Invalid collection name")
    
    try:
        aql_query = f"""
        FOR doc IN {collection_name}
            FILTER doc.human_readable_id IN @human_readable_ids
            RETURN {{
                human_readable_id: doc.human_readable_id,
                id: doc.id
            }}
        """
        
        # Bind parameters
        bind_vars = {
            "human_readable_ids": human_readable_ids
        }
        
        # Execute the query
        cursor = db.aql.execute(aql_query, bind_vars=bind_vars)
        
        # Get all results
        results = [doc for doc in cursor]
        
        return results
        
    except Exception as e:
        print(f"Error executing query: {str(e)}")
        raise

# Convenience functions for specific collections
def get_relationships_by_human_readable_ids(human_readable_ids: List[int], db):
    return get_documents_by_human_readable_ids(human_readable_ids, 'relationships', db)

def get_entities_by_human_readable_ids(human_readable_ids: List[int], db):
    return get_documents_by_human_readable_ids(human_readable_ids, 'entities', db)

def get_chunks_by_human_readable_ids(human_readable_ids: List[int], db):
    return get_documents_by_human_readable_ids(human_readable_ids, 'chunks', db)

def get_communities_by_human_readable_ids(human_readable_ids: List[int], db):
    return get_documents_by_human_readable_ids(human_readable_ids, 'communities', db)