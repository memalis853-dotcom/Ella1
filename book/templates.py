"""Jinja templates for each page type. Every page is one fixed A4 sheet."""

MACROS = r"""
{% macro footer(book, n) -%}
<div class="footer"><span class="fl">{{ mark }}{{ book }} · Tris Eliverson</span><span class="pn">{{ n }}</span></div>
{%- endmacro %}

{% macro recipe(r, kind, label, big=False) -%}
<div class="recipe {{ kind }}{% if big %} big{% endif %}">
  <div class="rh">
    <span class="meal">{{ label }}</span>
    <span class="rn">{{ r.name }}</span>
    <span class="meta">{% if r.region %}{{ r.region }}<br>{% endif %}{% if r.time %}{{ r.time }}{% endif %}</span>
  </div>
  <div class="rb">
    <div><div class="lbl">You need</div>
      <ul class="ing">{% for i in r.ing %}<li>{{ i }}</li>{% endfor %}</ul></div>
    <div><div class="lbl">Steps</div>
      <ol class="steps">{% for s in r.steps %}<li>{{ s }}</li>{% endfor %}</ol></div>
  </div>
  {% if r.goodfor %}<div class="goodfor">{% for g in r.goodfor %}<span class="pill">{{ g }}</span>{% endfor %}</div>{% endif %}
  {% if r.why or r.tip %}
  <div class="rf{% if not (r.why and r.tip) %} one{% endif %}">
    {% if r.why %}<div class="why"><b>Why it helps:</b> {{ r.why }}</div>{% endif %}
    {% if r.tip %}<div class="tip"><b>{{ r.tip_label or "Swap it" }}:</b> {{ r.tip }}</div>{% endif %}
  </div>{% endif %}
</div>
{%- endmacro %}
"""

PAGES = {
"cover": r"""
<section class="page cover">
  <div class="top"></div>
  {% if p.badge %}<div class="badge"><b>{{ p.badge[0] }}</b>{{ p.badge[1] }}</div>{% endif %}
  <div class="body">
    <h1>{{ p.title }}</h1>
    <div class="series">{{ p.series }}</div>
    <p class="sub">{{ p.subtitle }}</p>
    <div class="plate">{{ logos[p.logo] }}</div>
    <div class="free">{% for f in p.free %}<span>{{ f }}-free</span>{% endfor %}</div>
    {% if p.tagline %}<div class="tagline">{{ p.tagline }}</div>{% endif %}
  </div>
  <div class="author"><small>by</small>{{ p.author }}</div>
</section>""",

"text": r"""
<section class="page{% if p.white %} white{% endif %}">
  <div class="band"></div>
  <div class="inner">
    {% if p.kicker %}<div class="kicker">{{ p.kicker }}</div>{% endif %}
    {% if p.title %}<h1>{{ p.title }}</h1>{% endif %}
    {{ p.html }}
  </div>
  {{ footer(book, n) }}
</section>""",

"divider": r"""
<section class="page divider">
  <div class="band"></div>
  <div class="c">
    <div class="kicker">{{ p.kicker }}</div>
    <h1>{{ p.title }}</h1>
    <p>{{ p.text }}</p>
  </div>
</section>""",

"day": r"""
<section class="page">
  <div class="inner">
    <div class="dayhead">
      <div class="d"><small>Week {{ p.week }}</small>Day {{ p.day }}</div>
      {% if p.quote %}<div class="q">{{ p.quote }}</div>{% endif %}
    </div>
    {{ recipe(p.b, "breakfast", "Breakfast") }}
    {{ recipe(p.l, "lunch", "Lunch") }}
    {{ recipe(p.d, "dinner", "Dinner") }}
  </div>
  {{ footer(book, n) }}
</section>""",

"toc": r"""
<section class="page">
  <div class="band"></div>
  <div class="kicker">{{ p.kicker }}</div>
  <h1>{{ p.title }}</h1>
  <div class="toc">
  {% for t, pg in p["items"] %}<div class="ti"><span>{{ t }}</span><i></i><b>{{ pg }}</b></div>{% endfor %}
  </div>
  {{ footer(book, n) }}
</section>""",

"cards": r"""
<section class="page">
  <div class="band"></div>
  <div class="inner">
    {% if p.kicker %}<div class="kicker">{{ p.kicker }}</div>{% endif %}
    {% if p.title %}<h1 style="font-size:24pt">{{ p.title }}</h1>{% endif %}
    {% if p.intro %}<p class="muted">{{ p.intro }}</p>{% endif %}
    {% for r in p.recipes %}{{ recipe(r, p.kind, r.label) }}{% endfor %}
    {% if p.after %}{{ p.after }}{% endif %}
  </div>
  {{ footer(book, n) }}
</section>""",

"two": r"""
<section class="page">
  <div class="inner">
    {% for r in p.recipes %}{{ recipe(r, p.kind, r.label, not p.small) }}{% endfor %}
    {% if p.note %}<div class="sweetnote">{{ p.note }}</div>{% endif %}
  </div>
  {{ footer(book, n) }}
</section>""",

"calendar": r"""
<section class="page white">
  <div class="band"></div>
  <div class="kicker">{{ p.kicker }}</div>
  <h1 style="font-size:24pt">{{ p.title }}</h1>
  <table class="cal{% if p.month %} month{% endif %}{% if p.one %} one{% endif %}">
  {% for week in p.weeks %}<tr>
    {% for c in week %}{% if c %}<td><div class="dn">{{ c.day }}</div>
      {% for m in c.meals %}<div class="m {{ m[0] }}"><i>{{ m[1] }}</i>{{ m[2] }}</div>{% endfor %}</td>
    {% else %}<td class="empty"></td>{% endif %}{% endfor %}
  </tr>{% endfor %}
  </table>
  {{ footer(book, n) }}
</section>""",

"grocery": r"""
<section class="page">
  <div class="band"></div>
  <div class="kicker">{{ p.kicker }}</div>
  <h1 style="font-size:24pt">{{ p.title }}</h1>
  <p class="muted">{{ p.intro }}</p>
  <div class="groc">
    {% for cat, items in p.cats %}<div class="cat"><h3>{{ cat }}</h3><ul>{% for i in items %}<li>{{ i }}</li>{% endfor %}</ul></div>{% endfor %}
  </div>
  {% if p.after %}{{ p.after }}{% endif %}
  {{ footer(book, n) }}
</section>""",

"brands": r"""
<section class="page">
  <div class="band"></div>
  <div class="kicker">{{ p.kicker }}</div>
  <h1 style="font-size:24pt">{{ p.title }}</h1>
  <p class="muted small">{{ p.intro }}</p>
  <div class="brands">
    {% for reg in p.regions %}<div class="box"><h3>{{ reg.name }}</h3>
      {% for k, v in reg.rows %}<div class="row"><b>{{ k }}:</b> {{ v }}</div>{% endfor %}</div>{% endfor %}
  </div>
  {{ footer(book, n) }}
</section>""",
}

DOC = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{{ title }}</title>
<link rel="stylesheet" href="style.css"></head>
<body>
{% for p in pages %}{{ rendered[loop.index0] }}{% endfor %}
</body></html>"""
