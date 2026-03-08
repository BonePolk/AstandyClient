# Raw

## Raw services

### AchievementRemoteService
    
#### getCurrentPlayerAchievements

```python
request = GetCurrentPlayerAchievementsRequest()
# some vars here

response = client.raw.AchievementRemoteService.getCurrentPlayerAchievementsResponse(
    await client.send_request(
        *client.raw.AchievementRemoteService.getCurrentPlayerAchievementsRequest(
            request
        )
    )
)

client.logger.info(f'getCurrentPlayerAchievements response: {response}')
```
    
#### getPlayerAchievements

```python
request = GetPlayerAchievementsRequest()
# some vars here

response = client.raw.AchievementRemoteService.getPlayerAchievementsResponse(
    await client.send_request(
        *client.raw.AchievementRemoteService.getPlayerAchievementsRequest(
            request
        )
    )
)

client.logger.info(f'getPlayerAchievements response: {response}')
```
    
#### getAchievementDefinitions

```python
request = GetAchievementDefinitionsRequest()
# some vars here

response = client.raw.AchievementRemoteService.getAchievementDefinitionsResponse(
    await client.send_request(
        *client.raw.AchievementRemoteService.getAchievementDefinitionsRequest(
            request
        )
    )
)

client.logger.info(f'getAchievementDefinitions response: {response}')
```
### ClanRemoteService
    
#### assignRoleToMember2

```python
request = AssignRoleToMemberRequest()
# some vars here

response = client.raw.ClanRemoteService.assignRoleToMember2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.assignRoleToMember2Request(
            request
        )
    )
)

client.logger.info(f'assignRoleToMember2 response: {response}')
```
    
#### validateClanTag2

```python
request = ValidateClanTagRequest()
# some vars here

response = client.raw.ClanRemoteService.validateClanTag2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.validateClanTag2Request(
            request
        )
    )
)

client.logger.info(f'validateClanTag2 response: {response}')
```
    
#### getClanMembers2

```python
request = GetClanMembersRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanMembers2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanMembers2Request(
            request
        )
    )
)

client.logger.info(f'getClanMembers2 response: {response}')
```
    
#### getClan2

```python
request = GetClanRequest()
# some vars here

response = client.raw.ClanRemoteService.getClan2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClan2Request(
            request
        )
    )
)

client.logger.info(f'getClan2 response: {response}')
```
    
#### leaveClan2

```python
request = LeaveClanRequest()
# some vars here

response = client.raw.ClanRemoteService.leaveClan2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.leaveClan2Request(
            request
        )
    )
)

client.logger.info(f'leaveClan2 response: {response}')
```
    
#### setClanAvatar2

```python
request = SetClanAvatarRequest()
# some vars here

response = client.raw.ClanRemoteService.setClanAvatar2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.setClanAvatar2Request(
            request
        )
    )
)

client.logger.info(f'setClanAvatar2 response: {response}')
```
    
#### deleteClosedJoinRequest2

```python
request = DeleteClosedJoinRequestRequest()
# some vars here

response = client.raw.ClanRemoteService.deleteClosedJoinRequest2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.deleteClosedJoinRequest2Request(
            request
        )
    )
)

client.logger.info(f'deleteClosedJoinRequest2 response: {response}')
```
    
#### declineInviteRequest2

```python
request = DeclineInviteRequestRequest()
# some vars here

response = client.raw.ClanRemoteService.declineInviteRequest2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.declineInviteRequest2Request(
            request
        )
    )
)

client.logger.info(f'declineInviteRequest2 response: {response}')
```
    
#### declineJoinRequest2

```python
request = DeclineJoinRequestRequest()
# some vars here

response = client.raw.ClanRemoteService.declineJoinRequest2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.declineJoinRequest2Request(
            request
        )
    )
)

client.logger.info(f'declineJoinRequest2 response: {response}')
```
    
#### getClanSettings2

```python
request = GetClanSettingsRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanSettings2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanSettings2Request(
            request
        )
    )
)

client.logger.info(f'getClanSettings2 response: {response}')
```
    
#### getClanJoinRequests2

```python
request = GetClanJoinRequestsRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanJoinRequests2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanJoinRequests2Request(
            request
        )
    )
)

client.logger.info(f'getClanJoinRequests2 response: {response}')
```
    
#### assignLeaderRole2

```python
request = AssignLeaderRoleRequest()
# some vars here

response = client.raw.ClanRemoteService.assignLeaderRole2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.assignLeaderRole2Request(
            request
        )
    )
)

client.logger.info(f'assignLeaderRole2 response: {response}')
```
    
#### setClanDescription2

```python
request = SetClanDescriptionRequest()
# some vars here

response = client.raw.ClanRemoteService.setClanDescription2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.setClanDescription2Request(
            request
        )
    )
)

client.logger.info(f'setClanDescription2 response: {response}')
```
    
#### findClan2

```python
request = FindClanRequest()
# some vars here

response = client.raw.ClanRemoteService.findClan2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.findClan2Request(
            request
        )
    )
)

client.logger.info(f'findClan2 response: {response}')
```
    
#### deleteClosedInviteRequest2

```python
request = DeleteClosedInviteRequestRequest()
# some vars here

response = client.raw.ClanRemoteService.deleteClosedInviteRequest2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.deleteClosedInviteRequest2Request(
            request
        )
    )
)

client.logger.info(f'deleteClosedInviteRequest2 response: {response}')
```
    
#### getPlayerClosedJoinRequestsCount2

```python
request = GetPlayerClosedJoinRequestsCountRequest()
# some vars here

response = client.raw.ClanRemoteService.getPlayerClosedJoinRequestsCount2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getPlayerClosedJoinRequestsCount2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerClosedJoinRequestsCount2 response: {response}')
```
    
#### requestToJoinClan2

```python
request = RequestToJoinClanRequest()
# some vars here

response = client.raw.ClanRemoteService.requestToJoinClan2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.requestToJoinClan2Request(
            request
        )
    )
)

client.logger.info(f'requestToJoinClan2 response: {response}')
```
    
#### cancelJoinRequest2

```python
request = CancelJoinRequestRequest()
# some vars here

response = client.raw.ClanRemoteService.cancelJoinRequest2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.cancelJoinRequest2Request(
            request
        )
    )
)

client.logger.info(f'cancelJoinRequest2 response: {response}')
```
    
#### changeClanType2

```python
request = ChangeClanTypeRequest()
# some vars here

response = client.raw.ClanRemoteService.changeClanType2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.changeClanType2Request(
            request
        )
    )
)

client.logger.info(f'changeClanType2 response: {response}')
```
    
#### getClanInviteRequests2

```python
request = GetClanInviteRequestsRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanInviteRequests2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanInviteRequests2Request(
            request
        )
    )
)

client.logger.info(f'getClanInviteRequests2 response: {response}')
```
    
#### getPlayerInviteRequests2

```python
request = GetPlayerInviteRequestsRequest()
# some vars here

response = client.raw.ClanRemoteService.getPlayerInviteRequests2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getPlayerInviteRequests2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerInviteRequests2 response: {response}')
```
    
#### getRecommendedClans2

```python
request = GetRecommendedClansRequest()
# some vars here

response = client.raw.ClanRemoteService.getRecommendedClans2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getRecommendedClans2Request(
            request
        )
    )
)

client.logger.info(f'getRecommendedClans2 response: {response}')
```
    
#### validateClanName2

```python
request = ValidateClanNameRequest()
# some vars here

response = client.raw.ClanRemoteService.validateClanName2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.validateClanName2Request(
            request
        )
    )
)

client.logger.info(f'validateClanName2 response: {response}')
```
    
#### getClanByTag

```python
request = GetClanByTagRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanByTagResponse(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanByTagRequest(
            request
        )
    )
)

client.logger.info(f'getClanByTag response: {response}')
```
    
#### createClan2

```python
request = CreateClanRequest()
# some vars here

response = client.raw.ClanRemoteService.createClan2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.createClan2Request(
            request
        )
    )
)

client.logger.info(f'createClan2 response: {response}')
```
    
#### getClanJoinRequestsCount2

```python
request = GetClanJoinRequestsCountRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanJoinRequestsCount2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanJoinRequestsCount2Request(
            request
        )
    )
)

client.logger.info(f'getClanJoinRequestsCount2 response: {response}')
```
    
