"""empty message

Revision ID: 97f2af981001
Revises: 775f5f4d7a5c
Create Date: 2022-04-21 23:17:32.205667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f2af981001'
down_revision = '775f5f4d7a5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
