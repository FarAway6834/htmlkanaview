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
<ruby>り⃞⁣​⁣か⃞⁣​⁣い⃞<rp>（</rp><rt>理解</rt><rp）</rp></ruby>で⃞⁣​⁣き⃞⁣​⁣な⃞⁣​⁣い⃞⁣​⁣な⃞⁣​⁣
⃞⁣​⁣そ⃞⁣​⁣の⃞<ruby>ひ⃞⁣​⁣す⃞⁣​⁣て⃞⁣​⁣り⃞⁣​⁣ ⃞⁣​⁣っ⃞⁣​⁣く⃞<rp>（</rp><rt>ヒステリック</rt><rp）</rp></ruby>な⃞<ruby>じ⃞⁣​⁣ょ⃞⁣​⁣う⃞⁣​⁣ち⃞⁣​⁣ょ⃞<rp>（</rp><rt>情緒</rt><rp）</rp></ruby>
⃞<ruby>ど⃞⁣​⁣う⃞⁣​⁣ぶ⃞⁣​⁣つ⃞<rp>（</rp><rt>動物</rt><rp）</rp></ruby>み⃞⁣​⁣た⃞⁣​⁣い⃞⁣​⁣で⃞⁣​⁣
⃞⁣​⁣ま⃞⁣​⁣だ⃞<ruby>う⃞⁣​⁣ご⃞<rp>（</rp><rt>動</rt><rp）</rp></ruby>け⃞⁣​⁣な⃞⁣​⁣い⃞⁣​⁣な⃞⁣​⁣
⃞<ruby>ひ⃞⁣​⁣よ⃞⁣​⁣り⃞⁣​⁣み⃞<rp>（</rp><rt>日和見</rt><rp）</rp></ruby>の⃞<ruby>め⃞⁣​⁣っ⃞⁣​⁣せ⃞⁣​⁣ー⃞⁣​⁣じ⃞<rp>（</rp><rt>メッセージ</rt><rp）</rp></ruby>
⃞<ruby>ば⃞<rp>（</rp><rt>化</rt><rp）</rp></ruby>け⃞⁣​⁣た⃞<ruby>め⃞⁣​⁣い⃞⁣​⁣ろ⃞<rp>（</rp><rt>迷路</rt><rp）</rp></ruby>の⃞<ruby>す⃞⁣​⁣え⃞<rp>（</rp><rt>末</rt><rp）</rp></ruby>
⃞<ruby>ま⃞⁣​⁣っ⃞⁣​⁣た⃞⁣​⁣ん⃞⁣​⁣か⃞⁣​⁣か⃞⁣​⁣く⃞<rp>（</rp><rt>末端価格</rt><rp）</rp></ruby>の⃞<ruby>あ⃞⁣​⁣い⃞⁣​⁣ら⃞⁣​⁣び⃞⁣​⁣ゅ⃞⁣​⁣ー⃞<rp>（</rp><rt>アイラビュー</rt><rp）</rp></ruby>
⃞⁣​⁣そ⃞⁣​⁣の⃞⁣​⁣ひ⃞⁣​⁣と⃞⁣​⁣つ⃞⁣​⁣で⃞<ruby>せ⃞⁣​⁣か⃞⁣​⁣い⃞<rp>（</rp><rt>世界</rt><rp）</rp></ruby>は⃞⁣​⁣こ⃞⁣​⁣ん⃞⁣​⁣な⃞⁣​⁣に⃞⁣​⁣も⃞⁣​⁣
⃞⁣​⁣ね⃞⁣​⁣ぇ⃞<ruby>ぜ⃞⁣​⁣っ⃞⁣​⁣さ⃞⁣​⁣ん⃞⁣​⁣ど⃞⁣​⁣こ⃞<rp>（</rp><rt>絶賛何処</rt><rp）</rp></ruby>ぞ⃞⁣​⁣の⃞<ruby>ま⃞⁣​⁣り⃞⁣​⁣お⃞⁣​⁣ね⃞⁣​⁣っ⃞⁣​⁣と⃞<rp>（</rp><rt>マリオネット</rt><rp）</rp></ruby>
⃞<ruby>き⃞⁣​⁣ざ⃞<rp>（</rp><rt>刻</rt><rp）</rp></ruby>ま⃞⁣​⁣れ⃞⁣​⁣た⃞⁣​⁣「⃞<ruby>い⃞<rp>（</rp><rt>良</rt><rp）</rp></ruby>い⃞<ruby>こ⃞<rp>（</rp><rt>子</rt><rp）</rp></ruby>」⃞⁣​⁣の⃞⁣​⁣A⃞⁣​⁣ ⃞⁣​⁣t⃞⁣​⁣o⃞⁣​⁣ ⃞⁣​⁣Z⃞⁣​⁣
⃞⁣​⁣あ⃞⁣​⁣た⃞⁣​⁣し⃞<ruby>せ⃞⁣​⁣い⃞⁣​⁣じ⃞⁣​⁣ん⃞⁣​⁣く⃞⁣​⁣ん⃞⁣​⁣し⃞<rp>（</rp><rt>聖人君子</rt><rp）</rp></ruby>で⃞⁣​⁣あ⃞⁣​⁣り⃞⁣​⁣た⃞⁣​⁣い⃞⁣​⁣の⃞⁣​⁣
⃞<ruby>ち⃞⁣​⁣ゅ⃞⁣​⁣う⃞⁣​⁣し⃞⁣​⁣ょ⃞⁣​⁣う⃞<rp>（</rp><rt>中傷</rt><rp）</rp></ruby>も⃞<ruby>ひ⃞⁣​⁣ぼ⃞⁣​⁣う⃞<rp>（</rp><rt>誹謗</rt><rp）</rp></ruby>も⃞<ruby>ま⃞<rp>（</rp><rt>真</rt><rp）</rp></ruby>っ⃞<ruby>ぴ⃞⁣​⁣ら⃞<rp>（</rp><rt>平</rt><rp）</rp></ruby>で⃞⁣​⁣さ⃞⁣​⁣
⃞<ruby>せ⃞⁣​⁣い⃞⁣​⁣ひ⃞⁣​⁣ん⃞⁣​⁣か⃞⁣​⁣ち⃞<rp>（</rp><rt>製品価値</rt><rp）</rp></ruby>だ⃞⁣​⁣け⃞<ruby>ち⃞⁣​⁣ょ⃞⁣​⁣う⃞⁣​⁣だ⃞⁣​⁣い⃞<rp>（</rp><rt>頂戴</rt><rp）</rp></ruby>な⃞⁣​⁣
⃞<ruby>え⃞⁣​⁣が⃞⁣​⁣お⃞<rp>（</rp><rt>笑顔</rt><rp）</rp></ruby>は⃞<ruby>と⃞<rp>（</rp><rt>解</rt><rp）</rp></ruby>け⃞⁣​⁣な⃞⁣​⁣い⃞⁣​⁣
⃞⁣​⁣ま⃞⁣​⁣だ⃞<ruby>う⃞⁣​⁣ご⃞<rp>（</rp><rt>動</rt><rp）</rp></ruby>け⃞⁣​⁣な⃞⁣​⁣い⃞⁣​⁣ま⃞⁣​⁣ん⃞⁣​⁣ま⃞⁣​⁣
⃞<ruby>ふ⃞⁣​⁣ら⃞<rp>（</rp><rt>フラ</rt><rp）</rp></ruby>つ⃞⁣​⁣い⃞⁣​⁣た⃞<ruby>す⃞⁣​⁣て⃞⁣​⁣っ⃞⁣​⁣ぷ⃞<rp>（</rp><rt>ステップ</rt><rp）</rp></ruby>
⃞<ruby>ふ⃞<rp>（</rp><rt>踏</rt><rp）</rp></ruby>み⃞<ruby>は⃞⁣​⁣ず⃞<rp>（</rp><rt>外</rt><rp）</rp></ruby>さ⃞⁣​⁣な⃞⁣​⁣い⃞⁣​⁣よ⃞⁣​⁣う⃞⁣​⁣に⃞⁣​⁣
⃞⁣​⁣ほ⃞⁣​⁣ら⃞<ruby>ぜ⃞⁣​⁣ん⃞⁣​⁣ぶ⃞⁣​⁣ぜ⃞⁣​⁣ん⃞⁣​⁣ぶ⃞<rp>（</rp><rt>全部全部</rt><rp）</rp></ruby>が⃞⁣​⁣
⃞<ruby>さ⃞⁣​⁣い⃞⁣​⁣て⃞⁣​⁣き⃞<rp>（</rp><rt>最適</rt><rp）</rp></ruby>で⃞⁣​⁣あ⃞⁣​⁣る⃞⁣​⁣よ⃞⁣​⁣う⃞⁣​⁣に⃞
```

아 ㅅㅂ 배포하기 귀찮아