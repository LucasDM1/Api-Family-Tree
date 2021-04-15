"""empty message

Revision ID: 8c2a61fe26c9
Revises: 762402052503
Create Date: 2021-04-15 02:23:34.071130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8c2a61fe26c9'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_name', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=120), nullable=False))
    op.drop_index('email', table_name='user')
    op.drop_column('user', 'email')
    op.drop_column('user', 'password')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_column('user', 'name')
    op.drop_column('user', 'last_name')
    # ### end Alembic commands ###