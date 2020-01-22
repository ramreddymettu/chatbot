## upgrade path
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
    - form{"name": null}

## upgrade path
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## unhappy path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}

## unhappy path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## very unhappy path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}

## very unhappy path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
    - form{"name": null}

## stop but continue path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop and really stop path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm

## chitchat stop but continue path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
    - form{"name": null}

## chitchat stop but continue path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue and chitchat path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}

## stop but continue and chitchat path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat stop but continue and chitchat path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}

## chitchat stop but continue and chitchat path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* stop
    - utter_ask_continue
* affirm
    - upgrade_account_form
* chitchat
    - utter_chitchat
    - upgrade_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat, stop and really stop path upgrade account
* upgrade_account
    - upgrade_account_form
    - form{"name": "upgrade_account_form"}
* chitchat
    - utter_chitchat
    - upgrade_account_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm

## Story from conversation with me on June 19th 2019

* send_proposal
    - proposal_form
    - form{"name":"proposal_form"}
    - form{"name":null}
* status_enquiry
    - status_form
    - form{"name":"status_form"}
    - form{"name":null}
* affirm
    - utter_affirm

## Story from conversation with me on June 19th 2019

* document_copy
    - document_form
    - form{"name": "document_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## Story from conversation with me on June 19th 2019

* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## Story from conversation with me on June 19th 2019

* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* inform{"trans_id":"AB123CF2"}
    - slot{"trans_id":"AB123CF2"}
    - track_action
* affirm
    - utter_affirm

## Story from conversation with me on June 19th 2019
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## Story from conversation with me on June 19th 2019

* greet
    - utter_greet
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name": null}
* affirm
    - utter_affirm
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* affirm
    - utter_affirm
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* inform{"trans_id":"AB123CF2"}
    - slot{"trans_id":"AB123CF2"}
    - track_action
* affirm
    - utter_affirm
* document_copy
    - document_form
    - form{"name": "document_form"}
    - form{"name": null}
* affirm
    - utter_affirm
