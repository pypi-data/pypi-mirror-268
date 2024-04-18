import logging
from sqlalchemy import text

from dmm.db.models import Request, Site, Endpoint
from dmm.utils.siterm import get_siterm_list_of_endpoints

# Requests
def get_request_from_id(rule_id, session=None):
    req = session.query(Request).filter(Request.rule_id == rule_id).first()
    return req if req else None

def get_requests(status=None, session=None):
    if status is not None:
        return session.query(Request).filter(Request.transfer_status.in_(status)).all()
    else:
        return session.query(Request).all()

def get_request_cursor(session=None):
    return session.execute(text("SELECT * from requests")).cursor

def mark_requests(reqs, status, session=None):
    for req in reqs:
        req.update({
            "transfer_status": status,
            "fts_modified": False
        })
        logging.debug(f"Marked {req.rule_id} as {status}")

def update_bandwidth(req, bandwidth, session=None):
    req.update({
        "bandwidth": bandwidth
    })
    logging.debug(f"Updated bandwidth to {bandwidth} for {req.rule_id}")

def update_priority(req, priority, session=None):
    req.update({
        "priority": priority,
        "modified_priority": priority
    })
    logging.debug(f"Updated priority to {priority} for {req.rule_id}")

def update_sense_circuit_status(req, status, session=None):
    req.update({
        "sense_circuit_status": status
    })
    logging.debug(f"Updated sense_circuit_status to {status} for {req.rule_id}")

def mark_fts_modified(req, session=None):
    req.update({
        "fts_modified": True
    })
    logging.debug(f"Marked fts_modified for {req.rule_id}")

# Sites
def get_site(site_name, attr=None, session=None):
    if attr:
        query = session.query(Site).filter(Site.name == site_name).first()
        return getattr(query, attr)
    else:
        return session.query(Site).filter(Site.name == site_name).first()

def update_site(site, certs, session=None):
    site_exists = get_site(site, session=session)
    if not site_exists:
        site_ = Site(name=site)
        site_.save(session=session)
    else:
        site_ = site_exists
    for block, hostname in get_siterm_list_of_endpoints(site=site_, certs=certs):
        if get_endpoint(hostname, session=session) is None:
            new_endpoint = Endpoint(site=site_.name,
                                    ip_block=block,
                                    hostname=hostname,
                                    in_use=False
                                    )
            new_endpoint.save(session=session)

# Endpoints
def get_all_endpoints(session=None):
    endpoints = session.query(Endpoint).all()
    return endpoints

def get_endpoint(hostname, session=None):
    endpoint = session.query(Endpoint).filter(Endpoint.hostname == hostname).first()
    return endpoint

def get_unused_endpoint(site, session=None):
    endpoint = session.query(Endpoint).filter(Endpoint.site == site, Endpoint.in_use == False).first()
    endpoint.update({
        "in_use": True
    })
    return endpoint

def free_endpoint(hostname, session=None):
    endpoint = session.query(Endpoint).filter(Endpoint.hostname == hostname, Endpoint.in_use == True).first()
    endpoint.update({
        "in_use": False
    })
    return