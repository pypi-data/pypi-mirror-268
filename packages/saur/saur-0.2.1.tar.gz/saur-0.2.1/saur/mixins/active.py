from __future__ import annotations
from datetime import datetime, UTC

from sqlalchemy.orm import Mapped, mapped_column, declarative_mixin
from sqlalchemy.ext.hybrid import hybrid_property


@declarative_mixin
class ActiveMixin:
    created: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    deactivated: Mapped[datetime | None] = mapped_column(default=None)

    @hybrid_property
    def active(self) -> bool:
        return self.deactivated == None  # noqa: E711

    @active.inplace.setter
    def _active_setter(self, value: bool | None) -> None:
        if value is not None:
            if value and self.deactivated:
                self.deactivated = None
            elif not value and self.deactivated is None:
                self.deactivated = datetime.now(UTC)
