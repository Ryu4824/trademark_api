from pydantic import BaseModel
from typing import Optional, List

class Trademark(BaseModel):
    productName: Optional[str]
    productNameEng: Optional[str]
    applicationNumber: Optional[str]
    applicationDate: Optional[str]
    registerStatus: Optional[str]
    publicationNumber: Optional[str]
    publicationDate: Optional[str]
    registrationNumber: Optional[List[str]]
    registrationDate: Optional[List[str]]
    registrationPubNumber: Optional[str]
    registrationPubDate: Optional[str]
    internationalRegDate: Optional[str]
    internationalRegNumbers: Optional[List[str]]
    priorityClaimNumList: Optional[List[str]]
    priorityClaimDateList: Optional[List[str]]
    asignProductMainCodeList: Optional[List[str]]
    asignProductSubCodeList: Optional[List[str]]
    viennaCodeList: Optional[List[str]]
