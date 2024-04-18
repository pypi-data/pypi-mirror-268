from dataclasses import dataclass
from typing import Union

from bigdata.api.search import DiscoveryPanelResponse
from bigdata.models.entities import (
    Company,
    Concept,
    Facility,
    Landmark,
    Organization,
    OrganizationType,
    Place,
    Product,
    ProductType,
)
from bigdata.models.languages import Language
from bigdata.models.sources import Source
from bigdata.models.topics import Topic


@dataclass
class Comentions:
    companies: list[Company]
    concepts: list[Concept]
    languages: list[Language]
    organizations: list[Union[Organization, OrganizationType]]
    places: list[Union[Place, Facility, Landmark]]
    products: list[Union[Product, ProductType]]
    sources: list[Source]
    topics: list[Topic]

    @classmethod
    def from_response(cls, response: DiscoveryPanelResponse):
        return cls(
            companies=response.companies,
            concepts=response.concepts,
            languages=response.languages,
            organizations=response.organizations,
            places=response.places,
            products=response.products,
            sources=response.sources,
            topics=response.topics,
        )
