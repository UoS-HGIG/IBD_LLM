# Auto generated from diagnosis.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-20T14:29:37
# Schema: soton_ibd_diagnosis
#
# id: http://w3id.org/ontogpt/soton_ibd_diagnosis
# description: A custom template for extracting and grounding clinical reports focused on IBD pathologies.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ICD10CM = CurieNamespace('ICD10CM', 'http://purl.bioontology.org/ontology/ICD10CM/')
MESH = CurieNamespace('MESH', 'http://purl.bioontology.org/ontology/MESH/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://purl.bioontology.org/ontology/SNOMEDCT/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PATHOLOGY = CurieNamespace('pathology', 'http://w3id.org/ontogpt/soton_ibd_diagnosis')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SOTON_IBD_DIAGNOSIS = CurieNamespace('soton_ibd_diagnosis', 'http://w3id.org/ontogpt/soton_ibd_diagnosis/')
DEFAULT_ = SOTON_IBD_DIAGNOSIS


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class PatientDiagnosisNameId(NamedEntityId):
    pass


class PatientDiagnosisLocationId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass(repr=False)
class PathologyReport(YAMLRoot):
    """
    A semicolon-delimited list of statements, each describing a pathology, including any diagnoses, one or more
    specific qualities being measured and the anatomical location or tissue the pathology is measured in. Each
    statement should describe a single condition. STRICTLY output only statements in the specified format. Do not
    include any explanations, reasoning, colons, or additional text.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS["PathologyReport"]
    class_class_curie: ClassVar[str] = "soton_ibd_diagnosis:PathologyReport"
    class_name: ClassVar[str] = "PathologyReport"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.PathologyReport

    patient_diagnosis_statements: Optional[Union[Union[dict, "PatientDiagnosis"], List[Union[dict, "PatientDiagnosis"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.patient_diagnosis_statements, list):
            self.patient_diagnosis_statements = [self.patient_diagnosis_statements] if self.patient_diagnosis_statements is not None else []
        self.patient_diagnosis_statements = [v if isinstance(v, PatientDiagnosis) else PatientDiagnosis(**as_dict(v)) for v in self.patient_diagnosis_statements]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientDiagnosis(YAMLRoot):
    """
    A statement that describes the summary diagnosis from the report.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS["PatientDiagnosis"]
    class_class_curie: ClassVar[str] = "soton_ibd_diagnosis:PatientDiagnosis"
    class_name: ClassVar[str] = "PatientDiagnosis"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.PatientDiagnosis

    patient_diagnosis_name: Optional[Union[str, PatientDiagnosisNameId]] = None
    patient_diagnosis_severity: Optional[str] = None
    patient_diagnosis_location: Optional[Union[str, PatientDiagnosisLocationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.patient_diagnosis_name is not None and not isinstance(self.patient_diagnosis_name, PatientDiagnosisNameId):
            self.patient_diagnosis_name = PatientDiagnosisNameId(self.patient_diagnosis_name)

        if self.patient_diagnosis_severity is not None and not isinstance(self.patient_diagnosis_severity, str):
            self.patient_diagnosis_severity = str(self.patient_diagnosis_severity)

        if self.patient_diagnosis_location is not None and not isinstance(self.patient_diagnosis_location, PatientDiagnosisLocationId):
            self.patient_diagnosis_location = PatientDiagnosisLocationId(self.patient_diagnosis_location)

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class ExtractionResult(YAMLRoot):
    """
    A result of extracting knowledge on text
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["ExtractionResult"]
    class_class_curie: ClassVar[str] = "core:ExtractionResult"
    class_name: ClassVar[str] = "ExtractionResult"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.ExtractionResult

    input_id: Optional[str] = None
    input_title: Optional[str] = None
    input_text: Optional[str] = None
    raw_completion_output: Optional[str] = None
    prompt: Optional[str] = None
    extracted_object: Optional[Union[dict, Any]] = None
    named_entities: Optional[Union[Union[dict, Any], List[Union[dict, Any]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input_id is not None and not isinstance(self.input_id, str):
            self.input_id = str(self.input_id)

        if self.input_title is not None and not isinstance(self.input_title, str):
            self.input_title = str(self.input_title)

        if self.input_text is not None and not isinstance(self.input_text, str):
            self.input_text = str(self.input_text)

        if self.raw_completion_output is not None and not isinstance(self.raw_completion_output, str):
            self.raw_completion_output = str(self.raw_completion_output)

        if self.prompt is not None and not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["NamedEntity"]
    class_class_curie: ClassVar[str] = "core:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.NamedEntity

    id: Union[str, NamedEntityId] = None
    label: Optional[str] = None
    original_spans: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.original_spans, list):
            self.original_spans = [self.original_spans] if self.original_spans is not None else []
        self.original_spans = [v if isinstance(v, str) else str(v) for v in self.original_spans]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientDiagnosisName(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS["PatientDiagnosisName"]
    class_class_curie: ClassVar[str] = "soton_ibd_diagnosis:PatientDiagnosisName"
    class_name: ClassVar[str] = "PatientDiagnosisName"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.PatientDiagnosisName

    id: Union[str, PatientDiagnosisNameId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatientDiagnosisNameId):
            self.id = PatientDiagnosisNameId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientDiagnosisLocation(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS["PatientDiagnosisLocation"]
    class_class_curie: ClassVar[str] = "soton_ibd_diagnosis:PatientDiagnosisLocation"
    class_name: ClassVar[str] = "PatientDiagnosisLocation"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.PatientDiagnosisLocation

    id: Union[str, PatientDiagnosisLocationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatientDiagnosisLocationId):
            self.id = PatientDiagnosisLocationId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["CompoundExpression"]
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.CompoundExpression


@dataclass(repr=False)
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Triple"]
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.Triple

    subject: Optional[Union[str, NamedEntityId]] = None
    predicate: Optional[Union[str, RelationshipTypeId]] = None
    object: Optional[Union[str, NamedEntityId]] = None
    qualifier: Optional[str] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, NamedEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NamedEntityId):
            self.subject = NamedEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, RelationshipTypeId):
            self.predicate = RelationshipTypeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NamedEntityId):
            self.object = NamedEntityId(self.object)

        if self.qualifier is not None and not isinstance(self.qualifier, str):
            self.qualifier = str(self.qualifier)

        if self.subject_qualifier is not None and not isinstance(self.subject_qualifier, NamedEntityId):
            self.subject_qualifier = NamedEntityId(self.subject_qualifier)

        if self.object_qualifier is not None and not isinstance(self.object_qualifier, NamedEntityId):
            self.object_qualifier = NamedEntityId(self.object_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextWithTriples(YAMLRoot):
    """
    A text containing one or more relations of the Triple type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["TextWithTriples"]
    class_class_curie: ClassVar[str] = "core:TextWithTriples"
    class_name: ClassVar[str] = "TextWithTriples"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.TextWithTriples

    publication: Optional[Union[dict, "Publication"]] = None
    triples: Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if not isinstance(self.triples, list):
            self.triples = [self.triples] if self.triples is not None else []
        self.triples = [v if isinstance(v, Triple) else Triple(**as_dict(v)) for v in self.triples]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextWithEntity(YAMLRoot):
    """
    A text containing one or more instances of a single type of entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["TextWithEntity"]
    class_class_curie: ClassVar[str] = "core:TextWithEntity"
    class_name: ClassVar[str] = "TextWithEntity"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.TextWithEntity

    publication: Optional[Union[dict, "Publication"]] = None
    entities: Optional[Union[Union[str, NamedEntityId], List[Union[str, NamedEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if not isinstance(self.entities, list):
            self.entities = [self.entities] if self.entities is not None else []
        self.entities = [v if isinstance(v, NamedEntityId) else NamedEntityId(v) for v in self.entities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelationshipType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["RelationshipType"]
    class_class_curie: ClassVar[str] = "core:RelationshipType"
    class_name: ClassVar[str] = "RelationshipType"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Publication"]
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.Publication

    id: Optional[str] = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    combined_text: Optional[str] = None
    full_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.combined_text is not None and not isinstance(self.combined_text, str):
            self.combined_text = str(self.combined_text)

        if self.full_text is not None and not isinstance(self.full_text, str):
            self.full_text = str(self.full_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnotatorResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["AnnotatorResult"]
    class_class_curie: ClassVar[str] = "core:AnnotatorResult"
    class_name: ClassVar[str] = "AnnotatorResult"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_DIAGNOSIS.AnnotatorResult

    subject_text: Optional[str] = None
    object_id: Optional[str] = None
    object_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_text is not None and not isinstance(self.subject_text, str):
            self.subject_text = str(self.subject_text)

        if self.object_id is not None and not isinstance(self.object_id, str):
            self.object_id = str(self.object_id)

        if self.object_text is not None and not isinstance(self.object_text, str):
            self.object_text = str(self.object_text)

        super().__post_init__(**kwargs)


# Enumerations
class NullDataOptions(EnumDefinitionImpl):

    UNSPECIFIED_METHOD_OF_ADMINISTRATION = PermissibleValue(
        text="UNSPECIFIED_METHOD_OF_ADMINISTRATION",
        meaning=NCIT["C149701"])
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        meaning=NCIT["C18902"])
    NOT_MENTIONED = PermissibleValue(text="NOT_MENTIONED")

    _defn = EnumDefinition(
        name="NullDataOptions",
    )

# Slots
class slots:
    pass

slots.pathologyReport__patient_diagnosis_statements = Slot(uri=SOTON_IBD_DIAGNOSIS.patient_diagnosis_statements, name="pathologyReport__patient_diagnosis_statements", curie=SOTON_IBD_DIAGNOSIS.curie('patient_diagnosis_statements'),
                   model_uri=SOTON_IBD_DIAGNOSIS.pathologyReport__patient_diagnosis_statements, domain=None, range=Optional[Union[Union[dict, PatientDiagnosis], List[Union[dict, PatientDiagnosis]]]])

slots.patientDiagnosis__patient_diagnosis_name = Slot(uri=SOTON_IBD_DIAGNOSIS.patient_diagnosis_name, name="patientDiagnosis__patient_diagnosis_name", curie=SOTON_IBD_DIAGNOSIS.curie('patient_diagnosis_name'),
                   model_uri=SOTON_IBD_DIAGNOSIS.patientDiagnosis__patient_diagnosis_name, domain=None, range=Optional[Union[str, PatientDiagnosisNameId]])

slots.patientDiagnosis__patient_diagnosis_severity = Slot(uri=SOTON_IBD_DIAGNOSIS.patient_diagnosis_severity, name="patientDiagnosis__patient_diagnosis_severity", curie=SOTON_IBD_DIAGNOSIS.curie('patient_diagnosis_severity'),
                   model_uri=SOTON_IBD_DIAGNOSIS.patientDiagnosis__patient_diagnosis_severity, domain=None, range=Optional[str])

slots.patientDiagnosis__patient_diagnosis_location = Slot(uri=SOTON_IBD_DIAGNOSIS.patient_diagnosis_location, name="patientDiagnosis__patient_diagnosis_location", curie=SOTON_IBD_DIAGNOSIS.curie('patient_diagnosis_location'),
                   model_uri=SOTON_IBD_DIAGNOSIS.patientDiagnosis__patient_diagnosis_location, domain=None, range=Optional[Union[str, PatientDiagnosisLocationId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=SOTON_IBD_DIAGNOSIS.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=SOTON_IBD_DIAGNOSIS.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=SOTON_IBD_DIAGNOSIS.namedEntity__label, domain=None, range=Optional[str])

slots.namedEntity__original_spans = Slot(uri=CORE.original_spans, name="namedEntity__original_spans", curie=CORE.curie('original_spans'),
                   model_uri=SOTON_IBD_DIAGNOSIS.namedEntity__original_spans, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\d+:\d+$'))

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=SOTON_IBD_DIAGNOSIS.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=SOTON_IBD_DIAGNOSIS.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=SOTON_IBD_DIAGNOSIS.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=SOTON_IBD_DIAGNOSIS.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=SOTON_IBD_DIAGNOSIS.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=SOTON_IBD_DIAGNOSIS.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=SOTON_IBD_DIAGNOSIS.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=SOTON_IBD_DIAGNOSIS.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.textWithEntity__publication = Slot(uri=CORE.publication, name="textWithEntity__publication", curie=CORE.curie('publication'),
                   model_uri=SOTON_IBD_DIAGNOSIS.textWithEntity__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithEntity__entities = Slot(uri=CORE.entities, name="textWithEntity__entities", curie=CORE.curie('entities'),
                   model_uri=SOTON_IBD_DIAGNOSIS.textWithEntity__entities, domain=None, range=Optional[Union[Union[str, NamedEntityId], List[Union[str, NamedEntityId]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=SOTON_IBD_DIAGNOSIS.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=SOTON_IBD_DIAGNOSIS.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=SOTON_IBD_DIAGNOSIS.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=SOTON_IBD_DIAGNOSIS.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=SOTON_IBD_DIAGNOSIS.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=SOTON_IBD_DIAGNOSIS.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=SOTON_IBD_DIAGNOSIS.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=SOTON_IBD_DIAGNOSIS.annotatorResult__object_text, domain=None, range=Optional[str])
