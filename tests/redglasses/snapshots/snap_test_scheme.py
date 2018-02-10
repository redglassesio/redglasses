# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_categories 1'] = {
    'data': {
        'allUsers': {
            'edges': [
                {
                    'node': {
                        'firstName': '',
                        'id': 'VXNlck5vZGU6MQ==',
                        'lastName': '',
                        'username': 'User'
                    }
                }
            ]
        }
    }
}
