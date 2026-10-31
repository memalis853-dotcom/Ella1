"""Healing Words — Bonus Book 5: what God says about your child (31 days of declarations, KJV)."""
from preview import AUTHOR

BOOK6 = "Healing Words"
MARKS = {BOOK6: "words"}
VERSION = "King James Version (KJV)"


def v(theme, ref, text, says, word_says, declare):
    return dict(theme=theme, ref=ref, text=text, says=says, word_says=word_says, declare=declare)


DAYS = [
 # ---- Week 1: who my child is
 v("Wonderfully made", "Psalm 139:14",
   "I will praise thee; for I am fearfully and wonderfully made: marvellous are thy works; and that my soul knoweth right well.",
   "God made your child on purpose, with great care. Nothing about them is a mistake. Their mind, their body and their way of seeing the world are His marvellous work.",
   "my child is fearfully and wonderfully made",
   "I declare that my child is wonderfully made. They are not a mistake, not a problem to fix and not less than anyone. They are God's marvellous work, and I praise Him for them."),
 v("A gift from God", "Psalm 127:3",
   "Lo, children are an heritage of the LORD: and the fruit of the womb is his reward.",
   "Your child is a gift and a reward from God — not a burden. He chose you to carry, raise and love this precious child.",
   "my child is a heritage of the LORD",
   "I declare that my child is a gift from God to our family. I receive them with joy and thanksgiving. I was chosen to be their parent, and God will give me grace for every day."),
 v("A good future", "Jeremiah 29:11",
   "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.",
   "God already has good plans for your child's future. Whatever the reports say today, His thoughts towards them are peace and hope.",
   "God's thoughts toward my child are thoughts of peace and a good future",
   "I declare that my child has a good future. God's plans for them are peace, not evil. No diagnosis has the final word — God has the final word, and His word is hope."),
 v("Welcomed by Jesus", "Matthew 19:14",
   "But Jesus said, Suffer little children, and forbid them not, to come unto me: for of such is the kingdom of heaven.",
   "Jesus welcomes every child — including children who are loud, quiet, different or still learning. Nobody can stop your child from coming to Him.",
   "Jesus welcomes my child",
   "I declare that my child belongs. Jesus welcomes them with open arms. They are loved in God's house and nothing can keep them from His love."),
 v("God finishes what He starts", "Philippians 1:6",
   "Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ.",
   "God has started a good work in your child, and He will not stop halfway. Every small step forward is part of His bigger work.",
   "God will complete the good work He began in my child",
   "I declare that God is finishing the good work He started in my child. I celebrate every small step. What He has begun, He will complete."),
 v("Never alone", "Isaiah 41:10",
   "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.",
   "On the hard days, God is right there with you and your child. He promises to strengthen, help and hold you up.",
   "God is with my child, and He will strengthen, help and uphold them",
   "I declare that my child is never alone. God is with them at home, at school and everywhere they go. He strengthens them, helps them and holds them up."),
 v("Taught by the Lord", "Isaiah 54:13",
   "And all thy children shall be taught of the LORD; and great shall be the peace of thy children.",
   "God Himself is your child's teacher. He promises them great peace.",
   "my child shall be taught of the LORD and great shall be their peace",
   "I declare that my child is taught by the Lord. They will learn, understand and grow. Great is the peace of my child — in their mind, their body and their home."),
 # ---- Week 2: healing
 v("The Lord who heals", "Exodus 15:26",
   "…for I am the LORD that healeth thee.",
   "One of God's names is “the Lord who heals”. Healing is not just something He does — it is who He is.",
   "the LORD is the One who heals my child",
   "I declare that the Lord is my child's healer. Healing is God's nature, and I invite Him into every part of my child's body and mind today."),
 v("Health restored", "Jeremiah 30:17",
   "For I will restore health unto thee, and I will heal thee of thy wounds, saith the LORD…",
   "God promises to bring back health and to heal every wound — the ones we can see, and the ones we can't.",
   "God will restore health to my child and heal every wound",
   "I declare that God is restoring health to my child. Every weak and wounded place is being healed — in the gut, the brain, the nervous system and every cell."),
 v("By His stripes", "Isaiah 53:5",
   "But he was wounded for our transgressions, he was bruised for our iniquities: the chastisement of our peace was upon him; and with his stripes we are healed.",
   "Jesus carried our pain so that we could have peace and healing. Your child's healing has already been paid for on the cross.",
   "by the stripes of Jesus my child is healed",
   "I declare that by the stripes of Jesus, my child is healed. Jesus carried their pain and sickness, so that they can walk in peace and wholeness."),
 v("Who heals all diseases", "Psalm 103:2–3",
   "Bless the LORD, O my soul, and forget not all his benefits: Who forgiveth all thine iniquities; who healeth all thy diseases.",
   "Healing is one of God's good gifts — one of His “benefits”. He heals <b>all</b> diseases, not just some.",
   "God heals all of my child's diseases",
   "I bless the Lord and I will not forget His goodness. I declare that He heals all my child's diseases — every allergy, every illness, every weakness."),
 v("He sent His word", "Psalm 107:20",
   "He sent his word, and healed them, and delivered them from their destructions.",
   "God's word carries healing power. When you speak His word over your child, you are sending healing into their life.",
   "God sends His word to heal and deliver my child",
   "I declare that God's word is at work in my child right now. His word heals them and delivers them from everything that tries to destroy them."),
 v("Health and cure", "Jeremiah 33:6",
   "Behold, I will bring it health and cure, and I will cure them, and will reveal unto them the abundance of peace and truth.",
   "God doesn't just ease the symptoms — He brings health, cure and an overflow of peace.",
   "God brings health, cure and abundant peace to my child",
   "I declare health and cure over my child. God is revealing to them an abundance of peace and truth. Their body is coming into order."),
 v("Prosper and be in health", "3 John 1:2",
   "Beloved, I wish above all things that thou mayest prosper and be in health, even as thy soul prospereth.",
   "God's desire for your child is that they thrive in every way — body, mind and spirit.",
   "God wants my child to prosper and be in health",
   "I declare that my child prospers and is in good health. Their body, mind and spirit are thriving, because this is God's desire for them."),
 # ---- Week 3: speech, learning & understanding
 v("God is with your mouth", "Exodus 4:12",
   "Now therefore go, and I will be with thy mouth, and teach thee what thou shalt say.",
   "When Moses struggled to speak, God promised to be with his mouth and teach him what to say. God made our mouths, and He can help every child communicate.",
   "God is with my child's mouth and teaches them what to say",
   "I declare that God is with my child's mouth. He teaches them what to say. Words, sounds and communication are opening up in Jesus' name."),
 v("The tongue shall sing", "Isaiah 35:5–6",
   "Then the eyes of the blind shall be opened, and the ears of the deaf shall be unstopped. Then shall the lame man leap as an hart, and the tongue of the dumb sing…",
   "God's kingdom brings open eyes, open ears, strong legs and singing tongues. What seems stuck can be set free.",
   "my child's ears are open and their tongue shall sing",
   "I declare that my child's ears are open to hear and understand. Their legs are strong. Their tongue will speak and sing and praise God."),
 v("He makes the silent speak", "Mark 7:37",
   "And were beyond measure astonished, saying, He hath done all things well: he maketh both the deaf to hear, and the dumb to speak.",
   "Jesus healed a man who could not hear or speak, and the people said, “He has done all things well.” He still does all things well today.",
   "Jesus does all things well and makes the silent to speak",
   "I declare that Jesus does all things well in my child's life. Their ears hear and their mouth speaks. Our family will be astonished at God's goodness."),
 v("Knowledge and understanding", "Proverbs 2:6",
   "For the LORD giveth wisdom: out of his mouth cometh knowledge and understanding.",
   "Wisdom, knowledge and understanding are gifts that come straight from God.",
   "the LORD gives my child wisdom, knowledge and understanding",
   "I declare that my child receives wisdom, knowledge and understanding from the Lord. Their mind is clear and their brain is learning, growing and making new connections."),
 v("Wisdom freely given", "James 1:5",
   "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him.",
   "God gives wisdom generously and never makes us feel bad for asking. Ask Him for wisdom for your child — and for yourself as a parent.",
   "God gives wisdom generously to my child and to me",
   "Lord, I ask You for wisdom. I declare that You give it freely — to my child to learn, and to me to guide them. Thank You for showing me what my child needs."),
 v("Skill in all learning", "Daniel 1:17",
   "As for these four children, God gave them knowledge and skill in all learning and wisdom: and Daniel had understanding in all visions and dreams.",
   "God gave these young people knowledge and skill in all learning. He can give your child the same.",
   "God gives my child knowledge and skill in all learning",
   "I declare that God gives my child knowledge and skill in all learning. They will do well at school and at home, and they will understand what they are taught."),
 v("Growing in wisdom", "Luke 2:52",
   "And Jesus increased in wisdom and stature, and in favour with God and man.",
   "Even Jesus grew step by step — in wisdom, in body and in friendships. Growth is God's way.",
   "my child increases in wisdom and stature, and in favour with God and man",
   "I declare that my child grows in wisdom and in body. They have favour with God and with people — with teachers, friends, family and helpers."),
 # ---- Week 4: peace, sleep & strength
 v("A sound mind", "2 Timothy 1:7",
   "For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind.",
   "God gives power, love and a sound mind. Fear and confusion do not come from Him.",
   "God has given my child power, love and a sound mind",
   "I declare that my child has a sound mind. Fear has no place in them. They are filled with God's power and love, and their thoughts are calm and clear."),
 v("Peace that guards", "Philippians 4:7",
   "And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.",
   "God's peace stands like a guard over your child's heart and mind — even when things around them feel loud and overwhelming.",
   "the peace of God guards my child's heart and mind",
   "I declare that God's peace guards my child's heart and mind. In noisy places, in new places and in hard moments, His peace keeps them calm."),
 v("Perfect peace", "Isaiah 26:3",
   "Thou wilt keep him in perfect peace, whose mind is stayed on thee: because he trusteth in thee.",
   "When our minds rest on God, He keeps us in perfect peace — not a little peace, but perfect peace.",
   "God keeps my child in perfect peace",
   "I declare perfect peace over my child. Meltdowns are replaced with calm. Their mind rests in God, and our home is filled with His peace."),
 v("Lie down in peace", "Psalm 4:8",
   "I will both lay me down in peace, and sleep: for thou, LORD, only makest me dwell in safety.",
   "Bedtime can be a battle — but God promises peace and safety through the night.",
   "my child will lie down in peace and sleep in safety",
   "I declare that my child lies down in peace and sleeps. The Lord keeps them safe all night long. Our nights are restful and our mornings are bright."),
 v("Sweet sleep", "Proverbs 3:24",
   "When thou liest down, thou shalt not be afraid: yea, thou shalt lie down, and thy sleep shall be sweet.",
   "God's promise for bedtime: no fear, and sweet sleep.",
   "my child will not be afraid and their sleep shall be sweet",
   "I declare that my child is not afraid when they lie down. Their sleep is sweet, deep and peaceful. They wake up rested and refreshed."),
 v("Strength for the weak", "Isaiah 40:29",
   "He giveth power to the faint; and to them that have no might he increaseth strength.",
   "When your child — or you — feel weak and tired, God gives power and increases strength.",
   "God gives power and increases strength to my child",
   "I declare that God gives my child power and strength. Weak muscles grow strong, tired bodies are refreshed, and I too am strengthened for this journey."),
 # ---- Restoration, deliverance, protection & blessing
 v("Restoration", "Joel 2:25",
   "And I will restore to you the years that the locust hath eaten…",
   "God can give back what was lost — lost time, lost skills, lost sleep, lost joy. He is the God of restoration.",
   "God restores to my child everything that was lost",
   "I declare restoration over my child. Every lost year, every lost skill, every lost word is being restored. God is making up for lost time."),
 v("Delivered from all troubles", "Psalm 34:17",
   "The righteous cry, and the LORD heareth, and delivereth them out of all their troubles.",
   "God hears every cry — every prayer whispered at night. And He delivers from <b>all</b> troubles.",
   "the LORD hears my cry and delivers my child out of all their troubles",
   "I declare that the Lord hears my prayers for my child. He delivers them out of all their troubles — every sickness, every struggle, every fear."),
 v("Angels keep you", "Psalm 91:10–11",
   "There shall no evil befall thee, neither shall any plague come nigh thy dwelling. For he shall give his angels charge over thee, to keep thee in all thy ways.",
   "God surrounds your child with protection. He sends His angels to watch over them wherever they go.",
   "no evil shall befall my child, and God's angels keep them in all their ways",
   "I declare that no evil will come near my child. God's angels watch over them at home, at school, on the road and at play. My child is safe in God's care."),
 v("The Lord bless you", "Numbers 6:24–26",
   "The LORD bless thee, and keep thee: The LORD make his face shine upon thee, and be gracious unto thee: The LORD lift up his countenance upon thee, and give thee peace.",
   "This is God's own blessing over His children. Speak it over your child every night.",
   "the LORD blesses my child, keeps them, shines on them and gives them peace",
   "I bless my child in the name of the Lord. The Lord bless you and keep you. The Lord make His face shine on you and be gracious to you. The Lord lift His face towards you and give you peace."),
]

WELCOME_HTML = """<div class="author-photo small"><img src="img/author.webp" alt="Tris Eliverson"></div>
<div class="letter">
<p class="hello">Dear Mama, dear Papa,</p>
<p>Some days the reports, the waiting rooms and the worries are loud. On those days, I needed something louder: <b>what God says about my child</b>.</p>
<p>These 31 Bible verses are the ones I spoke over my own child — about healing, deliverance, restoration, speech, understanding, peace and strength. Each day has the verse, a simple explanation of what God is saying, and a declaration for you to speak out loud.</p>
<p>Say it over your child as they sleep, on the school run, or while you cook. Put their name in every declaration. And end each one the way I do:</p>
<p class="heart">“The Word says it — and I say Amen.” ♥</p>
<div class="sign">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div></div>"""

HOW_HTML = """
<p class="lead">Five minutes a day. One verse. One declaration. Spoken in faith over your child.</p>
<div class="step"><div class="n">1</div><div><h3>Read the verse</h3><p>Read it slowly — out loud if you can. All verses are from the King James Version (KJV).</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Understand what God is saying</h3><p>The simple explanation helps you see what the verse means for your child today.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Speak the declaration</h3><p>Put your child's name in the blank and declare it with faith. Lay your hand on them if they are comfortable with touch.</p></div></div>
<div class="step"><div class="n">4</div><div><h3>Say Amen</h3><p>“The Word says it — and I say Amen.” Amen means “so be it”. You are agreeing with God.</p></div></div>
<div class="step"><div class="n">5</div><div><h3>Write it down</h3><p>Use the lines at the bottom of each page to note prayers, answers and small victories.</p></div></div>
<div class="callout gold"><div class="t">My child's name</div><p>Write it here, and speak it every day: <span class="fill" style="min-width:90mm"></span></p></div>
<p class="disclaimer">Faith and good care walk together. Keep walking with your child's doctors, therapists and teachers — God works through them too.</p>
"""

