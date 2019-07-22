from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user

from app import db
from app.billing.forms import CreateBillingForm
from app.models import Billing

billing = Blueprint('billing', __name__)


@billing.route('/billing/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateBillingForm()

    if form.validate_on_submit():
        billing = Billing(title=form.title.data,
                          description=form.description.data,
                          value=form.value.data,
                          work_date=form.work_date.data,
                          user_id=current_user.get_id())

        db.session.add(billing)

        db.session.commit()

        return redirect(url_for('billing.pagination'))

    return render_template('create_billing.html', title='Create Billing', form=form)


@billing.route('/billing')
@login_required
def pagination():
    return render_template('pagination_billing.html', title='Search Billing')
