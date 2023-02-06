"""insert categories

Revision ID: 3239cdd1764d
Revises: 17138dc82aa1
Create Date: 2023-02-06 11:42:56.285556

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

from utils.models import Category


# revision identifiers, used by Alembic.
revision = '3239cdd1764d'
down_revision = '17138dc82aa1'
branch_labels = None
depends_on = None


categories = {
    'боевик': 94,
    'детектив': 97,
    'комедия': 95
}


def upgrade() -> None:
    with Category.Session_() as session:
        for name, _id in categories.items():
            category = Category(id=_id, name=name)
            session.add(category)
            try:
                session.commit()
            except IntegrityError:
                pass


def downgrade() -> None:
    with Category.Session_() as session:
        for _id in categories.values():
            session.delete(Category, _id)
            session.commit()
