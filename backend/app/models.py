from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
    Date, Boolean, UniqueConstraint, TIMESTAMP
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    task_members = relationship('TaskMember', back_populates='user', cascade='all, delete-orphan')
    project_members = relationship('ProjectMember', back_populates='user', cascade='all, delete-orphan')
    assigned_tasks = relationship('Task', back_populates='assigned_user', foreign_keys='Task.assigned_to')


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    tasks = relationship('Task', back_populates='project', cascade='all, delete-orphan')
    members = relationship('ProjectMember', back_populates='project', cascade='all, delete-orphan')
    task_members = relationship('TaskMember', back_populates='project', cascade='all, delete-orphan')


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(Text)
    status = Column(String(50), default='pendiente')
    due_date = Column(Date)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'))
    assigned_to = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    completed = Column(Integer, default=0)

    project = relationship('Project', back_populates='tasks')
    assigned_user = relationship('User', back_populates='assigned_tasks', foreign_keys=[assigned_to])
    task_members = relationship('TaskMember', back_populates='task', cascade='all, delete-orphan')


class TaskMember(Base):
    __tablename__ = 'task_members'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'))
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'))

    user = relationship('User', back_populates='task_members')
    project = relationship('Project', back_populates='task_members')
    task = relationship('Task', back_populates='task_members')

    __table_args__ = (
        UniqueConstraint('user_id', 'task_id', name='unique_user_task'),
    )


class ProjectMember(Base):
    __tablename__ = 'project_members'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    project = relationship('Project', back_populates='members')
    user = relationship('User', back_populates='project_members')

    __table_args__ = (
        UniqueConstraint('project_id', 'user_id', name='unique_project_member'),
    )
