from aleph.crawlers import DocumentCrawler
import os
import requests
import urlparse
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CLASS_COLLECTION = {
    'ZA_Crawler': 'ZA_gazettes',
    'ZA_EC_Crawler': 'ZA_EC_gazettes',
    'ZA_FS_Crawler': 'ZA_FS_gazettes',
    'ZA_GT_Crawler': 'ZA_GT_gazettes',
    'ZA_LP_Crawler': 'ZA_LP_gazettes',
    'ZA_MP_Crawler': 'ZA_MP_gazettes',
    'ZA_NC_Crawler': 'ZA_NC_gazettes',
    'ZA_NL_Crawler': 'ZA_NL_gazettes',
    'ZA_NW_Crawler': 'ZA_NW_gazettes',
    'ZA_WC_Crawler': 'ZA_WC_gazettes',
}

CLASS_JURISDICTION = {
    'ZA_Crawler': 'ZA',
    'ZA_EC_Crawler': 'ZA-EC',
    'ZA_FS_Crawler': 'ZA-FS',
    'ZA_GT_Crawler': 'ZA-GT',
    'ZA_LP_Crawler': 'ZA-LP',
    'ZA_MP_Crawler': 'ZA-MP',
    'ZA_NC_Crawler': 'ZA-NC',
    'ZA_NL_Crawler': 'ZA-NL',
    'ZA_NW_Crawler': 'ZA-NW',
    'ZA_WC_Crawler': 'ZA-WC',
}

CLASS_LABEL = {
    'ZA_Crawler': 'South African Government Gazettes',
    'ZA_EC_Crawler': 'Eastern Cape Provincial Gazettes',
    'ZA_FS_Crawler': 'Free State Provincial Gazettes',
    'ZA_GT_Crawler': 'Gauteng Provincial Gazettes',
    'ZA_LP_Crawler': 'Limpopo Provincial Gazettes',
    'ZA_MP_Crawler': 'Mpumalanga Provincial Gazettes',
    'ZA_NC_Crawler': 'Northern Cape Provincial Gazettes',
    'ZA_NL_Crawler': 'KwaZulu-Natal Provincial Gazettes',
    'ZA_NW_Crawler': 'North West Provincial Gazettes',
    'ZA_WC_Crawler': 'Western Cape Provincial Gazettes',
}


class Crawler(DocumentCrawler):
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

            if gazette.get('jurisdiction_code') != CLASS_JURISDICTION.get(self.__class__.__name__):
                continue

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


class ZA_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_Crawler')


class ZA_EC_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_EC_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_EC_Crawler')


class ZA_FS_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_FS_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_FS_Crawler')


class ZA_GT_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_GT_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_GT_Crawler')


class ZA_LP_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_LP_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_LP_Crawler')


class ZA_MP_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_MP_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_MP_Crawler')


class ZA_NC_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_NC_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_NC_Crawler')


class ZA_NL_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_NL_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_NL_Crawler')


class ZA_NW_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_NW_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_NW_Crawler')


class ZA_WC_Crawler(Crawler):
    COLLECTION_ID = CLASS_COLLECTION.get('ZA_WC_Crawler')
    COLLECTION_LABEL = CLASS_LABEL.get('ZA_WC_Crawler')