#### getClanMembersById2

```python
request = GetClanMembersByIdRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanMembersById2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanMembersById2Request(
            request
        )
    )
)

client.logger.info(f'getClanMembersById2 response: {response}')
```
    
#### getPlayerInviteRequestsCount2

```python
request = GetPlayerInviteRequestsCountRequest()
# some vars here

response = client.raw.ClanRemoteService.getPlayerInviteRequestsCount2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getPlayerInviteRequestsCount2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerInviteRequestsCount2 response: {response}')
```
    
#### getRoles2

```python
request = GetRolesRequest()
# some vars here

response = client.raw.ClanRemoteService.getRoles2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getRoles2Request(
            request
        )
    )
)

client.logger.info(f'getRoles2 response: {response}')
```
    
#### cancelInviteRequest2

```python
request = CancelInviteRequestRequest()
# some vars here

response = client.raw.ClanRemoteService.cancelInviteRequest2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.cancelInviteRequest2Request(
            request
        )
    )
)

client.logger.info(f'cancelInviteRequest2 response: {response}')
```
    
#### inviteToClan2

```python
request = InviteToClanRequest()
# some vars here

response = client.raw.ClanRemoteService.inviteToClan2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.inviteToClan2Request(
            request
        )
    )
)

client.logger.info(f'inviteToClan2 response: {response}')
```
    
#### kickMember2

```python
request = KickMemberRequest()
# some vars here

response = client.raw.ClanRemoteService.kickMember2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.kickMember2Request(
            request
        )
    )
)

client.logger.info(f'kickMember2 response: {response}')
```
    
#### getClanById2

```python
request = GetClanByIdRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanById2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanById2Request(
            request
        )
    )
)

client.logger.info(f'getClanById2 response: {response}')
```
    
#### getClanClosedInviteRequestsCount2

```python
request = GetClanClosedInviteRequestsCountRequest()
# some vars here

response = client.raw.ClanRemoteService.getClanClosedInviteRequestsCount2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getClanClosedInviteRequestsCount2Request(
            request
        )
    )
)

client.logger.info(f'getClanClosedInviteRequestsCount2 response: {response}')
```
    
#### getPlayerJoinRequests2

```python
request = GetPlayerJoinRequestsRequest()
# some vars here

response = client.raw.ClanRemoteService.getPlayerJoinRequests2Response(
    await client.send_request(
        *client.raw.ClanRemoteService.getPlayerJoinRequests2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerJoinRequests2 response: {response}')
```
### ClanMessagesRemoteService
    
#### getUnreadLogMessagesCount2

```python
request = GetUnreadLogMessagesCountRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.getUnreadLogMessagesCount2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.getUnreadLogMessagesCount2Request(
            request
        )
    )
)

client.logger.info(f'getUnreadLogMessagesCount2 response: {response}')
```
    
#### readClanLogMessages2

```python
request = ReadClanLogMessagesRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.readClanLogMessages2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.readClanLogMessages2Request(
            request
        )
    )
)

client.logger.info(f'readClanLogMessages2 response: {response}')
```
    
#### getClanChatMessages2

```python
request = GetClanChatMessagesRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.getClanChatMessages2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.getClanChatMessages2Request(
            request
        )
    )
)

client.logger.info(f'getClanChatMessages2 response: {response}')
```
    
#### sendClanChatMessage2

```python
request = SendClanChatMessageRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.sendClanChatMessage2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.sendClanChatMessage2Request(
            request
        )
    )
)

client.logger.info(f'sendClanChatMessage2 response: {response}')
```
    
#### getClanLogMessages2

```python
request = GetClanLogMessagesRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.getClanLogMessages2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.getClanLogMessages2Request(
            request
        )
    )
)

client.logger.info(f'getClanLogMessages2 response: {response}')
```
    
#### getUnreadChatMessagesCount2

```python
request = GetUnreadChatMessagesCountRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.getUnreadChatMessagesCount2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.getUnreadChatMessagesCount2Request(
            request
        )
    )
)

client.logger.info(f'getUnreadChatMessagesCount2 response: {response}')
```
    
#### readClanChatMessages2

```python
request = ReadClanChatMessagesRequest()
# some vars here

response = client.raw.ClanMessagesRemoteService.readClanChatMessages2Response(
    await client.send_request(
        *client.raw.ClanMessagesRemoteService.readClanChatMessages2Request(
            request
        )
    )
)

client.logger.info(f'readClanChatMessages2 response: {response}')
```
### PlayerStatsRemoteService
    
#### getCurrentStats

```python
request = GetCurrentStatsRequest()
# some vars here

response = client.raw.PlayerStatsRemoteService.getCurrentStatsResponse(
    await client.send_request(
        *client.raw.PlayerStatsRemoteService.getCurrentStatsRequest(
            request
        )
    )
)

client.logger.info(f'getCurrentStats response: {response}')
```
    
#### storeStats2

```python
request = StorePlayerStatsRequest()
# some vars here

response = client.raw.PlayerStatsRemoteService.storeStats2Response(
    await client.send_request(
        *client.raw.PlayerStatsRemoteService.storeStats2Request(
            request
        )
    )
)

client.logger.info(f'storeStats2 response: {response}')
```
    
#### getPlayerStats2

```python
request = GetPlayerStatsRequest()
# some vars here

response = client.raw.PlayerStatsRemoteService.getPlayerStats2Response(
    await client.send_request(
        *client.raw.PlayerStatsRemoteService.getPlayerStats2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerStats2 response: {response}')
```
### InventoryRemoteService
    
#### getOtherPlayerItemsEncrypted

```python
request = GetOtherPlayerItemsRequest()
# some vars here

response = client.raw.InventoryRemoteService.getOtherPlayerItemsEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.getOtherPlayerItemsEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'getOtherPlayerItemsEncrypted response: {response}')
```
    
#### setInventoryItemsPropertiesEncrypted

```python
request = SetItemsModificationsRequest()
# some vars here

response = client.raw.InventoryRemoteService.setInventoryItemsPropertiesEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.setInventoryItemsPropertiesEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'setInventoryItemsPropertiesEncrypted response: {response}')
```
    
#### setInventoryItemFlagsEncrypted

```python
request = SetInventoryItemFlagsRequest()
# some vars here

response = client.raw.InventoryRemoteService.setInventoryItemFlagsEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.setInventoryItemFlagsEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'setInventoryItemFlagsEncrypted response: {response}')
```
    
#### activateCouponEncrypted

```python
request = ActivateCouponRequest()
# some vars here

response = client.raw.InventoryRemoteService.activateCouponEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.activateCouponEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'activateCouponEncrypted response: {response}')
```
    
#### executeRecipeEncrypted2

```python
request = ExecuteRecipeRequest()
# some vars here

response = client.raw.InventoryRemoteService.executeRecipeEncrypted2Response(
    await client.send_request(
        *client.raw.InventoryRemoteService.executeRecipeEncrypted2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'executeRecipeEncrypted2 response: {response}')
```
    
#### mountInventoryItemEncrypted

```python
request = MountInventoryItemRequest()
# some vars here

response = client.raw.InventoryRemoteService.mountInventoryItemEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.mountInventoryItemEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'mountInventoryItemEncrypted response: {response}')
```
    
#### unmountInventoryItemEncrypted

```python
request = UnmountInventoryItemRequest()
# some vars here

response = client.raw.InventoryRemoteService.unmountInventoryItemEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.unmountInventoryItemEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'unmountInventoryItemEncrypted response: {response}')
```
    
#### buyInventoryItemEncrypted

```python
request = BuyInventoryItemRequest()
# some vars here

response = client.raw.InventoryRemoteService.buyInventoryItemEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.buyInventoryItemEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'buyInventoryItemEncrypted response: {response}')
```
    
#### getPlayerInventoryEncrypted

```python
request = GetPlayerInventoryRequest()
# some vars here

response = client.raw.InventoryRemoteService.getPlayerInventoryEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.getPlayerInventoryEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'getPlayerInventoryEncrypted response: {response}')
```
    
#### getInventoryItemPropertyDefinitionsEncrypted

