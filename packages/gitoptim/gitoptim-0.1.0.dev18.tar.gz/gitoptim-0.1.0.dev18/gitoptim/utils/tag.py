import uuid
from abc import ABC, abstractmethod
from typing import ClassVar, Optional


class Tag(ABC):
    @classmethod
    def generate_regex_pattern(cls, **kwargs):
        return f"<GITOPTIM (?:{cls._generate_regex_pattern(**kwargs)})>"

    @classmethod
    def _generate_regex_pattern(cls, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def _generate_tag_content(self):
        pass

    def __str__(self):
        return f"<GITOPTIM {self._generate_tag_content()}>"

    def __repr__(self):
        return str(self)


class StartTag(Tag):
    tag_id: str

    def __init__(self, tag_id):
        super().__init__()
        self.tag_id = tag_id

    @classmethod
    def _generate_regex_pattern(cls, name: Optional[str] = None, **kwargs):
        return "START " + (name if name is not None else r"[\w-]+")

    def _generate_tag_content(self):
        return f"START {self.tag_id}"


class EndTag(Tag):
    tag_id: str

    def __init__(self, tag_id):
        super().__init__()
        self.tag_id = tag_id

    @classmethod
    def _generate_regex_pattern(cls, name: Optional[str] = None, **kwargs):
        return "END " + (name if name is not None else r"[\w-]+")

    def _generate_tag_content(self):
        return f"END {self.tag_id}"


class TagFactory:
    execution_id: ClassVar[str] = str(uuid.uuid4())

    @staticmethod
    def create_start_tag(tag_id: Optional[str] = None):
        return StartTag(tag_id or TagFactory.execution_id)

    @staticmethod
    def create_end_tag(tag_id: Optional[str] = None):
        return EndTag(tag_id or TagFactory.execution_id)
