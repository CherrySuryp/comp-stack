from fastapi import HTTPException, status

FileNotFound = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="FILE_NOT_FOUND")
