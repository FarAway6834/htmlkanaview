from toolz import compose, partial, reduce

isolate = compose('\u2063\u200b\u2063'.join, partial(map, '{}\u20de'.format))

kanaview = compose("".join, partial(map, lambda x : x[1]), partial(sorted, key = lambda x : x[0]), lambda x : (([i, i + 1, i - 1][i % 3], [isolate, '\ufffa{}\ufffb'.format, compose('\ufff9'.__add__, isolate)][i % 3](j)) for i, j in enumerate((x for x in x.split(")") for x in x.split("[") for x in x.split("](")))))

ruby_replace_table = {"\ufff9" : "<ruby>", "\ufffa" : "<rp>（</rp><rt>", "\ufffb" : "</rt><rp）</rp></ruby>"}

RubyUnicode2Html = lambda x : reduce(lambda x, t : x.replace(*t), (x, *ruby_replace_table.items()))

RubyHtml2Unicode = lambda x : reduce(lambda x, t : x.replace(t[1], t[0]), (x, *ruby_replace_table.items()))

htmlkanaview = lambda x : RubyUnicode2Html(kanaview(x))