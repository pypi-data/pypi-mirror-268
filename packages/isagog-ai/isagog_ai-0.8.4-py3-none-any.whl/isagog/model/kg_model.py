"""
    A model for Knowledge Graph entities and relations
    (c) Isagog S.r.l. 2024, MIT License
"""
import logging
from typing import IO, TextIO, Any

from rdflib import OWL, Graph, RDF, URIRef, RDFS

# Type definitions

Reference = URIRef | str

OWL_ENTITY_TYPES = [OWL.Class, OWL.NamedIndividual, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty]

PROFILE_ATTRIBUTE = "https://isagog.com/ontology#profile"


def _uri_label(uri: str) -> str:
    """
    Extracts a label from a URI
    :param uri:
    :return:
    """
    if "#" in uri:
        return uri.split("#")[-1]
    elif "/" in uri:
        return uri.split("/")[-1]
    else:
        return uri


def _todict(obj, classkey=None):
    """
     Recursive object to dict converter
    """
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = _todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return _todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [_todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, _todict(value, classkey))
                     for key, value in obj.__dict__.items()
                     if not callable(value) and not key.startswith('_')])
        if not data:
            return str(obj)
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


class Entity(object):
    """
    Any identified knowledge entity, either predicative (property) or individual
    Every entity has a string identifier and an optional meta type, which can be an OWL type
    """

    def __init__(self, _id: Reference, **kwargs):
        """

        :param _id: the entity identifier, will be converted to a string
        :param kwargs:
        """
        assert _id
        self.id = str(_id).strip("<>")
        owl_type = kwargs.get('owl')
        if owl_type:
            if owl_type in OWL_ENTITY_TYPES:
                self.__meta__ = owl_type
            else:
                logging.warning("bad owl type %s", owl_type)
        else:
            self.__meta__ = kwargs.get('meta', None)

    def __eq__(self, other):
        return (
                (isinstance(other, Entity) and self.id == other.id)
                or (isinstance(other, URIRef) and self.id == str(other).strip("<>"))
                or (isinstance(other, str) and str(self.id) == other)
        )

    def __hash__(self):
        return self.id.__hash__()

    def to_dict(self) -> dict:
        return _todict(self)


class Concept(Entity):
    """
    Unary predicate
    """

    def __init__(self, _id: Reference, **kwargs):
        """

        :param _id: the concept identifier
        :param kwargs:
        """
        super().__init__(_id, owl=OWL.Class, **kwargs)
        self.comment = kwargs.get('comment', "")
        self.ontology = kwargs.get('ontology', "")
        self.parents = kwargs.get('parents', [OWL.Thing])


class Attribute(Entity):
    """
    Class of assertions ranging on concrete domains
    owl:DatatypeProperties
    """

    def __init__(self,
                 _id: Reference,
                 domain: Reference = None,
                 parents: list[Reference] = None,
                 **kwargs):
        """

        :param _id:
        :param kwargs: domain
        """

        super().__init__(_id, owl=OWL.DatatypeProperty)
        self.domain = domain if domain else OWL.Thing
        self.parents = parents if parents else [OWL.topDataProperty]
        if 'type' in kwargs:
            self.__type__ = kwargs.get('type')


class Relation(Entity):
    """
    Class of assertions ranging on individuals
    owl:ObjectProperty
    """

    def __init__(
            self,
            _id: Reference,
            domain: Reference = None,
            range: Reference = None,
            inverse: Reference = None,
            parents: list[Reference] = None,
            **kwargs
    ):
        """
        :param _id:
        :param kwargs: inverse, domain, range, label
        """

        super().__init__(_id, owl=OWL.ObjectProperty)
        self.inverse = inverse if inverse else None
        self.domain = domain if domain else OWL.Thing
        self.range = range if range else OWL.Thing
        self.label = kwargs.get('label', _uri_label(_id))
        self.parents = parents if parents else OWL.topObjectProperty


