# Auto generated from soton_ibd_imaging.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-20T11:21:26
# Schema: soton_ibd_imaging
#
# id: http://w3id.org/ontogpt/soton_ibd_imaging
# description: A custom template for extracting and grounding imaging reports focused on IBD pathologies.
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
PATHOLOGY = CurieNamespace('pathology', 'http://w3id.org/ontogpt/soton_ibd_imaging')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SOTON_IBD_IMAGING = CurieNamespace('soton_ibd_imaging', 'http://w3id.org/ontogpt/soton_ibd_imaging/')
DEFAULT_ = SOTON_IBD_IMAGING


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class DiagnosisId(NamedEntityId):
    pass


class AnatomicalEntityId(NamedEntityId):
    pass


class AnatomicalStructuresId(NamedEntityId):
    pass


class ClinicalHistoryEntityId(NamedEntityId):
    pass


class ClinicalHistoryLocationId(NamedEntityId):
    pass


class TreatmentNameId(NamedEntityId):
    pass


class TreatmentRouteId(NamedEntityId):
    pass


class PatientDiagnosisNameId(NamedEntityId):
    pass


class PatientDiagnosisLocationId(NamedEntityId):
    pass


class QualifierId(NamedEntityId):
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

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["PathologyReport"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:PathologyReport"
    class_name: ClassVar[str] = "PathologyReport"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.PathologyReport

    pathology_statements: Optional[Union[Union[dict, "PathologyStatement"], List[Union[dict, "PathologyStatement"]]]] = empty_list()
    clinical_history_statements: Optional[Union[Union[dict, "PatientClinicalHistory"], List[Union[dict, "PatientClinicalHistory"]]]] = empty_list()
    treatment_statements: Optional[Union[Union[dict, "Treatment"], List[Union[dict, "Treatment"]]]] = empty_list()
    patient_diagnosis_statements: Optional[Union[Union[dict, "PatientDiagnosis"], List[Union[dict, "PatientDiagnosis"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.pathology_statements, list):
            self.pathology_statements = [self.pathology_statements] if self.pathology_statements is not None else []
        self.pathology_statements = [v if isinstance(v, PathologyStatement) else PathologyStatement(**as_dict(v)) for v in self.pathology_statements]

        if not isinstance(self.clinical_history_statements, list):
            self.clinical_history_statements = [self.clinical_history_statements] if self.clinical_history_statements is not None else []
        self.clinical_history_statements = [v if isinstance(v, PatientClinicalHistory) else PatientClinicalHistory(**as_dict(v)) for v in self.clinical_history_statements]

        if not isinstance(self.treatment_statements, list):
            self.treatment_statements = [self.treatment_statements] if self.treatment_statements is not None else []
        self.treatment_statements = [v if isinstance(v, Treatment) else Treatment(**as_dict(v)) for v in self.treatment_statements]

        if not isinstance(self.patient_diagnosis_statements, list):
            self.patient_diagnosis_statements = [self.patient_diagnosis_statements] if self.patient_diagnosis_statements is not None else []
        self.patient_diagnosis_statements = [v if isinstance(v, PatientDiagnosis) else PatientDiagnosis(**as_dict(v)) for v in self.patient_diagnosis_statements]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathologyStatement(YAMLRoot):
    """
    A statement that describes a pathology, including any diagnoses, one or more specific qualities being measured and
    the anatomical location or tissue the pathology is measured in.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["PathologyStatement"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:PathologyStatement"
    class_name: ClassVar[str] = "PathologyStatement"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.PathologyStatement

    diagnosis: Optional[Union[str, DiagnosisId]] = None
    qualifiers: Optional[Union[str, List[str]]] = empty_list()
    severity: Optional[str] = None
    anatomical_entities: Optional[Union[Union[str, AnatomicalEntityId], List[Union[str, AnatomicalEntityId]]]] = empty_list()
    anatomical_structure: Optional[Union[Union[str, AnatomicalStructuresId], List[Union[str, AnatomicalStructuresId]]]] = empty_list()
    negative: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.diagnosis is not None and not isinstance(self.diagnosis, DiagnosisId):
            self.diagnosis = DiagnosisId(self.diagnosis)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, str) else str(v) for v in self.qualifiers]

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if not isinstance(self.anatomical_entities, list):
            self.anatomical_entities = [self.anatomical_entities] if self.anatomical_entities is not None else []
        self.anatomical_entities = [v if isinstance(v, AnatomicalEntityId) else AnatomicalEntityId(v) for v in self.anatomical_entities]

        if not isinstance(self.anatomical_structure, list):
            self.anatomical_structure = [self.anatomical_structure] if self.anatomical_structure is not None else []
        self.anatomical_structure = [v if isinstance(v, AnatomicalStructuresId) else AnatomicalStructuresId(v) for v in self.anatomical_structure]

        if self.negative is not None and not isinstance(self.negative, str):
            self.negative = str(self.negative)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientClinicalHistory(YAMLRoot):
    """
    A statement that describes a clinical history, including any diagnoses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["PatientClinicalHistory"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:PatientClinicalHistory"
    class_name: ClassVar[str] = "PatientClinicalHistory"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.PatientClinicalHistory

    clinical_history: Optional[Union[str, ClinicalHistoryEntityId]] = None
    clinical_history_severity: Optional[str] = None
    clinical_history_location: Optional[Union[str, ClinicalHistoryLocationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.clinical_history is not None and not isinstance(self.clinical_history, ClinicalHistoryEntityId):
            self.clinical_history = ClinicalHistoryEntityId(self.clinical_history)

        if self.clinical_history_severity is not None and not isinstance(self.clinical_history_severity, str):
            self.clinical_history_severity = str(self.clinical_history_severity)

        if self.clinical_history_location is not None and not isinstance(self.clinical_history_location, ClinicalHistoryLocationId):
            self.clinical_history_location = ClinicalHistoryLocationId(self.clinical_history_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Treatment(YAMLRoot):
    """
    A statement that describes a treatment or drug the patient has had.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["Treatment"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:Treatment"
    class_name: ClassVar[str] = "Treatment"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.Treatment

    treatment_name: Optional[Union[str, TreatmentNameId]] = None
    treatment_route: Optional[Union[str, TreatmentRouteId]] = None
    treatment_dose: Optional[str] = None
    treatment_interval: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.treatment_name is not None and not isinstance(self.treatment_name, TreatmentNameId):
            self.treatment_name = TreatmentNameId(self.treatment_name)

        if self.treatment_route is not None and not isinstance(self.treatment_route, TreatmentRouteId):
            self.treatment_route = TreatmentRouteId(self.treatment_route)

        if self.treatment_dose is not None and not isinstance(self.treatment_dose, str):
            self.treatment_dose = str(self.treatment_dose)

        if self.treatment_interval is not None and not isinstance(self.treatment_interval, str):
            self.treatment_interval = str(self.treatment_interval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientDiagnosis(YAMLRoot):
    """
    A statement that describes the summary diagnosis from the report.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["PatientDiagnosis"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:PatientDiagnosis"
    class_name: ClassVar[str] = "PatientDiagnosis"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.PatientDiagnosis

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.NamedEntity

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
class Diagnosis(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["Diagnosis"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.Diagnosis

    id: Union[str, DiagnosisId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiagnosisId):
            self.id = DiagnosisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntity(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["AnatomicalEntity"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:AnatomicalEntity"
    class_name: ClassVar[str] = "AnatomicalEntity"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalStructures(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["AnatomicalStructures"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:AnatomicalStructures"
    class_name: ClassVar[str] = "AnatomicalStructures"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.AnatomicalStructures

    id: Union[str, AnatomicalStructuresId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalStructuresId):
            self.id = AnatomicalStructuresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalHistoryEntity(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["ClinicalHistoryEntity"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:ClinicalHistoryEntity"
    class_name: ClassVar[str] = "ClinicalHistoryEntity"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.ClinicalHistoryEntity

    id: Union[str, ClinicalHistoryEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalHistoryEntityId):
            self.id = ClinicalHistoryEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalHistoryLocation(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["ClinicalHistoryLocation"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:ClinicalHistoryLocation"
    class_name: ClassVar[str] = "ClinicalHistoryLocation"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.ClinicalHistoryLocation

    id: Union[str, ClinicalHistoryLocationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalHistoryLocationId):
            self.id = ClinicalHistoryLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TreatmentName(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["TreatmentName"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:TreatmentName"
    class_name: ClassVar[str] = "TreatmentName"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.TreatmentName

    id: Union[str, TreatmentNameId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TreatmentNameId):
            self.id = TreatmentNameId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TreatmentRoute(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["TreatmentRoute"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:TreatmentRoute"
    class_name: ClassVar[str] = "TreatmentRoute"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.TreatmentRoute

    id: Union[str, TreatmentRouteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TreatmentRouteId):
            self.id = TreatmentRouteId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientDiagnosisName(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["PatientDiagnosisName"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:PatientDiagnosisName"
    class_name: ClassVar[str] = "PatientDiagnosisName"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.PatientDiagnosisName

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

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["PatientDiagnosisLocation"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:PatientDiagnosisLocation"
    class_name: ClassVar[str] = "PatientDiagnosisLocation"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.PatientDiagnosisLocation

    id: Union[str, PatientDiagnosisLocationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatientDiagnosisLocationId):
            self.id = PatientDiagnosisLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Qualifier(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING["Qualifier"]
    class_class_curie: ClassVar[str] = "soton_ibd_imaging:Qualifier"
    class_name: ClassVar[str] = "Qualifier"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.Qualifier

    id: Union[str, QualifierId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QualifierId):
            self.id = QualifierId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["CompoundExpression"]
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.CompoundExpression


@dataclass(repr=False)
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Triple"]
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.Triple

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.TextWithEntity

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.Publication

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
    class_model_uri: ClassVar[URIRef] = SOTON_IBD_IMAGING.AnnotatorResult

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

slots.pathologyReport__pathology_statements = Slot(uri=SOTON_IBD_IMAGING.pathology_statements, name="pathologyReport__pathology_statements", curie=SOTON_IBD_IMAGING.curie('pathology_statements'),
                   model_uri=SOTON_IBD_IMAGING.pathologyReport__pathology_statements, domain=None, range=Optional[Union[Union[dict, PathologyStatement], List[Union[dict, PathologyStatement]]]])

slots.pathologyReport__clinical_history_statements = Slot(uri=SOTON_IBD_IMAGING.clinical_history_statements, name="pathologyReport__clinical_history_statements", curie=SOTON_IBD_IMAGING.curie('clinical_history_statements'),
                   model_uri=SOTON_IBD_IMAGING.pathologyReport__clinical_history_statements, domain=None, range=Optional[Union[Union[dict, PatientClinicalHistory], List[Union[dict, PatientClinicalHistory]]]])

slots.pathologyReport__treatment_statements = Slot(uri=SOTON_IBD_IMAGING.treatment_statements, name="pathologyReport__treatment_statements", curie=SOTON_IBD_IMAGING.curie('treatment_statements'),
                   model_uri=SOTON_IBD_IMAGING.pathologyReport__treatment_statements, domain=None, range=Optional[Union[Union[dict, Treatment], List[Union[dict, Treatment]]]])

slots.pathologyReport__patient_diagnosis_statements = Slot(uri=SOTON_IBD_IMAGING.patient_diagnosis_statements, name="pathologyReport__patient_diagnosis_statements", curie=SOTON_IBD_IMAGING.curie('patient_diagnosis_statements'),
                   model_uri=SOTON_IBD_IMAGING.pathologyReport__patient_diagnosis_statements, domain=None, range=Optional[Union[Union[dict, PatientDiagnosis], List[Union[dict, PatientDiagnosis]]]])

slots.pathologyStatement__diagnosis = Slot(uri=SOTON_IBD_IMAGING.diagnosis, name="pathologyStatement__diagnosis", curie=SOTON_IBD_IMAGING.curie('diagnosis'),
                   model_uri=SOTON_IBD_IMAGING.pathologyStatement__diagnosis, domain=None, range=Optional[Union[str, DiagnosisId]])

slots.pathologyStatement__qualifiers = Slot(uri=SOTON_IBD_IMAGING.qualifiers, name="pathologyStatement__qualifiers", curie=SOTON_IBD_IMAGING.curie('qualifiers'),
                   model_uri=SOTON_IBD_IMAGING.pathologyStatement__qualifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.pathologyStatement__severity = Slot(uri=SOTON_IBD_IMAGING.severity, name="pathologyStatement__severity", curie=SOTON_IBD_IMAGING.curie('severity'),
                   model_uri=SOTON_IBD_IMAGING.pathologyStatement__severity, domain=None, range=Optional[str])

slots.pathologyStatement__anatomical_entities = Slot(uri=SOTON_IBD_IMAGING.anatomical_entities, name="pathologyStatement__anatomical_entities", curie=SOTON_IBD_IMAGING.curie('anatomical_entities'),
                   model_uri=SOTON_IBD_IMAGING.pathologyStatement__anatomical_entities, domain=None, range=Optional[Union[Union[str, AnatomicalEntityId], List[Union[str, AnatomicalEntityId]]]])

slots.pathologyStatement__anatomical_structure = Slot(uri=SOTON_IBD_IMAGING.anatomical_structure, name="pathologyStatement__anatomical_structure", curie=SOTON_IBD_IMAGING.curie('anatomical_structure'),
                   model_uri=SOTON_IBD_IMAGING.pathologyStatement__anatomical_structure, domain=None, range=Optional[Union[Union[str, AnatomicalStructuresId], List[Union[str, AnatomicalStructuresId]]]])

slots.pathologyStatement__negative = Slot(uri=SOTON_IBD_IMAGING.negative, name="pathologyStatement__negative", curie=SOTON_IBD_IMAGING.curie('negative'),
                   model_uri=SOTON_IBD_IMAGING.pathologyStatement__negative, domain=None, range=Optional[str])

slots.patientClinicalHistory__clinical_history = Slot(uri=SOTON_IBD_IMAGING.clinical_history, name="patientClinicalHistory__clinical_history", curie=SOTON_IBD_IMAGING.curie('clinical_history'),
                   model_uri=SOTON_IBD_IMAGING.patientClinicalHistory__clinical_history, domain=None, range=Optional[Union[str, ClinicalHistoryEntityId]])

slots.patientClinicalHistory__clinical_history_severity = Slot(uri=SOTON_IBD_IMAGING.clinical_history_severity, name="patientClinicalHistory__clinical_history_severity", curie=SOTON_IBD_IMAGING.curie('clinical_history_severity'),
                   model_uri=SOTON_IBD_IMAGING.patientClinicalHistory__clinical_history_severity, domain=None, range=Optional[str])

slots.patientClinicalHistory__clinical_history_location = Slot(uri=SOTON_IBD_IMAGING.clinical_history_location, name="patientClinicalHistory__clinical_history_location", curie=SOTON_IBD_IMAGING.curie('clinical_history_location'),
                   model_uri=SOTON_IBD_IMAGING.patientClinicalHistory__clinical_history_location, domain=None, range=Optional[Union[str, ClinicalHistoryLocationId]])

slots.treatment__treatment_name = Slot(uri=SOTON_IBD_IMAGING.treatment_name, name="treatment__treatment_name", curie=SOTON_IBD_IMAGING.curie('treatment_name'),
                   model_uri=SOTON_IBD_IMAGING.treatment__treatment_name, domain=None, range=Optional[Union[str, TreatmentNameId]])

slots.treatment__treatment_route = Slot(uri=SOTON_IBD_IMAGING.treatment_route, name="treatment__treatment_route", curie=SOTON_IBD_IMAGING.curie('treatment_route'),
                   model_uri=SOTON_IBD_IMAGING.treatment__treatment_route, domain=None, range=Optional[Union[str, TreatmentRouteId]])

slots.treatment__treatment_dose = Slot(uri=SOTON_IBD_IMAGING.treatment_dose, name="treatment__treatment_dose", curie=SOTON_IBD_IMAGING.curie('treatment_dose'),
                   model_uri=SOTON_IBD_IMAGING.treatment__treatment_dose, domain=None, range=Optional[str])

slots.treatment__treatment_interval = Slot(uri=SOTON_IBD_IMAGING.treatment_interval, name="treatment__treatment_interval", curie=SOTON_IBD_IMAGING.curie('treatment_interval'),
                   model_uri=SOTON_IBD_IMAGING.treatment__treatment_interval, domain=None, range=Optional[str])

slots.patientDiagnosis__patient_diagnosis_name = Slot(uri=SOTON_IBD_IMAGING.patient_diagnosis_name, name="patientDiagnosis__patient_diagnosis_name", curie=SOTON_IBD_IMAGING.curie('patient_diagnosis_name'),
                   model_uri=SOTON_IBD_IMAGING.patientDiagnosis__patient_diagnosis_name, domain=None, range=Optional[Union[str, PatientDiagnosisNameId]])

slots.patientDiagnosis__patient_diagnosis_severity = Slot(uri=SOTON_IBD_IMAGING.patient_diagnosis_severity, name="patientDiagnosis__patient_diagnosis_severity", curie=SOTON_IBD_IMAGING.curie('patient_diagnosis_severity'),
                   model_uri=SOTON_IBD_IMAGING.patientDiagnosis__patient_diagnosis_severity, domain=None, range=Optional[str])

slots.patientDiagnosis__patient_diagnosis_location = Slot(uri=SOTON_IBD_IMAGING.patient_diagnosis_location, name="patientDiagnosis__patient_diagnosis_location", curie=SOTON_IBD_IMAGING.curie('patient_diagnosis_location'),
                   model_uri=SOTON_IBD_IMAGING.patientDiagnosis__patient_diagnosis_location, domain=None, range=Optional[Union[str, PatientDiagnosisLocationId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=SOTON_IBD_IMAGING.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=SOTON_IBD_IMAGING.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=SOTON_IBD_IMAGING.namedEntity__label, domain=None, range=Optional[str])

slots.namedEntity__original_spans = Slot(uri=CORE.original_spans, name="namedEntity__original_spans", curie=CORE.curie('original_spans'),
                   model_uri=SOTON_IBD_IMAGING.namedEntity__original_spans, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\d+:\d+$'))

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=SOTON_IBD_IMAGING.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=SOTON_IBD_IMAGING.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=SOTON_IBD_IMAGING.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=SOTON_IBD_IMAGING.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=SOTON_IBD_IMAGING.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=SOTON_IBD_IMAGING.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=SOTON_IBD_IMAGING.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=SOTON_IBD_IMAGING.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.textWithEntity__publication = Slot(uri=CORE.publication, name="textWithEntity__publication", curie=CORE.curie('publication'),
                   model_uri=SOTON_IBD_IMAGING.textWithEntity__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithEntity__entities = Slot(uri=CORE.entities, name="textWithEntity__entities", curie=CORE.curie('entities'),
                   model_uri=SOTON_IBD_IMAGING.textWithEntity__entities, domain=None, range=Optional[Union[Union[str, NamedEntityId], List[Union[str, NamedEntityId]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=SOTON_IBD_IMAGING.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=SOTON_IBD_IMAGING.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=SOTON_IBD_IMAGING.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=SOTON_IBD_IMAGING.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=SOTON_IBD_IMAGING.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=SOTON_IBD_IMAGING.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=SOTON_IBD_IMAGING.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=SOTON_IBD_IMAGING.annotatorResult__object_text, domain=None, range=Optional[str])
