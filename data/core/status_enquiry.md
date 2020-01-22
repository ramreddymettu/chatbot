## status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}

## status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## status path
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action

## status path
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action
* affirm
    - utter_affirm

## stop but continue path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* stop
    - utter_ask_continue
* affirm
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action

## stop but continue path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* stop
    - utter_ask_continue
* affirm
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action
* affirm
    - utter_affirm

## stop and really stop path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm

## chitchat stop but continue path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* chitchat
    - utter_chitchat
    - status_form
* stop
    - utter_ask_continue
* affirm
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action

## chitchat stop but continue path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* chitchat
    - utter_chitchat
    - status_form
* stop
    - utter_ask_continue
* affirm
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action
* affirm
    - utter_affirm

## stop but continue and chitchat path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* stop
    - utter_ask_continue
* affirm
    - status_form
* chitchat
    - utter_chitchat
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action

## stop but continue and chitchat path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* stop
    - utter_ask_continue
* affirm
    - status_form
* chitchat
    - utter_chitchat
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action
* affirm
    - utter_affirm

## chitchat stop but continue and chitchat path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* chitchat
    - utter_chitchat
    - status_form
* stop
    - utter_ask_continue
* affirm
    - status_form
* chitchat
    - utter_chitchat
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action

## chitchat stop but continue and chitchat path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* chitchat
    - utter_chitchat
    - status_form
* stop
    - utter_ask_continue
* affirm
    - status_form
* chitchat
    - utter_chitchat
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CE1"}
    - track_action
* affirm
    - utter_affirm

## chitchat, stop and really stop path status enquiry
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* chitchat
    - utter_chitchat
    - status_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm
