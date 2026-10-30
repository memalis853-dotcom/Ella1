"""Healing series logo marks: a ring with a leaf, plus one symbol per book."""

GOLD, CREAM, LEAF, TERRA = "#E3A12F", "#FBF6EC", "#6FA37A", "#C8643B"


def _mark(inner, ring=GOLD):
    return f"""<svg viewBox="0 0 100 100" width="100%" height="100%">
  <circle cx="50" cy="50" r="46" fill="none" stroke="{ring}" stroke-width="5"/>
  <circle cx="50" cy="50" r="36" fill="{CREAM}"/>
  {inner}
</svg>"""


# a leaf growing out of the symbol — shared by all three
LEAF_SPRIG = f"""<path d="M50 44 C50 30 58 22 70 20 C70 33 62 42 50 44 Z" fill="{LEAF}"/>
  <path d="M50 44 C50 34 44 27 34 25 C34 35 41 42 50 44 Z" fill="#2E5E4E"/>"""

LOGOS = {
    # plate seen from the side + sprig
    "plates": _mark(LEAF_SPRIG + f"""
  <path d="M26 54 H74 C72 66 62 74 50 74 C38 74 28 66 26 54 Z" fill="{TERRA}"/>
  <rect x="22" y="50" width="56" height="5" rx="2.5" fill="#2E5E4E"/>"""),
    # lunch box with handle + sprig
    "box": _mark(LEAF_SPRIG + f"""
  <path d="M40 52 V48 A4 4 0 0 1 44 44 H56 A4 4 0 0 1 60 48 V52" fill="none" stroke="#2E5E4E" stroke-width="3"/>
  <rect x="27" y="52" width="46" height="24" rx="5" fill="{TERRA}"/>
  <rect x="27" y="60" width="46" height="3" fill="{GOLD}"/>"""),
    # glass with juice + sprig
    "sips": _mark(LEAF_SPRIG + f"""
  <path d="M35 46 H65 L61 78 H39 Z" fill="#fff" stroke="#2E5E4E" stroke-width="3" stroke-linejoin="round"/>
  <path d="M37 56 H63 L61 76 H39 Z" fill="{LEAF}"/>
  <circle cx="46" cy="66" r="2.2" fill="#fff"/><circle cx="54" cy="70" r="1.6" fill="#fff"/>"""),
}
