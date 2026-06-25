from datetime import datetime
import uuid
from backend.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, DateTime, func

class Canaries(Base):
    __tablename__='canaries'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[uuid.UUID] = mapped_column(UUID)
    description: Mapped[str]
    redirect_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )

