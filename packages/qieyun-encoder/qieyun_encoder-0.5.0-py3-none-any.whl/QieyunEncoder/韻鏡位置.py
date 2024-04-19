# -*- coding: utf-8 -*-

import re

from . import 常量
from .轉換 import 韻目到韻

_韻鏡母位置表 = [
    '脣音第一位', '脣音第二位', '脣音第三位', '脣音第四位',
    '舌音第一位', '舌音第二位', '舌音第三位', '舌音第四位',
    '牙音第一位', '牙音第二位', '牙音第三位', '牙音第四位',
    '齒音第一位', '齒音第二位', '齒音第三位', '齒音第四位', '齒音第五位',
    '喉音第一位', '喉音第二位', '喉音第三位', '喉音第四位',
    '舌齒音第一位', '舌齒音第二位',
]

_韻鏡母位置到韻鏡母號映射表 = {韻鏡母位置: 韻鏡母號 for 韻鏡母號, 韻鏡母位置 in enumerate(_韻鏡母位置表)}

_韻鏡母表 = [
    '幫非', '滂敷', '並奉', '明微',
    '端知', '透徹', '定澄', '泥孃',
    '見', '溪', '羣', '疑',
    '精照', '清穿', '從牀', '心審', '邪禪',
    '影', '曉', '匣', '喻',
    '來', '日',
]

_韻鏡母到韻鏡母號映射表 = {}

for 韻鏡母號, 韻鏡母 in enumerate(_韻鏡母表):
    _韻鏡母到韻鏡母號映射表[韻鏡母] = 韻鏡母號
    if len(韻鏡母) > 1:
        for 韻鏡母單字 in 韻鏡母:
            _韻鏡母到韻鏡母號映射表[韻鏡母單字] = 韻鏡母號

_韻鏡所有母 = ''.join(_韻鏡母表)

解析韻鏡位置描述 = re.compile('([%s])([%s])?([%s])([%s])([%s])' % (_韻鏡所有母, 常量.所有呼, 常量.所有等, 常量.所有韻, 常量.所有聲))

class 韻鏡位置:
    '''
    韻鏡位置。
    '''

    def __init__(self, 韻鏡母: str | int, 韻鏡開合: str | None, 韻鏡等: str, 韻: str, 聲: str) -> None:
        # normalize 母
        # - 韻鏡母號（0-22，從右至左計數）
        # - 韻鏡母位置（脣音第一位，etc）
        # - 韻鏡母
        #     - 精照，etc
        #     - 精，照，etc
        韻鏡母號 = _韻鏡母位置到韻鏡母號映射表.get(韻鏡母, _韻鏡母到韻鏡母號映射表.get(韻鏡母))
        if 韻鏡母號 is not None:
            self.韻鏡母號 = 韻鏡母號
        else:
            assert isinstance(韻鏡母, int), 'Unexpected 韻鏡母: ' + repr(韻鏡母)
            self.韻鏡母號 = 韻鏡母

        # normalize 開合
        # - 韻鏡轉號
        # - 韻鏡開合（開、合、None）
        韻1 = 韻目到韻(韻)
        if 韻1 in 常量.必爲開口的韻:
            韻鏡開合 = '開'
        elif 韻1 in 常量.必爲合口的韻:
            韻鏡開合 = '合'
        elif 韻1 in 常量.開合兼備的韻:
            assert 韻鏡開合 != None, 韻鏡開合
        elif 韻1 in 常量.開合中立的韻:
            韻鏡開合 = None
        self.韻鏡開合 = 韻鏡開合

        self.韻鏡等 = 韻鏡等

        # normalize 韻
        self.韻 = 韻目到韻(韻)

        self.聲 = 聲

    @property
    def 韻鏡母(self) -> str:
        return _韻鏡母表[self.韻鏡母號]

    @property
    def 最簡韻鏡母(self) -> str:
        韻鏡母號 = self.韻鏡母號
        韻鏡母 = self.韻鏡母

        if 0 <= 韻鏡母號 < 4:  # 幫非組
            return 韻鏡母[self.韻鏡等 == '三' and self.韻 in 常量.輕脣韻]
        if 4 <= 韻鏡母號 < 8 or 12 <= 韻鏡母號 < 17:  # 端知組、精照組
            return 韻鏡母[self.韻鏡等 in '二三']
        return 韻鏡母

    @staticmethod
    def from描述(描述: str):
        match = 解析韻鏡位置描述.fullmatch(描述)
        assert match is not None, 'Invalid 描述: ' + repr(描述)

        母, 韻鏡開合, 韻鏡等, 韻, 聲 = match.groups()

        return 韻鏡位置(母, 韻鏡開合, 韻鏡等, 韻, 聲)

    @property
    def 描述(self) -> str:
        return self.最簡韻鏡母 + (self.韻鏡開合 or '') + self.韻鏡等 + self.韻 + self.聲

    def __repr__(self) -> str:
        return f'<韻鏡位置 {self.描述}>'

    def __eq__(self, that) -> bool:
        if not isinstance(that, 韻鏡位置):
            return False
        return self.描述 == that.描述

    def __hash__(self) -> int:
        return hash(self.描述)
