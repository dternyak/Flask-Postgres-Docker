"""empty message

Revision ID: 3b0521515ca
Revises: 214cd9dc6bf
Create Date: 2016-01-25 08:48:17.997965

"""

# revision identifiers, used by Alembic.
revision = '3b0521515ca'
down_revision = '214cd9dc6bf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('something', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'something')
    ### end Alembic commands ###
