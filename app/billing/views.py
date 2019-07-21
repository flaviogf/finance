from flask import Blueprint, render_template
from flask_login import login_required

billing = Blueprint('billing', __name__)


@billing.route('/billing/create')
@login_required
def create():
    return render_template('create_billing.html')
