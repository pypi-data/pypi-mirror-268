from enum import Enum
from typing import Any, Dict, List, Optional, Type, TypeVar

from pydantic import BaseModel, Extra, validator

CustomFeatureTypeVar = TypeVar('CustomFeatureTypeVar', bound='CustomFeature')
DEFAULT_NUM_CLUSTERS = 5
DEFAULT_NUM_TAGS = 5


class CustomFeatureType(str, Enum):
    FROM_COLUMNS = 'FROM_COLUMNS'
    FROM_VECTOR = 'FROM_VECTOR'
    FROM_TEXT_EMBEDDING = 'FROM_TEXT_EMBEDDING'
    FROM_IMAGE_EMBEDDING = 'FROM_IMAGE_EMBEDDING'
    ENRICHMENT = 'ENRICHMENT'


class CustomFeature(BaseModel):
    name: str
    type: CustomFeatureType
    n_clusters: Optional[int] = DEFAULT_NUM_CLUSTERS
    centroids: Optional[List] = None

    @validator('n_clusters')
    def validate_n_clusters(cls, value: int) -> int:  # noqa: N805
        if value < 0:
            raise ValueError('n_clusters must be greater than 0')
        return value

    class Config:
        allow_mutation = False
        extra = Extra.forbid

    @classmethod
    def from_columns(
        cls, custom_name: str, cols: List[str], n_clusters: int = DEFAULT_NUM_CLUSTERS
    ) -> 'Multivariate':
        return Multivariate(
            name=custom_name,
            columns=cols,
            n_clusters=n_clusters,
        )

    @classmethod
    def from_dict(cls: Type[CustomFeatureTypeVar], deserialized_json: dict) -> Any:
        feature_type = CustomFeatureType(deserialized_json['type'])
        if feature_type == CustomFeatureType.FROM_COLUMNS:
            return Multivariate.parse_obj(deserialized_json)
        elif feature_type == CustomFeatureType.FROM_VECTOR:
            return VectorFeature.parse_obj(deserialized_json)
        elif feature_type == CustomFeatureType.FROM_TEXT_EMBEDDING:
            return TextEmbedding.parse_obj(deserialized_json)
        elif feature_type == CustomFeatureType.FROM_IMAGE_EMBEDDING:
            return ImageEmbedding.parse_obj(deserialized_json)
        elif feature_type == CustomFeatureType.ENRICHMENT:
            return Enrichment.parse_obj(deserialized_json)
        else:
            raise ValueError(f'Unsupported feature type: {feature_type}')

    def to_dict(self) -> Dict[str, Any]:
        return_dict: Dict[str, Any] = {
            'name': self.name,
            'type': self.type.value,
            'n_clusters': self.n_clusters,
        }
        if isinstance(self, Multivariate):
            return_dict['columns'] = self.columns
        elif isinstance(self, VectorFeature):
            return_dict['column'] = self.column
            if isinstance(self, (ImageEmbedding, TextEmbedding)):
                return_dict['source_column'] = self.source_column
                if isinstance(self, TextEmbedding):
                    return_dict['n_tags'] = self.n_tags
        elif isinstance(self, Enrichment):
            return_dict['columns'] = self.columns
            return_dict['enrichment'] = self.enrichment
            return_dict['config'] = self.config
        else:
            raise ValueError(f'Unsupported feature type: {self.type} {type(self)}')

        return return_dict


class Multivariate(CustomFeature):
    type: CustomFeatureType = CustomFeatureType.FROM_COLUMNS
    columns: List[str]
    monitor_components: bool = False

    @validator('columns')
    def validate_columns(cls, value: List[str]) -> List[str]:  # noqa: N805
        if len(value) < 2:
            raise ValueError('Multivariate features must have at least 2 columns')
        return value


class VectorFeature(CustomFeature):
    type: CustomFeatureType = CustomFeatureType.FROM_VECTOR
    source_column: Optional[str] = None
    column: str


class TextEmbedding(VectorFeature):
    type: CustomFeatureType = CustomFeatureType.FROM_TEXT_EMBEDDING
    n_tags: Optional[int] = DEFAULT_NUM_TAGS
    tf_idf: Optional[Dict[str, List]] = None

    @validator('source_column')
    def validate_source_column(cls, value: str) -> str:  # noqa: N805
        if value is None:
            raise ValueError('source_column must be specified')
        return value

    @validator('n_tags')
    def validate_n_tags(cls, value: int) -> int:  # noqa: N805
        if value < 1:
            raise ValueError('n_tags must be greater than 0')
        return value


class ImageEmbedding(VectorFeature):
    type: CustomFeatureType = CustomFeatureType.FROM_IMAGE_EMBEDDING

    @validator('source_column')
    def validate_source_column(cls, value: str) -> str:  # noqa: N805
        if value is None:
            raise ValueError('source_column must be specified')
        return value


class Enrichment(CustomFeature):
    type: CustomFeatureType = CustomFeatureType.ENRICHMENT
    columns: List[str]
    enrichment: str
    config: Dict[str, Any] = {}
