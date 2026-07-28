#This file was automatically generated!

from Astandy.errors import AstandyRPCException
from Astandy.schemes.messages_pb2 import Response
from .schemes_pb2 import *

class AchievementRemoteService:    
    @staticmethod
    def getCurrentPlayerAchievementsRequest(request: GetCurrentPlayerAchievementsRequest): 
        msg = request.SerializeToString()
        
        return 265, msg # Xmm: 0

    @staticmethod
    def getCurrentPlayerAchievementsResponse(response: Response) -> GetCurrentPlayerAchievementsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetCurrentPlayerAchievementsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerAchievementsRequest(request: GetPlayerAchievementsRequest): 
        msg = request.SerializeToString()
        
        return 266, msg # Xmm: 0

    @staticmethod
    def getPlayerAchievementsResponse(response: Response) -> GetPlayerAchievementsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerAchievementsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getAchievementDefinitionsRequest(request: GetAchievementDefinitionsRequest): 
        msg = request.SerializeToString()
        
        return 267, msg # Xmm: 0

    @staticmethod
    def getAchievementDefinitionsResponse(response: Response) -> GetAchievementDefinitionsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetAchievementDefinitionsResponse()
        msg.ParseFromString(data)

        return msg

class ClanRemoteService:    
    @staticmethod
    def assignRoleToMember2Request(request: AssignRoleToMemberRequest): 
        msg = request.SerializeToString()
        
        return 134, msg # Xmm: 0

    @staticmethod
    def assignRoleToMember2Response(response: Response) -> AssignRoleToMemberResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AssignRoleToMemberResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def validateClanTag2Request(request: ValidateClanTagRequest): 
        msg = request.SerializeToString()
        
        return 118, msg # Xmm: 0

    @staticmethod
    def validateClanTag2Response(response: Response) -> ValidateClanTagResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ValidateClanTagResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanMembers2Request(request: GetClanMembersRequest): 
        msg = request.SerializeToString()
        
        return 108, msg # Xmm: 0

    @staticmethod
    def getClanMembers2Response(response: Response) -> GetClanMembersResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanMembersResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClan2Request(request: GetClanRequest): 
        msg = request.SerializeToString()
        
        return 101, msg # Xmm: 0

    @staticmethod
    def getClan2Response(response: Response) -> GetClanResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def leaveClan2Request(request: LeaveClanRequest): 
        msg = request.SerializeToString()
        
        return 125, msg # Xmm: 0

    @staticmethod
    def leaveClan2Response(response: Response) -> LeaveClanResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = LeaveClanResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setClanAvatar2Request(request: SetClanAvatarRequest): 
        msg = request.SerializeToString()
        
        return 128, msg # Xmm: 0

    @staticmethod
    def setClanAvatar2Response(response: Response) -> SetClanAvatarResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetClanAvatarResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def deleteClosedJoinRequest2Request(request: DeleteClosedJoinRequestRequest): 
        msg = request.SerializeToString()
        
        return 117, msg # Xmm: 0

    @staticmethod
    def deleteClosedJoinRequest2Response(response: Response) -> DeleteClosedJoinRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeleteClosedJoinRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def declineInviteRequest2Request(request: DeclineInviteRequestRequest): 
        msg = request.SerializeToString()
        
        return 130, msg # Xmm: 0

    @staticmethod
    def declineInviteRequest2Response(response: Response) -> DeclineInviteRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeclineInviteRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def declineJoinRequest2Request(request: DeclineJoinRequestRequest): 
        msg = request.SerializeToString()
        
        return 120, msg # Xmm: 0

    @staticmethod
    def declineJoinRequest2Response(response: Response) -> DeclineJoinRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeclineJoinRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanSettings2Request(request: GetClanSettingsRequest): 
        msg = request.SerializeToString()
        
        return 103, msg # Xmm: 0

    @staticmethod
    def getClanSettings2Response(response: Response) -> GetClanSettingsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanSettingsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanJoinRequests2Request(request: GetClanJoinRequestsRequest): 
        msg = request.SerializeToString()
        
        return 116, msg # Xmm: 0

    @staticmethod
    def getClanJoinRequests2Response(response: Response) -> GetClanJoinRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanJoinRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def assignLeaderRole2Request(request: AssignLeaderRoleRequest): 
        msg = request.SerializeToString()
        
        return 135, msg # Xmm: 0

    @staticmethod
    def assignLeaderRole2Response(response: Response) -> AssignLeaderRoleResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AssignLeaderRoleResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setClanDescription2Request(request: SetClanDescriptionRequest): 
        msg = request.SerializeToString()
        
        return 127, msg # Xmm: 0

    @staticmethod
    def setClanDescription2Response(response: Response) -> SetClanDescriptionResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetClanDescriptionResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def findClan2Request(request: FindClanRequest): 
        msg = request.SerializeToString()
        
        return 115, msg # Xmm: 0

    @staticmethod
    def findClan2Response(response: Response) -> FindClanResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = FindClanResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def deleteClosedInviteRequest2Request(request: DeleteClosedInviteRequestRequest): 
        msg = request.SerializeToString()
        
        return 123, msg # Xmm: 0

    @staticmethod
    def deleteClosedInviteRequest2Response(response: Response) -> DeleteClosedInviteRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeleteClosedInviteRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerClosedJoinRequestsCount2Request(request: GetPlayerClosedJoinRequestsCountRequest): 
        msg = request.SerializeToString()
        
        return 105, msg # Xmm: 0

    @staticmethod
    def getPlayerClosedJoinRequestsCount2Response(response: Response) -> GetPlayerClosedJoinRequestsCountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerClosedJoinRequestsCountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def requestToJoinClan2Request(request: RequestToJoinClanRequest): 
        msg = request.SerializeToString()
        
        return 111, msg # Xmm: 0

    @staticmethod
    def requestToJoinClan2Response(response: Response) -> RequestToJoinClanResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RequestToJoinClanResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def cancelJoinRequest2Request(request: CancelJoinRequestRequest): 
        msg = request.SerializeToString()
        
        return 121, msg # Xmm: 0

    @staticmethod
    def cancelJoinRequest2Response(response: Response) -> CancelJoinRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CancelJoinRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def changeClanType2Request(request: ChangeClanTypeRequest): 
        msg = request.SerializeToString()
        
        return 132, msg # Xmm: 0

    @staticmethod
    def changeClanType2Response(response: Response) -> ChangeClanTypeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ChangeClanTypeResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanInviteRequests2Request(request: GetClanInviteRequestsRequest): 
        msg = request.SerializeToString()
        
        return 119, msg # Xmm: 0

    @staticmethod
    def getClanInviteRequests2Response(response: Response) -> GetClanInviteRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanInviteRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerInviteRequests2Request(request: GetPlayerInviteRequestsRequest): 
        msg = request.SerializeToString()
        
        return 112, msg # Xmm: 0

    @staticmethod
    def getPlayerInviteRequests2Response(response: Response) -> GetPlayerInviteRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerInviteRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getRecommendedClans2Request(request: GetRecommendedClansRequest): 
        msg = request.SerializeToString()
        
        return 109, msg # Xmm: 0

    @staticmethod
    def getRecommendedClans2Response(response: Response) -> GetRecommendedClansResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetRecommendedClansResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def validateClanName2Request(request: ValidateClanNameRequest): 
        msg = request.SerializeToString()
        
        return 124, msg # Xmm: 0

    @staticmethod
    def validateClanName2Response(response: Response) -> ValidateClanNameResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ValidateClanNameResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanByTagRequest(request: GetClanByTagRequest): 
        msg = request.SerializeToString()
        
        return 129, msg # Xmm: 0

    @staticmethod
    def getClanByTagResponse(response: Response) -> GetClanByTagResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanByTagResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def createClan2Request(request: CreateClanRequest): 
        msg = request.SerializeToString()
        
        return 131, msg # Xmm: 0

    @staticmethod
    def createClan2Response(response: Response) -> CreateClanResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CreateClanResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanJoinRequestsCount2Request(request: GetClanJoinRequestsCountRequest): 
        msg = request.SerializeToString()
        
        return 106, msg # Xmm: 0

    @staticmethod
    def getClanJoinRequestsCount2Response(response: Response) -> GetClanJoinRequestsCountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanJoinRequestsCountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanMembersById2Request(request: GetClanMembersByIdRequest): 
        msg = request.SerializeToString()
        
        return 110, msg # Xmm: 0

    @staticmethod
    def getClanMembersById2Response(response: Response) -> GetClanMembersByIdResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanMembersByIdResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerInviteRequestsCount2Request(request: GetPlayerInviteRequestsCountRequest): 
        msg = request.SerializeToString()
        
        return 104, msg # Xmm: 0

    @staticmethod
    def getPlayerInviteRequestsCount2Response(response: Response) -> GetPlayerInviteRequestsCountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerInviteRequestsCountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getRoles2Request(request: GetRolesRequest): 
        msg = request.SerializeToString()
        
        return 102, msg # Xmm: 0

    @staticmethod
    def getRoles2Response(response: Response) -> GetRolesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetRolesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def cancelInviteRequest2Request(request: CancelInviteRequestRequest): 
        msg = request.SerializeToString()
        
        return 133, msg # Xmm: 0

    @staticmethod
    def cancelInviteRequest2Response(response: Response) -> CancelInviteRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CancelInviteRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def inviteToClan2Request(request: InviteToClanRequest): 
        msg = request.SerializeToString()
        
        return 122, msg # Xmm: 0

    @staticmethod
    def inviteToClan2Response(response: Response) -> InviteToClanResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = InviteToClanResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def kickMember2Request(request: KickMemberRequest): 
        msg = request.SerializeToString()
        
        return 126, msg # Xmm: 0

    @staticmethod
    def kickMember2Response(response: Response) -> KickMemberResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = KickMemberResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanById2Request(request: GetClanByIdRequest): 
        msg = request.SerializeToString()
        
        return 113, msg # Xmm: 0

    @staticmethod
    def getClanById2Response(response: Response) -> GetClanByIdResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanByIdResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanClosedInviteRequestsCount2Request(request: GetClanClosedInviteRequestsCountRequest): 
        msg = request.SerializeToString()
        
        return 107, msg # Xmm: 0

    @staticmethod
    def getClanClosedInviteRequestsCount2Response(response: Response) -> GetClanClosedInviteRequestsCountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanClosedInviteRequestsCountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerJoinRequests2Request(request: GetPlayerJoinRequestsRequest): 
        msg = request.SerializeToString()
        
        return 114, msg # Xmm: 0

    @staticmethod
    def getPlayerJoinRequests2Response(response: Response) -> GetPlayerJoinRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerJoinRequestsResponse()
        msg.ParseFromString(data)

        return msg

