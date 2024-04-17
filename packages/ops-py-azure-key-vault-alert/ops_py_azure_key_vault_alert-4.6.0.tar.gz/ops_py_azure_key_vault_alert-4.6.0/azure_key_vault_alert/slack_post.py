#!/usr/bin/env python

import logging


def slack_post(msg_handler, payloads=None, posts=None):
    if isinstance(payloads, list):
        success_counter = 0
        for p in payloads:
            msg_handler.set_payload(p)
            msg_handler.post_payload()

            # If any of the payloads are sent it is considered a success
            response_code = msg_handler.get_response_code()
            if isinstance(response_code, int) and response_code == 200:
                success_counter += 1
            else:
                logging.error(f"Failed to send message to Slack App. Response code {str(response_code)}.")

        # Return True if success so that we know at least one message have been sent
        if success_counter:
            logging.info(f"{success_counter} messages posted to the Slack app.")
            return True

    if isinstance(posts, list):
        success_counter = 0
        for title_, text_ in posts:
            msg_handler.build_payload(Title=title_, Text=text_)
            msg_handler.post_payload()

            # If any of the payloads are sent it is considered a success
            response_code = msg_handler.get_response_code()
            if isinstance(response_code, int) and response_code == 200:
                success_counter += 1
            else:
                logging.error(f"Failed to send message to Slack Workflow. Response code {str(response_code)}.")

        # Return True if success so that we know at least one message have been sent
        if success_counter:
            logging.info(f"{success_counter} messages posted to the Slack Workflow.")
            return True
