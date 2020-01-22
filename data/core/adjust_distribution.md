## adjust path
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
    - form{"name": null}

## adjust path
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
    - form{"name": null}
* affirm
    - utter_affirm

## unhappy path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}

## unhappy path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## very unhappy path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}

## very unhappy path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
    - form{"name": null}

## stop and really stop path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
    - form{"name": null}

## chitchat stop but continue path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## stop but continue and chitchat path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}

## stop but continue and chitchat path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat stop but continue and chitchat path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}
* affirm
    - utter_affirm

## chitchat stop but continue and chitchat path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* stop
    - utter_ask_continue
* affirm
    - retirement_account_form
* chitchat
    - utter_chitchat
    - retirement_account_form
    - form{"name": null}

## chitchat, stop and really stop path adjust distribution
* adjust_distribution
    - retirement_account_form
    - form{"name": "retirement_account_form"}
* chitchat
    - utter_chitchat
    - retirement_account_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_affirm
