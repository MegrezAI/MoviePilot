"""2.0.5

Revision ID: ecf3c693fdf3
Revises: a73f2dbf5c09
Create Date: 2024-10-21 12:36:20.631963

"""
import contextlib

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecf3c693fdf3'
down_revision = 'a73f2dbf5c09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # 将String转换为JSON类型
    with contextlib.suppress(Exception):
        op.alter_column('subscribehistory', 'sites', existing_type=sa.String(), type_=sa.JSON())
    with contextlib.suppress(Exception):
        op.add_column('subscribehistory', sa.Column('custom_words', sa.String(), nullable=True))
        op.add_column('subscribehistory', sa.Column('media_category', sa.String(), nullable=True))
        op.add_column('subscribehistory', sa.Column('filter_groups', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    pass