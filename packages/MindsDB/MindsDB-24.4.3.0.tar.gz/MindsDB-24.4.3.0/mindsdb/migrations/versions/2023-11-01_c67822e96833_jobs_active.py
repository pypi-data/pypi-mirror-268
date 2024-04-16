"""jobs_active

Revision ID: c67822e96833
Revises: 309db3d07cf4
Create Date: 2023-11-01 15:42:53.249859

"""
from alembic import op
import sqlalchemy as sa
import mindsdb.interfaces.storage.db # noqa

# revision identifiers, used by Alembic.
revision = 'c67822e96833'
down_revision = '309db3d07cf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###