CLOSING_HTML = """
<p class="lead">Thirty-one days of speaking life over your child. The words you have spoken are seeds — keep watering them.</p>
<div class="grid2">
 <div class="box"><h3>Keep going</h3><ul>
  <li>Start again at Day 1 next month.</li>
  <li>Choose a “verse of the week” and stick it on the fridge.</li>
  <li>Teach your child a short verse to say with you.</li></ul></div>
 <div class="box"><h3>Remember</h3><ul>
  <li>God hears every whispered prayer.</li>
  <li>Celebrate every answer — big or small.</li>
  <li>You are not alone on this journey.</li></ul></div>
</div>
<div class="verse-quote" style="margin-top:5mm">“The LORD bless thee, and keep thee.”<span>Numbers 6:24 · KJV</span></div>
<div class="sign" style="margin-top:6mm">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div>
<p class="disclaimer" style="margin-top:8mm">© Tris Eliverson. All rights reserved. For personal use only — please do not share or resell. Scripture quotations are from the King James Version (KJV), which is in the public domain. This book is for encouragement and prayer and does not replace medical care.</p>
"""


def pages():
    out = []

    def add(kind, data, toc=None):
        out.append((kind, data, toc))

    add("cover", dict(series="Bonus Book 5", title=BOOK6, logo="words",
        subtitle="What God Says About Your Child — 31 Days of Bible Declarations for Parents",
        tagline="The Word says it — and I say Amen.", free=[], badge=("31", "daily<br>declarations"), author=AUTHOR))
    add("text", dict(kicker="Welcome", title="What God says about your child", html=WELCOME_HTML), "What God says about your child")
    add("toc", None)
    add("text", dict(kicker="Start here", title="How to use this book", html=HOW_HTML), "How to use this book")
    sections = {1: "Week 1 · Who my child is", 8: "Week 2 · Healing", 15: "Week 3 · Speech, learning & understanding",
                22: "Week 4 · Peace, sleep & strength", 29: "Restoration, protection & blessing"}
    group = ""
    for i, d in enumerate(DAYS, 1):
        group = sections.get(i, group)
        add("verse", dict(d, day=i, version=VERSION, group=group.split(" · ")[-1]), sections.get(i))
    add("text", dict(kicker="Amen", title="Keep speaking life", html=CLOSING_HTML), "Keep speaking life")

    toc = [(t, i + 1) for i, (_, _, t) in enumerate(out) if t]
    for kind, data, _ in out:
        if kind == "toc":
            data = dict(kicker="Inside this book", title="Contents", items=toc)
        yield BOOK6, kind, data
