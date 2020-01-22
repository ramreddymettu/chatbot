# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional
import re
import csv
import time

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import (
    Action, 
    Tracker, 
    ActionExecutionRejection
)
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    FollowupAction,
    Form,
)

email_pattern = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
account_pattern = r"^[0-9]{2}[A-za-z]{1}[0-9]{6}$"
trans_id_pattern = r"^[A-Z]{2}[0-9]{3}[A-Z]{2}[0-9]{1}$"

data_base = []
with open('database/database.csv') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        data_base.append(row)


class ProposalForm(FormAction):
    """ Custom action for Renew"""

    def name(self) -> Text:
        """ Unique name of Form Action"""

        return "proposal_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        if tracker.get_slot("name"):
            return ["name", "email", "confirm_email"]
        else:
            return ["email", "confirm_email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": self.from_entity(
                entity="name", intent= ["inform", "send_proposal"]
            ),
            "email": [
                self.from_entity(entity="email", intent=["inform", "send_proposal"]),
                self.from_entity(entity="email"),
                self.from_text(intent='inform')
            ],
            "confirm_email":[
                self.from_intent(intent="confirm", value=True),
                self.from_intent(intent="cancel", value=False),
            ]
            
        }


    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        if re.match(email_pattern, value):
            return {"email": value}
        else:
            dispatcher.utter_template("utter_wrong_email", tracker)
            return {"email": None}

    def validate_confirm_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        if value == False:
            return {"confirm_email": None, "email": None}
        return {"confirm_email": value}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        print("Name :", tracker.get_slot("name"))
        print("Name entity :", list(tracker.get_latest_entity_values("name")))
        if tracker.get_slot("name"):
            dispatcher.utter_template("utter_slots_name_email", tracker)
        else:
            dispatcher.utter_template("utter_slots_email", tracker)
        
        return [Form(None), SlotSet('confirm_email', None), SlotSet('name', None)]



class StatusForm(FormAction):
    """ Custom action for Renew"""

    def name(self) -> Text:
        """ Unique name of Form Action"""

        return "status_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["account_number", "confirm_account_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:


        return {
            "account_number": [
            self.from_entity(entity="account_number", intent=["inform", "status_enquiry"]),
            self.from_entity(entity="account_number"),
            self.from_text(intent='inform')
            ],
            "confirm_account_number": [
                self.from_intent(intent="cancel", value=False),
                self.from_intent(intent="confirm", value=True)
           ],
        }

    def validate_account_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if re.match(account_pattern, value):
            return {"account_number": value}
        else:
            dispatcher.utter_template("utter_wrong_account_number", tracker)

            return {"account_number": None}
    
    def validate_confirm_account_number(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

       if value == False:
           return {'confirm_account_number': None, "account_number": None}
       return {'confirm_account_number': value}



    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        account_number = tracker.get_slot('account_number')
        
        history = []
        for t in data_base:
            if t['Account_Number'].strip() == account_number:
                history.append(t)

        if len(history) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find transation history for {}".format(account_number)
            )
            return [SlotSet('confirm_account_number', None)]

        message_1 = """Amount | Date | Satatus"""

        message = """{}) {} | {} | {}"""
        buttons = []
        i = 1
        for tran in history:
            tran['Trans_Id']
            payload = "/inform{\"trans_id\":\"" + tran['Trans_Id'] + "\"}"
            title = message.format(i, tran['Amount'], tran['Date'], tran['Status'])
            buttons.append({"title": title, "payload": payload})
            i += 1
        
        dispatcher.utter_button_message("Here is last transactions list \n Amount | Date | Status", buttons)
        
        return [SlotSet('confirm_account_number', None)]


class TrackAction(Action):

    def name(self) -> Text:
        return "track_action"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        trans_id = tracker.get_slot('trans_id')
        
        message = """Trans ID  | {} 
                     Date      | {}
                     Amount    | {}
                     Status    | {}
                     Track ID  | {}"""


        for t in data_base: 
            if t['Trans_Id'].strip() == trans_id:

                dispatcher.utter_message(message.format(t['Trans_Id'], t['Date'], t['Amount'],t['Status'], t['Track_Id']))
                return []

