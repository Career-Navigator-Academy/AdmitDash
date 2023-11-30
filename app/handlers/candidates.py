"""Candidate Handler

Module for CRUD operations on the Candidate model.

Functions:
    create_candidate:
        Create a new candidate.

        Example:
            create_candidate('John', 'Doe', 'john@example.com', 30)

    get_candidate_by_id:
        Retrieve a candidate by ID.

        Example:
            get_candidate_by_id(1)

    get_all_candidates:
        Retrieve all candidates with pagination and optional filters.

        Example:
            get_all_candidates(page=1, per_page=10, filters={'age': 25, 'lastname': 'Doe'})

    update_candidate:
        Update a candidate's information.

        Example:
            update_candidate(candidate, {'age': 31, 'lastname': 'Smith'})

    delete_candidate:
        Delete a candidate.

        Example:
            delete_candidate(candidate)
"""

from typing import Optional, Dict, Any, List
import logging
from werkzeug.exceptions import Conflict, InternalServerError
from sqlalchemy.exc import SQLAlchemyError
from app.models import candidates, db

logger = logging.getLogger(__name__)

Candidate = candidates.Candidate


def create_candidate(
    firstname: str, lastname: str, email: str, age: int
) -> Optional[Candidate]:
    """Create a new candidate.

    Args:
        firstname: The candidate's first name.
        lastname: The candidate's last name.
        email: The candidate's email address.
        age: The candidate's age.

    Raises:
        Conflict: If a candidate with the provided email already exists.
        InternalServerError: If an unexpected error occurs during creation.

    Returns:
        Optional[Candidate]: The created candidate object, if successful.
    """
    try:
        if Candidate.query.filter_by(email=email).first():
            logger.info("Duplicate email found: %s", email)
            raise Conflict(description="Candidate with this email already exists.")

        new_candidate = Candidate(
            firstname=firstname, lastname=lastname, email=email, age=age
        )
        db.session.add(new_candidate)
        db.session.commit()
        logger.info("New candidate created: %s", new_candidate.id)
        return new_candidate
    except SQLAlchemyError as e:
        logger.error("Error creating candidate: %s", e, exc_info=True)
        raise InternalServerError(
            description="Error creating candidate. Please try again later."
        ) from e


def get_candidate_by_id(candidate_id: int) -> Optional[Candidate]:
    """Retrieve a candidate by ID.

    Args:
        candidate_id: The ID of the candidate to retrieve.

    Raises:
        InternalServerError: If an unexpected error occurs during retrieval.

    Returns:
        Optional[Candidate]: The candidate object if found, otherwise None.
    """
    try:
        candidate = Candidate.query.get(candidate_id)
        if candidate:
            return candidate

        logger.info("Candidate not found with ID: %s", candidate_id)
        return None
    except SQLAlchemyError as e:
        logger.error("Error retrieving candidate by ID: %s", e, exc_info=True)
        raise InternalServerError(
            description="Error retrieving candidate. Please try again later."
        ) from e


def get_all_candidates(
    page: int = 1, per_page: int = 10, filters: dict = None
) -> List[Candidate]:
    """Retrieve all candidates with pagination and optional filters.

    Args:
        page: Page number for pagination (default is 1).
        per_page: Number of candidates per page (default is 10).
        filters: Optional filters as a dictionary (e.g., {'age': 25, 'lastname': 'Doe'}).

    Returns:
        List[Candidate]: List of candidates based on provided filters and pagination.
    """
    try:
        query = Candidate.query

        if filters:
            for key, value in filters.items():
                query = query.filter(getattr(Candidate, key) == value)

        candidates = query.paginate(page, per_page, error_out=False).items
        return candidates

    except Exception as e:
        logger.error("Error retrieving candidates: %s", e, exc_info=True)
        raise InternalServerError(
            description="Error retrieving candidates. Please try again later."
        ) from e


def update_candidate(candidate: Candidate, new_data: Dict[str, Any]) -> None:
    """Update a candidate's information.

    Args:
        candidate: The candidate object to update.
        new_data: Dictionary containing updated data for the candidate.

    Raises:
        InternalServerError: If an unexpected error occurs during update.
    """
    try:
        for key, value in new_data.items():
            setattr(candidate, key, value)
        db.session.commit()
        logger.info("Candidate %s updated successfully", candidate.id)
    except SQLAlchemyError as e:
        logger.error("Error updating candidate: %s", e, exc_info=True)
        raise InternalServerError(
            description="Error updating candidate. Please try again later."
        ) from e


def delete_candidate(candidate: Candidate) -> None:
    """Delete a candidate.

    Args:
        candidate: The candidate object to delete.

    Raises:
        InternalServerError: If an unexpected error occurs during deletion.
    """
    try:
        db.session.delete(candidate)
        db.session.commit()
        logger.info("Candidate %s deleted successfully", candidate.id)
    except SQLAlchemyError as e:
        logger.error("Error deleting candidate: %s", e, exc_info=True)
        raise InternalServerError(
            description="Error deleting candidate. Please try again later."
        ) from e
