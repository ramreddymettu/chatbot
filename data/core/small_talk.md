## greet path
* greet
    - utter_greet

## thank you path
* thankyou
    - utter_noworries
    - utter_help

## chitchat path
* chitchat
   - utter_chitchat

## affirm story
* affirm
   - utter_affirm

## Proposal + Status + Track story
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* inform{"trans_id":"AB123CF2"}
    - track_action
    - proposal_form
    - form{"name": null}

## Status + Proposal + Track action story
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name": null}
    - status_form
    - form{"name": null}
* inform{"trans_id":"AB123CF2"}
    - track_action