class  DocumentForm(FormAction):
    
    def name(self) -> Text:

        return 'document_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

         return ['account_number', 'trans_id', 'confirm_account_number', 'confirm_trans_id', 'doc_type', 'doc_format']


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "trans_id": [
            self.from_entity(entity="trans_id", intent=["inform", "document_copy"]),
            self.from_entity(entity="trans_id"),
            self.from_intent(intent="deny", value="Not Provided"),
            self.from_text(intent='inform'),
            ],
            "account_number": [
            self.from_entity(entity="account_number", intent=["inform", "document_copy"]),
            self.from_entity(entity="account_number"),
            self.from_intent(intent="deny", value="Not Provided"),
            self.from_text(intent='inform')
            ],
            "confirm_account_number": [
                self.from_intent(intent="cancel", value=False),
                self.from_intent(intent="confirm", value=True)
           ],
           "confirm_trans_id": [
                self.from_intent(intent="cancel", value=False),
                self.from_intent(intent="confirm", value=True)
           ],
           "known_slot": [
                self.from_entity(entity="known_slot", intent=["inform"]),
                self.from_intent(intent="deny", value="Not Provided")
           ],
            "doc_type": self.from_entity(
                entity="doc_type", intent=["inform", "document_copy"]
            ),
            "doc_format": self.from_entity(
                entity="doc_format", intent=["inform", "document_copy"]
            )
        }

    def validate_confirm_account_number(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

       if value == False:
           return {'confirm_account_number': None, "account_number": None}
       return {'confirm_account_number': value}

    def validate_confirm_trans_id(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

       if value == False:
           return {'confirm_trans_id': None, "trans_id": None}
       return {'confirm_trans_id': value}

    def validate_known_slot(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if value == "account_number":
            return {'known_slot': value, "account_number": None}

        if value == "trans_id":
            return {'known_slot': value, "trans_id": None}

        return {'known_slot': value}

    def validate_account_number(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if value == "Not Provided":
            return {'known_slot': None, "account_number": value}

        if re.match(account_pattern, value):
            return {'known_slot': None, "account_number": value}
        else:
            dispatcher.utter_template("utter_wrong_account_number", tracker)
            return {'known_slot': None, "account_number": None}
    def validate_trans_id(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if value == "Not Provided":
            return {'known_slot': None, "trans_id": value}

        if re.match(trans_id_pattern, value):
            return {'known_slot': None, "trans_id": value}
        else:
            dispatcher.utter_template("utter_wrong_trans_id", tracker)
            return {'known_slot': None, "trans_id": None}


    def request_next_slot(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type: Dict[Text, Any]
    ):
        # type: (...) -> Optional[List[Dict]]
        """Request the next slot and utter template if needed,
            else return None"""
        optional_slots = ['account_number', 'trans_id']

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                
                opt_list = []
                for opt_slot in optional_slots:
                    if tracker.get_slot(opt_slot) != "Not Provided" and tracker.get_slot(opt_slot) is not None:
                        opt_list.append(True)

                if slot in optional_slots and any(opt_list):
                    continue 

                if all([tracker.get_slot(opt_slot) == "Not Provided" for opt_slot in optional_slots]):
                    if tracker.get_slot('known_slot') == None:
                        dispatcher.utter_template(
                            "utter_ask_known_slot",
                            tracker,
                            silent_fail=False,
                            **tracker.slots
                        )
                        return [SlotSet(REQUESTED_SLOT, 'known_slot')]

                    if tracker.get_slot('known_slot') == "Not Provided":
                        dispatcher.utter_message(
                            "At least one piece of Optional Slot information required"
                            )
                        return [Form(None), 
                                SlotSet('known_slot', None),
                                SlotSet('account_number', None),
                                SlotSet('trans_id', None), 
                                SlotSet('confirm_account_number', None), 
                                SlotSet('confirm_trans_id', None), 
                                SlotSet('doc_type', None), 
                                SlotSet('doc_format', None)
                            ]



                if slot.startswith('confirm_') and (tracker.get_slot(slot[8:]) == "Not Provided" or tracker.get_slot(slot[8:]) is None):
                    continue 



                dispatcher.utter_template(
                    "utter_ask_{}".format(slot),
                    tracker,
                    silent_fail=False,
                    **tracker.slots
                )
               
                return [SlotSet(REQUESTED_SLOT, slot)]

        """
        if all([tracker.get_slot(opt_slot) == "Not Provided" for opt_slot in optional_slots]):
            if tracker.get_slot('known_slot') == None:
                dispatcher.utter_template(
                    "utter_ask_known_slot",
                    tracker,
                    silent_fail=False,
                    **tracker.slots
                )
                return [SlotSet(REQUESTED_SLOT, 'known_slot')]

            if tracker.get_slot('known_slot') == "Not Provided":
                dispatcher.utter_message(
                    "At least one of Optional Slot information required"
                    )
                return [Form(None), SlotSet('known_slot', None)]
        """


        # no more required slots to fill
        return None

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        doc_format = tracker.get_slot('doc_format')
        trans_id = tracker.get_slot('trans_id')
        account_number = tracker.get_slot('account_number')
        doc_type = tracker.get_slot('doc_type')

        print(doc_format, trans_id, doc_type)
        
        if doc_format == 'pdf':
            dispatcher.utter_message("Ok, please click [here](https://cira.cognicor.com/bnymintegration/assets/files/4003555710.pdf) to download.")
        else:
            dispatcher.utter_message("Ok, please check your inbox")
        return [SlotSet('known_slot', None), 
                SlotSet('confirm_account_number', None), 
                SlotSet('confirm_trans_id', None), 
                SlotSet('doc_type', None), 
                SlotSet('doc_format', None),
                SlotSet('account_number', None if account_number == "Not Provided" else account_number),
                SlotSet('trans_id', None if trans_id == "Not Provided" else trans_id)
            ]

# Vijay FormActions

class AccountNumberForm(FormAction):
    """ Custom action for Account Form"""
    def name(self) -> Text:

        return "account_number_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["account_number", "confirm_account_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "account_number": [
            self.from_entity(entity="account_number", intent=["inform", "lost_card"]),
            self.from_entity(entity="account_number"),
            self.from_text(intent='inform')
            ],
            "confirm_account_number": [
                self.from_intent(intent="cancel", value=False),
                self.from_intent(intent="confirm", value=True)
            ]
        }

    def validate_account_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if re.match(account_pattern, value):
            return {"account_number": value}
        else:
            dispatcher.utter_template("utter_wrong_account_number", tracker)
            return {"account_number": None}

    def validate_confirm_account_number(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

       if value == False:
           return {'confirm_account_number': None, "account_number": None}
       return {'confirm_account_number': value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        dispatcher.utter_template("utter_slots_lost_card", tracker)
        
        return [SlotSet('confirm_account_number', None)]

class UpGradeAccountForm(FormAction):
    def name(self) -> Text:

        return "upgrade_account_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["account_number", "confirm_account_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "account_number": [
            self.from_entity(entity="account_number", intent=["inform", "upgrade_account"]),
            self.from_entity(entity="account_number"),
            self.from_text(intent='inform')
            ],
            "confirm_account_number": [
                self.from_intent(intent="cancel", value=False),
                self.from_intent(intent="confirm", value=True)
           ],
        }

    def validate_account_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if re.match(account_pattern, value):
            return {"account_number": value}
        else:
            dispatcher.utter_template("utter_wrong_account_number", tracker)
            return {"account_number": None}

    def validate_confirm_account_number(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

       if value == False:
           return {'confirm_account_number': None, "account_number": None}
       return {'confirm_account_number': value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_template("utter_slots_upgrade_account", tracker)
        
        return [SlotSet('confirm_account_number', None)]

class RetireAccountForm(FormAction):
    """ Custom action for Renew"""
    def name(self) -> Text:
        return "retirement_account_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["account_number", "confirm_account_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "account_number": [
            self.from_entity(entity="account_number", intent=["inform", "adjust_distribution"]),
            self.from_entity(entity="account_number"),
            self.from_text(intent='inform')
            ],
            "confirm_account_number": [
                self.from_intent(intent="cancel", value=False),
                self.from_intent(intent="confirm", value=True)
           ],
        }

    def validate_account_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if re.match(account_pattern, value):
            return {"account_number": value}
        else:
            dispatcher.utter_template("utter_wrong_account_number", tracker)
            return {"account_number": None}

    def validate_confirm_account_number(
       self,
       value: Text,
       dispatcher: CollectingDispatcher,
       tracker: Tracker,
       domain: Dict[Text, Any],
    ) -> Optional[Text]:

       if value == False:
           return {'confirm_account_number': None, "account_number": None}
       return {'confirm_account_number': value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_template("utter_slots_retirement_account", tracker)
        
        return [SlotSet('confirm_account_number', None)]