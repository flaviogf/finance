from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required

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
    page = request.args.get('page', 1, type=int)

    billings = (Billing.query
                .filter_by(user_id=current_user.get_id())
                .paginate(page=page, per_page=1))

    return render_template('pagination_billing.html', title='Search Billing', billings=billings)


@billing.route('/billing/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    billing = Billing.query.get_or_404(id)

    form = CreateBillingForm()

    if form.validate_on_submit():
        billing.title = form.title.data
        billing.description = form.description.data
        billing.value = form.value.data
        billing.work_date = form.work_date.data

        db.session.commit()

        flash('Billing updated with successfully.')

        return redirect(url_for('billing.update', id=id))
    elif request.method == 'GET':
        form.title.data = billing.title
        form.description.data = billing.description
        form.value.data = billing.value
        form.work_date.data = billing.work_date

    return render_template('create_billing.html', title='Update Billing', form=form)


@billing.route('/billing/<int:id>/confirm-receive')
@login_required
def confirm_receive(id):
    billing = Billing.query.get_or_404(id)

    if current_user.get_id() != billing.user_id:
        abort(403)

    billing.confirm_receive()

    db.session.commit()

    return redirect(url_for('billing.pagination'))


@billing.route('/billing/<int:id>/cancel-receive')
@login_required
def cancel_receive(id):
    billing = Billing.query.get_or_404(id)

    if current_user.get_id() != billing.user_id:
        abort(403)

    billing.cancel_receive()

    db.session.commit()

    return redirect(url_for('billing.pagination'))
