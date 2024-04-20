#!/usr/bin/env python

import logging


########################################################################################################################


class SlackPayloads(object):
    """

    Attributes
    ----------
    title : str
        The title of the Slack message
    summary : str
        The report summary. Only used it the split_msg() method has to be called.
    report : str
        The report. Only used it the split_msg() method has to be called.
    report_summary : str
        The report and summary combined. Used as default if the split_msg() does not have to be called.
    max_chars : int
        Count of characters for when the Slack message is considered too long and will be split into multiple messages
        (default: 3500)

    Methods
    -------
    get_app_payloads()
        Creates and returns Slack Payload(s) built to be posted to a Slack App: {"text": "bla. bla"}.
        If a payload is above the 'max_char' limit, then the split_msg() method is called in order
        to split the payload into multiple payloads. A payload is formatted with a bold heading (title)
        and the summary/report as plain text (*title*\n ```bla. bla.```).
        If split into multiple payloads, then a 'part number' is appended to the title of each payload.
    get_workflow_posts()
        Add a tuple of 'title' and 'report_summary' to a posts list which may be used to post to a Slack Workflow
        If the summary and report combined is above the 'max_char' limit, then the split_msg() method is called in order
        to split the message into multiple posts.
        If split into multiple payloads, then a 'part number' is appended to the title of each payload.
        The first part will be the summary, then followed by the 'report' spilt into parts
    split_msg()
        Splits long messages into multiple parts - to be posted to Slack individually
        If splitting up a message to a Slack App, each message will be a payload in the following format:
        {"text": "formatted message"}
        If splitting up a message to a Slack App, each message will be a post, consisting of a tuple pair of:
        title, text

    """
    def __init__(self, title, summary, report, report_summary, max_chars=3500):
        """
        Parameters
        ----------
        title : str
            The title of the Slack message
        summary : str
            The report summary. Only used it the split_msg() method has to be called.
        report : str
            The report. Only used it the split_msg() method has to be called.
        report_summary : str
            The report and summary combined. Used as default if the split_msg() does not have to be called.
        max_chars : int
            Count of characters for when the Slack message is considered too long and will be split into multiple messages
            (default: 3500)
        """
        self.title = title
        self.summary = summary
        self.report = report
        self.report_summary = report_summary
        self.max_chars = max_chars

    def get_app_payloads(self):
        """Creates and returns Slack Payloads built to be posted to a Slack App

        Returns
        -------
        payloads : list
            A list of dicts.
        """

        if not self.report_summary:
            return

        # Building payloads for Slack app
        logging.info("Building payload for Slack App..")
        payloads = [{"text": f"*{self.title}*\n```{self.report_summary}```"}]

        # If the payload is too large for the Slack App it will be split into multiple posts
        if len(str(payloads)) > self.max_chars:
            logging.info("The message will be to large. Splitting up into chunks..")
            payloads = self.split_msg(as_app=True)

        logging.info(f"{len(payloads)} slack app payloads created. ")

        return payloads

    def get_workflow_posts(self):
        """Add a tuple of 'title' and 'report_summary' to a posts list which may be used to post to a Slack Workflow

        Returns
        -------
        posts : list
            A list of tuples.
        """

        # If posting to a Slack Workflow the payload is build by the Message Handler
        if not self.report_summary:
            return

        logging.info("Building payload for Slack Workflow..")
        posts = [(self.title, self.report_summary)]

        # If the payload is too large for the Slack App it will be split into multiple posts
        if len(self.report_summary) > self.max_chars:
            logging.info("The message will be to large. Splitting up into chunks..")
            posts = self.split_msg(as_app=False)

        logging.info(f"{len(posts)} post will be posted..")
        return posts

    def split_msg(self, as_app=False):
        """splits long messages into multiple parts - to be posted to Slack individually

        Returns
        -------
        results : list
            The list of the split messages, dict or tuples
        """

        results = []

        # If Slack App then the messages have to be formatted. Triple backticks are added in the beginning and in the
        # end of each message. If Slack Workflow, the formatting is handled by the Slack Workflow itself.
        # For Slack App 'payloads' are created. For Slack Workflow 'txt' items are created.
        cb = ""
        if as_app:
            cb = "```"

        # The summary payload is created first and added to the list of results (to be posted)
        if as_app:
            payload = {"text": f"*{self.title} - summary*\n{cb}{self.summary}{cb}"}
            results.append(payload)
        else:
            results.append((f"{self.title} - summary", self.summary))

        # Then the report is split into chucks
        report_lines = self.report.splitlines()

        # The two first lines of the report is the header, which will be used in every part
        header = f"{cb}{report_lines.pop(0)}\n{report_lines.pop(0)}\n"

        # The first part of the first report payload / txt is initialized
        part = 1
        txt = ""
        payload = {"text": f"*{self.title} - Part {part}*\n{header}"}

        # Parse through every line of data in the report and add it to individual payloads / txt
        for line in report_lines:
            if len(txt) <= self.max_chars:
                txt += f"{line}\n"
                payload["text"] += f"{line}\n"
            else:
                # When a payload / txt have reacted it's max size it is added to the list of results
                if as_app:
                    payload["text"] += cb
                    results.append(payload)
                else:
                    results.append((f"{self.title} - Part {part}", f"{header}{txt}"))

                # Then a new payload / txt is initialized
                part += 1
                txt = f"{line}\n"
                payload = {"text": f"*{self.title} - Part {part}*\n{header}{txt}"}

        # If a remaining payload / txt exists, then it will also be added to the list of payloads
        if txt:
            if as_app:
                payload["text"] += cb
                results.append(payload)
            else:
                results.append((f"{self.title} - Part {part}", f"{header}{txt}"))

        logging.info(f"Message was split into {len(results)} chunks.")

        return results
