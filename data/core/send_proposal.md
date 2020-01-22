## proposal path
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name": null}

## proposal path
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## unhappy path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}

## unhappy path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## very unhappy path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}

## very unhappy path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* affirm
    - proposal_form
    - form{"name": null}

## stop but continue path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* affirm
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop and really stop path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm

## chitchat stop but continue path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* stop
    - utter_ask_continue
* affirm
    - proposal_form
    - form{"name": null}

## chitchat stop but continue path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* stop
    - utter_ask_continue
* affirm
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue and chitchat path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* affirm
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}

## stop but continue and chitchat path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* affirm
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat stop but continue and chitchat path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* stop
    - utter_ask_continue
* affirm
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}

## chitchat stop but continue and chitchat path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* stop
    - utter_ask_continue
* affirm
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat, stop and really stop path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm

## very unhappy path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}

## very unhappy path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
* chitchat
    - utter_chitchat
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* affirm
    - proposal_form
    - form{"name": null}

## stop but continue path send proposal
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* stop
    - utter_ask_continue
* affirm
    - proposal_form
    - form{"name": null}
* affirm
    - utter_affirm
