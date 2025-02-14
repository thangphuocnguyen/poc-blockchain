"""empty message

Revision ID: 9c88482f995a
Revises: 
Create Date: 2018-09-10 20:54:04.174665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c88482f995a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('addr', sa.String(), nullable=False),
    sa.Column('pubkey', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('review', sa.Text(), nullable=False),
    sa.Column('sig', sa.String(), nullable=False),
    sa.Column('pointer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sproviders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(), nullable=False),
    sa.Column('pubkey', sa.Text(), nullable=False),
    sa.Column('privkey', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer_transactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('trans_identifier', sa.String(), nullable=False),
    sa.Column('pubkey', sa.Text(), nullable=False),
    sa.Column('privkey', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.Column('sprovider_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sprovider_id'], ['sproviders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('customer_transactions')
    op.drop_table('sproviders')
    op.drop_table('reviews')
    op.drop_table('customers')
    # ### end Alembic commands ###
