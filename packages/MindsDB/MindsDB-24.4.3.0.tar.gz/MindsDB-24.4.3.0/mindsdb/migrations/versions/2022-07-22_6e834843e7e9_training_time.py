"""training_time

Revision ID: 6e834843e7e9
Revises: b5b53e0ea7f8
Create Date: 2022-07-22 13:32:34.796604

"""
from alembic import op
import sqlalchemy as sa
import mindsdb.interfaces.storage.db    # noqa


# revision identifiers, used by Alembic.
revision = '6e834843e7e9'
down_revision = 'b5b53e0ea7f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('predictor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('training_start_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('training_stop_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('predictor', schema=None) as batch_op:
        batch_op.drop_column('training_stop_at')
        batch_op.drop_column('training_start_at')
    # ### end Alembic commands ###
