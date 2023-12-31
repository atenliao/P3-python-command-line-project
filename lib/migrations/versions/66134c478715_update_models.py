"""update models

Revision ID: 66134c478715
Revises: 
Create Date: 2023-09-08 21:42:05.302826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66134c478715'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=5), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('worker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lastname', sa.String(length=255), nullable=False),
    sa.Column('firstname', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=40), nullable=False),
    sa.Column('shift', sa.String(length=255), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('Employee_ID', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Employee_ID')
    )
    op.create_table('workerrole',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workers_id', sa.Integer(), nullable=True),
    sa.Column('roles_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roles_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['workers_id'], ['worker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workerrole')
    op.drop_table('worker')
    op.drop_table('role')
    op.drop_table('department')
    # ### end Alembic commands ###
