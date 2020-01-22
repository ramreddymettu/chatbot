## fed fund path
* fed_fund_inquiry
    - utter_fed_fund_inquiry

## fed fund path
* fed_fund_inquiry
    - utter_fed_fund_inquiry
* affirm
    - utter_affirm

## Story from conversation with me on July 24th 2019

* send_proposal
    - proposal_form
    - form{"name":"proposal_form"}
* status_enquiry
    - status_form
    - form{"name":"status_form"}
    - form{"name": null}
* inform{"trans_id":"AB123CF2"}
    - track_action
* affirm OR thankyou
    - utter_previous_msg
* affirm
    - proposal_form
    - form{"name": null}
