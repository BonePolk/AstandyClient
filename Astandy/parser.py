from typing import Any, Sequence

from Astandy.errors import AstandyRPCException
from Astandy.schemes.messages_pb2 import ClientMsg, BinaryValue, Response, ServerMsg, ExceptionExplained
from google.protobuf.json_format import MessageToDict, ParseDict
class Parser:
    translates = {
        "RpcExceptions/RPC1001": "Invalid data. Please try again.",
        "RpcExceptions/RPC1002": "Hacking app detected! (Game Guardian, Game Killer, or other)",
        "RpcExceptions/RPC1003": "Your device is rooted so you cannot connect. Please, unroot the device and try again.",
        "RpcExceptions/RPC1006": "It seems that you have a third-party version of Standoff 2 installed on your device. Please, download the game from official sources (App Store, Google Play, GetApps or AppGallery).",
        "RpcExceptions/RPC1007": "Google security check failed. Restart the game and try again.",
        "RpcExceptions/RPC1100": "Action blocked or not available right now. Check the requirements and try again.",
        "RpcExceptions/RPC1200": "Please enter a valid email address",
        "RpcExceptions/RPC1201": "A data export request has already been made for this account. Please wait for the results to be sent to the specified email address.",
        "RpcExceptions/RPC1202": "Account recovery failed. Deletion request not found. Make sure you are using the right account.",
        "RpcExceptions/RPC1500": "This feature has been temporarily disabled. We are working on restoring it. Please try again later.",
        "RpcExceptions/RPC1501": "This authorization method is currently unavailable. Please, wait a while or choose another method. ",
        "RpcExceptions/RPC1511": "This feature has been temporarily disabled. We are working on restoring it. Please try again later.",
        "RpcExceptions/RPC1512": "This feature has been temporarily disabled. We are working on restoring it. Please try again later.",
        "RpcExceptions/RPC1513": "This feature has been temporarily disabled. We are working on restoring it. Please try again later.",
        "RpcExceptions/RPC1514": "This feature has been temporarily disabled. We are working on restoring it. Please try again later.",
        "RpcExceptions/RPC2000": "A new version of Standoff 2 is available. You can download the update in your application store.",
        "RpcExceptions/RPC2001": "Match not found or no longer available.",
        "RpcExceptions/RPC2002": "Not enough Clan rights. Message the Clan Leader or an Officer for help.",
        "RpcExceptions/RPC2003": "Session time expired. Please restart the game.",
        "RpcExceptions/RPC2007": "Could not connect to the server. Try again later or restart the game.",
        "RpcExceptions/RPC2008": "Clan not found",
        "RpcExceptions/RPC2009": "This player is not in your Clan. Action not available.",
        "RpcExceptions/RPC2010": "You have already sent an application to this clan.",
        "RpcExceptions/RPC2011": "You already invited this player to the Clan. Wait for their reply or cancel the invite.",
        "RpcExceptions/RPC2013": "You cannot add a player because the clan is full.\nIncrease the max number of clan members and try again.",
        "RpcExceptions/RPC2015": "Cannot expand the lobby. Player limit reached.",
        "RpcExceptions/RPC2016": "Invalid clan tag",
        "RpcExceptions/RPC2017": "Invalid clan name",
        "RpcExceptions/RPC2018": "Clan name is already in use",
        "RpcExceptions/RPC2019": "Tag is already in use",
        "RpcExceptions/RPC2020": "You already sent a clan invitation.",
        "RpcExceptions/RPC2022": "Restricted words are used",
        "RpcExceptions/RPC2023": "Leadership can be transferred only 14 days after the creation of the clan.",
        "RpcExceptions/RPC2024": "This player is not in your Clan. Action not available.",
        "RpcExceptions/RPC2025": "You can’t leave the clan while other members are in there",
        "RpcExceptions/RPC2026": "The action is unavailable because this clan is blocked",
        "RpcExceptions/RPC2101": "Account linked to this login service not found. Make sure you are using the right profile.",
        "RpcExceptions/RPC2104": "Unable to sign in through that service. Please try again later.",
        "RpcExceptions/RPC2105": "This service is already linked to an account. Please use a different login method.",
        "RpcExceptions/RPC2107": "Unable to link account. The account selected is already linked to another Standoff 2 profile.",
        "RpcExceptions/RPC2201": "Google Play authentication failed",
        "RpcExceptions/RPC2202": "Google Play authentication failed",
        "RpcExceptions/RPC2203": "Google Play authentication failed",
        "RpcExceptions/RPC2204": "Google sign in failed. Please try again later.",
        "RpcExceptions/RPC2205": "Something went wrong with Google sign in. Try again later or use a different login method.",
        "RpcExceptions/RPC2211": "We had a problem logging you in via Game Center.",
        "RpcExceptions/RPC2221": "Could not confirm your Apple ID/Huawei login. Sign out and sign back in.",
        "RpcExceptions/RPC2231": "VK sign in failed. Please try again later.",
        "RpcExceptions/RPC2301": "This statistic is not available right now. Update the game and try again.",
        "RpcExceptions/RPC2501": "This player has restricted conversations in their privacy settings. Your message cannot be delivered.",
        "RpcExceptions/RPC2502": "This player isn't accepting clan invitations.",
        "RpcExceptions/RPC2503": "This player isn't accepting lobby invitations.",
        "RpcExceptions/RPC2504": "This player isn't accepting friend requests.",
        "RpcExceptions/RPC2505": "This player made their match history private.",
        "RpcExceptions/RPC2506": "This player made their statistics private.",
        "RpcExceptions/RPC2601": "You have reached your friend limit. Please unfriend someone from your list and try again.",
        "RpcExceptions/RPC2602": "You've sent too many friend requests in the last 24 hours. Please try again later.",
        "RpcExceptions/RPC3002": "You are currently in a match. Please finish it before starting another.",
        "RpcExceptions/RPC3003": "Match not started. You can only do this during a match.",
        "RpcExceptions/RPC3005": "Team size is not right for a Clan match. Get the right number of players and try again.",
        "RpcExceptions/RPC3006": "No competitive filters selected. Please try again.",
        "RpcExceptions/RPC3007": "You are not in this Clan. Cannot join a Clan match.",
        "RpcExceptions/RPC3008": "This mode requires a higher account level.",
        "RpcExceptions/RPC3101": "Player not found",
        "RpcExceptions/RPC3102": "This player has blocked you.",
        "RpcExceptions/RPC3104": "Too many messages. Please wait and try again.",
        "RpcExceptions/RPC3105": "Invalid name or tag.",
        "RpcExceptions/RPC3106": "Chat with this player not found. Send them a message again.",
        "RpcExceptions/RPC3107": "This avatar is not available. Please choose a different one.",
        "RpcExceptions/RPC3108": "In the past 24 hours, you have sent too many messages to users who are not on your friend list. Try again later.",
        "RpcExceptions/RPC3109": "Invalid nickname. Check length and allowed characters.",
        "RpcExceptions/RPC3110": "Failed to upload an avatar picture. You’re changing your avatar image too often. Try again later.",
        "RpcExceptions/RPC3202": "The item was not found.\nIt may have been used in crafting or put up for sale in the Marketplace.",
        "RpcExceptions/RPC3204": "Failed to list item. Wrong item selection or data mismatch. Try selecting the item again.",
        "RpcExceptions/RPC3205": "You are trying to list too many items at once. Try listing fewer items.",
        "RpcExceptions/RPC3301": "This currency is not available right now. Try again later.",
        "RpcExceptions/RPC3302": "This item can't be purchased",
        "RpcExceptions/RPC3303": "Not enough currency for this action.",
        "RpcExceptions/RPC3304": "You do not have the required items for this action.",
        "RpcExceptions/RPC3305": "Invalid operation. Check your action and try again.",
        "RpcExceptions/RPC3306": "The lot was not found.\nIt may already have been sold or removed from the Marketplace.",
        "RpcExceptions/RPC3307": "Your price is below the Marketplace minimum. Please set a higher price.",
        "RpcExceptions/RPC3308": "You cannot sell this item on the Marketplace.",
        "RpcExceptions/RPC3311": "Invalid operation. Check your action and try again.",
        "RpcExceptions/RPC3312": "You already made a purchase request for this item.",
        "RpcExceptions/RPC3313": "You cannot buy or sell this item on the Marketplace.",
        "RpcExceptions/RPC3314": "Please enter a valid number of items.",
        "RpcExceptions/RPC3315": "This item is already listed for sale.",
        "RpcExceptions/RPC3321": "You can't perform that operation with a negative balance.",
        "RpcExceptions/RPC3322": "This modification is not found or not available. Please choose another and retry.",
        "RpcExceptions/RPC3323": "You cannot remove this modification from the item.",
        "RpcExceptions/RPC3324": "You cannot sell an item with a charm attached. Remove it first and try again.",
        "RpcExceptions/RPC3325": "You cannot use this item as a modification.",
        "RpcExceptions/RPC3326": "This modification does not fit that item or slot.",
        "RpcExceptions/RPC3327": "The Rental Market is closed. Your request can't be fulfilled.",
        "RpcExceptions/RPC3328": "You’ve reached the limit of transactions on the market. Try again later.",
        "RpcExceptions/RPC3401": "Crafting recipe not found.",
        "RpcExceptions/RPC3402": "You need more resources to do that.",
        "RpcExceptions/RPC3403": "Not enough resources to complete this action.",
        "RpcExceptions/RPC3404": "Too many components selected. Please choose the right amount.",
        "RpcExceptions/RPC3405": "Too many attempts. Please wait and try again.",
        "RpcExceptions/RPC3406": "Too many attempts in a row. Please wait and try again.",
        "RpcExceptions/RPC3407": "Operation declined. Try again later.",
        "RpcExceptions/RPC3411": "This action does not support multipliers. Remove it and try again.",
        "RpcExceptions/RPC3501": "Event not found or no longer available. Check the current events in the game.",
        "RpcExceptions/RPC3502": "Could not claim reward. Please try again.",
        "RpcExceptions/RPC3601": "Challenge not found or no longer available. Refresh the challenge list and try again.",
        "RpcExceptions/RPC3701": "Challenge not found or no longer available.",
        "RpcExceptions/RPC3704": "This task expired. Progress not saved.",
        "RpcExceptions/RPC3705": "Could not update quest progress. Restart the game and try again.",
        "RpcExceptions/RPC3801": "Invalid code.",
        "RpcExceptions/RPC3802": "This code has already been activated on your account.",
        "RpcExceptions/RPC3803": "This code has reached its activation limit.",
        "RpcExceptions/RPC3804": "Too many code activation attempts. Try again later.",
        "RpcExceptions/RPC400": "Request failed. Please try again later.",
        "RpcExceptions/RPC4002": "Could not find the match. It might be over or unavailable.",
        "RpcExceptions/RPC401": "You haven't logged in yet. Sign in to your game account.",
        "RpcExceptions/RPC404": "Request not found or expired. Refresh the screen and try again.",
        "RpcExceptions/RPC4101": "System message not found.",
        "RpcExceptions/RPC500": "A server error has occurred.\nWe'll have all the issues fixed very soon. Please try again later.\nCode: 500\n",
        "RpcExceptions/RPC5001": "Lobby not found",
        "RpcExceptions/RPC5002": "Only the lobby owner can do this.",
        "RpcExceptions/RPC5003": "You are not a member of this lobby",
        "RpcExceptions/RPC5004": "You are not in a lobby.",
        "RpcExceptions/RPC5005": "No access to lobby",
        "RpcExceptions/RPC5006": "Lobby is full",
        "RpcExceptions/RPC5007": "That player is already in a lobby.",
        "RpcExceptions/RPC5008": "Invalid settings. Cannot create lobby. Try again.",
        "RpcExceptions/RPC5011": "Group chat not found. It may have been deleted.",
        "RpcExceptions/RPC5012": "This is a friends only lobby. Add this player to your friends or ask them for an invite.",
        "RpcExceptions/RPC5013": "An error occurred while connecting to the lobby.",
        "RpcExceptions/RPC5101": "Match not found",
        "RpcExceptions/RPC5300": "You already follow another Commander. Unsubscribe from them first.",
        "RpcExceptions/RPC5301": "Recruit not found",
        "RpcExceptions/RPC5302": "Recruit already in squad",
        "RpcExceptions/RPC5303": "Only squad recruits can do this.",
        "RpcExceptions/RPC5304": "You cannot subscribe to yourself.",
        "RpcExceptions/RPC5305": "You installed the game more than 24 hours ago, and can no longer choose a Commander.",
        "RpcExceptions/RPC600": "Failed to connect to servers. Code: 600",
        "RpcExceptions/RPC6001": "Game server not found. Check your internet connection and try again later.",
        "RpcExceptions/RPC6102": "Ad reward is not available right now. Try again later.",
        "RpcExceptions/RPC6201": "You can only rate the app once.",
        "RpcExceptions/RPC6301": "Could not save the image. Check your device storage.",
        "RpcExceptions/RPC7001": "Failed to save changes. Try again.",
        "RpcExceptions/RPC7002": "Data changed while processing. Please try again.",
        "RpcExceptions/RPC8001": "Could not confirm your purchase. Try again later.",
        "RpcExceptions/RPC8002": "Item not found.",
        "RpcExceptions/RPC8003": "Purchase failed because of a data error. Please try again later.",
        "RpcExceptions/RPC8021": "Invalid code",
        "RpcExceptions/RPC8022": "Subscribing to this creator is not available right now.",
        "RpcExceptions/RPC9901": "Saved data missing. Please try again later.",
        "RpcExceptions/RPC9902": "Cannot save this data type.",
        "RpcExceptions/RPC9903": "Failed to save. Invalid data format.",
        "RpcExceptions/RPC9904": "Cannot save more of this data type. Remove some and try again.",
        "RpcExceptions/RPC9905": "Failed to save. Data size is too big. Adjust your settings and try again.",
        "RpcExceptions/RPC9998": "Your device has been banned",
        "RpcExceptions/RPC9999": "Your account is banned",
    }
    
    @staticmethod
    def new_msg(
        uuid: str,
        code: int,
        payload: bytes,
        service: str = "",
        method: str = "",
    ):
        msg = ClientMsg(id=uuid, code=code)
        if code == 0:
            msg.cls = service
            msg.func = method

        msg.data.append(BinaryValue(one=payload))

        return msg.SerializeToString()
    
    @staticmethod
    def parse_response(request: bytes) -> ServerMsg:
        msg = ServerMsg()
        msg.ParseFromString(request)

        return msg

    @staticmethod
    def raise_for_exception(response: Response) -> None:
        if response.exception.code:
            error_key = "RpcExceptions/RPC" + str(response.exception.code)
            edata = MessageToDict(response.exception, preserving_proto_field_name=True)
            edata['description'] = "" if error_key not in Parser.translates else Parser.translates[error_key]
            explained_error = ExceptionExplained()
            ParseDict(edata, explained_error)
            raise AstandyRPCException(explained_error)
                
    @staticmethod
    def parse_rpc_response(response: Response, response_cls: type) -> Any:
        Parser.raise_for_exception(response)
        payload = response.data[0].one if response.data else b""
        message = response_cls()
        message.ParseFromString(payload)
        return message

    @staticmethod
    def parse_empty_rpc_response(response: Response) -> None:
        Parser.raise_for_exception(response)
        return None

    @staticmethod
    def serialize_primitive_payload(value: Any, type_name: str) -> bytes:
        from Astandy.generated.protos import rpc_message_pb2

        if type_name == "string":
            return rpc_message_pb2.String(value=value).SerializeToString()
        if type_name == "byte[]":
            return rpc_message_pb2.Byte(value=bytes(value)).SerializeToString()
        if type_name == "int":
            return rpc_message_pb2.Integer(value=value).SerializeToString()
        if type_name == "long":
            return rpc_message_pb2.Long(value=value).SerializeToString()
        if type_name == "float":
            return rpc_message_pb2.Float(value=value).SerializeToString()
        if type_name == "double":
            return rpc_message_pb2.Double(value=value).SerializeToString()
        if type_name == "bool":
            return rpc_message_pb2.Boolean(value=value).SerializeToString()
        raise TypeError(f"unsupported primitive RPC parameter type: {type_name}")

    @staticmethod
    def serialize_primitive_request(params: list[tuple[str, Any]]) -> list[bytes]:
        return [
            Parser.serialize_primitive_payload(value, type_name)
            for type_name, value in params
        ]
