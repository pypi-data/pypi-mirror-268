from typing import List, Union, NewType
from datetime import date as d, datetime as dt




text = NewType('text', str)
picklist = NewType('picklist', List[str])
textarea = NewType('textarea', str)
checkbox = NewType('checkbox', bool)
date = NewType('date', d)
datetime = NewType('datetime', dt)
number = NewType('number', Union[int, float])