class Assertion(object):
    """
    Assertion axiom of the form: property(subject, values)
    """

    def __init__(self,
                 predicate: Reference = None,
                 subject: Reference = None,
                 values: list = None,
                 **kwargs):
        """

        :param predicate:
        :param subject:
        :param values:
        """
        if predicate is None:
            # try to get the predicate from aliases in kwargs, if not present raise an error
            predicate = kwargs.get('property', kwargs.get('id', None))
            if predicate is None:
                raise ValueError("missing predicate")

        self.predicate = str(predicate).strip("<>")
        self.subject = str(subject).strip("<>") if subject else None
        self.values = list(values) if values else list()

    def to_dict(self) -> dict:
        return _todict(self)

    def is_empty(self) -> bool:
        return not self.values


class Ontology(Graph):
    """
    In-memory, read-only RDF representation of an ontology.
    Manages basic reasoning on declared inclusion dependencies (RDFS.subClassOf).
    Also, it manages classes annotated as 'category' in the ontology. Categories
    are 'rigid' concepts,
    i.e. they (should) hold for an individual in every 'possible world'.
    Categories should be (a) disjoint from their siblings, (b) maximal, i.e.
    for any category,
    no super-categories allowed.
    """

    def __init__(
            self,
            source: IO[bytes] | TextIO | str,
            publicIRI: str,
            source_format="turtle"
    ):
        """
        :param source:  Path to the ontology source file.
        :param publicIRI:  Base IRI for the ontology.
        :param source_format:  Format of the ontology.

        """
        Graph.__init__(self, identifier=publicIRI)
        self.parse(source=source, publicID=publicIRI, format=source_format)

        self.concepts = [
            Concept(cls)
            for cls in self.subjects(predicate=RDF.type, object=OWL.Class)
            if isinstance(cls, URIRef)
        ]
        self.relations = [
            Relation(rl)
            for rl in self.subjects(
                predicate=RDF.type, object=OWL.ObjectProperty
            )
            if isinstance(rl, URIRef)
        ]
        self.attributes = [
            Attribute(att)
            for att in self.subjects(
                predicate=RDF.type, object=OWL.DatatypeProperty
            )
            if isinstance(att, URIRef)
        ]
        for ann in self.subjects(
                predicate=RDF.type, object=OWL.AnnotationProperty
        ):
            if isinstance(ann, URIRef):
                self.attributes.append(Attribute(ann))

        self._submap = dict[Concept, list[Concept]]()

    def subclasses(self, sup: Concept) -> list[Concept]:
        """
        Gets direct subclasses of a given concept
        """
        if sup not in self._submap:
            self._submap[sup] = [
                Concept(sc)
                for sc in self.subjects(RDFS.subClassOf, sup.id)
                if isinstance(sc, URIRef)
            ]
        return self._submap[sup]

    def is_subclass(self, sub: Concept, sup: Concept) -> bool:
        """
        Tells if a given concept implies another given concept (i.e. is a subclass)
        :param sub:  Subconcept
        :param sup:  Superconcept
        """

        if sub == sup:
            return True
        subcls = self.subclasses(sup)
        found = False
        while not found:
            if sub in subcls:
                found = True
            else:
                for _sc in subcls:
                    if self.is_subclass(sub, _sc):
                        found = True
                        break
                break
        return found


