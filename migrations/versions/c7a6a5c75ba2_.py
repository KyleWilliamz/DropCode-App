"""empty message

Revision ID: c7a6a5c75ba2
Revises: 2e44f6bda974
Create Date: 2019-04-25 16:22:11.082859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a6a5c75ba2'
down_revision = '2e44f6bda974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('output', sa.String(length=1000), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('locations')
    op.add_column('user', sa.Column('rank', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'rank')
    op.create_table('locations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('cityName', sa.VARCHAR(length=64), nullable=False),
    sa.Column('country', sa.VARCHAR(length=64), nullable=False),
    sa.Column('time', sa.VARCHAR(length=64), nullable=False),
    sa.Column('phone', sa.VARCHAR(length=32), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('levels')
    # ### end Alembic commands ###
