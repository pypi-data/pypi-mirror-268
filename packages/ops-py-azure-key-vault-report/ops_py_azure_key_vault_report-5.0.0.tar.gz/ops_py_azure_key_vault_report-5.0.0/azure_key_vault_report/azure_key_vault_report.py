#!/usr/bin/env python

import logging
import datetime
from .html_table import HTMLTable
from .ms_teams_json import MSTeamsPayload
from .set_timestamp import set_timestamp, now
from .markdown import Markdown
from .config import *
from .slack_payloads import SlackPayloads


########################################################################################################################


class AzureKeyVaultReport(object):
    """generates a report from the results of 'az keyvault' commands

    The values of 'updated', 'created' and 'expires' are converted to date object
    and the age (in days) is calculated.

    Then a table is generated and sorted by (from top to bottom):
    the oldest 'Expiration' date, then by
    the oldest 'Last Updated' date


    Attributes
    ----------

    results : list
        The list of results from the 'az keyvault' commands, enriched with 'vault_name' and 'record_type'
    items : list
        The list of items.
        Items are enriched with more data, e.g. age of each date element, vault_name, record_type, record_name
    html_table :
        The html table object which are used to provide an HTML table for the MS Teams payload.
    vaults : list
         The unique list of vaults processed
    summary_values: dict
        The config for the summary report. Read from config.py
    report_values: dict
        The config for the report. Read from config.py
    report: str
        The report as standard Markdown
    summary: str
        The summary as standard Markdown


    Methods
    -------

    parse_results()
        Parse through the provided 'results' from the azure cli keyvault cmd outputs.
        For each result in the results new item is created and added to the items list.
        Each item contains the following data:
        - Date objects, created from the 'updated', 'created' and 'expires' values and stored as values
          in new X_ts keys.
        - The age (in days) is calculated from each of the date objects and stored as values in new X_age keys.
        - 'vault_name' and 'record_type
    add_report(self, expire_threshold=None, ignore_no_expiration=True, include_all=False, teams_json=False):
        Creates a detailed 'column and rows' report, from which a Markdown table is generated.
        An optional html may also be generated from this report.
        The columns: "Record Name", "Record Type", "Vault Name", "Last Updated", "Expiration" and "Comment"
        are defined in the 'config.py'
        The values for the "Comment" column is generated according to the age of 'updated', 'created' and 'expires'.
        If missing 'expires' then a comment concerning that is added.
    add_summary()
        Creates a Markdown table of the summary report. The text for this table is defined in the config.py
    sort_items():
        Returns a sorted list of all the records
    get_markdown_report()
        Returns the report(s) as Markdown table(s). The report and/or just the summary.
    get_teams_payload()
        Create and returns an MS Teams payload. The HTML table is added as a part of the payload, if no other
        text is provided as argument.
    get_html_table()
        Returns the HTML table which is used in the MS Teams payload.
    get_markdown_report_only()
        Returns the report as plaintext Markdown table.
    get_markdown_summary()
        Returns the summary as plaintext Markdown table.
    """

    def __init__(self, results):
        """
        Parameters
        ----------
        results : list
            The list of results from the 'az keyvault' commands, enriched with 'vault_name' and 'record_type'
        """

        self.results = results
        self.items = []
        self.vaults = []        # The unique list of vaults processed
        self.html_table = None  # HTML table object. Used for MS Teams
        self.report_md = ""
        self.report = []
        self.summary = {}
        self.summary_md = ""
        self.report_summary_md = ""
        self.slack_rows_md = []
        self.summary_values = config.get("summary")
        self.report_values = config.get("report")
        self.report_full = {
            "created_at": datetime.datetime.utcnow().isoformat(),
            "summary": {},
            "report": {}
        }

    def sort_items(self, expired_days=7, will_expire_days=14):
        """Sort the list of dict items by days to expiration

        If no parameters provided, this method will return a sorted list of all the records.
        The list will be sorted from top and down, by the oldest 'Expiration' date and then followed
        by the oldest 'Last Updated' date and then returns the sorted list.

        If any of the parameters provided, it will first create and sort an 'expired' list and then the same with
        a 'will_expire' list, and the finally a list with the other records.
        Each list will be sorted from top and down, by the oldest 'Expiration' date and then followed
        by the oldest 'Last Updated' date and then returns a combined list.

        Parameters
        ----------
        expired_days : int
            If provided, the record will be added to a separate list (expired),
            if the expires_age (days since expiration) of the record
            is between 0 the days provided in the expired_days argument.

        will_expire_days : int
            If provided, the record will be added to a separate list (will_expire),
            if the expires_age (days to expiration) of the record
            is between 0 the days provided in the will_expire_days argument,
            and the record is not already added to the expired list.
        """

        if not isinstance(expired_days, int):
            return sorted(self.items, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)

        expired = []
        will_expire = []
        others = []
        for item in self.items:
            expires_age = item.get("expires_age")
            if isinstance(expires_age, int) and expires_age <= 0 and abs(expires_age) <= expired_days:
                expired.append(item)
                continue

            if isinstance(expires_age, int) and 0 <= expires_age <= will_expire_days:
                will_expire.append(item)
                continue

            others.append(item)

        sorted_list = sorted(expired, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)
        sorted_list += sorted(will_expire, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)
        sorted_list += sorted(others, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)

        return sorted_list

    def parse_results(self):
        """parse through the result from the azure cli keyvault cmd output"""
        if not isinstance(self.results, list):
            return

        for r in self.results:
            for o in r.get("out"):
                item = {}
                if isinstance(o, dict):
                    vault_name = r.get("vault_name")
                    if vault_name not in self.vaults:
                        self.vaults.append(vault_name)

                    item["vault_name"] = vault_name
                    item["record_type"] = r.get("record_type")
                    item["record_name"] = o.get("name")

                    a = o.get("attributes")
                    if isinstance(a, dict):
                        for k, v in a.items():

                            if "enabled" in k:
                                item["enabled"] = v

                            if "updated" in k or "created" in k or "expires" in k and v:
                                value = v.split("T")[0]
                                item[k] = value
                                ts = set_timestamp(value)
                                item[f"{k}_ts"] = ts
                                age = (now() - ts).days
                                item[f"{k}_age"] = age

                                # Update the update age counters:

                                # If already expired
                                if "expires" in k and age > 0:
                                    self.summary_values["expired"]["value"] += 1

                                # One year and older, but less than two years
                                if "updated" in k and age < 365:
                                    self.summary_values["this_year"]["value"] += 1

                                # One year and older, but less than two years
                                if "updated" in k and (365 <= age < 365 * 2):
                                    self.summary_values["one_year"]["value"] += 1

                                # Two year and older, but less than three years
                                elif "updated" in k and (365 * 2 <= age < 365 * 3):
                                    self.summary_values["two_years"]["value"] += 1

                                # Three years and older
                                elif "updated" in k and age >= 365 * 3:
                                    self.summary_values["three_years"]["value"] += 1

                            if "expires" in k and not v:
                                self.summary_values["missing"]["value"] += 1

                self.items.append(item)

    def add_summary(self):
        """adds the summary as Markdown"""
        self.summary = {}
        self.summary_values["vaults"]["value"] = len(self.vaults)
        self.summary_values["records"]["value"] = len(self.items)

        rows = []
        for k, v in self.summary_values.items():
            if "heading" in k:
                rows.append(v)
            elif isinstance(v, dict):
                value = v.get("value")
                if value:
                    text = v.get("text")
                    rows.append([text, value])
                    self.summary[text] = value

        md = Markdown(rows)
        md.set_widths()
        self.summary_md = md.get_output(1)
        self.report_full["summary"]["rows"] = [self.summary]

    def add_report(self, expire_threshold=None, ignore_no_expiration=True, include_all=False, teams_json=False):
        """creates a plain text report and initiates ms team report generation if specified.
        returns the plain text report.

        Parameters
        ----------
        expire_threshold : int
            Ignore to report the record if days till the secret will expire are more than this 'expire_threshold' value
            NOTE: Secrets expiring today or already expired will always be reported.
        ignore_no_expiration : bool
            Report all records if set to False. If set to True only secrets with Expiration Date set will be reported.
        include_all : bool
            If set to True all records are included in the output.
        teams_json : bool
            If set to True then a report in json format containing a html table will also be generated.
        """
        if not isinstance(self.results, list):
            return

        # If argument 'teams_json' is True, then a html table is initialized. To be used with the MS Teams payload
        if teams_json:
            self.html_table = HTMLTable(self.report_values.get("heading"))
            self.html_table.init_html_table()

        # Ensure only heading and no data rows
        rows = [self.report_values["heading"]]
        rows_all = [self.report_values["heading"]]

        # Sort the items from top and down
        # First sort by the oldest 'Expiration' date
        # Then sort by the oldest 'Last Updated' date
        items = self.sort_items()

        logging.info(f"expire_threshold: {expire_threshold} {type(expire_threshold)} - "
                     f"ignore_no_expiration: {ignore_no_expiration} ({type(ignore_no_expiration)}) - "
                     f"include_all: {include_all} {type(include_all)}")

        for item in items:
            # Get name of the record. If no name, we skip to next item in the list
            record_name = item.get("record_name")
            if not record_name:
                continue

            # Get the record type
            record_type = item.get("record_type", "")

            # Get the Vault Name
            vault_name = item.get("vault_name", "")

            # Get the expires, update and enabled values
            expires = item.get("expires", "")
            expires_age = item.get("expires_age")
            updated = item.get("updated")
            updated_age = item.get("updated_age")
            enabled = item.get("enabled")

            # Add to row: the values of: 'record_name', 'record_type', 'vault_name' and 'updated'
            row = [record_name, record_type, vault_name, updated]

            # Add to row: the value of: 'expires' (if any)
            if expires:
                row.append(expires)
            else:
                row.append(" ")

            # Create 'comment' variable
            # The value of 'Comment' is dependent of the info from the 'expires' and 'update' values
            comment = ""
            if not enabled:
                comment += "Disabled. "

            if isinstance(expires_age, int):
                if expires_age <= 0:
                    comment += f"Will expire in {abs(expires_age)} days. "
                if expires_age > 0:
                    comment += f"Expired {expires_age} days ago. "

            if not expires:
                comment += f"Has no expiration date. "

            if isinstance(updated_age, int):
                comment += f"Updated {updated_age} days ago. "

            # A little cosmetic touch to avoid plural where it should not be used
            comment = comment.replace(" 1 days", " 1 day")

            # Add to row: the value of: 'comment'
            row.append(comment)

            # Add the row to the rows_all (The ones that will be stored in db, but not necessarily will be alerted on)
            rows_all.append(row)

            # Only include disabled entries if set to include_all
            if not include_all and not enabled:
                continue

            # Skip records with no Expiration Date set, only if 'ignore_no_expiration' and not 'include_all'
            if not expires:
                if ignore_no_expiration and not include_all:
                    continue

            # Handle those with Expiration Date
            if isinstance(expires_age, int):

                # Handle those which has not expired yet
                if expires_age < 0:
                    logging.info(f"'{record_name}' has not expired yet. "
                                 f"It will expire in {abs(expires_age)} days ({expires}).")

                    # Handle those within valid 'expire_threshold'
                    if isinstance(expire_threshold, int) and expire_threshold < abs(expires_age):
                        logging.info(f"'{record_name}' Expiration Date is within the valid specified threshold of "
                                     f"{expire_threshold} days. This record will start to be "
                                     f"reported in {abs(expires_age) - expire_threshold} days.")

                        # Only skipped if 'include_all' is not specified.
                        if not include_all:
                            continue

            # Then finally add the row to the rows (The ones that will be reported)
            rows.append(row)

            # Get Slack Markdown Payload of current row and add it is to list of Slack Markdown payloads
            slack_md_payload = self.get_slack_md(row)
            if slack_md_payload:
                self.slack_rows_md.append(slack_md_payload)

            # If a html_table is created, then also add the row to the html table. Used in MS Teams payload
            if self.html_table:
                self.html_table.add_html_row(*row)

        self.report_full["report"]["rows"] = self.create_kv_rows(rows_all)

        if include_all:
            rows = rows_all

        if not rows:
            logging.error("No report generated.")
            return

        # Create markdown of the report
        md = Markdown(rows)
        md.set_widths()
        if len(rows) > 1:
            self.report_md = md.get_output()

            # Create json of the report
            self.report = self.create_kv_rows(rows)

        logging.info("report generated.")

    def get_slack_md(self, row):
        payload = {"text": ""}
        for i, x in enumerate(self.report_values["heading"]):
            payload["text"] += f"*{row[i]}:* {x}\n"

        if payload.get("text"):
            return payload

    def create_kv_rows(self, rows):
        kv_rows = []
        for i, r in enumerate(rows):
            if i > 0:
                j = {}
                for n, v in enumerate(self.report_values.get("heading")):
                    j[v] = r[n]
                kv_rows.append(j)
        return kv_rows

    def get_report_full(self):
        return self.report_full

    def get_report(self):
        return self.report

    def get_summary(self):
        return self.summary

    def get_summary_markdown(self):
        """return the Markdown summary"""
        return self.summary_md

    def get_report_markdown(self):
        """return the Markdown report"""
        return self.report_md

    def get_report_summary_markdown(self):
        """return the plain text report"""
        if self.report_md:
            self.report_summary_md = f"{self.summary_md}\n\n{self.report_md}"
        else:
            self.report_summary_md = self.summary_md

        return self.report_summary_md

    def get_teams_payload(self, title, text=""):
        """build and return the MS Teams payload"""
        if not isinstance(self.results, list):
            return

        if len(self.items) == 0:
            return

        if not text:
            text = self.get_html_table()

        ms_teams_payload = MSTeamsPayload(title, text, self.summary_values)
        ms_teams_payload.set_json_facts()
        return ms_teams_payload.get_json_output()

    def get_html_table(self):
        """return the html table"""
        if self.html_table:
            return self.html_table.get_table()

    def get_slack_payloads(self, title, max_chars=3500, app=True, md=True):

        if md:
            return self.slack_rows_md

        self.get_summary_markdown()
        self.get_report_summary_markdown()
        self.get_report_markdown()

        p = SlackPayloads(title, self.summary_md, self.report_md, self.report_summary_md, max_chars=max_chars)
        if app:
            return p.get_app_payloads()

        return p.get_workflow_posts()