```python
request = GetInventoryItemPropertyDefinitionsRequest()
# some vars here

response = client.raw.InventoryRemoteService.getInventoryItemPropertyDefinitionsEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.getInventoryItemPropertyDefinitionsEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'getInventoryItemPropertyDefinitionsEncrypted response: {response}')
```
    
#### getInventoryItemDefinitionsEncrypted

```python
request = GetInventoryItemDefinitionsRequest()
# some vars here

response = client.raw.InventoryRemoteService.getInventoryItemDefinitionsEncryptedResponse(
    await client.send_request(
        *client.raw.InventoryRemoteService.getInventoryItemDefinitionsEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'getInventoryItemDefinitionsEncrypted response: {response}')
```
### BoltIdAuthRemoteService
    
#### unLinkAuth

```python
request = BoltIdUnLinkAuthRequest()
# some vars here

response = client.raw.BoltIdAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.BoltIdAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### linkAuth

```python
request = BoltIdLinkAuthRequest()
# some vars here

response = client.raw.BoltIdAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.BoltIdAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
    
#### encryptedAuth2

```python
request = BoltIdAuthRequest()
# some vars here

response = client.raw.BoltIdAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.BoltIdAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
### TestAuthRemoteService
    
#### encryptedAuth2

```python
request = TestAuthRequest()
# some vars here

response = client.raw.TestAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.TestAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
### AppStoreInAppRemoteService
    
#### buyInApp2

```python
request = AppStoreBuyInappRequest()
# some vars here

response = client.raw.AppStoreInAppRemoteService.buyInApp2Response(
    await client.send_request(
        *client.raw.AppStoreInAppRemoteService.buyInApp2Request(
            request
        )
    )
)

client.logger.info(f'buyInApp2 response: {response}')
```
### GameSettingsRemoteService
    
#### getGameSettingsEncrypted2

```python
request = GetGameSettingsEncryptedRequest()
# some vars here

response = client.raw.GameSettingsRemoteService.getGameSettingsEncrypted2Response(
    await client.send_request(
        *client.raw.GameSettingsRemoteService.getGameSettingsEncrypted2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'getGameSettingsEncrypted2 response: {response}')
```
### IdTokenRemoteService
    
#### getIdToken

```python
request = GetIdTokenRequest()
# some vars here

response = client.raw.IdTokenRemoteService.getIdTokenResponse(
    await client.send_request(
        *client.raw.IdTokenRemoteService.getIdTokenRequest(
            request
        )
    )
)

client.logger.info(f'getIdToken response: {response}')
```
### AppGalleryInAppRemoteService
    
#### buyInApp

```python
request = AppGalleryBuyInappRequest()
# some vars here

response = client.raw.AppGalleryInAppRemoteService.buyInAppResponse(
    await client.send_request(
        *client.raw.AppGalleryInAppRemoteService.buyInAppRequest(
            request
        )
    )
)

client.logger.info(f'buyInApp response: {response}')
```
### GoogleInAppRemoteService
    
#### buyInApp2

```python
request = GoogleBuyInappRequest()
# some vars here

response = client.raw.GoogleInAppRemoteService.buyInApp2Response(
    await client.send_request(
        *client.raw.GoogleInAppRemoteService.buyInApp2Request(
            request
        )
    )
)

client.logger.info(f'buyInApp2 response: {response}')
```
### GameCenterAuthRemoteService
    
#### linkAuth

```python
request = GameCenterLinkAuthRequest()
# some vars here

response = client.raw.GameCenterAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.GameCenterAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
    
#### unLinkAuth

```python
request = GameCenterUnLinkAuthRequest()
# some vars here

response = client.raw.GameCenterAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.GameCenterAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### encryptedAuth2

```python
request = GameCenterAuthRequest()
# some vars here

response = client.raw.GameCenterAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.GameCenterAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
### OffersRemoteService
    
#### getSpecialOffers

```python
request = GetSpecialOffersRequest()
# some vars here

response = client.raw.OffersRemoteService.getSpecialOffersResponse(
    await client.send_request(
        *client.raw.OffersRemoteService.getSpecialOffersRequest(
            request
        )
    )
)

client.logger.info(f'getSpecialOffers response: {response}')
```
### FacebookAuthRemoteService
    
#### encryptedAuth2

```python
request = FacebookAuthRequest()
# some vars here

response = client.raw.FacebookAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.FacebookAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
    
#### unLinkAuth

```python
request = FacebookUnLinkAuthRequest()
# some vars here

response = client.raw.FacebookAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.FacebookAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### linkAuth

```python
request = FacebookLinkAuthRequest()
# some vars here

response = client.raw.FacebookAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.FacebookAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
### AccountLinkRemoteService
    
#### getLinkedAuth

```python
request = GetLinkedAuthRequest()
# some vars here

response = client.raw.AccountLinkRemoteService.getLinkedAuthResponse(
    await client.send_request(
        *client.raw.AccountLinkRemoteService.getLinkedAuthRequest(
            request
        )
    )
)

client.logger.info(f'getLinkedAuth response: {response}')
```
### GoogleAuthRemoteService
    
#### encryptedAuth2

```python
request = GoogleAuthRequest()
# some vars here

response = client.raw.GoogleAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.GoogleAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
    
#### unLinkAuth

```python
request = GoogleUnLinkAuthRequest()
# some vars here

response = client.raw.GoogleAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.GoogleAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### linkAuth

```python
request = GoogleLinkAuthRequest()
# some vars here

response = client.raw.GoogleAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.GoogleAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
### SeasonalStatsRemoteService
    
#### getStatsForSeason

```python
request = GetStatsForSeasonRequest()
# some vars here

response = client.raw.SeasonalStatsRemoteService.getStatsForSeasonResponse(
    await client.send_request(
        *client.raw.SeasonalStatsRemoteService.getStatsForSeasonRequest(
            request
        )
    )
)

client.logger.info(f'getStatsForSeason response: {response}')
```
    
#### getClanStatsForSeason

```python
request = GetClanStatsForSeasonRequest()
# some vars here

response = client.raw.SeasonalStatsRemoteService.getClanStatsForSeasonResponse(
    await client.send_request(
        *client.raw.SeasonalStatsRemoteService.getClanStatsForSeasonRequest(
            request
        )
    )
)

client.logger.info(f'getClanStatsForSeason response: {response}')
```
    
#### getPlayerStatsForSeason

```python
request = GetPlayerStatsForSeasonRequest()
# some vars here

response = client.raw.SeasonalStatsRemoteService.getPlayerStatsForSeasonResponse(
    await client.send_request(
        *client.raw.SeasonalStatsRemoteService.getPlayerStatsForSeasonRequest(
            request
        )
    )
)

client.logger.info(f'getPlayerStatsForSeason response: {response}')
```
    
#### getCurrentClanStatsForSeason

```python
request = GetCurrentClanStatsForSeasonRequest()
# some vars here

response = client.raw.SeasonalStatsRemoteService.getCurrentClanStatsForSeasonResponse(
    await client.send_request(
        *client.raw.SeasonalStatsRemoteService.getCurrentClanStatsForSeasonRequest(
            request
        )
    )
)

client.logger.info(f'getCurrentClanStatsForSeason response: {response}')
```
### DlcRemoteService
    
#### getAllReleasedDlc

```python
request = ReleasedDlcRequest()
# some vars here

response = client.raw.DlcRemoteService.getAllReleasedDlcResponse(
    await client.send_request(
        *client.raw.DlcRemoteService.getAllReleasedDlcRequest(
            request
        )
    )
)

client.logger.info(f'getAllReleasedDlc response: {response}')
```
    
#### getAllDlc

```python
request = PreviewDlcRequest()
# some vars here

response = client.raw.DlcRemoteService.getAllDlcResponse(
    await client.send_request(
        *client.raw.DlcRemoteService.getAllDlcRequest(
            request
        )
    )
)

client.logger.info(f'getAllDlc response: {response}')
```
### ClanStatsRemoteService
    
#### getClanStats

```python
request = GetClanStatsRequest()
# some vars here

response = client.raw.ClanStatsRemoteService.getClanStatsResponse(
    await client.send_request(
        *client.raw.ClanStatsRemoteService.getClanStatsRequest(
            request
        )
    )
)

client.logger.info(f'getClanStats response: {response}')
```
    
#### getCurrentClanStats

```python
request = GetCurrentClanStatsRequest()
# some vars here

