"""
Candidate API Routes

Module containing API routes for CRUD operations on candidates.

Functions:
    add_candidate: Route to create a new candidate.
    get_single_candidate: Route to retrieve a single candidate by ID.
    get_all: Route to retrieve all candidates with pagination and filters.
    update_single_candidate: Route to update a single candidate by ID.
    delete_single_candidate: Route to delete a single candidate by ID.
"""

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest, Conflict, InternalServerError
from app.handlers.candidates import (
    create_candidate,
    get_candidate_by_id,
    get_all_candidates,
    update_candidate,
    delete_candidate,
)

blueprint = Blueprint("v1", __name__)


@blueprint.route("/candidates", methods=["POST"])
def add_candidate():
    """Create a new candidate.

    Request JSON body:
    {
        "firstname": "string",
        "lastname": "string",
        "email": "string",
        "age": integer
    }

    Returns:
        JSON response with the created candidate's data.
    """
    try:
        data = request.json
        new_candidate = create_candidate(
            data["firstname"], data["lastname"], data["email"], data["age"]
        )
        return jsonify(new_candidate.serialize()), 201
    except Conflict as e:
        return jsonify({"message": e.description}), 409
    except BadRequest as e:
        return jsonify({"message": e.description}), 400
    except InternalServerError as e:
        return jsonify({"message": e.description}), 500


@blueprint.route("/candidates/<int:candidate_id>", methods=["GET"])
def get_single_candidate(candidate_id):
    """Retrieve a single candidate by ID.

    Args:
        candidate_id: ID of the candidate to retrieve.

    Returns:
        JSON response with the candidate's data if found, else 404 Not Found.
    """
    candidate = get_candidate_by_id(candidate_id)
    if candidate:
        return jsonify(candidate.serialize()), 200
    else:
        raise NotFound(description=f"Candidate with ID {candidate_id} not found")


@blueprint.route("/candidates", methods=["GET"])
def get_all():
    """Retrieve all candidates with pagination and optional filters.

    Request query parameters:
        page: Page number for pagination (default is 1).
        per_page: Number of candidates per page (default is 10).
        filters: Optional filters as query parameters.

    Returns:
        JSON response with a list of candidates based on provided filters and pagination.
    """
    try:
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))
        filters = request.args.to_dict()
        candidates = get_all_candidates(page=page, per_page=per_page, filters=filters)
        return jsonify([candidate.serialize() for candidate in candidates]), 200
    except InternalServerError as e:
        return jsonify({"error": e.description}), 500


@blueprint.route("/candidates/<int:candidate_id>", methods=["PUT"])
def update_single_candidate(candidate_id):
    """Update a single candidate by ID.

    Args:
        candidate_id: ID of the candidate to update.

    Request JSON body:
    {
        "firstname": "string",
        "lastname": "string",
        "email": "string",
        "age": integer
    }

    Returns:
        JSON response confirming the update or 404 Not Found if the candidate does not exist.
    """
    try:
        candidate = get_candidate_by_id(candidate_id)
        if not candidate:
            raise NotFound(description=f"Candidate with ID {candidate_id} not found")

        data = request.json
        update_candidate(candidate, data)
        return (
            jsonify({"message": f"Candidate {candidate_id} updated successfully"}),
            200,
        )
    except InternalServerError as e:
        return jsonify({"message": e.description}), 500


@blueprint.route("/candidates/<int:candidate_id>", methods=["DELETE"])
def delete_single_candidate(candidate_id):
    """Delete a single candidate by ID.

    Args:
        candidate_id: ID of the candidate to delete.

    Returns:
        JSON response confirming the deletion or 404 Not Found if the candidate does not exist.
    """
    try:
        candidate = get_candidate_by_id(candidate_id)
        if not candidate:
            raise NotFound(description=f"Candidate with ID {candidate_id} not found")

        delete_candidate(candidate)
        return (
            jsonify({"message": f"Candidate {candidate_id} deleted successfully"}),
            200,
        )
    except InternalServerError as e:
        return jsonify({"message": e.description}), 500
