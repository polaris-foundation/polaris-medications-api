"""empty message

Revision ID: 36118e617124
Revises: 7d351725116f
Create Date: 2018-01-08 17:27:32.382049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36118e617124'
down_revision = '7d351725116f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
                    sa.Column('uuid', sa.String(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('tag', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('uuid'),
                    sa.UniqueConstraint('tag')
                    )
    op.create_table('relationship_table',
                    sa.Column('medication_id', sa.String(), nullable=False),
                    sa.Column('tag_id', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['medication_id'], ['medication.uuid'], ),
                    sa.ForeignKeyConstraint(['tag_id'], ['tag.uuid'], ),
                    sa.PrimaryKeyConstraint('medication_id', 'tag_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relationship_table')
    op.drop_table('tag')
    # ### end Alembic commands ###