response = client.raw.ClanStatsRemoteService.getCurrentClanStatsResponse(
    await client.send_request(
        *client.raw.ClanStatsRemoteService.getCurrentClanStatsRequest(
            request
        )
    )
)

client.logger.info(f'getCurrentClanStats response: {response}')
```
### GameAnnouncementRemoteService
    
#### getAllAnnouncements

```python
request = GetAllGameAnnouncementsRequest()
# some vars here

response = client.raw.GameAnnouncementRemoteService.getAllAnnouncementsResponse(
    await client.send_request(
        *client.raw.GameAnnouncementRemoteService.getAllAnnouncementsRequest(
            request
        )
    )
)

client.logger.info(f'getAllAnnouncements response: {response}')
```
### BoltRemoteService
    
#### unsubscribe2

```python
request = UnsubscribeRequest()
# some vars here

response = client.raw.BoltRemoteService.unsubscribe2Response(
    await client.send_request(
        *client.raw.BoltRemoteService.unsubscribe2Request(
            request
        )
    )
)

client.logger.info(f'unsubscribe2 response: {response}')
```
    
#### subscribe2

```python
request = SubscribeRequest()
# some vars here

response = client.raw.BoltRemoteService.subscribe2Response(
    await client.send_request(
        *client.raw.BoltRemoteService.subscribe2Request(
            request
        )
    )
)

client.logger.info(f'subscribe2 response: {response}')
```
### PlayerRemoteService
    
#### setAwayStatus2

```python
request = SetAwayStatusRequest()
# some vars here

response = client.raw.PlayerRemoteService.setAwayStatus2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.setAwayStatus2Request(
            request
        )
    )
)

client.logger.info(f'setAwayStatus2 response: {response}')
```
    
#### setPlayerAvatar2

```python
request = SetPlayerAvatarRequest()
# some vars here

response = client.raw.PlayerRemoteService.setPlayerAvatar2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.setPlayerAvatar2Request(
            request
        )
    )
)

client.logger.info(f'setPlayerAvatar2 response: {response}')
```
    
#### setPlayerFirebaseToken2

```python
request = SetPlayerFirebaseTokenRequest()
# some vars here

response = client.raw.PlayerRemoteService.setPlayerFirebaseToken2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.setPlayerFirebaseToken2Request(
            request
        )
    )
)

client.logger.info(f'setPlayerFirebaseToken2 response: {response}')
```
    
#### getPlayerSettings2

```python
request = GetPlayerSettingsRequest()
# some vars here

response = client.raw.PlayerRemoteService.getPlayerSettings2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.getPlayerSettings2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerSettings2 response: {response}')
```
    
#### setPlayerSettings2

```python
request = SetPlayerSettingsRequest()
# some vars here

response = client.raw.PlayerRemoteService.setPlayerSettings2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.setPlayerSettings2Request(
            request
        )
    )
)

client.logger.info(f'setPlayerSettings2 response: {response}')
```
    
#### setOnlineStatus2

```python
request = SetOnlineStatusRequest()
# some vars here

response = client.raw.PlayerRemoteService.setOnlineStatus2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.setOnlineStatus2Request(
            request
        )
    )
)

client.logger.info(f'setOnlineStatus2 response: {response}')
```
    
#### setDefaultAvatar

```python
request = SetDefaultAvatarRequest()
# some vars here

response = client.raw.PlayerRemoteService.setDefaultAvatarResponse(
    await client.send_request(
        *client.raw.PlayerRemoteService.setDefaultAvatarRequest(
            request
        )
    )
)

client.logger.info(f'setDefaultAvatar response: {response}')
```
    
#### setPlayerName2

```python
request = SetPlayerNameRequest()
# some vars here

response = client.raw.PlayerRemoteService.setPlayerName2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.setPlayerName2Request(
            request
        )
    )
)

client.logger.info(f'setPlayerName2 response: {response}')
```
    
#### getPlayer2

```python
request = GetPlayerRequest()
# some vars here

response = client.raw.PlayerRemoteService.getPlayer2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.getPlayer2Request(
            request
        )
    )
)

client.logger.info(f'getPlayer2 response: {response}')
```
### RateGameRemoteService
    
#### getLastRateGame

```python
request = GetLastRateGameRequest()
# some vars here

response = client.raw.RateGameRemoteService.getLastRateGameResponse(
    await client.send_request(
        *client.raw.RateGameRemoteService.getLastRateGameRequest(
            request
        )
    )
)

client.logger.info(f'getLastRateGame response: {response}')
```
    
#### askLater

```python
request = AskLaterRequest()
# some vars here

response = client.raw.RateGameRemoteService.askLaterResponse(
    await client.send_request(
        *client.raw.RateGameRemoteService.askLaterRequest(
            request
        )
    )
)

client.logger.info(f'askLater response: {response}')
```
    
#### dontAskLater

```python
request = DontAskLaterRequest()
# some vars here

response = client.raw.RateGameRemoteService.dontAskLaterResponse(
    await client.send_request(
        *client.raw.RateGameRemoteService.dontAskLaterRequest(
            request
        )
    )
)

client.logger.info(f'dontAskLater response: {response}')
```
    
#### rateGame

```python
request = RateGameRequest()
# some vars here

response = client.raw.RateGameRemoteService.rateGameResponse(
    await client.send_request(
        *client.raw.RateGameRemoteService.rateGameRequest(
            request
        )
    )
)

client.logger.info(f'rateGame response: {response}')
```
### AvatarRemoteService
    
#### getDefaultAvatars

```python
request = GetDefaultAvatarsRequest()
# some vars here

response = client.raw.AvatarRemoteService.getDefaultAvatarsResponse(
    await client.send_request(
        *client.raw.AvatarRemoteService.getDefaultAvatarsRequest(
            request
        )
    )
)

client.logger.info(f'getDefaultAvatars response: {response}')
```
### ChatRemoteService
    
#### readFriendMsgs2

```python
request = ReadFriendMsgsRequest()
# some vars here

response = client.raw.ChatRemoteService.readFriendMsgs2Response(
    await client.send_request(
        *client.raw.ChatRemoteService.readFriendMsgs2Request(
            request
        )
    )
)

client.logger.info(f'readFriendMsgs2 response: {response}')
```
    
#### deleteFriendMsgs2

```python
request = DeleteFriendMsgsRequest()
# some vars here

response = client.raw.ChatRemoteService.deleteFriendMsgs2Response(
    await client.send_request(
        *client.raw.ChatRemoteService.deleteFriendMsgs2Request(
            request
        )
    )
)

client.logger.info(f'deleteFriendMsgs2 response: {response}')
```
    
#### sendFriendMsg2

```python
request = SendFriendMsgRequest()
# some vars here

response = client.raw.ChatRemoteService.sendFriendMsg2Response(
    await client.send_request(
        *client.raw.ChatRemoteService.sendFriendMsg2Request(
            request
        )
    )
)

client.logger.info(f'sendFriendMsg2 response: {response}')
```
    
#### getChatUser

```python
request = GetChatUserRequest()
# some vars here

response = client.raw.ChatRemoteService.getChatUserResponse(
    await client.send_request(
        *client.raw.ChatRemoteService.getChatUserRequest(
            request
        )
    )
)

client.logger.info(f'getChatUser response: {response}')
```
    
#### getChatUsersLite

```python
request = GetChatUsersLiteRequest()
# some vars here

response = client.raw.ChatRemoteService.getChatUsersLiteResponse(
    await client.send_request(
        *client.raw.ChatRemoteService.getChatUsersLiteRequest(
            request
        )
    )
)

client.logger.info(f'getChatUsersLite response: {response}')
```
    
#### getFriendMsgsByOffset2

```python
request = GetFriendMsgsByOffsetRequest()
# some vars here

response = client.raw.ChatRemoteService.getFriendMsgsByOffset2Response(
    await client.send_request(
        *client.raw.ChatRemoteService.getFriendMsgsByOffset2Request(
            request
        )
    )
)

client.logger.info(f'getFriendMsgsByOffset2 response: {response}')
```
### MatchmakingRemoteService
    
#### setLobbyData2

```python
request = SetLobbyDataRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyData2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyData2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyData2 response: {response}')
```
    
#### setLobbyOwner2

```python
request = SetLobbyOwnerRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyOwner2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyOwner2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyOwner2 response: {response}')
```
    
#### joinLobbyAs2

```python
request = JoinLobbyAsRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.joinLobbyAs2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.joinLobbyAs2Request(
            request
        )
    )
)

