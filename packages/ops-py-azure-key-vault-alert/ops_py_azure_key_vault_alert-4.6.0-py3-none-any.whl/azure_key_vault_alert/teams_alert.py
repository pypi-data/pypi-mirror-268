#!/usr/bin/env python

import logging


def teams_alert(title, kv, max_chars, stdout_only=False, msg_handler=None):
    """Gets a payload from azure_key_vault_report object and push it to the msg_handler,
    or optionally just print to standard out.

    Parameters
    ----------
    title : str
        The title of the message
    kv : __init__.py
        An azure_key_vault_report object
    max_chars : int
        The max length of the report. The MS Teams api will not be able to handle too large payloads.
        Reports above this value will be truncated and a warning will be added to the title of the message.
    stdout_only : bool
        If True the reports will only be printed to standard output instead of sent to the Message Handler.
    msg_handler : __init__.py
        A message_handler object

    Returns
    -------
    True
        If response from the POST has return code 200
    """

    # A payload with the report as html table is generated
    payload = kv.get_teams_payload(title)

    # Return if no payload
    if not payload:
        logging.error("Unable to retrieve MS Teams payload")
        return

    # If stdout_only we print the payload to standard output only and then return
    if stdout_only:
        print(payload)
        return

    # If payload is too large with the report as html, a new payload is generated.
    # A custom text is provided instead, which will be used instead of the html report.
    if len(payload) > max_chars:
        warning_msg = f"The {title} length is above the character limit count of {max_chars}"
        logging.warning(warning_msg)
        title = f"WARNING! {warning_msg}"
        text = "The html report have been omitted from the report due to size limits."
        payload = kv.get_teams_payload(title, text=text)

    # The payload is set and posted and return code set
    logging.info(f"Using payload: {payload}")

    if msg_handler:
        msg_handler.set_payload(payload)
        msg_handler.post_payload()
        response_code = msg_handler.get_response_code()

        # Return True if response code is 200
        if isinstance(response_code, int) and response_code == 200:
            return True