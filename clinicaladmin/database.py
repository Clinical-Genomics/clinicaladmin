from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Column, Integer, String, DateTime, Text, Enum,
                        ForeignKey, UniqueConstraint, Numeric, Date)
from sqlalchemy.orm import relationship, backref
from clinicaladmin.config import DEMULTIPLEX_DATABASE_URI


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DEMULTIPLEX_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    customer_number = db.Column(db.String(500))
    customer_name = db.Column(db.String(500))
    agreement_date = db.Column(db.String(500))
    primary_contact_name = db.Column(db.String(500))
    primary_contact_email = db.Column(db.String(500))
    primary_contact_delivery_name = db.Column(db.String(500))
    primary_contact_delivery_email = db.Column(db.String(500))
    access_to_scout = db.Column(db.String(500))
    uppmax_account = db.Column(db.String(500))
    agreement_diarie_number = db.Column(db.String(500))
    clinical_genomics_project_account_KI = db.Column(db.String(500))
    clinical_genomics_project_account_KTH = db.Column(db.String(500))
    organisation_number = db.Column(db.String(500))
    invoicing_address = db.Column(db.String(500))
    invoicing_reference = db.Column(db.String(500))
    invoicing_contact_person = db.Column(db.String(500))
    invoicing_email = db.Column(db.String(500))


class ApplicationDetails(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    #application_tag = db.Column(db.String(500))
    version = db.Column(db.String(500))
    application_tag = db.Column(db.String(500)) #db.Column(db.String(50), db.ForeignKey('application_tags.application_tag'))
    application_tag_id = db.Column(db.ForeignKey('application_tags.id'), nullable=False)
    application_tag_data = relationship('ApplicationTagData', backref=backref('details'))
    date_valid_from = db.Column(db.String(500))
    express_price = db.Column(db.String(500))
    standard_price = db.Column(db.String(500))
    priority_price = db.Column(db.String(500))
    research_price = db.Column(db.String(500))
    accredited = db.Column(db.String(500))
    description = db.Column(db.String(500))
    comment = db.Column(db.String(500))
    percent_charged_to_kth = db.Column(db.String(500))

    def __repr__(self):
        return '{} v{}'.format(self.application_tag, self.version)

#(u"{self.application_tag_data.application_tag}: {self.application_tag_data.application_tag_version}"
                #.format(self=self))


class ApplicationTagData(db.Model):
    __tablename__ = 'application_tags'
    id = db.Column(db.Integer, primary_key=True)
#    details_id = db.Column(db.ForeignKey('details.id'))
#    details = relationship('ApplicationDetails', cascade='all,delete', backref='application')
    application_tag = db.Column(db.String(50))
    created_at = db.Column(db.String(500))
    minimum_order = db.Column(db.String(500))
    sequencing_depth = db.Column(db.String(500))
    sample_amount = db.Column(db.String(500))
    sample_volume = db.Column(db.String(500))
    sample_concentration = db.Column(db.String(500))
    turnaround_time = db.Column(db.String(500))
    priority_processing = db.Column(db.String(500))

    def __repr__(self):
        return self.application_tag


class MethodDescription(db.Model):
    __tablename__ = 'methods'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(500))
    method_nr = db.Column(db.String(500))
    information = db.Column(db.String(500))
    limitations = db.Column(db.String(500))
    version = db.Column(db.String(500))


class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.String(500))
    customer = db.Column(db.String(500))
    invoice_date = db.Column(db.String(500))
