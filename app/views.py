"""
Views Blueprint

This blueprint defines routes for rendering pages related to candidate management.
These routes interact with the v1_blueprint API to perform CRUD operations on candidates.

Routes:
    list_candidates: Render a page listing all candidates.
    view_candidate: Render details of a specific candidate.
    add_candidate: Render a form to add a new candidate.
    edit_candidate: Render a form to edit a candidate's details.
    delete_candidate: Delete a candidate.

Each route corresponds to a specific page view or form submission related to candidate management.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from app.api import v1

views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/candidates", methods=["GET"])
def list_candidates():
    """Render a page listing all candidates."""
    candidates = v1.get_all()
    return render_template("candidates_list.html", candidates=candidates)


# @views_blueprint.route("/candidates/<int:candidate_id>", methods=["GET"])
# def view_candidate(candidate_id):
#     """Render details of a specific candidate."""
#     candidate = v1_blueprint.get_candidate_by_id(candidate_id)
#     if not candidate:
#         flash("Candidate not found", "error")
#         return redirect(url_for("views.list_candidates"))
#     return render_template("candidate_details.html", candidate=candidate)


# @views_blueprint.route("/candidates/add", methods=["GET", "POST"])
# def add_candidate():
#     """Render a form to add a new candidate."""
#     form = CandidateForm()
#     if form.validate_on_submit():
#         try:
#             v1_blueprint.create_candidate(
#                 form.firstname.data, form.lastname.data, form.email.data, form.age.data
#             )
#             flash("Candidate added successfully", "success")
#             return redirect(url_for("views.list_candidates"))
#         except Exception as e:
#             flash(str(e), "error")
#     return render_template("add_candidate.html", form=form)


# @views_blueprint.route("/candidates/<int:candidate_id>/edit", methods=["GET", "POST"])
# def edit_candidate(candidate_id):
#     """Render a form to edit a candidate's details."""
#     candidate = v1_blueprint.get_candidate_by_id(candidate_id)
#     if not candidate:
#         flash("Candidate not found", "error")
#         return redirect(url_for("views.list_candidates"))
#     form = CandidateForm(obj=candidate)
#     if form.validate_on_submit():
#         try:
#             v1_blueprint.update_candidate(
#                 candidate,
#                 {
#                     "firstname": form.firstname.data,
#                     "lastname": form.lastname.data,
#                     "email": form.email.data,
#                     "age": form.age.data,
#                 },
#             )
#             flash("Candidate updated successfully", "success")
#             return redirect(url_for("views.view_candidate", candidate_id=candidate_id))
#         except Exception as e:
#             flash(str(e), "error")
#     return render_template("edit_candidate.html", form=form, candidate_id=candidate_id)


# @views_blueprint.route("/candidates/<int:candidate_id>/delete", methods=["POST"])
# def delete_candidate(candidate_id):
#     """Delete a candidate."""
#     candidate = v1_blueprint.get_candidate_by_id(candidate_id)
#     if not candidate:
#         flash("Candidate not found", "error")
#         return redirect(url_for("views.list_candidates"))
#     try:
#         v1_blueprint.delete_candidate(candidate)
#         flash("Candidate deleted successfully", "success")
#     except Exception as e:
#         flash(str(e), "error")
#     return redirect(url_for("views.list_candidates"))