class AttributeInstance(Assertion):
    """
    Attributive assertion
    """

    def __init__(self,
                 predicate: Reference = None,
                 subject: Reference = None,
                 values: list[str | int | float | bool] = None,
                 **kwargs):
        """
        :param subject: the asserted subject
        :param predicate: the asserted property
        :param values: the asserted values, they can be strings, integers, floats or booleans
        :param kwargs:
        """
        self.value_type = kwargs.get('type')
        if values:
            specimen = values[0]
            if isinstance(specimen, str):
                if self.value_type:
                    if self.value_type == "string":
                        pass
                    else:
                        raise ValueError("bad values for string attribute")
                else:
                    self.value_type = "string"

            elif isinstance(specimen, int):
                if self.value_type:
                    if self.value_type == "int":
                        pass
                    else:
                        raise ValueError("bad values for int attribute")
                else:
                    self.value_type = "int"
                raise ValueError("bad values for int attribute")

            elif isinstance(specimen, float):
                if self.value_type:
                    if self.value_type == "float":
                        pass
                    else:
                        raise ValueError("bad values for float attribute")
                else:
                    self.value_type = "float"

            elif isinstance(specimen, bool):
                if self.value_type:
                    if self.value_type == "bool":
                        pass
                    else:
                        raise ValueError("bad values for bool attribute")
                else:
                    self.value_type = "bool"
            else:
                raise ValueError("bad values for attribute")
        super().__init__(predicate=predicate,
                         subject=subject,
                         values=values,
                         **kwargs)

    def all_values_as_string(self) -> str:
        match len(self.values):
            case 0:
                return ""
            case 1:
                return str(self.values[0])
            case _:
                return "\n".join([str(v) for v in self.values])

    def all_values(self) -> list:
        return self.values

    def first_value(self, default=None) -> str | int | float | bool | None:
        if len(self.values) > 0:
            return self.values[0]
        else:
            return default


VOID_ATTRIBUTE = AttributeInstance(predicate='https://isagog.com/attribute#void')


class RelationInstance(Assertion):
    """
    Relational assertion
    """

    def __init__(self, predicate: Reference = None,
                 subject: Reference = None,
                 values: list[Any | Reference | dict] = None,
                 **kwargs):
        """

        :param property: the asserted property
        :param subject: the assertion's subject
        :param values: the asserted values, they can be individuals, references or dictionaries
        :param kwargs:
        """
        if values:
            specimen = values[0]
            if isinstance(specimen, (Individual, Reference)):
                # values are acceptable
                pass
            elif isinstance(specimen, dict):
                # if values are dictionaries, then convert them to Individuals
                inst_values = [Individual(_id=r_data.get('id'), **r_data) for r_data in values]
                values = inst_values
            else:
                raise ValueError("bad values for relational assertion")
        super().__init__(predicate=predicate,
                         subject=subject,
                         values=values,
                         **kwargs)

    def all_values(self, only_id=True) -> list:
        """
        Returns all values of the relation instance
        :param only_id:
        :return:
        """
        if only_id:
            return [ind.id for ind in self.values]
        else:
            return self.values

    def first_value(self, only_id=True, default=None) -> Any | None:
        if len(self.values) > 0:
            if only_id:
                return self.values[0].id
            else:
                return self.values[0]
        else:
            return default

    def kind_map(self) -> dict:
        """
        Returns a map of individuals by kind
        :return: a map of kind : individuals
        """
        kind_map = {}
        for individual in self.values:
            for kind in individual.kind:
                if kind not in kind_map:
                    kind_map[kind] = []
                kind_map[kind].append(individual)
        return kind_map


VOID_RELATION = RelationInstance(predicate='https://isagog.com/relation#void')