client.logger.info(f'joinLobbyAs2 response: {response}')
```
    
#### createLobbyWithSpectators2

```python
request = CreateLobbyWithSpectatorsRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.createLobbyWithSpectators2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.createLobbyWithSpectators2Request(
            request
        )
    )
)

client.logger.info(f'createLobbyWithSpectators2 response: {response}')
```
    
#### getInvitesToLobby2

```python
request = GetInvitesToLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.getInvitesToLobby2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.getInvitesToLobby2Request(
            request
        )
    )
)

client.logger.info(f'getInvitesToLobby2 response: {response}')
```
    
#### setLobbyMaxSpectators2

```python
request = SetLobbyMaxSpectatorsRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyMaxSpectators2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyMaxSpectators2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyMaxSpectators2 response: {response}')
```
    
#### revokePlayerInvitationToLobby2

```python
request = RevokePlayerInvitationToLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.revokePlayerInvitationToLobby2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.revokePlayerInvitationToLobby2Request(
            request
        )
    )
)

client.logger.info(f'revokePlayerInvitationToLobby2 response: {response}')
```
    
#### kickPlayerFromLobby2

```python
request = KickPlayerFromLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.kickPlayerFromLobby2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.kickPlayerFromLobby2Request(
            request
        )
    )
)

client.logger.info(f'kickPlayerFromLobby2 response: {response}')
```
    
#### setLobbyMaxMembers2

```python
request = SetLobbyMaxMembersRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyMaxMembers2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyMaxMembers2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyMaxMembers2 response: {response}')
```
    
#### getLobby2

```python
request = GetLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.getLobby2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.getLobby2Request(
            request
        )
    )
)

client.logger.info(f'getLobby2 response: {response}')
```
    
#### setLobbyType2

```python
request = SetLobbyTypeRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyType2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyType2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyType2 response: {response}')
```
    
#### sendLobbyChatMsg2

```python
request = SendLobbyChatMsgRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.sendLobbyChatMsg2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.sendLobbyChatMsg2Request(
            request
        )
    )
)

client.logger.info(f'sendLobbyChatMsg2 response: {response}')
```
    
#### leaveLobby2

```python
request = LeaveLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.leaveLobby2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.leaveLobby2Request(
            request
        )
    )
)

client.logger.info(f'leaveLobby2 response: {response}')
```
    
#### searchLobby

```python
request = SearchLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.searchLobbyResponse(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.searchLobbyRequest(
            request
        )
    )
)

client.logger.info(f'searchLobby response: {response}')
```
    
#### invitePlayerToLobbyAs2

```python
request = InvitePlayerToLobbyAsRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.invitePlayerToLobbyAs2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.invitePlayerToLobbyAs2Request(
            request
        )
    )
)

client.logger.info(f'invitePlayerToLobbyAs2 response: {response}')
```
    
#### setLobbyPhotonGame2

```python
request = SetLobbyPhotonGameRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyPhotonGame2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyPhotonGame2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyPhotonGame2 response: {response}')
```
    
#### changeLobbyOtherPlayerType2

```python
request = ChangeLobbyOtherPlayerTypeRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.changeLobbyOtherPlayerType2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.changeLobbyOtherPlayerType2Request(
            request
        )
    )
)

client.logger.info(f'changeLobbyOtherPlayerType2 response: {response}')
```
    
#### setLobbyJoinable2

```python
request = SetLobbyJoinableRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.setLobbyJoinable2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.setLobbyJoinable2Request(
            request
        )
    )
)

client.logger.info(f'setLobbyJoinable2 response: {response}')
```
    
#### refuseInvitationToLobby2

```python
request = RefuseInvitationToLobbyRequest()
# some vars here

response = client.raw.MatchmakingRemoteService.refuseInvitationToLobby2Response(
    await client.send_request(
        *client.raw.MatchmakingRemoteService.refuseInvitationToLobby2Request(
            request
        )
    )
)

client.logger.info(f'refuseInvitationToLobby2 response: {response}')
```
### MarketplaceRemoteService
    
#### getTrades2

```python
request = GetTradesRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getTrades2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getTrades2Request(
            request
        )
    )
)

client.logger.info(f'getTrades2 response: {response}')
```
    
#### getFilteredTradeOpenSaleRequests

```python
request = GetTradeOpenSaleRequestsRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getFilteredTradeOpenSaleRequestsResponse(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getFilteredTradeOpenSaleRequestsRequest(
            request
        )
    )
)

client.logger.info(f'getFilteredTradeOpenSaleRequests response: {response}')
```
    
#### getPlayerClosedRequests2

```python
request = GetPlayerClosedRequestsRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getPlayerClosedRequests2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getPlayerClosedRequests2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerClosedRequests2 response: {response}')
```
    
#### cancelRequest2

```python
request = CancelRequestRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.cancelRequest2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.cancelRequest2Request(
            request
        )
    )
)

client.logger.info(f'cancelRequest2 response: {response}')
```
    
#### getTrade2

```python
request = GetTradeRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getTrade2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getTrade2Request(
            request
        )
    )
)

client.logger.info(f'getTrade2 response: {response}')
```
    
#### getMarketplaceSettings2

```python
request = GetMarketplaceSettingsRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getMarketplaceSettings2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getMarketplaceSettings2Request(
            request
        )
    )
)

client.logger.info(f'getMarketplaceSettings2 response: {response}')
```
    
#### getPlayerOpenRequests2

```python
request = GetPlayerOpenRequestsRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getPlayerOpenRequests2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getPlayerOpenRequests2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerOpenRequests2 response: {response}')
```
    
#### getPlayerProcessingRequests2

```python
request = GetPlayerProcessingRequestRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getPlayerProcessingRequests2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getPlayerProcessingRequests2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerProcessingRequests2 response: {response}')
```
    
#### getTradeOpenSaleRequests2

```python
request = GetTradeOpenSaleRequestsRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.getTradeOpenSaleRequests2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.getTradeOpenSaleRequests2Request(
            request
        )
    )
)

client.logger.info(f'getTradeOpenSaleRequests2 response: {response}')
```
    
#### createPurchaseRequestBySale2

```python
request = CreatePurchaseRequestBySaleRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.createPurchaseRequestBySale2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.createPurchaseRequestBySale2Request(
            request
        )
    )
)

client.logger.info(f'createPurchaseRequestBySale2 response: {response}')
```
    
#### createPurchaseRequest2

```python
request = CreatePurchaseRequestRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.createPurchaseRequest2Response(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.createPurchaseRequest2Request(
            request
        )
    )
)

client.logger.info(f'createPurchaseRequest2 response: {response}')
```
    
#### createSale

```python
request = CreateSaleRequest()
# some vars here

response = client.raw.MarketplaceRemoteService.createSaleResponse(
    await client.send_request(
        *client.raw.MarketplaceRemoteService.createSaleRequest(
            request
        )
    )
)

client.logger.info(f'createSale response: {response}')
```
### HandshakeRemoteService
    
#### encryptedHandshake

```python
request = Handshake()
# some vars here

