from aleph.crawlers import DocumentCrawler
import os
import requests
import urlparse
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Crawler(DocumentCrawler):
    COLLECTION_ID = 'zagazettes'
    COLLECTION_LABEL = 'South African Government Gazettes'
    SCHEDULE = DocumentCrawler.DAILY

    ARCHIVE_URI = os.environ.get('ZA_GAZETTE_ARCHIVE_URI')

    def crawl(self):
        index_url = urlparse.urljoin(
            self.ARCHIVE_URI, 'index/gazette-index-latest.jsonlines')
        logger.info("Fetching %s" % index_url)
        r = requests.get(index_url)
        r.raise_for_status()
        for idx, line in enumerate(r.text.splitlines()):
            gazette = json.loads(line)

            if self.skip_incremental(gazette.get('unique_id')):
                continue

            meta = self.make_meta({
                'foreign_id': gazette.get('unique_id'),
                'title': gazette.get('issue_title'),
                'extension': 'pdf',
                'mime_type': 'application/pdf',
                'file_name': os.path.basename(gazette.get('archive_path')),
                'source_url': gazette.get('original_uri'),
            })
            logger.info("Emitting %s" % gazette.get('unique_id'))
            self.emit_url(meta, gazette.get('archive_url'))
