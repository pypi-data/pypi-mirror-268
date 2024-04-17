"""
A python implementation of the JsonCanvas format: https://github.com/obsidianmd/jsoncanvas/blob/main/spec/1.0.md
It allows you to read and write JsonCanvas files in Python, as well as create them from scratch.
"""
import collections.abc
from functools import partialmethod, singledispatchmethod
from itertools import chain
from uuid import uuid4

from pydantic import BaseModel, Field
from typing import Any, Iterator, Literal, Optional, Type

__version__: str = '3.0.0'
__spec_version__: str = '1.0'


class CanvasData(BaseModel, collections.abc.MutableMapping):
    """Base class for all canvas data classes."""

    def __len__(self) -> int:
        return len(self.__dict__)

    def __contains__(self, key: str) -> bool:
        return key in self.__dict__

    def __iter__(self) -> Iterator[str]:
        return iter(self.__dict__)

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        delattr(self, key)

    class Config:
        validate_assignment = True
        validate_default = True
        extra = 'allow'


class Node(CanvasData):
    """Base class for all node classes."""

    id: str
    type: str
    x: int
    y: int
    width: int = 100
    height: int = 50
    color: Optional[str] = None


class TextNode(Node):
    """A node that contains text."""

    text: str
    type: str = 'text'


class FileNode(Node):
    """A node that contains a file."""

    file: str
    type: str = 'file'
    subpath: Optional[str] = None


class LinkNode(Node):
    """A node that contains a link."""
    url: str
    type: str = 'link'


class GroupNode(Node):
    """A node that contains other nodes."""

    type: str = 'group'
    label: Optional[str] = None
    background: Optional[str] = None
    backgroundStyle: Optional[str] = None


class Edge(CanvasData):
    """An edge between two nodes."""

    id: str
    fromNode: str
    toNode: str
    fromSide: Optional[Literal['top', 'right', 'bottom', 'left']] = None
    toSide: Optional[Literal['top', 'right', 'bottom', 'left']] = None
    fromEnd: Optional[Literal['none', 'arrow']] = None
    toEnd: Optional[Literal['none', 'arrow']] = None
    color: Optional[str] = None
    label: Optional[str] = None

class Canvas(BaseModel):
    
    """
    The main class that represents a canvas.
    This class stores the nodes and edges of the canvas, and handles the logics for adding, deleting,
    updating, and creating nodes and edges.
    """

    @staticmethod
    def _generate_next_id_(prefix: str = "") -> str:
        return f'{prefix}{uuid4().hex}'

    @singledispatchmethod
    def __contains__(self, item: CanvasData):
        raise TypeError(f'Unsupported type: {type(item)}')

    @__contains__.register(Node)
    def contains_node(self, item: Node):
        return item in self.nodes

    @__contains__.register(Edge)
    def contains_edges(self, item: Edge):
        return item in self.edges

    @__contains__.register(str)
    def contains_id(self, item: str):
        return any(node.id == item for node in chain(self.nodes, self.edges))

    ### core

    def __add(self, *objs: CanvasData, __prop: str):
        getattr(self, __prop).extend(objs)
        return self

    def __create(self, *, __type: Type[CanvasData] | str, __prop: str, **kwargs):
        if isinstance(__type, str):
            if not (__type := self.__class_getitem__(__type)):
                raise ValueError(f'Could not find class with name: {__type}')
        if 'id' not in kwargs:
            kwargs['id'] = self._generate_next_id_(__prop)
        self.__add(__type(**kwargs), _Canvas__prop = __prop)  # type: ignore
        return self

    def __get(self, __id: str) -> Node | Edge | None:
        for node in chain(self.nodes, self.edges):
            if node.id == __id:
                return node
        return None

    def __update(self, obj: CanvasData, **kwargs):
        for key, value in kwargs.items():
            setattr(obj, key, value)
        return self

    def __delete(self, *objs: CanvasData, __prop: str):
        setattr(self, __prop, [item for item in getattr(self, __prop) if item.id not in {obj.id for obj in objs}])
        if __prop != 'edges':
            ids = {obj.id for obj in objs}
            self.edges = [edge for edge in self.edges if edge.fromNode not in ids and edge.toNode not in ids]
        return self

    ### User Functions

    @singledispatchmethod
    def links(self, obj) -> tuple[Edge | Node]:
        raise TypeError(f'Unsupported type: {type(obj)}')

    @links.register(Node)
    def _(self, obj: Node) -> tuple[Edge]:
        return [edge for edge in self.edges if edge.fromNode == obj.id or edge.toNode == obj.id]

    @links.register(Edge)
    def _(self, obj: Edge) -> tuple[Node]:
        return [node for node in self.nodes if node.id in {obj.fromNode, obj.toNode}]

    def clear_canvas(self):
        self.nodes.clear()
        self.edges.clear()
        return self

    # IO functions

    def to_file(self, path: str):
        with open(path, 'w') as f:
            f.write(self.model_dump_json())
            
    def to_dict(self) -> dict:
        return self.dict()

    def to_json(self) -> str:
        return self.json()

    @classmethod
    def from_file(cls, path: str):
        return cls.parse_file(path)

    @classmethod
    def from_dict(cls, data: dict):
        return cls.parse_obj(data)

    @classmethod
    def from_json(cls, data: str):
        return cls.parse_raw(data)

    # Attrs

    nodes: list[Node] = Field(default_factory = list)
    edges: list[Edge] = Field(default_factory = list)

    # Partial functions

    add_nodes = partialmethod(__add, _Canvas__prop = 'nodes')
    add_edges = partialmethod(__add, _Canvas__prop = 'edges')

    create_text_node = partialmethod(__create, _Canvas__type = "TextNode", _Canvas__prop = 'nodes')
    create_file_node = partialmethod(__create, _Canvas__type = "FileNode", _Canvas__prop = 'nodes')
    create_link_node = partialmethod(__create, _Canvas__type = "LinkNode", _Canvas__prop = 'nodes')
    create_group_node = partialmethod(__create, _Canvas__type = "GroupNode", _Canvas__prop = 'nodes')

    create_edge = partialmethod(__create, _Canvas__type = "Edge", _Canvas__prop = 'edges')

    get_node = partialmethod(__get, __prop = 'nodes')
    get_edge = partialmethod(__get, __prop = 'edges')

    update_node = partialmethod(__update, _Canvas__prop = 'nodes')
    update_edge = partialmethod(__update, _Canvas__prop = 'edges')

    delete_nodes = partialmethod(__delete, _Canvas__prop = 'nodes')
    delete_edges = partialmethod(__delete, _Canvas__prop = 'edges')

    def link_nodes(self, fromNode: Node | str, toNode: Node | str, **kwargs):
        match fromNode, toNode:
            case Node(), Node():
                self.create_edge(fromNode = fromNode.id, toNode = toNode.id, **kwargs)
            case str(), str():
                self.link_nodes(self.get_node(fromNode), self.get_node(toNode), **kwargs)
            case Node(), str():
                self.link_nodes(fromNode, self.get_node(toNode), **kwargs)
            case str(), Node():
                self.link_nodes(self.get_node(fromNode), toNode, **kwargs)
        return self
            
    # Pydantic Config

    class Config:
        validate_assignment = True
        validate_default = True
        extra = 'allow'