class Individual(Entity):
    """
    Individual entity

    """

    def __init__(self, _id: Reference,
                 attributes: list[AttributeInstance | dict] = None,
                 relations: list[RelationInstance | dict] = None,
                 **kwargs):
        """

        :param _id: the individual identifier
        :param attributes: the individual attributes
        :param relations: the individual relations
        :param kwargs:
        """
        super().__init__(_id, owl=OWL.NamedIndividual, **kwargs)
        self.attributes = list()
        self.relations = list()
        if attributes:
            for attribute in attributes:
                if isinstance(attribute, dict):
                    attribute = AttributeInstance(**attribute)
                self.add_attribute(instance=attribute)

        if relations:
            for relation in relations:
                if isinstance(relation, dict):
                    relation = RelationInstance(**relation)
                self.add_relation(instance=relation)
        if 'score' in kwargs:
            self.score = float(kwargs.get('score'))
        if self.has_attribute(PROFILE_ATTRIBUTE):
            self.profile = {
                profile_value.split("=")[0]: int(profile_value.split("=")[1])
                for profile_value in self.get_attribute(PROFILE_ATTRIBUTE).values
            }
        else:
            self.profile = {}
        self._refresh = True

    def has_attribute(self, attribute_id: Reference) -> bool:
        """
        Checks if the individual has a given ontology defined attribute
        :param attribute_id:
        :return:
        """
        found = next(filter(lambda x: x.predicate == attribute_id, self.attributes), None)
        return found and not found.is_empty()

    def get_attribute(self, attribute_id: Reference) -> AttributeInstance | None:
        """
        Gets the ontology defined attribute instance of the individual
        :param attribute_id:
        :return:
        """
        found = next(filter(lambda x: x.predicate == attribute_id, self.attributes), None)
        if found and not found.is_empty():
            return found
        else:
            return VOID_ATTRIBUTE

    def has_relation(self, relation_id: Reference) -> bool:
        """
        Checks if the individual has a given ontology defined relation
        :param relation_id:
        :return:
        """
        found = next(filter(lambda x: x.predicate == relation_id, self.relations), None)
        return found and not found.is_empty()

    def get_relation(self, relation_id: Reference) -> RelationInstance | None:
        """
        Gets the ontology defined relation instance of the individual
        :param relation_id:
        :return:
        """
        found = next(filter(lambda x: x.predicate == relation_id, self.relations), None)
        if found and not found.is_empty():
            return found
        else:
            return VOID_RELATION

    def get_assertions(self) -> list[Assertion]:
        """
        Gets all assertions about the individual
        :return:
        """
        return self.attributes + self.relations

    def set_score(self, score: float):
        self.score = score

    def get_score(self) -> float | None:
        if hasattr(self, 'score'):
            return self.score
        else:
            return None

    def has_score(self) -> bool:
        return hasattr(self, 'score')

    def add_attribute(self,
                      predicate: Reference | str = None,
                      values: list[str | int | float | bool] = None,
                      instance: AttributeInstance = None):
        """
        Adds an attribute to the individual
        One of predicate or instance must be provided (but not both: in that case, instance is preferred)
        :param values:
        :param predicate:
        :param instance:
        """
        if instance:
            if not isinstance(instance, AttributeInstance):
                raise ValueError("bad instance")
            if instance.subject and instance.subject != self.id:
                logging.warning("attribute for %s redeclared for %s", instance.subject, self.id)
            instance.subject = self.id
            existing = self.get_attribute(instance.predicate)
            if not existing or existing.is_empty():
                self.attributes.append(instance)
            else:
                existing.values.extend([value for value in instance.values if value not in existing.values])
        else:
            if not predicate:
                raise ValueError("missing property")
            if not isinstance(predicate, (Reference, str)):
                raise ValueError("bad property")
            self.add_attribute(instance=AttributeInstance(predicate=predicate, values=values))
        self._refresh = True

    def add_relation(self,
                     predicate: Reference | str = None,
                     values: list[Reference | str] = None,
                     instance: RelationInstance = None):
        """
        Adds a relation to the individual
        One of predicate or instance must be provided (but not both: in that case, instance is preferred)
        :param instance:
        :param values:
        :param predicate:
        :return:
        """
        if instance:
            if not isinstance(instance, RelationInstance):
                raise ValueError("bad instance")
            if instance.subject and instance.subject != self.id:
                logging.warning("relation for %s redeclared for %s", instance.subject, self.id)
            instance.subject = self.id
            existing = self.get_relation(instance.predicate)
            if not existing or existing.is_empty():
                self.relations.append(instance)
            else:
                existing.values.extend([value for value in instance.values if value not in existing.values])
            self._refresh = True
        else:
            if not predicate:
                raise ValueError("missing property")
            if not isinstance(predicate, (Reference, str)):
                raise ValueError("bad property")
            self.add_relation(instance=RelationInstance(predicate=predicate, values=values))

    def need_update(self):
        return self._refresh

    def updated(self):
        self._refresh = False
