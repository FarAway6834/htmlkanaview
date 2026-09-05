# htmlkanaview - 보카로 노래 연습용 라이브러리

htmlkanaview.py
```python
from toolz import compose, partial, reduce

isolate = compose('\u2063\u200b\u2063'.join, partial(map, '{}\u20de'.format))

kanaview = compose("".join, partial(map, lambda x : x[1]), partial(sorted, key = lambda x : x[0]), lambda x : (([i, i + 1, i - 1][i % 3], [isolate, '\ufffa{}\ufffb'.format, compose('\ufff9'.__add__, isolate)][i % 3](j)) for i, j in enumerate((x for x in x.split(")") for x in x.split("[") for x in x.split("](")))))

ruby_replace_table = {"\ufff9" : "<ruby>", "\ufffa" : "<rp>（</rp><rt>", "\ufffb" : "</rt><rp）</rp></ruby>"}

RubyUnicode2Html = lambda x : reduce(lambda x, t : x.replace(*t), (x, *ruby_replace_table.items()))

RubyHtml2Unicode = lambda x : reduce(lambda x, t : x.replace(t[1], t[0]), (x, *ruby_replace_table.items()))

htmlkanaview = lambda x : RubyUnicode2Html(kanaview(x))
```

## 배포 후 기대

```python
>>> from htmlkanaview import htmlkanaview
>>> print(htmlkanaview("""\
[理解](りかい)できないな
その[ヒステリック](ひすてり っく)な[情緒](じょうちょ)
[動物](どうぶつ)みたいで
まだ[動](うご)けないな
[日和見](ひよりみ)の[メッセージ](めっせーじ)
[化](ば)けた[迷路](めいろ)の[末](すえ)
[末端価格](まったんかかく)の[アイラビュー](あいらびゅー)
そのひとつで[世界](せかい)はこんなにも
ねぇ[絶賛何処](ぜっさんどこ)ぞの[マリオネット](まりおねっと)
[刻](きざ)まれた「[良](い)い[子](こ)」のA to Z
あたし[聖人君子](せいじんくんし)でありたいの
[中傷](ちゅうしょう)も[誹謗](ひぼう)も[真](ま)っ[平](ぴら)でさ
[製品価値](せいひんかち)だけ[頂戴](ちょうだい)な
[笑顔](えがお)は[解](と)けない
まだ[動](うご)けないまんま
[フラ](ふら)ついた[ステップ](すてっぷ)
[踏](ふ)み[外](はず)さないように
ほら[全部全部](ぜんぶぜんぶ)が
[最適](さいてき)であるように\
"""))
```

아 ㅅㅂ 배포하기 귀찮아