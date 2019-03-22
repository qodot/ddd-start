"""add table order

Revision ID: 558b3242ab0d
Revises: 
Create Date: 2019-03-22 16:19:50.468933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '558b3242ab0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('orderer_id', sa.String(), nullable=False),
    sa.Column('shipping_zipcode', sa.String(), nullable=True),
    sa.Column('shipping_address1', sa.String(), nullable=True),
    sa.Column('shipping_address2', sa.String(), nullable=True),
    sa.Column('receiver_name', sa.String(), nullable=True),
    sa.Column('receiver_phone', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###