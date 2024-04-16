from atcommon.models.base import BaseCoreModel
from pandas import DataFrame

def f(d: DataFrame):
    d.columns.all()

class Question:

    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"Q[{self.content}]"


class UserQuestion(Question):

    def __str__(self):
        return f"USER-Q[{self.content}]"



class StrucQuery:

    def __init__(self, content: str, params: dict = None):
        self.content = content
        self.params = params or {}

    def __str__(self):
        return self.to_string()


    def __repr__(self):
        return f"SQ[{self.to_string()[:20]}...]"

    def to_string(self):
        if self.params:
            params_formatted = "\n".join([f"{key}={value}" for key, value in self.params.items()])
            return f"{self.content}\nParams:\n{params_formatted}"
        else:
            return f"{self.content}"


class QueryResult:

    def __init__(self, query: StrucQuery, result):  # result: DataFrame
        self.query = query
        self.result = result

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.query} -> R[{self.row_count} 行 {self.column_count} 列]"

    def to_dict(self):
        return {
            "query": self.query.to_string(),
            "result_info": {
                "row_count": self.row_count,
                "column_count": self.column_count,
                "columns": self.columns.tolist(),
            }
        }

    def to_string(self, top_n=100):
        # 截取 前N行
        query_str = str(self.query)
        result_str = self.result.head(top_n).to_string(index=False)
        return f"\nQuery: \n{query_str}\nResult({top_n} of {self.row_count}rows):\n{result_str}"

    @property
    def rows(self):
        return self.result.to_numpy()

    @property
    def columns(self):
        return self.result.columns

    @property
    def row_count(self):
        return len(self.result)

    @property
    def column_count(self):
        return len(self.columns)


class BIAnswer(BaseCoreModel):
    __properties_init__ = [
        'status',
        'elapsed_time',
        'answer_text',
        'files',
        'charts',
        'query_insights',  # Transparency Reports
        'payload',

    ]

    def __str__(self):
        file_str = f"[File:{[f.get('url') for f in self.files]}]" if self.files else ''
        image_str = f"[Image:{[c.get('url') for c in self.charts]}]" if self.charts else ''
        return f"[{self.status}-{self.elapsed_time}s] {self.answer_text} {file_str} {image_str}"

    def __repr__(self):
        return self.__str__()

