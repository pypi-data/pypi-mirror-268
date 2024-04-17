#!/usr/bin/env python

import logging


########################################################################################################################


class SlackPayloads(object):
    def __init__(self, title, summary, report, report_summary, max_chars=3500):
        self.title = title
        self.summary = summary
        self.report = report
        self.report_summary = report_summary
        self.max_chars = max_chars

    def get_app_payloads(self):
        if not self.report_summary:
            return

        # Building payloads for slack app
        logging.info("Building payload for Slack App..")
        payloads = [{"text": f"*{self.title}*\n```{self.report_summary}```"}]

        # If the payload is too large for the Slack App it will be split into multiple posts
        if len(str(payloads)) > self.max_chars:
            logging.info("The message will be to large. Splitting up into chunks..")
            payloads = self.split_msg(as_app=True)

        logging.info(f"{len(payloads)} slack app payloads created. ")

        return payloads

    def get_workflow_posts(self, max_chars=3500):
        # If posting to a Slack Workflow the payload is build by the Message Handler
        if not self.report_summary:
            return

        logging.info("Building payload for Slack Workflow..")
        posts = [(self.title, self.report_summary)]

        # If the payload is too large for the Slack App it will be split into multiple posts
        if len(self.report_summary) > max_chars:
            logging.info("The message will be to large. Splitting up into chunks..")
            posts = self.split_msg(as_app=False)

        logging.info(f"{len(posts)} post will be posted..")
        return posts

    def split_msg(self, as_app=False):
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
