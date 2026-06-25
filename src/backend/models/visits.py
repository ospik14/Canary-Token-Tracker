from datetime import datetime
from backend.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func, ForeignKey

class Visits(Base):
    __tablename__='visits'

    id: Mapped[int] = mapped_column(primary_key=True)
    canary_id: Mapped[int] = mapped_column(ForeignKey('canaries.id', ondelete='CASCADE'))
    ip_address: Mapped[str] 
    user_agent: Mapped[str]
    country: Mapped[str]
    city: Mapped[str]
    isp: Mapped[str]
    visited_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )