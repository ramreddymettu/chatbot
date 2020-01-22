## proposal + document copy path
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* document_copy
    - document_form
    - form{"name":"document_form"}
    - form{"name":null}
* affirm OR thankyou
    - utter_previous_msg
* affirm
    - proposal_form
    - form{"name":null}

## document + proposal story
* document_copy
    - document_form
    - form{"name":"document_form"}
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name":null}
* affirm OR thankyou
    - utter_previous_msg
* affirm
    - document_form
    - form{"name":null}

## proposal + status story
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
* status_enquiry
    - status_form
    - form{"name": "status_form"}
    - form{"name": null}
* affirm OR thankyou
    - utter_previous_msg
* affirm
    - proposal_form
    - form{"name": null}

## status + proposal story
* status_enquiry
    - status_form
    - form{"name": "status_form"}
* send_proposal
    - proposal_form
    - form{"name": "proposal_form"}
    - form{"name": null}
* affirm OR thankyou
    - utter_previous_msg
* affirm
    - status_form
    - form{"name": null}
