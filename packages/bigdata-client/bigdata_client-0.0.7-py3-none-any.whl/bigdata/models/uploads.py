from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class DocumentStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    DELETED = "DELETED"


class Document(BaseModel):
    id: Optional[str] = Field(validation_alias="file_id")
    name: str = Field(validation_alias="file_name")
    status: DocumentStatus = Field(validation_alias="status")
    uploaded_at: Optional[datetime] = Field(validation_alias="upload_ts")
    raw_size: Optional[int]
    folder_id: Optional[str] = Field(validation_alias="folder_id")
    trashed: bool
    starred: bool
    tags: Optional[List[str]]

    def get_status(self) -> DocumentStatus:
        """Returns the "upload-status" of the document."""

    def save_content(self, filename: str):
        """Downloads the content of the document to a file in the disk."""


class UploadQuotaFiles(BaseModel):
    available: int
    error: int
    total: int


class UploadQuotaUsage(BaseModel):
    max_units_allowed: int
    storage_bytes_used: int
    units_remaining: int
    units_used: int


class UploadQuotaSubscriptionUsage(BaseModel):
    current_month: UploadQuotaUsage
    subscription: UploadQuotaUsage


class UploadQuota(BaseModel):
    files: UploadQuotaFiles
    quota: UploadQuotaSubscriptionUsage
