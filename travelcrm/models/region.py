# -*-coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint,
)

from sqlalchemy.orm import (
    relationship,
    backref
)

from ..models import (
    DBSession,
    Base
)


class Region(Base):
    __tablename__ = 'region'
    __table_args__ = (
        UniqueConstraint(
            'name',
            'country_id',
            name='unique_idx_name_country_id_region',
            use_alter=True,
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    resource_id = Column(
        Integer,
        ForeignKey(
            'resource.id',
            name="fk_resource_id_region",
            ondelete='restrict',
            onupdate='cascade',
            use_alter=True,
        ),
        nullable=False,
    )
    country_id = Column(
        Integer(),
        ForeignKey(
            'country.id',
            name='fk_region_country_id',
            onupdate='cascade',
            ondelete='restrict',
            use_alter=True,
        ),
        nullable=False,
    )
    name = Column(
        String(length=32),
        nullable=False,
    )
    resource = relationship(
        'Resource',
        backref=backref('region', uselist=False),
        uselist=False
    )
    country = relationship(
        'Country',
        backref=backref(
            'regions',
            uselist=True,
            lazy="dynamic"
        ),
        uselist=False
    )

    @classmethod
    def get(cls, id):
        if id is None:
            return None
        return DBSession.query(cls).get(id)
