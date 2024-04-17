# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import datetime
import typing

from sqlalchemy import INTEGER, JSON, REAL, TEXT, TIMESTAMP, Column, Index
from sqlalchemy.orm import Mapped, declarative_base

from promptflow._sdk._constants import EVENT_TABLENAME, LINE_RUN_TABLENAME, SPAN_TABLENAME, TRACE_LIST_DEFAULT_LIMIT
from promptflow._sdk._errors import LineRunNotFoundError

from .retry import sqlite_retry
from .session import trace_mgmt_db_session


class EventIndexName:
    TRACE_ID_SPAN_ID = "idx_events_trace_id_span_id"


class SpanIndexName:
    TRACE_ID = "idx_spans_trace_id"
    TRACE_ID_SPAN_ID = "idx_spans_trace_id_span_id"


class LineRunIndexName:
    RUN_LINE_NUMBER = "idx_line_runs_run_line_number"  # query parent line run
    PARENT_ID = "idx_line_runs_parent_id"
    COLLECTION = "idx_line_runs_collection"
    RUN = "idx_line_runs_run"
    EXPERIMENT = "idx_line_runs_experiment"
    TRACE_ID = "idx_line_runs_trace_id"
    SESSION_ID = "idx_line_runs_session_id"


Base = declarative_base()


class Event(Base):
    __tablename__ = EVENT_TABLENAME

    event_id: Mapped[str] = Column(TEXT, primary_key=True)
    trace_id: Mapped[str] = Column(TEXT)
    span_id: Mapped[str] = Column(TEXT)
    data: Mapped[str] = Column(TEXT)

    __table_args__ = (Index(EventIndexName.TRACE_ID_SPAN_ID, "trace_id", "span_id"),)

    @sqlite_retry
    def persist(self) -> None:
        with trace_mgmt_db_session() as session:
            session.add(self)
            session.commit()

    @staticmethod
    @sqlite_retry
    def get(event_id: str) -> "Event":
        with trace_mgmt_db_session() as session:
            event = session.query(Event).filter(Event.event_id == event_id).first()
            # TODO: validate event is None
            return event

    @staticmethod
    @sqlite_retry
    def list(trace_id: str, span_id: str) -> typing.List["Event"]:
        with trace_mgmt_db_session() as session:
            events = session.query(Event).filter(Event.trace_id == trace_id, Event.span_id == span_id).all()
            return events


class Span(Base):
    __tablename__ = SPAN_TABLENAME

    trace_id: Mapped[str] = Column(TEXT)
    span_id: Mapped[str] = Column(TEXT, primary_key=True)
    name: Mapped[str] = Column(TEXT)
    context: Mapped[typing.Dict] = Column(JSON)
    kind: Mapped[str] = Column(TEXT)
    parent_id: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    start_time: Mapped[datetime.datetime] = Column(TIMESTAMP)
    end_time: Mapped[datetime.datetime] = Column(TIMESTAMP)
    status: Mapped[typing.Dict] = Column(JSON)
    attributes: Mapped[typing.Optional[typing.Dict]] = Column(JSON, nullable=True)
    links: Mapped[typing.Optional[typing.List]] = Column(JSON, nullable=True)
    events: Mapped[typing.Optional[typing.List]] = Column(JSON, nullable=True)
    resource: Mapped[typing.Dict] = Column(JSON)

    __table_args__ = (
        Index(SpanIndexName.TRACE_ID, "trace_id"),
        Index(SpanIndexName.TRACE_ID_SPAN_ID, "trace_id", "span_id"),
    )

    @sqlite_retry
    def persist(self) -> None:
        with trace_mgmt_db_session() as session:
            session.add(self)
            session.commit()

    @staticmethod
    @sqlite_retry
    def get(span_id: str, trace_id: typing.Optional[str] = None) -> "Span":
        with trace_mgmt_db_session() as session:
            query = session.query(Span)
            if trace_id is not None:
                query = query.filter(Span.trace_id == trace_id, Span.span_id == span_id)
            else:
                query = query.filter(Span.span_id == span_id)
            span = query.first()
            # TODO: validate span is None
            return span

    @staticmethod
    @sqlite_retry
    def list(trace_ids: typing.Union[str, typing.List[str]]) -> typing.List["Span"]:
        if isinstance(trace_ids, str):
            trace_ids = [trace_ids]
        with trace_mgmt_db_session() as session:
            spans = session.query(Span).filter(Span.trace_id.in_(trace_ids)).all()
            return spans


