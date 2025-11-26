from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import datetime
import uuid

# revision identifiers, used by Alembic.
revision = 'dcd08df85579'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create members table
    op.create_table(
        'members',
        sa.Column('member_id', postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

    # Create books table
    op.create_table(
        'books',
        sa.Column('book_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('author', sa.String(), nullable=False),
        sa.Column('is_borrowed', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('borrowed_date', sa.DateTime(), nullable=True),
        sa.Column('borrowed_by', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.text('now()'))
    )


def downgrade() -> None:
    op.drop_table('books')
    op.drop_table('members')