response = client.raw.HandshakeRemoteService.encryptedHandshakeResponse(
    await client.send_request(
        *client.raw.HandshakeRemoteService.encryptedHandshakeRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedHandshake response: {response}')
```
    
#### encryptedHandshake

```python
request = GACHFBFBBEHDAAD()
# some vars here

response = client.raw.HandshakeRemoteService.encryptedHandshakeResponse(
    await client.send_request(
        *client.raw.HandshakeRemoteService.encryptedHandshakeRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedHandshake response: {response}')
```
### StorageRemoteService
    
#### readFiles

```python
request = ReadFilesRequest()
# some vars here

response = client.raw.StorageRemoteService.readFilesResponse(
    await client.send_request(
        *client.raw.StorageRemoteService.readFilesRequest(
            request
        )
    )
)

client.logger.info(f'readFiles response: {response}')
```
    
#### writeFile2

```python
request = WriteFileRequest()
# some vars here

response = client.raw.StorageRemoteService.writeFile2Response(
    await client.send_request(
        *client.raw.StorageRemoteService.writeFile2Request(
            request
        )
    )
)

client.logger.info(f'writeFile2 response: {response}')
```
### HuaweiAuthRemoteService
    
#### linkAuth

```python
request = HuaweiLinkAuthRequest()
# some vars here

response = client.raw.HuaweiAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.HuaweiAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
    
#### unLinkAuth

```python
request = HuaweiUnLinkAuthRequest()
# some vars here

response = client.raw.HuaweiAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.HuaweiAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### encryptedAuth2

```python
request = HuaweiAuthRequest()
# some vars here

response = client.raw.HuaweiAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.HuaweiAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
### SystemMessagesRemoteService
    
#### getSystemMessages

```python
request = GetSystemMessagesRequest()
# some vars here

response = client.raw.SystemMessagesRemoteService.getSystemMessagesResponse(
    await client.send_request(
        *client.raw.SystemMessagesRemoteService.getSystemMessagesRequest(
            request
        )
    )
)

client.logger.info(f'getSystemMessages response: {response}')
```
    
#### readSystemMessages

```python
request = ReadSystemMessagesRequest()
# some vars here

response = client.raw.SystemMessagesRemoteService.readSystemMessagesResponse(
    await client.send_request(
        *client.raw.SystemMessagesRemoteService.readSystemMessagesRequest(
            request
        )
    )
)

client.logger.info(f'readSystemMessages response: {response}')
```
    
#### getSystemMessageDetails

```python
request = GetSystemMessageDetailsRequest()
# some vars here

response = client.raw.SystemMessagesRemoteService.getSystemMessageDetailsResponse(
    await client.send_request(
        *client.raw.SystemMessagesRemoteService.getSystemMessageDetailsRequest(
            request
        )
    )
)

client.logger.info(f'getSystemMessageDetails response: {response}')
```
    
#### countUnreadSystemMessages

```python
request = CountUnreadSystemMessagesRequest()
# some vars here

response = client.raw.SystemMessagesRemoteService.countUnreadSystemMessagesResponse(
    await client.send_request(
        *client.raw.SystemMessagesRemoteService.countUnreadSystemMessagesRequest(
            request
        )
    )
)

client.logger.info(f'countUnreadSystemMessages response: {response}')
```
    
#### deleteSystemMessages

```python
request = DeleteSystemMessagesRequest()
# some vars here

response = client.raw.SystemMessagesRemoteService.deleteSystemMessagesResponse(
    await client.send_request(
        *client.raw.SystemMessagesRemoteService.deleteSystemMessagesRequest(
            request
        )
    )
)

client.logger.info(f'deleteSystemMessages response: {response}')
```
### NewsFeedRemoteService
    
#### getItems2

```python
request = GetItemsRequest()
# some vars here

response = client.raw.NewsFeedRemoteService.getItems2Response(
    await client.send_request(
        *client.raw.NewsFeedRemoteService.getItems2Request(
            request
        )
    )
)

client.logger.info(f'getItems2 response: {response}')
```
### AppleIdAuthRemoteService
    
#### unLinkAuth

```python
request = AppleIdUnLinkAuthRequest()
# some vars here

response = client.raw.AppleIdAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.AppleIdAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### linkAuth

```python
request = AppleIdLinkAuthRequest()
# some vars here

response = client.raw.AppleIdAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.AppleIdAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
    
#### encryptedAuth2

```python
request = AppleIdAuthRequest()
# some vars here

response = client.raw.AppleIdAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.AppleIdAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
### InAppRemoteService
    
#### subscribeCreator

```python
request = SubscribeCreatorRequest()
# some vars here

response = client.raw.InAppRemoteService.subscribeCreatorResponse(
    await client.send_request(
        *client.raw.InAppRemoteService.subscribeCreatorRequest(
            request
        )
    )
)

client.logger.info(f'subscribeCreator response: {response}')
```
    
#### findCreatorSubscription

```python
request = GetSubscribedCreatorRequest()
# some vars here

response = client.raw.InAppRemoteService.findCreatorSubscriptionResponse(
    await client.send_request(
        *client.raw.InAppRemoteService.findCreatorSubscriptionRequest(
            request
        )
    )
)

client.logger.info(f'findCreatorSubscription response: {response}')
```
    
#### findCreator

```python
request = FindCreatorRequest()
# some vars here

response = client.raw.InAppRemoteService.findCreatorResponse(
    await client.send_request(
        *client.raw.InAppRemoteService.findCreatorRequest(
            request
        )
    )
)

client.logger.info(f'findCreator response: {response}')
```
### VkAuthRemoteService
    
#### unLinkAuth

```python
request = VkUnLinkAuthRequest()
# some vars here

response = client.raw.VkAuthRemoteService.unLinkAuthResponse(
    await client.send_request(
        *client.raw.VkAuthRemoteService.unLinkAuthRequest(
            request
        )
    )
)

client.logger.info(f'unLinkAuth response: {response}')
```
    
#### linkAuth

```python
request = VkLinkAuthRequest()
# some vars here

response = client.raw.VkAuthRemoteService.linkAuthResponse(
    await client.send_request(
        *client.raw.VkAuthRemoteService.linkAuthRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'linkAuth response: {response}')
```
    
#### encryptedAuth2

```python
request = VkAuthRequest()
# some vars here

response = client.raw.VkAuthRemoteService.encryptedAuth2Response(
    await client.send_request(
        *client.raw.VkAuthRemoteService.encryptedAuth2Request(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'encryptedAuth2 response: {response}')
```
### FriendsRemoteService
    
#### ignoreFriendRequest2

```python
request = IgnoreFriendRequestRequest()
# some vars here

response = client.raw.FriendsRemoteService.ignoreFriendRequest2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.ignoreFriendRequest2Request(
            request
        )
    )
)

client.logger.info(f'ignoreFriendRequest2 response: {response}')
```
    
#### getPlayerFriends2

```python
request = GetPlayerFriendsRequest()
# some vars here

response = client.raw.FriendsRemoteService.getPlayerFriends2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.getPlayerFriends2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerFriends2 response: {response}')
```
    
#### getPlayerFriendByUid2

```python
request = GetPlayerFriendByUidRequest()
# some vars here

response = client.raw.FriendsRemoteService.getPlayerFriendByUid2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.getPlayerFriendByUid2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerFriendByUid2 response: {response}')
```
    
#### revokeFriendRequest2

```python
request = RevokeFriendRequestRequest()
# some vars here

response = client.raw.FriendsRemoteService.revokeFriendRequest2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.revokeFriendRequest2Request(
            request
        )
    )
)

client.logger.info(f'revokeFriendRequest2 response: {response}')
```
    
#### getPlayerFriendsIds2

```python
request = GetPlayerFriendsIdsRequest()
# some vars here

response = client.raw.FriendsRemoteService.getPlayerFriendsIds2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.getPlayerFriendsIds2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerFriendsIds2 response: {response}')
```
    
#### acceptFriendRequest2

```python
request = AcceptFriendRequestRequest()
# some vars here

response = client.raw.FriendsRemoteService.acceptFriendRequest2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.acceptFriendRequest2Request(
            request
        )
    )
)

client.logger.info(f'acceptFriendRequest2 response: {response}')
```
    
#### searchPlayers2

```python
request = SearchPlayersRequest()
# some vars here

response = client.raw.FriendsRemoteService.searchPlayers2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.searchPlayers2Request(
            request
        )
    )
)

client.logger.info(f'searchPlayers2 response: {response}')
```
    
#### getPlayerFriendById2

```python
request = GetPlayerFriendByIdRequest()
# some vars here

response = client.raw.FriendsRemoteService.getPlayerFriendById2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.getPlayerFriendById2Request(
            request
        )
    )
)

client.logger.info(f'getPlayerFriendById2 response: {response}')
```
    
#### sendFriendRequest2

```python
request = SendFriendRequestRequest()
# some vars here

response = client.raw.FriendsRemoteService.sendFriendRequest2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.sendFriendRequest2Request(
            request
        )
    )
)

client.logger.info(f'sendFriendRequest2 response: {response}')
```
    
#### blockFriend2

```python
request = BlockFriendRequest()
# some vars here

response = client.raw.FriendsRemoteService.blockFriend2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.blockFriend2Request(
            request
        )
    )
)