class LineRun(Base):
    __tablename__ = LINE_RUN_TABLENAME

    line_run_id: Mapped[str] = Column(TEXT, primary_key=True)
    trace_id: Mapped[str] = Column(TEXT)
    root_span_id: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    inputs: Mapped[typing.Optional[typing.Dict]] = Column(JSON, nullable=True)
    outputs: Mapped[typing.Optional[typing.Dict]] = Column(JSON, nullable=True)
    start_time: Mapped[datetime.datetime] = Column(TIMESTAMP)
    end_time: Mapped[typing.Optional[datetime.datetime]] = Column(TIMESTAMP, nullable=True)
    status: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    duration: Mapped[typing.Optional[float]] = Column(REAL, nullable=True)
    name: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    kind: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    cumulative_token_count: Mapped[typing.Optional[typing.Dict]] = Column(JSON, nullable=True)
    parent_id: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    run: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    line_number: Mapped[typing.Optional[int]] = Column(INTEGER, nullable=True)
    experiment: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    session_id: Mapped[typing.Optional[str]] = Column(TEXT, nullable=True)
    collection: Mapped[str] = Column(TEXT)

    __table_args__ = (
        Index(LineRunIndexName.RUN_LINE_NUMBER, "run", "line_number"),
        Index(LineRunIndexName.PARENT_ID, "parent_id"),
        Index(LineRunIndexName.COLLECTION, "collection"),
        Index(LineRunIndexName.RUN, "run"),
        Index(LineRunIndexName.EXPERIMENT, "experiment"),
        Index(LineRunIndexName.TRACE_ID, "trace_id"),
        Index(LineRunIndexName.SESSION_ID, "session_id"),
    )

    @sqlite_retry
    def persist(self) -> None:
        with trace_mgmt_db_session() as session:
            session.add(self)
            session.commit()

    @staticmethod
    @sqlite_retry
    def get(line_run_id: str) -> "LineRun":
        with trace_mgmt_db_session() as session:
            line_run = session.query(LineRun).filter(LineRun.line_run_id == line_run_id).first()
            if line_run is None:
                raise LineRunNotFoundError(f"Line run {line_run_id!r} cannot found.")
            return line_run

    @staticmethod
    @sqlite_retry
    def _get_with_run_and_line_number(run: str, line_number: int) -> typing.Optional["LineRun"]:
        # this function is currently exclusively used to query parent line run
        with trace_mgmt_db_session() as session:
            line_run = (
                session.query(LineRun)
                .filter(
                    LineRun.run == run,
                    LineRun.line_number == line_number,
                )
                .first()
            )
            return line_run

    @staticmethod
    @sqlite_retry
    def list(
        collection: typing.Optional[str] = None,
        runs: typing.Optional[typing.List[str]] = None,
        experiments: typing.Optional[typing.List[str]] = None,
        trace_ids: typing.Optional[typing.List[str]] = None,
    ) -> typing.List["LineRun"]:
        with trace_mgmt_db_session() as session:
            query = session.query(LineRun)
            if collection is not None:
                query = query.filter(LineRun.collection == collection)
            elif runs is not None:
                query = query.filter(LineRun.run.in_(runs))
            elif experiments is not None:
                query = query.filter(LineRun.experiment.in_(experiments))
            elif trace_ids is not None:
                query = query.filter(LineRun.trace_id.in_(trace_ids))
            query = query.order_by(LineRun.start_time.desc())
            if collection is not None:
                query = query.limit(TRACE_LIST_DEFAULT_LIMIT)
            return query.all()

    @sqlite_retry
    def _update(self) -> None:
        update_dict = {
            "root_span_id": self.root_span_id,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "end_time": self.end_time,
            "status": self.status,
            "duration": self.duration,
            "name": self.name,
            "kind": self.kind,
            "cumulative_token_count": self.cumulative_token_count,
        }
        with trace_mgmt_db_session() as session:
            session.query(LineRun).filter(LineRun.line_run_id == self.line_run_id).update(update_dict)
            session.commit()

    @staticmethod
    @sqlite_retry
    def _get_children(line_run_id: str) -> typing.List["LineRun"]:
        with trace_mgmt_db_session() as session:
            line_runs = session.query(LineRun).filter(LineRun.parent_id == line_run_id).all()
            return line_runs
