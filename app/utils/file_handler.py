import os
import shutil
import time
from fastapi import UploadFile
from typing import Optional


class FileHandler:
    """
    Utility class untuk handling file uploads.
    Encapsulates file operations untuk better code organization.
    """
    
    def __init__(self, upload_dir: str = "uploads"):
        """
        Initialize FileHandler.
        
        Args:
            upload_dir: Directory untuk menyimpan uploaded files
        """
        self.upload_dir = upload_dir
        # Ensure upload directory exists
        os.makedirs(self.upload_dir, exist_ok=True)
    
    def save_upload_file(self, file: UploadFile, prefix: str = "file") -> str:
        """
        Save uploaded file to upload directory.
        
        Args:
            file: UploadFile object from FastAPI
            prefix: Prefix untuk filename (biasanya nama produk)
            
        Returns:
            str: Saved filename
        """
        # Generate unique filename
        file_extension = os.path.splitext(file.filename)[1]
        safe_prefix = prefix.replace(' ', '_').replace('/', '_')
        timestamp = int(time.time() * 1000)
        filename = f"{safe_prefix}_{timestamp}{file_extension}"
        
        # Save file
        file_path = os.path.join(self.upload_dir, filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return filename
    
    def delete_file(self, filename: str) -> bool:
        """
        Delete file from upload directory.
        
        Args:
            filename: Name of file to delete
            
        Returns:
            bool: True if deleted, False otherwise
        """
        if not filename:
            return False
        
        # Try multiple possible paths
        file_paths = [
            os.path.join(self.upload_dir, filename),
            os.path.join("..", self.upload_dir, filename)
        ]
        
        for file_path in file_paths:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    return True
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
        
        return False
    
    def file_exists(self, filename: str) -> bool:
        """
        Check if file exists.
        
        Args:
            filename: Name of file to check
            
        Returns:
            bool: True if exists, False otherwise
        """
        if not filename:
            return False
        
        file_path = os.path.join(self.upload_dir, filename)
        return os.path.exists(file_path)
    
    def get_file_path(self, filename: str) -> Optional[str]:
        """
        Get full path to file if it exists.
        
        Args:
            filename: Name of file
            
        Returns:
            Optional[str]: Full path or None if not found
        """
        if not filename:
            return None
        
        file_path = os.path.join(self.upload_dir, filename)
        
        if os.path.exists(file_path):
            return file_path
        
        return None
