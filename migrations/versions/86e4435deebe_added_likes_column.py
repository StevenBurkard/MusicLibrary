"""Added likes column

Revision ID: 86e4435deebe
Revises: 348bdf59baa6
Create Date: 2023-06-22 10:43:49.988471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86e4435deebe'
down_revision = '348bdf59baa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.drop_column('likes')

    # ### end Alembic commands ###
