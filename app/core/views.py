from decimal import Decimal

from flask import Blueprint, render_template
from flask_login import current_user, login_required
from sqlalchemy import func

from app import db
from app.models import Billing

core = Blueprint('core', __name__)


@core.route('/')
@login_required
def home():
    total_billing_received = (db.session
                              .query(func.sum(Billing.value).label('result'))
                              .filter(
                                  Billing.user_id == current_user.get_id(),
                                  Billing.received == True
                              )
                              .first().result) or Decimal('0.00')

    total_billing_receivable = (db.session
                                .query(func.sum(Billing.value).label('result'))
                                .filter(
                                    Billing.user_id == current_user.get_id(),
                                    Billing.received == False
                                )
                                .first().result) or Decimal('0.00')

    return render_template('home.html',
                           title='Home',
                           total_billing_received=total_billing_received,
                           total_billing_receivable=total_billing_receivable)
