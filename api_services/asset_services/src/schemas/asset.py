import strawberry
from strawberry.federation import field as federated_field
@strawberry.federation.type(keys=["id"], extend=True)
class UserResponse:
    id:strawberry.ID = federated_field(external=True)
    @staticmethod
    def resolver_reference(id:strawberry.ID)->"UserResponse":
        return UserResponse(id=id)

@strawberry.input
class CreateAsset:
    name:str

@strawberry.type
class GetAsset:
    id:int
    name:str

@strawberry.input
class CreateAssetAllocation:
    assetid:int
    userid:int

@strawberry.type
class GetAssetAllocated:
    id:int
    asset:GetAsset
    users:UserResponse
    