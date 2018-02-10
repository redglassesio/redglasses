# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_post 1'] = {
    'data': {
        'allPosts': {
            'edges': [
                {
                    'node': {
                        'body': '',
                        'category': None,
                        'goLiveAt': '2018-01-05T05:36:00+00:00',
                        'id': 'UG9zdE5vZGU6MQ==',
                        'live': True,
                        'locked': False,
                        'seoTitle': '',
                        'slug': 'title',
                        'tags': {
                            'edges': [
                            ]
                        },
                        'title': 'Title '
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_categories 1'] = {
    'data': {
        'allCategories': {
            'edges': [
                {
                    'node': {
                        'id': 'Q2F0ZWdvcnlOb2RlOjE=',
                        'name': 'Category cat',
                        'slug': 'category-cat'
                    }
                }
            ]
        }
    }
}
