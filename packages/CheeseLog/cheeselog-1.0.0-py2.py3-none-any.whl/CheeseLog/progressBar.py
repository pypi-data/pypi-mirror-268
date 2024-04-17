from typing import Tuple

class ProgressBar:
    def __init__(self, length: int = 20, template: str = '%b%l%r%b %p%', *, boundaryStr: str = '|', leftStr: str = '█', rightStr: str = '-'):
        self.length: int = length
        self.template: str = template
        self.boundaryStr: str = boundaryStr
        self.leftStr: str = leftStr
        self.rightStr: str = rightStr

    def __call__(self, value: float) -> Tuple[str, str]:
        left = round(value * self.length)
        right = self.length - left

        return self.template.replace('%b', self.boundaryStr).replace('%l', self.leftStr * left).replace('%r', self.rightStr * right).replace('%p', '{:.2f}'.format(value * 100)), self.template.replace('%b', self.boundaryStr).replace('%l', self.leftStr * left).replace('%r', self.rightStr * right).replace('%p', '<blue>{:.2f}</blue>'.format(value * 100)).replace('%', '%%')
