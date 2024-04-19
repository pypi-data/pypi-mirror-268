from pydantic import BaseModel

from mmisp.api_schemas.tags.get_tag_response import TagAttributesResponse


class TaxonomyEntrySchema(BaseModel):
    tag: str
    expanded: str
    exclusive_predicate: bool
    description: str
    existing_tag: bool | TagAttributesResponse


class GetIdTaxonomyResponse(BaseModel):
    id: str
    namespace: str
    description: str
    version: str
    enabled: bool
    exclusive: bool
    required: bool
    highlighted: bool
    entries: list[TaxonomyEntrySchema]

    class Config:
        orm_mode = True


class GetIdTaxonomyResponseWrapper(BaseModel):
    Taxonomy: GetIdTaxonomyResponse
