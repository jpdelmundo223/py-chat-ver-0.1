"""Initial migration.

Revision ID: 079e5e1cb2a7
Revises: 
Create Date: 2022-03-19 21:34:43.598545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079e5e1cb2a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('username', sa.String(length=20)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'username')
    # ### end Alembic commands ###