class ClanMessagesRemoteService:    
    @staticmethod
    def getUnreadLogMessagesCount2Request(request: GetUnreadLogMessagesCountRequest): 
        msg = request.SerializeToString()
        
        return 201, msg # Xmm: 0

    @staticmethod
    def getUnreadLogMessagesCount2Response(response: Response) -> GetUnreadLogMessagesCountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetUnreadLogMessagesCountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def readClanLogMessages2Request(request: ReadClanLogMessagesRequest): 
        msg = request.SerializeToString()
        
        return 206, msg # Xmm: 0

    @staticmethod
    def readClanLogMessages2Response(response: Response) -> ReadClanLogMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ReadClanLogMessagesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanChatMessages2Request(request: GetClanChatMessagesRequest): 
        msg = request.SerializeToString()
        
        return 203, msg # Xmm: 0

    @staticmethod
    def getClanChatMessages2Response(response: Response) -> GetClanChatMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanChatMessagesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def sendClanChatMessage2Request(request: SendClanChatMessageRequest): 
        msg = request.SerializeToString()
        
        return 205, msg # Xmm: 0

    @staticmethod
    def sendClanChatMessage2Response(response: Response) -> SendClanChatMessageResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SendClanChatMessageResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanLogMessages2Request(request: GetClanLogMessagesRequest): 
        msg = request.SerializeToString()
        
        return 207, msg # Xmm: 0

    @staticmethod
    def getClanLogMessages2Response(response: Response) -> GetClanLogMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanLogMessagesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getUnreadChatMessagesCount2Request(request: GetUnreadChatMessagesCountRequest): 
        msg = request.SerializeToString()
        
        return 202, msg # Xmm: 0

    @staticmethod
    def getUnreadChatMessagesCount2Response(response: Response) -> GetUnreadChatMessagesCountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetUnreadChatMessagesCountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def readClanChatMessages2Request(request: ReadClanChatMessagesRequest): 
        msg = request.SerializeToString()
        
        return 204, msg # Xmm: 0

    @staticmethod
    def readClanChatMessages2Response(response: Response) -> ReadClanChatMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ReadClanChatMessagesResponse()
        msg.ParseFromString(data)

        return msg

