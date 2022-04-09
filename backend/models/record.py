import hashlib
from xml.etree import ElementTree

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Record(db.Model):
    id = db.Column('id', db.INT, primary_key=True)
    type = db.Column('type', db.TEXT, nullable=False)
    type_id = db.Column('type_id', db.INT, nullable=False)
    current = db.Column('current', db.BOOLEAN, nullable=False)
    md5_hash = db.Column('md5_hash', UUID, nullable=False)
    data = db.Column('data', db.TEXT, nullable=False)
    created_at = db.Column('created_at', db.TIMESTAMP, server_default=func.now())

    @classmethod
    def update_data(cls, type_str, type_id, element, ignore_list=None):
        """Save a record to the DB with hash."""
        ignore_list = ignore_list or []

        data = ElementTree.tostring(element).decode()

        # ignore some fields for hashing
        for i in ignore_list:
            element.attrib.pop(i, None)

        # hash
        md5_str = ElementTree.tostring(element).decode().replace("\n", " ")
        md5_hash = hashlib.md5(md5_str.encode('utf-8')).hexdigest()

        # check if this is already in the db as the current
        existing = Record.query.filter_by(type=type_str, type_id=type_id, current=True).first()

        if existing:
            # hash is stored as uuid with extra dashes, remove them when comparing hashes
            if existing.md5_hash.replace('-', '') == md5_hash:
                # if we ignored fields, update them, but don't make a new record.
                if ignore_list:
                    if existing.data != data:
                        existing.data = data
                        db.session.commit()

                return
            else:
                # new hash and data, previous record is no more the current
                existing.current = False

        # create the new record and save it in database
        new_record = cls(
            type=type_str,
            type_id=type_id,
            current=True,
            md5_hash=md5_hash,
            data=data,
        )

        db.session.add(new_record)
        db.session.commit()

    @classmethod
    def set_not_current(cls, type_str, type_id):
        """Set record's current state to False in the DB."""

        existing = Record.query.filter_by(type=type_str, type_id=type_id, current=True).first()
        existing.current = False
        db.session.commit()

    @classmethod
    def purge_old_records(cls, type_str, still_presents_ids):
        """Disable old records not presents in API."""

        current_ids = Record.query.filter_by(type=type_str, current=True).with_entities(Record.type_id).all()
        current_ids = [current_id[0] for current_id in current_ids]
        no_more_presents_ids = list(set(current_ids) - set(still_presents_ids))

        for no_more_presents_id in no_more_presents_ids:
            Record.set_not_current(type_str, no_more_presents_id)