client.logger.info(f'blockFriend2 response: {response}')
```
    
#### removeFriend2

```python
request = RemoveFriendRequest()
# some vars here

response = client.raw.FriendsRemoteService.removeFriend2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.removeFriend2Request(
            request
        )
    )
)

client.logger.info(f'removeFriend2 response: {response}')
```
    
#### unblockFriend2

```python
request = UnblockFriendRequest()
# some vars here

response = client.raw.FriendsRemoteService.unblockFriend2Response(
    await client.send_request(
        *client.raw.FriendsRemoteService.unblockFriend2Request(
            request
        )
    )
)

client.logger.info(f'unblockFriend2 response: {response}')
```
### GameEventRemoteService
    
#### getCachedPlayerGameEvents

```python
request = GetCachedPlayerGameEventsRequest()
# some vars here

response = client.raw.GameEventRemoteService.getCachedPlayerGameEventsResponse(
    await client.send_request(
        *client.raw.GameEventRemoteService.getCachedPlayerGameEventsRequest(
            request
        )
    )
)

client.logger.info(f'getCachedPlayerGameEvents response: {response}')
```
    
#### getPlayerGameEventsProgresses

```python
request = GetPlayerGameEventsProgressesRequest()
# some vars here

response = client.raw.GameEventRemoteService.getPlayerGameEventsProgressesResponse(
    await client.send_request(
        *client.raw.GameEventRemoteService.getPlayerGameEventsProgressesRequest(
            request
        )
    )
)

client.logger.info(f'getPlayerGameEventsProgresses response: {response}')
```
    
#### processChallenge

```python
request = ProgressChallengeRequest()
# some vars here

response = client.raw.GameEventRemoteService.processChallengeResponse(
    await client.send_request(
        *client.raw.GameEventRemoteService.processChallengeRequest(
            request
        )
    )
)

client.logger.info(f'processChallenge response: {response}')
```
### GdprRemoteService
    
#### recoverAccount

```python
request = RecoverAccountRequest()
# some vars here

response = client.raw.GdprRemoteService.recoverAccountResponse(
    await client.send_request(
        *client.raw.GdprRemoteService.recoverAccountRequest(
            request
        )
    )
)

client.logger.info(f'recoverAccount response: {response}')
```
    
#### createRequestEncrypted

```python
request = CreateRequestEncryptedRequest()
# some vars here

response = client.raw.GdprRemoteService.createRequestEncryptedResponse(
    await client.send_request(
        *client.raw.GdprRemoteService.createRequestEncryptedRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'createRequestEncrypted response: {response}')
```
    
#### deleteAccount

```python
request = DeleteAccountRequest()
# some vars here

response = client.raw.GdprRemoteService.deleteAccountResponse(
    await client.send_request(
        *client.raw.GdprRemoteService.deleteAccountRequest(
            request
        )
    )
)

client.logger.info(f'deleteAccount response: {response}')
```
### HelloRemoteService
    
#### hello

```python
request = CHGACEEHFADEDHH()
# some vars here

response = client.raw.HelloRemoteService.helloResponse(
    await client.send_request(
        *client.raw.HelloRemoteService.helloRequest(
            request,client.cipher
        )
    ),client.cipher
)

client.logger.info(f'hello response: {response}')
```

----------------

## Raw listeners

### MarketplaceRemoteEventListener

#### onPlayerRequestOpened
 
```python
@client.MarketplaceRemoteEventListenerOnPlayerRequestOpened()
async def marketplace_remote_event_listener(client, event: MarketplaceRemoteEventListenerOnPlayerRequestOpenedUpdate):
    client.logger.info(f'response: {event}')
```

#### onTradeUpdated
 
```python
@client.MarketplaceRemoteEventListenerOnTradeUpdated()
async def marketplace_remote_event_listener(client, event: MarketplaceRemoteEventListenerOnTradeUpdatedUpdate):
    client.logger.info(f'response: {event}')
```

#### onTradeRequestOpened
 
```python
@client.MarketplaceRemoteEventListenerOnTradeRequestOpened()
async def marketplace_remote_event_listener(client, event: MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerRequestClosed
 
```python
@client.MarketplaceRemoteEventListenerOnPlayerRequestClosed()
async def marketplace_remote_event_listener(client, event: MarketplaceRemoteEventListenerOnPlayerRequestClosedUpdate):
    client.logger.info(f'response: {event}')
```

#### onTradeRequestClosed
 
```python
@client.MarketplaceRemoteEventListenerOnTradeRequestClosed()
async def marketplace_remote_event_listener(client, event: MarketplaceRemoteEventListenerOnTradeRequestClosedUpdate):
    client.logger.info(f'response: {event}')
```
### SystemMessagesRemoteEventListener

#### onSystemMessageReceived
 
```python
@client.SystemMessagesRemoteEventListenerOnSystemMessageReceived()
async def system_messages_remote_event_listener(client, event: SystemMessagesRemoteEventListenerOnSystemMessageReceivedUpdate):
    client.logger.info(f'response: {event}')
```
### MatchmakingRemoteEventListener

#### onRevokeInviteToLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onNewSpectatorInvitedToLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyPhotonGameChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyMaxMembersChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyDataChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyDataChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyDataChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyTypeChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyTypeChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyTypeChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onReceivedInviteToLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyJoinableChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyJoinableChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onNewPlayerJoinedLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onRefuseInviteToLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyChatMessageEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyChatMessageEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyChatMessageEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerKickedFromLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyPlayerTypeChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onReceivedSpectatorInviteToLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyOwnerChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyOwnerChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onNewPlayerInvitedToLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyGameServerChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyGameServerChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyNameChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyNameChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyNameChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerLeftLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnPlayerLeftLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onNewSpectatorJoinedLobbyEvent
 
```python
@client.MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onLobbyMaxSpectatorsChangedEvent
 
```python
@client.MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEvent()
async def matchmaking_remote_event_listener(client, event: MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventUpdate):
    client.logger.info(f'response: {event}')
```
### InAppsRemoteEventListener

#### onInAppEvent
 
```python
@client.InAppsRemoteEventListenerOnInAppEvent()
async def in_apps_remote_event_listener(client, event: InAppsRemoteEventListenerOnInAppEventUpdate):
    client.logger.info(f'response: {event}')
```
### ClansRemoteEventListener

#### onClanMembersCountIncreased
 
```python
@client.ClansRemoteEventListenerOnClanMembersCountIncreased()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnClanMembersCountIncreasedUpdate):
    client.logger.info(f'response: {event}')
```

#### onReadClosedInviteRequestEvent
 
```python
@client.ClansRemoteEventListenerOnReadClosedInviteRequestEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnReadClosedInviteRequestEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onJoinRequestDeclinedEvent
 
```python
@client.ClansRemoteEventListenerOnJoinRequestDeclinedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnJoinRequestDeclinedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### OnKickedMember
 
```python
@client.ClansRemoteEventListenerOnKickedMember()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnKickedMemberUpdate):
    client.logger.info(f'response: {event}')
```

#### OnJoinRequestCancelledEvent
 
```python
@client.ClansRemoteEventListenerOnJoinRequestCancelledEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnJoinRequestCancelledEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onClanTypeChanged
 
```python
@client.ClansRemoteEventListenerOnClanTypeChanged()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnClanTypeChangedUpdate):
    client.logger.info(f'response: {event}')
```

#### onAssignedLeaderRoleEvent
 
```python
@client.ClansRemoteEventListenerOnAssignedLeaderRoleEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnAssignedLeaderRoleEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onClanTagAndNameChanged
 
```python
@client.ClansRemoteEventListenerOnClanTagAndNameChanged()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnClanTagAndNameChangedUpdate):
    client.logger.info(f'response: {event}')
```

#### onLeftFromClan
 
```python
@client.ClansRemoteEventListenerOnLeftFromClan()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnLeftFromClanUpdate):
    client.logger.info(f'response: {event}')
```

#### onClanMemberDeclinedRequestEvent
 
```python
@client.ClansRemoteEventListenerOnClanMemberDeclinedRequestEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnClanMemberDeclinedRequestEventUpdate):
    client.logger.info(f'response: {event}')