class PlayerStatsRemoteService:    
    @staticmethod
    def getCurrentStatsRequest(request: GetCurrentStatsRequest): 
        msg = request.SerializeToString()
        
        return 181, msg # Xmm: 0

    @staticmethod
    def getCurrentStatsResponse(response: Response) -> GetCurrentStatsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetCurrentStatsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def storeStats2Request(request: StorePlayerStatsRequest): 
        msg = request.SerializeToString()
        
        return 180, msg # Xmm: 0

    @staticmethod
    def storeStats2Response(response: Response) -> StorePlayerStatsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = StorePlayerStatsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerStats2Request(request: GetPlayerStatsRequest): 
        msg = request.SerializeToString()
        
        return 182, msg # Xmm: 0

    @staticmethod
    def getPlayerStats2Response(response: Response) -> GetPlayerStatsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerStatsResponse()
        msg.ParseFromString(data)

        return msg

class InventoryRemoteService:    
    @staticmethod
    def getOtherPlayerItemsEncryptedRequest(request: GetOtherPlayerItemsRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 50, msg # Xmm: 0

    @staticmethod
    def getOtherPlayerItemsEncryptedResponse(response: Response, cipher) -> GetOtherPlayerItemsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GetOtherPlayerItemsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setInventoryItemsPropertiesEncryptedRequest(request: SetItemsModificationsRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 51, msg # Xmm: 0

    @staticmethod
    def setInventoryItemsPropertiesEncryptedResponse(response: Response, cipher) -> SetItemsModificationsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = SetItemsModificationsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setInventoryItemFlagsEncryptedRequest(request: SetInventoryItemFlagsRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 52, msg # Xmm: 0

    @staticmethod
    def setInventoryItemFlagsEncryptedResponse(response: Response, cipher) -> SetInventoryItemFlagsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = SetInventoryItemFlagsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def activateCouponEncryptedRequest(request: ActivateCouponRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 60, msg # Xmm: 0

    @staticmethod
    def activateCouponEncryptedResponse(response: Response, cipher) -> ActivateCouponResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = ActivateCouponResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def executeRecipeEncrypted2Request(request: ExecuteRecipeRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 56, msg # Xmm: 0

    @staticmethod
    def executeRecipeEncrypted2Response(response: Response, cipher) -> ExecuteRecipeEncrypted2Response:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = ExecuteRecipeEncrypted2Response()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def mountInventoryItemEncryptedRequest(request: MountInventoryItemRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 58, msg # Xmm: 0

    @staticmethod
    def mountInventoryItemEncryptedResponse(response: Response, cipher) -> MountInventoryItemResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = MountInventoryItemResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def unmountInventoryItemEncryptedRequest(request: UnmountInventoryItemRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 59, msg # Xmm: 0

    @staticmethod
    def unmountInventoryItemEncryptedResponse(response: Response, cipher) -> UnmountInventoryItemResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = UnmountInventoryItemResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def buyInventoryItemEncryptedRequest(request: BuyInventoryItemRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 57, msg # Xmm: 0

    @staticmethod
    def buyInventoryItemEncryptedResponse(response: Response, cipher) -> BuyInventoryItemResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = BuyInventoryItemResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerInventoryEncryptedRequest(request: GetPlayerInventoryRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 53, msg # Xmm: 0

    @staticmethod
    def getPlayerInventoryEncryptedResponse(response: Response, cipher) -> GetPlayerInventoryResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GetPlayerInventoryResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getInventoryItemPropertyDefinitionsEncryptedRequest(request: GetInventoryItemPropertyDefinitionsRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 55, msg # Xmm: 0

    @staticmethod
    def getInventoryItemPropertyDefinitionsEncryptedResponse(response: Response, cipher) -> GetInventoryItemPropertyDefinitionsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GetInventoryItemPropertyDefinitionsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getInventoryItemDefinitionsEncryptedRequest(request: GetInventoryItemDefinitionsRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 54, msg # Xmm: 0

    @staticmethod
    def getInventoryItemDefinitionsEncryptedResponse(response: Response, cipher) -> GetInventoryItemDefinitionsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GetInventoryItemDefinitionsResponse()
        msg.ParseFromString(data)

        return msg

class BoltIdAuthRemoteService:    
    @staticmethod
    def unLinkAuthRequest(request: BoltIdUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 417, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> BoltIdUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = BoltIdUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def linkAuthRequest(request: BoltIdLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 416, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> BoltIdLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = BoltIdLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def encryptedAuth2Request(request: BoltIdAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 415, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> BoltIdAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = BoltIdAuthResponse()
        msg.ParseFromString(data)

        return msg

class TestAuthRemoteService:    
    @staticmethod
    def encryptedAuth2Request(request: TestAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 410, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> TestAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = TestAuthResponse()
        msg.ParseFromString(data)

        return msg

class AppStoreInAppRemoteService:    
    @staticmethod
    def buyInApp2Request(request: AppStoreBuyInappRequest): 
        msg = request.SerializeToString()
        
        return 400, msg # Xmm: 0

    @staticmethod
    def buyInApp2Response(response: Response) -> AppStoreBuyInappResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AppStoreBuyInappResponse()
        msg.ParseFromString(data)

        return msg

class GameSettingsRemoteService:    
    @staticmethod
    def getGameSettingsEncrypted2Request(request: GetGameSettingsEncryptedRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 285, msg # Xmm: 0

    @staticmethod
    def getGameSettingsEncrypted2Response(response: Response, cipher) -> GetGameSettingsEncryptedResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GetGameSettingsEncryptedResponse()
        msg.ParseFromString(data)

        return msg

class IdTokenRemoteService:    
    @staticmethod
    def getIdTokenRequest(request: GetIdTokenRequest): 
        msg = request.SerializeToString()
        
        return 385, msg # Xmm: 0

    @staticmethod
    def getIdTokenResponse(response: Response) -> GetIdTokenResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetIdTokenResponse()
        msg.ParseFromString(data)

        return msg

class AppGalleryInAppRemoteService:    
    @staticmethod
    def buyInAppRequest(request: AppGalleryBuyInappRequest): 
        msg = request.SerializeToString()
        
        return 395, msg # Xmm: 0

    @staticmethod
    def buyInAppResponse(response: Response) -> AppGalleryBuyInappResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AppGalleryBuyInappResponse()
        msg.ParseFromString(data)

        return msg

class GoogleInAppRemoteService:    
    @staticmethod
    def buyInApp2Request(request: GoogleBuyInappRequest): 
        msg = request.SerializeToString()
        
        return 390, msg # Xmm: 0

    @staticmethod
    def buyInApp2Response(response: Response) -> GoogleBuyInappResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GoogleBuyInappResponse()
        msg.ParseFromString(data)

        return msg

class GameCenterAuthRemoteService:    
    @staticmethod
    def linkAuthRequest(request: GameCenterLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 356, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> GameCenterLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GameCenterLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def unLinkAuthRequest(request: GameCenterUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 357, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> GameCenterUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GameCenterUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def encryptedAuth2Request(request: GameCenterAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 355, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> GameCenterAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GameCenterAuthResponse()
        msg.ParseFromString(data)

        return msg

class OffersRemoteService:    
    @staticmethod
    def getSpecialOffersRequest(request: GetSpecialOffersRequest): 
        msg = request.SerializeToString()
        
        return 300, msg # Xmm: 0

    @staticmethod
    def getSpecialOffersResponse(response: Response) -> GetSpecialOffersResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetSpecialOffersResponse()
        msg.ParseFromString(data)

        return msg

class FacebookAuthRemoteService:    
    @staticmethod
    def encryptedAuth2Request(request: FacebookAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 375, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> FacebookAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = FacebookAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def unLinkAuthRequest(request: FacebookUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 377, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> FacebookUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = FacebookUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def linkAuthRequest(request: FacebookLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 376, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> FacebookLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = FacebookLinkAuthResponse()
        msg.ParseFromString(data)

        return msg

class AccountLinkRemoteService:    
    @staticmethod
    def getLinkedAuthRequest(request: GetLinkedAuthRequest): 
        msg = request.SerializeToString()
        
        return 260, msg # Xmm: 0

    @staticmethod
    def getLinkedAuthResponse(response: Response) -> GetLinkedAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetLinkedAuthResponse()
        msg.ParseFromString(data)

        return msg

class GoogleAuthRemoteService:    
    @staticmethod
    def encryptedAuth2Request(request: GoogleAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 315, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> GoogleAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GoogleAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def unLinkAuthRequest(request: GoogleUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 317, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> GoogleUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GoogleUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def linkAuthRequest(request: GoogleLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 316, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> GoogleLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = GoogleLinkAuthResponse()
        msg.ParseFromString(data)

        return msg

class SeasonalStatsRemoteService:    
    @staticmethod
    def getStatsForSeasonRequest(request: GetStatsForSeasonRequest): 
        msg = request.SerializeToString()
        
        return 326, msg # Xmm: 0

    @staticmethod
    def getStatsForSeasonResponse(response: Response) -> GetPlayerStatsForSeasonResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerStatsForSeasonResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getClanStatsForSeasonRequest(request: GetClanStatsForSeasonRequest): 
        msg = request.SerializeToString()
        
        return 328, msg # Xmm: 0

    @staticmethod
    def getClanStatsForSeasonResponse(response: Response) -> GetClanStatsForSeasonResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanStatsForSeasonResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerStatsForSeasonRequest(request: GetPlayerStatsForSeasonRequest): 
        msg = request.SerializeToString()
        
        return 325, msg # Xmm: 0

    @staticmethod
    def getPlayerStatsForSeasonResponse(response: Response) -> GetPlayerStatsForSeasonResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerStatsForSeasonResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getCurrentClanStatsForSeasonRequest(request: GetCurrentClanStatsForSeasonRequest): 
        msg = request.SerializeToString()
        
        return 327, msg # Xmm: 0

    @staticmethod
    def getCurrentClanStatsForSeasonResponse(response: Response) -> GetCurrentClanStatsForSeasonResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetCurrentClanStatsForSeasonResponse()
        msg.ParseFromString(data)

        return msg

class DlcRemoteService:    
    @staticmethod
    def getAllReleasedDlcRequest(request: ReleasedDlcRequest): 
        msg = request.SerializeToString()
        
        return 226, msg # Xmm: 0

    @staticmethod
    def getAllReleasedDlcResponse(response: Response) -> DlcResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DlcResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getAllDlcRequest(request: PreviewDlcRequest): 
        msg = request.SerializeToString()
        
        return 225, msg # Xmm: 0

    @staticmethod
    def getAllDlcResponse(response: Response) -> DlcResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DlcResponse()
        msg.ParseFromString(data)

        return msg

class ClanStatsRemoteService:    
    @staticmethod
    def getClanStatsRequest(request: GetClanStatsRequest): 
        msg = request.SerializeToString()
        
        return 241, msg # Xmm: 0

    @staticmethod
    def getClanStatsResponse(response: Response) -> GetClanStatsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetClanStatsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getCurrentClanStatsRequest(request: GetCurrentClanStatsRequest): 
        msg = request.SerializeToString()
        
        return 240, msg # Xmm: 0

    @staticmethod
    def getCurrentClanStatsResponse(response: Response) -> GetCurrentClanStatsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetCurrentClanStatsResponse()
        msg.ParseFromString(data)

        return msg

class GameAnnouncementRemoteService:    
    @staticmethod
    def getAllAnnouncementsRequest(request: GetAllGameAnnouncementsRequest): 
        msg = request.SerializeToString()
        
        return 280, msg # Xmm: 0

    @staticmethod
    def getAllAnnouncementsResponse(response: Response) -> GetAllGameAnnouncementsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetAllGameAnnouncementsResponse()
        msg.ParseFromString(data)

        return msg

class BoltRemoteService:    
    @staticmethod
    def unsubscribe2Request(request: UnsubscribeRequest): 
        msg = request.SerializeToString()
        
        return 42, msg # Xmm: 0

    @staticmethod
    def unsubscribe2Response(response: Response) -> UnsubscribeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = UnsubscribeResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def subscribe2Request(request: SubscribeRequest): 
        msg = request.SerializeToString()
        
        return 41, msg # Xmm: 0

    @staticmethod
    def subscribe2Response(response: Response) -> SubscribeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SubscribeResponse()
        msg.ParseFromString(data)

        return msg

class PlayerRemoteService:    
    @staticmethod
    def setAwayStatus2Request(request: SetAwayStatusRequest): 
        msg = request.SerializeToString()
        
        return 20, msg # Xmm: 0

    @staticmethod
    def setAwayStatus2Response(response: Response) -> SetAwayStatusResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetAwayStatusResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setPlayerAvatar2Request(request: SetPlayerAvatarRequest): 
        msg = request.SerializeToString()
        
        return 25, msg # Xmm: 0

    @staticmethod
    def setPlayerAvatar2Response(response: Response) -> SetPlayerAvatarResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetPlayerAvatarResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setPlayerFirebaseToken2Request(request: SetPlayerFirebaseTokenRequest): 
        msg = request.SerializeToString()
        
        return 24, msg # Xmm: 0

    @staticmethod
    def setPlayerFirebaseToken2Response(response: Response) -> SetPlayerFirebaseTokenResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetPlayerFirebaseTokenResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerSettings2Request(request: GetPlayerSettingsRequest): 
        msg = request.SerializeToString()
        
        return 22, msg # Xmm: 0

    @staticmethod
    def getPlayerSettings2Response(response: Response) -> GetPlayerSettingsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerSettingsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setPlayerSettings2Request(request: SetPlayerSettingsRequest): 
        msg = request.SerializeToString()
        
        return 27, msg # Xmm: 0

    @staticmethod
    def setPlayerSettings2Response(response: Response) -> SetPlayerSettingsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetPlayerSettingsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setOnlineStatus2Request(request: SetOnlineStatusRequest): 
        msg = request.SerializeToString()
        
        return 21, msg # Xmm: 0

    @staticmethod
    def setOnlineStatus2Response(response: Response) -> SetOnlineStatusResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetOnlineStatusResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setDefaultAvatarRequest(request: SetDefaultAvatarRequest): 
        msg = request.SerializeToString()
        
        return 28, msg # Xmm: 0

    @staticmethod
    def setDefaultAvatarResponse(response: Response) -> SetDefaultAvatarResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetDefaultAvatarResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setPlayerName2Request(request: SetPlayerNameRequest): 
        msg = request.SerializeToString()
        
        return 26, msg # Xmm: 0

    @staticmethod
    def setPlayerName2Response(response: Response) -> SetPlayerNameResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetPlayerNameResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayer2Request(request: GetPlayerRequest): 
        msg = request.SerializeToString()
        
        return 23, msg # Xmm: 0

    @staticmethod
    def getPlayer2Response(response: Response) -> GetPlayerResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerResponse()
        msg.ParseFromString(data)

        return msg

class RateGameRemoteService:    
    @staticmethod
    def getLastRateGameRequest(request: GetLastRateGameRequest): 
        msg = request.SerializeToString()
        
        return 250, msg # Xmm: 0

    @staticmethod
    def getLastRateGameResponse(response: Response) -> GetLastRateGameResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetLastRateGameResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def askLaterRequest(request: AskLaterRequest): 
        msg = request.SerializeToString()
        
        return 251, msg # Xmm: 0

    @staticmethod
    def askLaterResponse(response: Response) -> AskLaterResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AskLaterResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def dontAskLaterRequest(request: DontAskLaterRequest): 
        msg = request.SerializeToString()
        
        return 253, msg # Xmm: 0

    @staticmethod
    def dontAskLaterResponse(response: Response) -> DontAskLaterResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DontAskLaterResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def rateGameRequest(request: RateGameRequest): 
        msg = request.SerializeToString()
        
        return 252, msg # Xmm: 0

    @staticmethod
    def rateGameResponse(response: Response) -> RateGameResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RateGameResponse()
        msg.ParseFromString(data)

        return msg

class AvatarRemoteService:    
    @staticmethod
    def getDefaultAvatarsRequest(request: GetDefaultAvatarsRequest): 
        msg = request.SerializeToString()
        
        return 275, msg # Xmm: 0

    @staticmethod
    def getDefaultAvatarsResponse(response: Response) -> GetDefaultAvatarsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetDefaultAvatarsResponse()
        msg.ParseFromString(data)

        return msg

class ChatRemoteService:    
    @staticmethod
    def readFriendMsgs2Request(request: ReadFriendMsgsRequest): 
        msg = request.SerializeToString()
        
        return 193, msg # Xmm: 0

    @staticmethod
    def readFriendMsgs2Response(response: Response) -> ReadFriendMsgsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ReadFriendMsgsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def deleteFriendMsgs2Request(request: DeleteFriendMsgsRequest): 
        msg = request.SerializeToString()
        
        return 195, msg # Xmm: 0

    @staticmethod
    def deleteFriendMsgs2Response(response: Response) -> DeleteFriendMsgsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeleteFriendMsgsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def sendFriendMsg2Request(request: SendFriendMsgRequest): 
        msg = request.SerializeToString()
        
        return 192, msg # Xmm: 0

    @staticmethod
    def sendFriendMsg2Response(response: Response) -> SendFriendMsgResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SendFriendMsgResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getChatUserRequest(request: GetChatUserRequest): 
        msg = request.SerializeToString()
        
        return 194, msg # Xmm: 0

    @staticmethod
    def getChatUserResponse(response: Response) -> GetChatUserResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetChatUserResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getChatUsersLiteRequest(request: GetChatUsersLiteRequest): 
        msg = request.SerializeToString()
        
        return 190, msg # Xmm: 0

    @staticmethod
    def getChatUsersLiteResponse(response: Response) -> GetChatUsersLiteResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetChatUsersLiteResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getFriendMsgsByOffset2Request(request: GetFriendMsgsByOffsetRequest): 
        msg = request.SerializeToString()
        
        return 191, msg # Xmm: 0

    @staticmethod
    def getFriendMsgsByOffset2Response(response: Response) -> GetFriendMsgsByOffsetResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetFriendMsgsByOffsetResponse()
        msg.ParseFromString(data)

        return msg

class MatchmakingRemoteService:    
    @staticmethod
    def setLobbyData2Request(request: SetLobbyDataRequest): 
        msg = request.SerializeToString()
        
        return 70, msg # Xmm: 0

    @staticmethod
    def setLobbyData2Response(response: Response) -> SetLobbyDataResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyDataResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setLobbyOwner2Request(request: SetLobbyOwnerRequest): 
        msg = request.SerializeToString()
        
        return 88, msg # Xmm: 0

    @staticmethod
    def setLobbyOwner2Response(response: Response) -> SetLobbyOwnerResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyOwnerResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def joinLobbyAs2Request(request: JoinLobbyAsRequest): 
        msg = request.SerializeToString()
        
        return 76, msg # Xmm: 0

    @staticmethod
    def joinLobbyAs2Response(response: Response) -> JoinLobbyAsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = JoinLobbyAsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def createLobbyWithSpectators2Request(request: CreateLobbyWithSpectatorsRequest): 
        msg = request.SerializeToString()
        
        return 77, msg # Xmm: 0

    @staticmethod
    def createLobbyWithSpectators2Response(response: Response) -> CreateLobbyWithSpectatorsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CreateLobbyWithSpectatorsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getInvitesToLobby2Request(request: GetInvitesToLobbyRequest): 
        msg = request.SerializeToString()
        
        return 72, msg # Xmm: 0

    @staticmethod
    def getInvitesToLobby2Response(response: Response) -> GetInvitesToLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetInvitesToLobbyResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setLobbyMaxSpectators2Request(request: SetLobbyMaxSpectatorsRequest): 
        msg = request.SerializeToString()
        
        return 83, msg # Xmm: 0

    @staticmethod
    def setLobbyMaxSpectators2Response(response: Response) -> SetLobbyMaxSpectatorsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyMaxSpectatorsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def revokePlayerInvitationToLobby2Request(request: RevokePlayerInvitationToLobbyRequest): 
        msg = request.SerializeToString()
        
        return 86, msg # Xmm: 0

    @staticmethod
    def revokePlayerInvitationToLobby2Response(response: Response) -> RevokePlayerInvitationToLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RevokePlayerInvitationToLobbyResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def kickPlayerFromLobby2Request(request: KickPlayerFromLobbyRequest): 
        msg = request.SerializeToString()
        
        return 84, msg # Xmm: 0

    @staticmethod
    def kickPlayerFromLobby2Response(response: Response) -> KickPlayerFromLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = KickPlayerFromLobbyResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setLobbyMaxMembers2Request(request: SetLobbyMaxMembersRequest): 
        msg = request.SerializeToString()
        
        return 78, msg # Xmm: 0

    @staticmethod
    def setLobbyMaxMembers2Response(response: Response) -> SetLobbyMaxMembersResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyMaxMembersResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getLobby2Request(request: GetLobbyRequest): 
        msg = request.SerializeToString()
        
        return 82, msg # Xmm: 0

    @staticmethod
    def getLobby2Response(response: Response) -> GetLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetLobbyResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setLobbyType2Request(request: SetLobbyTypeRequest): 
        msg = request.SerializeToString()
        
        return 81, msg # Xmm: 0

    @staticmethod
    def setLobbyType2Response(response: Response) -> SetLobbyTypeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyTypeResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def sendLobbyChatMsg2Request(request: SendLobbyChatMsgRequest): 
        msg = request.SerializeToString()
        
        return 74, msg # Xmm: 0

    @staticmethod
    def sendLobbyChatMsg2Response(response: Response) -> SendLobbyChatMsgResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SendLobbyChatMsgResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def leaveLobby2Request(request: LeaveLobbyRequest): 
        msg = request.SerializeToString()
        
        return 75, msg # Xmm: 0

    @staticmethod
    def leaveLobby2Response(response: Response) -> LeaveLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = LeaveLobbyResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def searchLobbyRequest(request: SearchLobbyRequest): 
        msg = request.SerializeToString()
        
        return 79, msg # Xmm: 0

    @staticmethod
    def searchLobbyResponse(response: Response) -> SearchLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SearchLobbyResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def invitePlayerToLobbyAs2Request(request: InvitePlayerToLobbyAsRequest): 
        msg = request.SerializeToString()
        
        return 73, msg # Xmm: 0

    @staticmethod
    def invitePlayerToLobbyAs2Response(response: Response) -> InvitePlayerToLobbyAsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = InvitePlayerToLobbyAsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setLobbyPhotonGame2Request(request: SetLobbyPhotonGameRequest): 
        msg = request.SerializeToString()
        
        return 80, msg # Xmm: 0

    @staticmethod
    def setLobbyPhotonGame2Response(response: Response) -> SetLobbyPhotonGameResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyPhotonGameResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def changeLobbyOtherPlayerType2Request(request: ChangeLobbyOtherPlayerTypeRequest): 
        msg = request.SerializeToString()
        
        return 87, msg # Xmm: 0

    @staticmethod
    def changeLobbyOtherPlayerType2Response(response: Response) -> ChangeLobbyOtherPlayerTypeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ChangeLobbyOtherPlayerTypeResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def setLobbyJoinable2Request(request: SetLobbyJoinableRequest): 
        msg = request.SerializeToString()
        
        return 71, msg # Xmm: 0

    @staticmethod
    def setLobbyJoinable2Response(response: Response) -> SetLobbyJoinableResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SetLobbyJoinableResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def refuseInvitationToLobby2Request(request: RefuseInvitationToLobbyRequest): 
        msg = request.SerializeToString()
        
        return 85, msg # Xmm: 0

    @staticmethod
    def refuseInvitationToLobby2Response(response: Response) -> RefuseInvitationToLobbyResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RefuseInvitationToLobbyResponse()
        msg.ParseFromString(data)

        return msg

class MarketplaceRemoteService:    
    @staticmethod
    def getTrades2Request(request: GetTradesRequest): 
        msg = request.SerializeToString()
        
        return 16, msg # Xmm: 0

    @staticmethod
    def getTrades2Response(response: Response) -> GetTradesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetTradesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getFilteredTradeOpenSaleRequestsRequest(request: GetTradeOpenSaleRequestsRequest): 
        msg = request.SerializeToString()
        
        return 15, msg # Xmm: 0

    @staticmethod
    def getFilteredTradeOpenSaleRequestsResponse(response: Response) -> GetTradeOpenSaleRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetTradeOpenSaleRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerClosedRequests2Request(request: GetPlayerClosedRequestsRequest): 
        msg = request.SerializeToString()
        
        return 10, msg # Xmm: 0

    @staticmethod
    def getPlayerClosedRequests2Response(response: Response) -> GetPlayerClosedRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerClosedRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def cancelRequest2Request(request: CancelRequestRequest): 
        msg = request.SerializeToString()
        
        return 13, msg # Xmm: 0

    @staticmethod
    def cancelRequest2Response(response: Response) -> CancelRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CancelRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getTrade2Request(request: GetTradeRequest): 
        msg = request.SerializeToString()
        
        return 8, msg # Xmm: 0

    @staticmethod
    def getTrade2Response(response: Response) -> GetTradeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetTradeResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getMarketplaceSettings2Request(request: GetMarketplaceSettingsRequest): 
        msg = request.SerializeToString()
        
        return 6, msg # Xmm: 0

    @staticmethod
    def getMarketplaceSettings2Response(response: Response) -> GetMarketplaceSettingsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetMarketplaceSettingsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerOpenRequests2Request(request: GetPlayerOpenRequestsRequest): 
        msg = request.SerializeToString()
        
        return 7, msg # Xmm: 0

    @staticmethod
    def getPlayerOpenRequests2Response(response: Response) -> GetPlayerOpenRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerOpenRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerProcessingRequests2Request(request: GetPlayerProcessingRequestRequest): 
        msg = request.SerializeToString()
        
        return 5, msg # Xmm: 0

    @staticmethod
    def getPlayerProcessingRequests2Response(response: Response) -> GetPlayerProcessingRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerProcessingRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getTradeOpenSaleRequests2Request(request: GetTradeOpenSaleRequestsRequest): 
        msg = request.SerializeToString()
        
        return 14, msg # Xmm: 0

    @staticmethod
    def getTradeOpenSaleRequests2Response(response: Response) -> GetTradeOpenSaleRequestsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetTradeOpenSaleRequestsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def createPurchaseRequestBySale2Request(request: CreatePurchaseRequestBySaleRequest): 
        msg = request.SerializeToString()
        
        return 12, msg # Xmm: 0

    @staticmethod
    def createPurchaseRequestBySale2Response(response: Response) -> CreatePurchaseRequestBySaleResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CreatePurchaseRequestBySaleResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def createPurchaseRequest2Request(request: CreatePurchaseRequestRequest): 
        msg = request.SerializeToString()
        
        return 11, msg # Xmm: 0

    @staticmethod
    def createPurchaseRequest2Response(response: Response) -> CreatePurchaseRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CreatePurchaseRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def createSaleRequest(request: CreateSaleRequest): 
        msg = request.SerializeToString()
        
        return 9, msg # Xmm: 0

    @staticmethod
    def createSaleResponse(response: Response) -> CreateSaleResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CreateSaleResponse()
        msg.ParseFromString(data)

        return msg

class HandshakeRemoteService:    
    @staticmethod
    def encryptedHandshakeRequest(request: Handshake, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 3, msg # Xmm: 0

    @staticmethod
    def encryptedHandshakeResponse(response: Response, cipher) -> HandshakeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = HandshakeResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def encryptedHandshakeRequest(request: GACHFBFBBEHDAAD, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 3, msg # Xmm: 0

    @staticmethod
    def encryptedHandshakeResponse(response: Response, cipher) -> ADHHEGBDFBEBGGC:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = ADHHEGBDFBEBGGC()
        msg.ParseFromString(data)

        return msg

class StorageRemoteService:    
    @staticmethod
    def readFilesRequest(request: ReadFilesRequest): 
        msg = request.SerializeToString()
        
        return 172, msg # Xmm: 0

    @staticmethod
    def readFilesResponse(response: Response) -> ReadFilesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ReadFilesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def writeFile2Request(request: WriteFileRequest): 
        msg = request.SerializeToString()
        
        return 171, msg # Xmm: 0

    @staticmethod
    def writeFile2Response(response: Response) -> WriteFileResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = WriteFileResponse()
        msg.ParseFromString(data)

        return msg

class HuaweiAuthRemoteService:    
    @staticmethod
    def linkAuthRequest(request: HuaweiLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 366, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> HuaweiLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = HuaweiLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def unLinkAuthRequest(request: HuaweiUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 367, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> HuaweiUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = HuaweiUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def encryptedAuth2Request(request: HuaweiAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 365, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> HuaweiAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = HuaweiAuthResponse()
        msg.ParseFromString(data)

        return msg

class SystemMessagesRemoteService:    
    @staticmethod
    def getSystemMessagesRequest(request: GetSystemMessagesRequest): 
        msg = request.SerializeToString()
        
        return 305, msg # Xmm: 0

    @staticmethod
    def getSystemMessagesResponse(response: Response) -> GetSystemMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetSystemMessagesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def readSystemMessagesRequest(request: ReadSystemMessagesRequest): 
        msg = request.SerializeToString()
        
        return 308, msg # Xmm: 0

    @staticmethod
    def readSystemMessagesResponse(response: Response) -> ReadSystemMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ReadSystemMessagesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getSystemMessageDetailsRequest(request: GetSystemMessageDetailsRequest): 
        msg = request.SerializeToString()
        
        return 307, msg # Xmm: 0

    @staticmethod
    def getSystemMessageDetailsResponse(response: Response) -> GetSystemMessageDetailsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetSystemMessageDetailsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def countUnreadSystemMessagesRequest(request: CountUnreadSystemMessagesRequest): 
        msg = request.SerializeToString()
        
        return 306, msg # Xmm: 0

    @staticmethod
    def countUnreadSystemMessagesResponse(response: Response) -> CountUnreadSystemMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = CountUnreadSystemMessagesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def deleteSystemMessagesRequest(request: DeleteSystemMessagesRequest): 
        msg = request.SerializeToString()
        
        return 309, msg # Xmm: 0

    @staticmethod
    def deleteSystemMessagesResponse(response: Response) -> DeleteSystemMessagesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeleteSystemMessagesResponse()
        msg.ParseFromString(data)

        return msg

class NewsFeedRemoteService:    
    @staticmethod
    def getItems2Request(request: GetItemsRequest): 
        msg = request.SerializeToString()
        
        return 295, msg # Xmm: 0

    @staticmethod
    def getItems2Response(response: Response) -> GetItemsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetItemsResponse()
        msg.ParseFromString(data)

        return msg

class AppleIdAuthRemoteService:    
    @staticmethod
    def unLinkAuthRequest(request: AppleIdUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 347, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> AppleIdUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AppleIdUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def linkAuthRequest(request: AppleIdLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 346, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> AppleIdLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = AppleIdLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def encryptedAuth2Request(request: AppleIdAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 345, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> AppleIdAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = AppleIdAuthResponse()
        msg.ParseFromString(data)

        return msg

class InAppRemoteService:    
    @staticmethod
    def subscribeCreatorRequest(request: SubscribeCreatorRequest): 
        msg = request.SerializeToString()
        
        return 291, msg # Xmm: 0

    @staticmethod
    def subscribeCreatorResponse(response: Response) -> SubscribeCreatorResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SubscribeCreatorResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def findCreatorSubscriptionRequest(request: GetSubscribedCreatorRequest): 
        msg = request.SerializeToString()
        
        return 290, msg # Xmm: 0

    @staticmethod
    def findCreatorSubscriptionResponse(response: Response) -> GetSubscribedCreatorResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetSubscribedCreatorResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def findCreatorRequest(request: FindCreatorRequest): 
        msg = request.SerializeToString()
        
        return 292, msg # Xmm: 0

    @staticmethod
    def findCreatorResponse(response: Response) -> FindCreatorResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = FindCreatorResponse()
        msg.ParseFromString(data)

        return msg

class VkAuthRemoteService:    
    @staticmethod
    def unLinkAuthRequest(request: VkUnLinkAuthRequest): 
        msg = request.SerializeToString()
        
        return 337, msg # Xmm: 0

    @staticmethod
    def unLinkAuthResponse(response: Response) -> VkUnLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = VkUnLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def linkAuthRequest(request: VkLinkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 336, msg # Xmm: 0

    @staticmethod
    def linkAuthResponse(response: Response, cipher) -> VkLinkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = VkLinkAuthResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def encryptedAuth2Request(request: VkAuthRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 335, msg # Xmm: 0

    @staticmethod
    def encryptedAuth2Response(response: Response, cipher) -> VkAuthResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = VkAuthResponse()
        msg.ParseFromString(data)

        return msg

class FriendsRemoteService:    
    @staticmethod
    def ignoreFriendRequest2Request(request: IgnoreFriendRequestRequest): 
        msg = request.SerializeToString()
        
        return 158, msg # Xmm: 0

    @staticmethod
    def ignoreFriendRequest2Response(response: Response) -> IgnoreFriendRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = IgnoreFriendRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerFriends2Request(request: GetPlayerFriendsRequest): 
        msg = request.SerializeToString()
        
        return 150, msg # Xmm: 0

    @staticmethod
    def getPlayerFriends2Response(response: Response) -> GetPlayerFriendsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerFriendsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerFriendByUid2Request(request: GetPlayerFriendByUidRequest): 
        msg = request.SerializeToString()
        
        return 161, msg # Xmm: 0

    @staticmethod
    def getPlayerFriendByUid2Response(response: Response) -> GetPlayerFriendByUidResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerFriendByUidResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def revokeFriendRequest2Request(request: RevokeFriendRequestRequest): 
        msg = request.SerializeToString()
        
        return 155, msg # Xmm: 0

    @staticmethod
    def revokeFriendRequest2Response(response: Response) -> RevokeFriendRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RevokeFriendRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerFriendsIds2Request(request: GetPlayerFriendsIdsRequest): 
        msg = request.SerializeToString()
        
        return 152, msg # Xmm: 0

    @staticmethod
    def getPlayerFriendsIds2Response(response: Response) -> GetPlayerFriendsIdsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerFriendsIdsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def acceptFriendRequest2Request(request: AcceptFriendRequestRequest): 
        msg = request.SerializeToString()
        
        return 156, msg # Xmm: 0

    @staticmethod
    def acceptFriendRequest2Response(response: Response) -> AcceptFriendRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = AcceptFriendRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def searchPlayers2Request(request: SearchPlayersRequest): 
        msg = request.SerializeToString()
        
        return 154, msg # Xmm: 0

    @staticmethod
    def searchPlayers2Response(response: Response) -> SearchPlayersResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SearchPlayersResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerFriendById2Request(request: GetPlayerFriendByIdRequest): 
        msg = request.SerializeToString()
        
        return 151, msg # Xmm: 0

    @staticmethod
    def getPlayerFriendById2Response(response: Response) -> GetPlayerFriendByIdResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerFriendByIdResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def sendFriendRequest2Request(request: SendFriendRequestRequest): 
        msg = request.SerializeToString()
        
        return 153, msg # Xmm: 0

    @staticmethod
    def sendFriendRequest2Response(response: Response) -> SendFriendRequestResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = SendFriendRequestResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def blockFriend2Request(request: BlockFriendRequest): 
        msg = request.SerializeToString()
        
        return 159, msg # Xmm: 0

    @staticmethod
    def blockFriend2Response(response: Response) -> BlockFriendResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = BlockFriendResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def removeFriend2Request(request: RemoveFriendRequest): 
        msg = request.SerializeToString()
        
        return 157, msg # Xmm: 0

    @staticmethod
    def removeFriend2Response(response: Response) -> RemoveFriendResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RemoveFriendResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def unblockFriend2Request(request: UnblockFriendRequest): 
        msg = request.SerializeToString()
        
        return 160, msg # Xmm: 0

    @staticmethod
    def unblockFriend2Response(response: Response) -> UnblockFriendResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = UnblockFriendResponse()
        msg.ParseFromString(data)

        return msg

class GameEventRemoteService:    
    @staticmethod
    def getCachedPlayerGameEventsRequest(request: GetCachedPlayerGameEventsRequest): 
        msg = request.SerializeToString()
        
        return 216, msg # Xmm: 0

    @staticmethod
    def getCachedPlayerGameEventsResponse(response: Response) -> GetCachedPlayerGameEventsResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetCachedPlayerGameEventsResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def getPlayerGameEventsProgressesRequest(request: GetPlayerGameEventsProgressesRequest): 
        msg = request.SerializeToString()
        
        return 215, msg # Xmm: 0

    @staticmethod
    def getPlayerGameEventsProgressesResponse(response: Response) -> GetPlayerGameEventsProgressesResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = GetPlayerGameEventsProgressesResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def processChallengeRequest(request: ProgressChallengeRequest): 
        msg = request.SerializeToString()
        
        return 217, msg # Xmm: 0

    @staticmethod
    def processChallengeResponse(response: Response) -> ProgressChallengeResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = ProgressChallengeResponse()
        msg.ParseFromString(data)

        return msg

class GdprRemoteService:    
    @staticmethod
    def recoverAccountRequest(request: RecoverAccountRequest): 
        msg = request.SerializeToString()
        
        return 405, msg # Xmm: 0

    @staticmethod
    def recoverAccountResponse(response: Response) -> RecoverAccountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = RecoverAccountResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def createRequestEncryptedRequest(request: CreateRequestEncryptedRequest, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 407, msg # Xmm: 0

    @staticmethod
    def createRequestEncryptedResponse(response: Response, cipher) -> CreateRequestEncryptedResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = CreateRequestEncryptedResponse()
        msg.ParseFromString(data)

        return msg
    
    @staticmethod
    def deleteAccountRequest(request: DeleteAccountRequest): 
        msg = request.SerializeToString()
        
        return 406, msg # Xmm: 0

    @staticmethod
    def deleteAccountResponse(response: Response) -> DeleteAccountResponse:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        
        msg = DeleteAccountResponse()
        msg.ParseFromString(data)

        return msg

class HelloRemoteService:    
    @staticmethod
    def helloRequest(request: CHGACEEHFADEDHH, cipher): 
        msg = request.SerializeToString()
        msg = cipher.encrypt(msg)
        return 1, msg # Xmm: 0

    @staticmethod
    def helloResponse(response: Response, cipher) -> BBFGDBCEGCBFBEE:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

        data = response.data[0].one 
        data = cipher.decrypt(data)
        msg = BBFGDBCEGCBFBEE()
        msg.ParseFromString(data)

        return msg

