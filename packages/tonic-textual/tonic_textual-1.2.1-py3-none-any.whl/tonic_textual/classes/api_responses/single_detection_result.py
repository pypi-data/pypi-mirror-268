import json
from typing import Optional

class SingleDetectionResult(dict):
    def __init__(self, start: int, end: int, label: str, text: str, score: float, json_path: Optional[str]=None):
        self.start = start
        self.end = end
        self.label = label
        self.text = text
        self.score = score
        self.jsonPath = json_path
        if json_path is None:
            dict.__init__(self, start=start, end=end, label=label, text=text, score=score)
        else:
            dict.__init__(self, start=start, end=end, label=label, text=text, score=score, json_path=json_path)
            
    def describe(self):
        print(json.dumps(self))