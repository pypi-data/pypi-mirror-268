#!/usr/bin/env python

import json


########################################################################################################################

class MSTeamsPayload(object):
    """Build a default MS Teams payload. Uses the provided 'title', 'text' and 'summary'.
    The text may be a html table.
    The summary is a dict where the key/value pairs name 'text'/'value' will be used to as facts in the payload.


    Attributes
    ----------
    title : str
        The title of the MS Teams message
    text : str
        The text of the MS Teams message, e.g. a html table
    summary : dict
        The dict which populates the 'facts'
    facts : list
        The list of facts which will be populated by the provided summary


    Methods
    -------
    set_json_facts()
        Parse the summary dict values. If any values contain a dict with a 'text' key it will be added to the list of
        dicts in the facts list. 'name': value of 'text'. 'value': value of 'value'.
    get_facts()
        Returns the list of facts
    get_json_output()
        Build a default MS Teams payload. Uses the provided 'title', 'text' and 'summary'. The 'text' dicts of the
        'summary' makes up the facts.
    """

    def __init__(self, title, text, summary):
        """
        Parameters
        ----------
        title : str
            The 'activityTitle' which is the title of the message in MS Teams
        text : str
            The text to be added below the 'facts'. The 'text' may be in html format.
        summary : dict
            The summary part of the config which will make upt the 'facts'.
        """

        self.title = str(title)
        self.text = str(text)
        self.summary = summary
        self.facts = []

    def set_json_facts(self):
        """generates the fact used in the json output for MS Teams"""

        self.facts = []
        for v in self.summary.values():
            if "text" in v:
                self.facts.append({"name": v.get("text"),
                                   "value": v.get("value")})

    def get_facts(self):
        return self.facts

    def get_json_output(self):
        """add the facts and text to the json output for MS Teams, and then return the json output

        Returns
        -------
        json object
            A payload in json format. If not fact are provided, then None is returned.
        """

        if not self.facts:
            return

        json_output = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0076D7",
            "summary": "-",
            "sections": [
                {
                    "activityTitle": self.title,
                    "activitySubtitle": "",
                    "activityImage": "",
                    "facts": [],
                    "markdown": True
                },
                {
                    "startGroup": True,
                    "text": ""
                }
            ]
        }

        json_output["sections"][0]["facts"] = self.facts
        json_output["sections"][1]["text"] = self.text

        return json.dumps(json_output)
