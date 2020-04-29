# -*- coding: utf-8 -*-

import gkeepapi
import time
import os
from tqdm import tqdm
import json

if "GOOGLE_KEEP_APP_USER" not in os.environ:
    raise ValueError(
        "GOOGLE_KEEP_APP_USER must be present in .env"
    )
if "GOOGLE_KEEP_APP_PASS" not in os.environ:
    raise ValueError(
        "GOOGLE_KEEP_APP_PASS must be present in .env"
    )

class SyncService:
    """Singleton class for syncing Google Keep Notes with local (and remote)
    git repository.

    >>> ss = SyncService()
    >>> ss.sync_all_notes()
    """
    def __init__(self):
        # config = self._load_config("app.config.json")
        self.filestore = "/notes"
        self.apprun_date = datetime.datetime.utcnow().date().isoformat()
        self.login_fail_sleep_time = 30
        self.keep = gkeepapi.Keep()

    def sync_all_notes(self):
        self._login()
        self._download_notes()
        self._write_notes_filestore()

    # def _load_config(config_file):
    #     with open(config_file, 'r') as f:
    #         config = json.load(f)
    #     return config

    def _login(self, num=0):
        print("Attempting to log in with .env credentials")
        try:
            success = keep.login(
                os.getenv("GOOGLE_KEEP_APP_USER"),
                os.getenv("GOOGLE_KEEP_APP_PASS"),
            )
        except Exception as e:
            if num >= 3:
                raise
            print("Exception raised:")
            print(e)
            print("Sleeping {} seconds and trying again".format(self._login_sleep_time))
            print(time.sleep(self.login_fail_sleep_time))
            return self._login(num=num+1)

        if not success:
            print("WARNING: login unsuccessful")
        return success


    def _download_notes(self):
        self.gnotes = keep.all()
        print("Downloaded {} notes".format(len(self.gnotes)))


    def _write_notes_filestore(self):
        text = """
        last_sync_date: {date}
        id: {id}
        title: {title}
        labels: {labels}
        body:
        {body}
        """
        if not self.gnotes:
            raise ValueError(
                "No google notes downloaded. Exiting."
            )

        if not os.path.isdir(self.filestore):
            os.makedirs(self.filestore)

        for note in tqdm(self.gnotes):
            fields = self._parse_note_fields(note)
            file_name = "{title}_{id}.txt".format(
                title=fields.get('title'),
                id=fields.get('id')
            )
            file_path = os.path.join(self.filestore, file_name)
            _text = text.format(
                date=self.apprun_date,
                id=fields.get('id'),
                title=fields.get('title'),
                labels=fields.get('labels'),
                body=fields.get('body'),
            )
            print("Writing to file: {}".format(file_name))
            with open(file_path, 'w') as f:
                f.write(_text)


    def _parse_note_fields(self, note):
        fields = {}
        fields["id"] = note.id or "none"
        fields["title"] = note.title or "unnamed"
        fields["labels"] = ", ".join(note.labels.all())
        fields["body"] = note.text
        return fields