```

#### OnMemberJoinedToClan
 
```python
@client.ClansRemoteEventListenerOnMemberJoinedToClan()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnMemberJoinedToClanUpdate):
    client.logger.info(f'response: {event}')
```

#### OnJoinRequestTaken
 
```python
@client.ClansRemoteEventListenerOnJoinRequestTaken()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnJoinRequestTakenUpdate):
    client.logger.info(f'response: {event}')
```

#### onInviteRequestDeclinedEvent
 
```python
@client.ClansRemoteEventListenerOnInviteRequestDeclinedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnInviteRequestDeclinedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### OnInviteRequestCancelledEvent
 
```python
@client.ClansRemoteEventListenerOnInviteRequestCancelledEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnInviteRequestCancelledEventUpdate):
    client.logger.info(f'response: {event}')
```

#### OnAssignedRoleEvent
 
```python
@client.ClansRemoteEventListenerOnAssignedRoleEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnAssignedRoleEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerAvatarChangedEvent
 
```python
@client.ClansRemoteEventListenerOnPlayerAvatarChangedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnPlayerAvatarChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onOnlineStatusChangedEvent
 
```python
@client.ClansRemoteEventListenerOnOnlineStatusChangedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnOnlineStatusChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerNameChangedEvent
 
```python
@client.ClansRemoteEventListenerOnPlayerNameChangedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnPlayerNameChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onKickedEvent
 
```python
@client.ClansRemoteEventListenerOnKickedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnKickedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onClanDescriptionChangedEvent
 
```python
@client.ClansRemoteEventListenerOnClanDescriptionChangedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnClanDescriptionChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerAttributesChanged
 
```python
@client.ClansRemoteEventListenerOnPlayerAttributesChanged()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnPlayerAttributesChangedUpdate):
    client.logger.info(f'response: {event}')
```

#### onClanAvatarChangedEvent
 
```python
@client.ClansRemoteEventListenerOnClanAvatarChangedEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnClanAvatarChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### OnInvitedToClanEvent
 
```python
@client.ClansRemoteEventListenerOnInvitedToClanEvent()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnInvitedToClanEventUpdate):
    client.logger.info(f'response: {event}')
```

#### OnJoinedToClan
 
```python
@client.ClansRemoteEventListenerOnJoinedToClan()
async def clans_remote_event_listener(client, event: ClansRemoteEventListenerOnJoinedToClanUpdate):
    client.logger.info(f'response: {event}')
```
### InventoryRemoteEventListener

#### onInventoryChanged
 
```python
@client.InventoryRemoteEventListenerOnInventoryChanged()
async def inventory_remote_event_listener(client, event: InventoryRemoteEventListenerOnInventoryChangedUpdate):
    client.logger.info(f'response: {event}')
```

#### onCouponActivated
 
```python
@client.InventoryRemoteEventListenerOnCouponActivated()
async def inventory_remote_event_listener(client, event: InventoryRemoteEventListenerOnCouponActivatedUpdate):
    client.logger.info(f'response: {event}')
```
### MatchesRemoteEventListener

#### OnMatchFinished
 
```python
@client.MatchesRemoteEventListenerOnMatchFinished()
async def matches_remote_event_listener(client, event: MatchesRemoteEventListenerOnMatchFinishedUpdate):
    client.logger.info(f'response: {event}')
```
### FriendsRemoteEventListener

#### onFriendNameChangedEvent
 
```python
@client.FriendsRemoteEventListenerOnFriendNameChangedEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnFriendNameChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerStatusChangedEvent
 
```python
@client.FriendsRemoteEventListenerOnPlayerStatusChangedEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnPlayerStatusChangedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayerAttributesChanged
 
```python
@client.FriendsRemoteEventListenerOnPlayerAttributesChanged()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnPlayerAttributesChangedUpdate):
    client.logger.info(f'response: {event}')
```

#### onFriendRemovedEvent
 
```python
@client.FriendsRemoteEventListenerOnFriendRemovedEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnFriendRemovedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onRevokeFriendshipRequestEvent
 
```python
@client.FriendsRemoteEventListenerOnRevokeFriendshipRequestEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnRevokeFriendshipRequestEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onFriendAddedEvent
 
```python
@client.FriendsRemoteEventListenerOnFriendAddedEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnFriendAddedEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onNewFriendshipRequestEvent
 
```python
@client.FriendsRemoteEventListenerOnNewFriendshipRequestEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnNewFriendshipRequestEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onFriendAvatarChangedEvent
 
```python
@client.FriendsRemoteEventListenerOnFriendAvatarChangedEvent()
async def friends_remote_event_listener(client, event: FriendsRemoteEventListenerOnFriendAvatarChangedEventUpdate):
    client.logger.info(f'response: {event}')
```
### MessagesRemoteEventListener

#### onMsgFromFriendEvent
 
```python
@client.MessagesRemoteEventListenerOnMsgFromFriendEvent()
async def messages_remote_event_listener(client, event: MessagesRemoteEventListenerOnMsgFromFriendEventUpdate):
    client.logger.info(f'response: {event}')
```
### ClanStatsRemoteEventListener

#### onClanStatsUpdated
 
```python
@client.ClanStatsRemoteEventListenerOnClanStatsUpdated()
async def clan_stats_remote_event_listener(client, event: ClanStatsRemoteEventListenerOnClanStatsUpdatedUpdate):
    client.logger.info(f'response: {event}')
```
### GameEventRemoteEventListener

#### onGamePassChanged
 
```python
@client.GameEventRemoteEventListenerOnGamePassChanged()
async def game_event_remote_event_listener(client, event: GameEventRemoteEventListenerOnGamePassChangedUpdate):
    client.logger.info(f'response: {event}')
```

#### onProgressGameEvent
 
```python
@client.GameEventRemoteEventListenerOnProgressGameEvent()
async def game_event_remote_event_listener(client, event: GameEventRemoteEventListenerOnProgressGameEventUpdate):
    client.logger.info(f'response: {event}')
```

#### onProgressChallengeEvent
 
```python
@client.GameEventRemoteEventListenerOnProgressChallengeEvent()
async def game_event_remote_event_listener(client, event: GameEventRemoteEventListenerOnProgressChallengeEventUpdate):
    client.logger.info(f'response: {event}')
```
### ClanMessagesRemoteEventListener

#### onIncomingClanChatMessageEvent
 
```python
@client.ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEvent()
async def clan_messages_remote_event_listener(client, event: ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventUpdate):
    client.logger.info(f'response: {event}')
```
### AdsRemoteEventListener

#### onAdRewardEvent
 
```python
@client.AdsRemoteEventListenerOnAdRewardEvent()
async def ads_remote_event_listener(client, event: AdsRemoteEventListenerOnAdRewardEventUpdate):
    client.logger.info(f'response: {event}')
```
### PlayerStatsRemoteEventListener

#### onStatsUpdatedEvent
 
```python
@client.PlayerStatsRemoteEventListenerOnStatsUpdatedEvent()
async def player_stats_remote_event_listener(client, event: PlayerStatsRemoteEventListenerOnStatsUpdatedEventUpdate):
    client.logger.info(f'response: {event}')
```
### MatchmakingRemoteListener

#### onMatchmakingProgress
 
```python
@client.MatchmakingRemoteListenerOnMatchmakingProgress()
async def matchmaking_remote_listener(client, event: MatchmakingRemoteListenerOnMatchmakingProgressUpdate):
    client.logger.info(f'response: {event}')
```

#### onPlayersConfirmed
 
```python
@client.MatchmakingRemoteListenerOnPlayersConfirmed()
async def matchmaking_remote_listener(client, event: MatchmakingRemoteListenerOnPlayersConfirmedUpdate):
    client.logger.info(f'response: {event}')
```

#### onMatchmakingDone
 
```python
@client.MatchmakingRemoteListenerOnMatchmakingDone()
async def matchmaking_remote_listener(client, event: MatchmakingRemoteListenerOnMatchmakingDoneUpdate):
    client.logger.info(f'response: {event}')
```

#### onMatchmakingFail
 
```python
@client.MatchmakingRemoteListenerOnMatchmakingFail()
async def matchmaking_remote_listener(client, event: MatchmakingRemoteListenerOnMatchmakingFailUpdate):
    client.logger.info(f'response: {event}')
```
