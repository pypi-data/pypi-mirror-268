from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from datetime import datetime
import json

from dmm.db.session import get_engine
from dmm.utils.sense import get_site_info

BASE = declarative_base()

class ModelBase(object):
    def __setitem__(self, key, value):
        setattr(self, key, value)
    def __getitem__(self, key):
        return getattr(self, key)
    @declared_attr
    def created_at(cls):
        return Column("created_at", DateTime, default=datetime.utcnow)
    @declared_attr
    def updated_at(cls):
        return Column("updated_at", DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    def save(self, session=None):
        """Save this object"""
        session.add(self)
    def delete(self, session=None):
        """Delete this object"""
        session.delete(self)
    def update(self, values, session=None):
        """dict.update() behaviour."""
        for k, v in values.items():
            self[k] = v

# DMM Data Structures
class Request(BASE, ModelBase):
    __tablename__ = "requests"
    rule_id = Column(String(255), primary_key=True)
    transfer_status = Column(String(255))
    src_site = Column(String(255))
    src_ipv6_block = Column(String(255))
    src_url = Column(String(255))
    dst_site = Column(String(255))
    dst_ipv6_block = Column(String(255))
    dst_url = Column(String(255))
    priority = Column(Integer())
    modified_priority = Column(Integer())
    max_bandwidth = Column(Float())
    bandwidth = Column(Float())
    sense_uuid = Column(String(255))
    sense_circuit_status = Column(String(255))
    fts_modified = Column(Boolean())

    def __init__(self, **kwargs):
        super(Request, self).__init__(**kwargs)

class Site(BASE, ModelBase):
    __tablename__ = "sites"
    name = Column(String(255), primary_key=True)
    sense_uri = Column(String(255))
    port_capacity = Column(Integer())
    query_url = Column(String(255))

    def __init__(self, **kwargs):
        super(Site, self).__init__(**kwargs)
        site_info = get_site_info(self.name)
        site_info = json.loads(site_info)
        self.sense_uri = site_info["domain_uri"]
        if not self.port_capacity:
            self.port_capacity = float(site_info["peer_points"][0]["port_capacity"]) * 0.8
        self.query_url = site_info["domain_url"]

class Endpoint(BASE, ModelBase):
    __tablename__ = "endpoints"
    id = Column(Integer(), autoincrement=True, primary_key=True)
    site = Column(String(255))
    ip_block = Column(String(255))
    hostname = Column(String(255))
    in_use = Column(Boolean())

    def __init__(self, **kwargs):
        super(Endpoint, self).__init__(**kwargs)

# Create the tables if don't exist when module first imported.
engine=get_engine()
Request.__table__.create(bind=engine, checkfirst=True)
Site.__table__.create(bind=engine, checkfirst=True)
Endpoint.__table__.create(bind=engine, checkfirst=True)