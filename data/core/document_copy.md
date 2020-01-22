## doc_form path
* document_copy
    - document_form
    - form{"name":"document_form"}
    - form{"name": null}

## doc_form path
* document_copy
    - document_form
    - form{"name":"document_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## unhappy path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}

## unhappy path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
* affirm
    - utter_affirm

## very unhappy path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* chitchat
    - utter_chitchat
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}

## very unhappy path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* chitchat
    - utter_chitchat
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* affirm
    - document_form
    - form{"name": null}

## stop but continue path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* affirm
    - document_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop and really stop path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm

## chitchat stop but continue path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* affirm
    - document_form
    - form{"name": null}

## chitchat stop but continue path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* affirm
    - document_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue and chitchat path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* affirm
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}

## stop but continue and chitchat path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* affirm
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat stop but continue and chitchat path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* affirm
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}

## chitchat stop but continue and chitchat path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* affirm
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat, stop and really stop path document copy
* document_copy
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm
