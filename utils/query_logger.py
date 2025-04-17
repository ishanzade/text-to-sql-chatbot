import json
import os
from collections import Counter

class QueryLogger:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def log_query(self, query):
        queries = self._load_queries()
        queries.append(query)
        with open(self.file_path, 'w') as f:
            json.dump(queries, f)

    def get_top_queries(self, n=5):
        queries = self._load_queries()
        counter = Counter(queries)
        return [q for q, _ in counter.most_common(n)]

    def _load_queries(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
