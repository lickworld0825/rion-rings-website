#!/usr/bin/env python3
"""Generate series-b through series-j HTML pages for Rion website."""
import os, re

SERIES = {
  'b': {
    'slug':'b','letter':'B','folder':'series-b',
    'name_en':'The <em>Pendant</em> Necklace','type_en':'Necklace · Sealed Hair Chamber',
    'name_ar':'قلادة <em>المعلّقة</em>','type_ar':'قلادة · غرفة شعر مختومة',
    'name_ja':'<em>ペンダント</em>ネックレス','type_ja':'ネックレス · 毛髪密封チャンバー',
    'badge_en':'Series B · Pendant','badge_ar':'السلسلة B · قلادة','badge_ja':'シリーズB · ペンダント',
    'desc_en':'A delicate necklace with a sealed pendant enclosing a strand of hair. Worn near the heart. The only necklace in the Rion collection — refined, intimate, and eternal.',
    'desc_ar':'قلادة رقيقة بميدالية مختومة تحوي خصلة شعر. تُرتدى قريباً من القلب. القلادة الوحيدة في مجموعة Rion — راقية وحميمية وأبدية.',
    'desc_ja':'毛髪を封入したペンダントを備えた繊細なネックレス。心に近い位置で。Rionコレクション唯一のネックレス——洗練されていて、親密で、永遠。',
    'type_tag_en':'Necklace · Sealed Hair Chamber',
    'sv_type_en':'Necklace','sv_type_ar':'قلادة','sv_type_ja':'ネックレス',
    'variants':[
      {'code':'B-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 26,800','img':'series-b/b1.jpg','popular':False},
      {'code':'B-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 28,800','img':'series-b/b2.jpg','popular':False},
      {'code':'B-3','key':'pg','mat_en':'K18 Pink Gold','mat_ar':'ذهب K18 زهري','mat_ja':'K18ピンクゴールド','price':'AED 26,800','img':'series-b/b3.jpg','popular':True},
      {'code':'B-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 25,000','img':'series-b/b4.jpg','popular':False},
    ],
    'default_variant':2, # index of default (B-3 Pink, popular)
    'related':[
      {'slug':'series-a','img':'series-a/a4.jpg','sname':'Series A','rname':'The <em>Classic</em> Ring','price':'AED 22,000'},
      {'slug':'series-c','img':'series-c/c4.jpg','sname':'Series C','rname':'The <em>Birthstone</em> Ring','price':'AED 27,800'},
      {'slug':'series-g','img':'series-g/g4.jpg','sname':'Series G','rname':'The <em>Refined</em> Ring','price':'AED 25,400'},
    ],
    'craft_p_en':'Every Series B necklace is handcrafted from start to finish by one artisan in our Japanese atelier. The pendant is hermetically sealed by hand, with the hair enclosed at its centre — invisible from outside, permanent within.',
    'craft_p_ar':'كل قلادة من السلسلة B مصنوعة من الألف إلى الياء بواسطة حرفي واحد في أتيليه الياباني. الميدالية مختومة يدوياً، مع الشعر في مركزها — غير مرئية من الخارج، دائمة من الداخل.',
    'craft_p_ja':'シリーズBのすべてのネックレスは、日本のアトリエで一人のアーティザンが最初から最後まで手作りします。ペンダントは手作業で気密封印され、毛髪がその中心に封じ込められています——外からは見えず、内側で永遠に。',
    'special_note':'',
  },
  'c': {
    'slug':'c','letter':'C','folder':'series-c',
    'name_en':'The <em>Birthstone</em> Ring','type_en':'Ring · 2 Birthstones',
    'name_ar':'خاتم <em>حجر الميلاد</em>','type_ar':'خاتم · حجران كريمان',
    'name_ja':'<em>誕生石</em>リング','type_ja':'リング · 誕生石2石',
    'badge_en':'Series C · 2 Birthstones','badge_ar':'السلسلة C · حجرا ميلاد','badge_ja':'シリーズC · 誕生石2石',
    'desc_en':'A ring with a sealed hair chamber and two birthstones of your choice — diamond, ruby, sapphire, emerald, and more. Perfect for commemorating a date or honouring a person whose birth month matters to you.',
    'desc_ar':'خاتم بغرفة شعر مختومة وحجرين من اختياركم — ألماس، ياقوت، ياقوت أزرق، زمرد، وأكثر. مثالي لإحياء ذكرى تاريخ أو تكريم شخص.',
    'desc_ja':'密封された毛髪チャンバーとお選びいただける2つの誕生石——ダイヤ・ルビー・サファイヤ・エメラルドほか。大切な日や大切な方の誕生月を記念するのに最適です。',
    'type_tag_en':'Ring · 2 Birthstones',
    'sv_type_en':'Ring','sv_type_ar':'خاتم','sv_type_ja':'リング',
    'variants':[
      {'code':'C-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 28,600','img':'series-c/c1.jpg','popular':False},
      {'code':'C-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 30,400','img':'series-c/c2.jpg','popular':False},
      {'code':'C-3','key':'pg','mat_en':'K18 Pink Gold','mat_ar':'ذهب K18 زهري','mat_ja':'K18ピンクゴールド','price':'AED 28,600','img':'series-c/c3.jpg','popular':False},
      {'code':'C-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 27,800','img':'series-c/c4.jpg','popular':True},
    ],
    'default_variant':3,
    'related':[
      {'slug':'series-a','img':'series-a/a4.jpg','sname':'Series A','rname':'The <em>Classic</em> Ring','price':'AED 22,000'},
      {'slug':'series-d','img':'series-d/d4.jpg','sname':'Series D','rname':'The <em>Half Eternity</em> Ring','price':'AED 34,600'},
      {'slug':'series-b','img':'series-b/b3.jpg','sname':'Series B','rname':'The <em>Pendant</em> Necklace','price':'AED 25,000'},
    ],
    'craft_p_en':'Every Series C ring is handcrafted in our Japanese atelier. The birthstones are hand-set by our master jeweller, alongside the hermetically sealed hair chamber. Choose any two stones — we guide you through the selection.',
    'craft_p_ar':'كل خاتم من السلسلة C مصنوع يدوياً في أتيليه الياباني. تُركّب الأحجار يدوياً بواسطة صائغنا الرئيسي، إلى جانب غرفة الشعر المختومة. اختاري أي حجرين — نرشدك في الاختيار.',
    'craft_p_ja':'シリーズCのすべてのリングは日本のアトリエで手作りされます。誕生石はヘッドジュエラーが手作業でセッティングし、気密封印された毛髪チャンバーと組み合わせます。どの2石でもお選びいただけます——選択のご案内はお任せください。',
    'special_note':'Birthstones: Choose any 2 from diamond, ruby, sapphire, emerald, amethyst, aquamarine, garnet, peridot, topaz, tourmaline, citrine, or tanzanite. Tell us your selection when you enquire.',
  },
  'd': {
    'slug':'d','letter':'D','folder':'series-d',
    'name_en':'The <em>Half Eternity</em> Ring','type_en':'Ring · Diamond Band',
    'name_ar':'خاتم <em>نصف الأبدية</em>','type_ar':'خاتم · حلقة ألماس',
    'name_ja':'<em>ハーフエタニティ</em>リング','type_ja':'リング · ダイヤモンドバンド',
    'badge_en':'Series D · Diamond Band','badge_ar':'السلسلة D · حلقة ألماس','badge_ja':'シリーズD · ダイヤモンドバンド',
    'desc_en':'A half eternity ring set with diamonds across the band, with a sealed inner chamber for hair. Exceptional brilliance, eternal meaning. For those who want their love to shine as well as endure.',
    'desc_ar':'خاتم نصف أبدي مرصع بالألماس عبر الحلقة، مع غرفة داخلية مختومة للشعر. تألق استثنائي ومعنى أبدي. لمن يريدن أن يتألق حبهن بالإضافة إلى بقائه.',
    'desc_ja':'バンドにダイヤモンドを配置し、内側に毛髪を封入するハーフエタニティリング。比類なき輝きと永遠の意味。愛を輝かせ、かつ永続させたい方のために。',
    'type_tag_en':'Ring · Diamond Band',
    'sv_type_en':'Ring','sv_type_ar':'خاتم','sv_type_ja':'リング',
    'variants':[
      {'code':'D-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 35,000','img':'series-d/d1.jpg','popular':False},
      {'code':'D-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 36,600','img':'series-d/d2.jpg','popular':False},
      {'code':'D-3','key':'pg','mat_en':'K18 Pink Gold','mat_ar':'ذهب K18 زهري','mat_ja':'K18ピンクゴールド','price':'AED 35,000','img':'series-d/d3.jpg','popular':False},
      {'code':'D-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 34,600','img':'series-d/d4.jpg','popular':True},
    ],
    'default_variant':3,
    'related':[
      {'slug':'series-c','img':'series-c/c4.jpg','sname':'Series C','rname':'The <em>Birthstone</em> Ring','price':'AED 27,800'},
      {'slug':'series-j','img':'series-j/j1.jpg','sname':'Series J','rname':'The <em>Statement</em> Ring','price':'AED 32,600'},
      {'slug':'series-a','img':'series-a/a4.jpg','sname':'Series A','rname':'The <em>Classic</em> Ring','price':'AED 22,000'},
    ],
    'craft_p_en':'Every Series D ring is handcrafted in our Japanese atelier. Diamonds are hand-set across the band by our master jeweller; the hair chamber is hermetically sealed within the inner band. Two crafts, one jewel — and your love at its heart.',
    'craft_p_ar':'كل خاتم من السلسلة D مصنوع يدوياً في أتيليه الياباني. يُركّب الألماس يدوياً عبر الحلقة بواسطة صائغنا الرئيسي؛ غرفة الشعر مختومة داخل الحلقة الداخلية. حرفتان، جوهرة واحدة — وحبك في مركزها.',
    'craft_p_ja':'シリーズDのすべてのリングは日本のアトリエで手作りされます。ダイヤモンドはヘッドジュエラーがバンドに手作業でセッティングし、毛髪チャンバーは内側のバンドに気密封印されています。2つのクラフト、1つのジュエリー——その中心にあなたの愛を。',
    'special_note':'Diamonds are included in the price. Diamond specifications are confirmed at the time of order.',
  },
  'f': {
    'slug':'f','letter':'F','folder':'series-f',
    'name_en':'The <em>Sculptural</em> Ring','type_en':'Ring · Statement Form',
    'name_ar':'الخاتم <em>المنحوت</em>','type_ar':'خاتم · شكل مميز',
    'name_ja':'<em>スカルプチュラル</em>リング','type_ja':'リング · ステートメントフォルム',
    'badge_en':'Series F · Sculptural','badge_ar':'السلسلة F · منحوت','badge_ja':'シリーズF · スカルプチュラル',
    'desc_en':'A more architectural, sculptural form. Bold lines, refined finish. For those who want a jewel that commands presence — a design that is worn as confidently as it is felt.',
    'desc_ar':'شكل أكثر معمارية ونحتاً. خطوط جريئة وتشطيب راقٍ. لأولئك الذين يريدون جوهرة تفرض حضورها — تصميم يُرتدى بنفس ثقة الإحساس به.',
    'desc_ja':'より建築的・彫刻的なフォルム。大胆なラインと洗練された仕上げ。存在感を放つジュエリーをお求めの方へ——身に着ける自信と同じくらい、感じる自信に応えるデザイン。',
    'type_tag_en':'Ring · Sculptural Form',
    'sv_type_en':'Ring','sv_type_ar':'خاتم','sv_type_ja':'リング',
    'variants':[
      {'code':'F-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 30,600','img':'series-f/f1.jpg','popular':False},
      {'code':'F-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 31,800','img':'series-f/f2.jpg','popular':False},
      {'code':'F-3','key':'pg','mat_en':'K18 Pink Gold','mat_ar':'ذهب K18 زهري','mat_ja':'K18ピンクゴールド','price':'AED 30,600','img':'series-f/f3.jpg','popular':False},
      {'code':'F-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 28,800','img':'series-f/f4.jpg','popular':True},
    ],
    'default_variant':3,
    'related':[
      {'slug':'series-h','img':'series-h/h4.jpg','sname':'Series H','rname':'The <em>Modern</em> Ring','price':'AED 27,500'},
      {'slug':'series-j','img':'series-j/j1.jpg','sname':'Series J','rname':'The <em>Statement</em> Ring','price':'AED 32,600'},
      {'slug':'series-a','img':'series-a/a4.jpg','sname':'Series A','rname':'The <em>Classic</em> Ring','price':'AED 22,000'},
    ],
    'craft_p_en':'Every Series F ring is handcrafted in our Japanese atelier. The sculptural form requires additional hand-finishing to achieve its precise, architectural edges — a process our artisans approach with meticulous care.',
    'craft_p_ar':'كل خاتم من السلسلة F مصنوع يدوياً في أتيليه الياباني. يتطلب الشكل النحتي تشطيباً إضافياً باليد لتحقيق حوافه المعمارية الدقيقة — عملية يتعامل معها حرفيونا بعناية فائقة.',
    'craft_p_ja':'シリーズFのすべてのリングは日本のアトリエで手作りされます。彫刻的なフォルムは、その正確で建築的なエッジを実現するために追加の手仕上げが必要です——職人が細心の注意を払って行う工程です。',
    'special_note':'',
  },
  'g': {
    'slug':'g','letter':'G','folder':'series-g',
    'name_en':'The <em>Refined</em> Ring','type_en':'Ring · Understated Luxury',
    'name_ar':'الخاتم <em>الراقي</em>','type_ar':'خاتم · فخامة هادئة',
    'name_ja':'<em>リファインド</em>リング','type_ja':'リング · 洗練された贅沢',
    'badge_en':'Series G · Refined','badge_ar':'السلسلة G · راقٍ','badge_ja':'シリーズG · リファインド',
    'desc_en':'A refined, elegant design with subtle detailing. Understated luxury — for those who carry their story quietly. Every detail has meaning; nothing is by accident.',
    'desc_ar':'تصميم راقٍ وأنيق بتفاصيل دقيقة. فخامة هادئة — لمن يحملون قصتهم بهدوء. كل تفصيل له معنى؛ لا شيء عرضي.',
    'desc_ja':'繊細なディテールを備えた上品で洗練されたデザイン。控えめな贅沢——物語を静かに身に着ける方へ。すべての細部に意味があり、偶然は何もありません。',
    'type_tag_en':'Ring · Understated Luxury',
    'sv_type_en':'Ring','sv_type_ar':'خاتم','sv_type_ja':'リング',
    'variants':[
      {'code':'G-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 26,200','img':'series-g/g1.jpg','popular':False},
      {'code':'G-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 27,500','img':'series-g/g2.jpg','popular':False},
      {'code':'G-3','key':'pg','mat_en':'K18 Pink Gold','mat_ar':'ذهب K18 زهري','mat_ja':'K18ピンクゴールド','price':'AED 26,200','img':'series-g/g3.jpg','popular':False},
      {'code':'G-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 25,400','img':'series-g/g4.jpg','popular':True},
    ],
    'default_variant':3,
    'related':[
      {'slug':'series-a','img':'series-a/a4.jpg','sname':'Series A','rname':'The <em>Classic</em> Ring','price':'AED 22,000'},
      {'slug':'series-h','img':'series-h/h4.jpg','sname':'Series H','rname':'The <em>Modern</em> Ring','price':'AED 27,500'},
      {'slug':'series-b','img':'series-b/b3.jpg','sname':'Series B','rname':'The <em>Pendant</em> Necklace','price':'AED 25,000'},
    ],
    'craft_p_en':'Every Series G ring is handcrafted in our Japanese atelier. The subtle surface detailing is achieved through patient hand-engraving — each motif applied individually by a single artisan over many hours.',
    'craft_p_ar':'كل خاتم من السلسلة G مصنوع يدوياً في أتيليه الياباني. يُحقق التفصيل السطحي الدقيق من خلال النقش اليدوي الصبور — كل نقش يُطبّق بشكل فردي بواسطة حرفي واحد على مدى ساعات طويلة.',
    'craft_p_ja':'シリーズGのすべてのリングは日本のアトリエで手作りされます。繊細な表面のディテールは、忍耐強い手彫りによって実現されています——各モチーフは一人の職人が何時間もかけて個別に施します。',
    'special_note':'',
  },
  'h': {
    'slug':'h','letter':'H','folder':'series-h',
    'name_en':'The <em>Modern</em> Ring','type_en':'Ring · Contemporary Form',
    'name_ar':'الخاتم <em>العصري</em>','type_ar':'خاتم · شكل معاصر',
    'name_ja':'<em>モダン</em>リング','type_ja':'リング · コンテンポラリーフォルム',
    'badge_en':'Series H · Modern','badge_ar':'السلسلة H · عصري','badge_ja':'シリーズH · モダン',
    'desc_en':'A contemporary form with clean geometry. Strong, modern, and deeply personal. The design that speaks without words — for those who find meaning in simplicity and strength.',
    'desc_ar':'شكل معاصر بهندسة نظيفة. قوي وعصري وشخصي. التصميم الذي يتحدث بلا كلمات — لمن يجدون المعنى في البساطة والقوة.',
    'desc_ja':'クリーンなジオメトリーの現代的フォルム。力強く、モダンで、深くパーソナル。言葉なく語るデザイン——シンプルさと強さに意味を見出す方へ。',
    'type_tag_en':'Ring · Contemporary Form',
    'sv_type_en':'Ring','sv_type_ar':'خاتم','sv_type_ja':'リング',
    'variants':[
      {'code':'H-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 28,200','img':'series-h/h1.jpg','popular':False},
      {'code':'H-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 29,400','img':'series-h/h2.jpg','popular':False},
      {'code':'H-3','key':'pg','mat_en':'K18 Pink Gold','mat_ar':'ذهب K18 زهري','mat_ja':'K18ピンクゴールド','price':'AED 28,200','img':'series-h/h3.jpg','popular':False},
      {'code':'H-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 27,500','img':'series-h/h4.jpg','popular':True},
    ],
    'default_variant':3,
    'related':[
      {'slug':'series-f','img':'series-f/f4.jpg','sname':'Series F','rname':'The <em>Sculptural</em> Ring','price':'AED 28,800'},
      {'slug':'series-g','img':'series-g/g4.jpg','sname':'Series G','rname':'The <em>Refined</em> Ring','price':'AED 25,400'},
      {'slug':'series-j','img':'series-j/j1.jpg','sname':'Series J','rname':'The <em>Statement</em> Ring','price':'AED 32,600'},
    ],
    'craft_p_en':'Every Series H ring is handcrafted in our Japanese atelier. The clean geometric form demands absolute precision in every angle and surface — achieved through careful hand-finishing that takes several days per piece.',
    'craft_p_ar':'كل خاتم من السلسلة H مصنوع يدوياً في أتيليه الياباني. يتطلب الشكل الهندسي النظيف دقة مطلقة في كل زاوية وسطح — تُحقق من خلال التشطيب اليدوي الدقيق الذي يستغرق عدة أيام لكل قطعة.',
    'craft_p_ja':'シリーズHのすべてのリングは日本のアトリエで手作りされます。クリーンなジオメトリックフォルムは、すべての角と表面に絶対的な精度を要求します——各作品に数日をかけた丁寧な手仕上げによって実現されます。',
    'special_note':'',
  },
  'j': {
    'slug':'j','letter':'J','folder':'series-j',
    'name_en':'The <em>Statement</em> Ring','type_en':'Ring · Statement Design',
    'name_ar':'خاتم <em>التميّز</em>','type_ar':'خاتم · تصميم مميز',
    'name_ja':'<em>ステートメント</em>リング','type_ja':'リング · ステートメントデザイン',
    'badge_en':'Series J · Statement','badge_ar':'السلسلة J · تميّز','badge_ja':'シリーズJ · ステートメント',
    'desc_en':'A bold, distinctive form — our most expressive design. For those who want their love to be seen as well as felt. Worn by those who carry loss openly, and find strength in it.',
    'desc_ar':'شكل جريء ومميز — تصميمنا الأكثر تعبيراً. لأولئك الذين يريدون أن يُرى حبهم كما يُحس. يرتديه من يحملون الخسارة بشكل علني، ويجدون فيها القوة.',
    'desc_ja':'大胆で印象的なフォルム——私たちの最も表現力豊かなデザイン。愛を感じるだけでなく、見せたい方へ。喪失を公に抱き、そこに強さを見出す方が身に着けます。',
    'type_tag_en':'Ring · Statement Design',
    'sv_type_en':'Ring','sv_type_ar':'خاتم','sv_type_ja':'リング',
    'variants':[
      {'code':'J-1','key':'yg','mat_en':'K18 Yellow Gold','mat_ar':'ذهب K18 أصفر','mat_ja':'K18イエローゴールド','price':'AED 33,400','img':'series-j/j1.jpg','popular':False},
      {'code':'J-2','key':'wg','mat_en':'K18 White Gold','mat_ar':'ذهب K18 أبيض','mat_ja':'K18ホワイトゴールド','price':'AED 34,600','img':'series-j/j2.jpg','popular':False},
      {'code':'J-4','key':'pt','mat_en':'Platinum Pt900','mat_ar':'بلاتين Pt900','mat_ja':'プラチナPt900','price':'AED 32,600','img':'series-j/j4.jpg','popular':True},
    ],
    'default_variant':2,
    'related':[
      {'slug':'series-d','img':'series-d/d4.jpg','sname':'Series D','rname':'The <em>Half Eternity</em> Ring','price':'AED 34,600'},
      {'slug':'series-f','img':'series-f/f4.jpg','sname':'Series F','rname':'The <em>Sculptural</em> Ring','price':'AED 28,800'},
      {'slug':'series-h','img':'series-h/h4.jpg','sname':'Series H','rname':'The <em>Modern</em> Ring','price':'AED 27,500'},
    ],
    'craft_p_en':'Every Series J ring is handcrafted in our Japanese atelier. The bold form requires advanced hand-crafting techniques — forged and finished over many days by a single artisan who treats each piece as a sculpture.',
    'craft_p_ar':'كل خاتم من السلسلة J مصنوع يدوياً في أتيليه الياباني. يتطلب الشكل الجريء تقنيات متقدمة للصناعة اليدوية — يُطرق ويُشطّب على مدى أيام من قبل حرفي واحد يتعامل مع كل قطعة كمنحوتة.',
    'craft_p_ja':'シリーズJのすべてのリングは日本のアトリエで手作りされます。大胆なフォルムには高度な手作業技術が必要です——各作品を彫刻として扱う一人の職人が何日もかけて鍛造・仕上げします。',
    'special_note':'',
  },
}

def build_variants_tabs_js(variants):
    lines = []
    for v in variants:
        pop = str(v['popular']).lower()
        lines.append(f"  {v['key']}:{{code:'{v['code']}',price:'{v['price']}',img:'images/{v['img']}',label:'{v['mat_en']}',popular:{pop}}}")
    return ',\n'.join(lines)

def build_variant_cards(variants):
    cards = []
    for v in variants:
        pop_badge = ' <span class="material-tag" data-i18n="popular">Popular</span>' if v['popular'] else ''
        cards.append(f'''    <a class="variant-card" href="product.html?code={v['code']}">
      <img src="images/{v['img']}" alt="{v['code']} {v['mat_en']}" loading="lazy">
      <div class="variant-info">
        <p class="variant-code">{v['code']}{pop_badge}</p>
        <p class="variant-material" data-i18n="mat_{v['key']}">{v['mat_en']}</p>
        <p class="variant-price">{v['price']}</p>
        <span class="variant-cta" data-i18n="view_detail">View Details →</span>
      </div>
    </a>''')
    return '\n'.join(cards)

def build_price_table_rows(variants):
    rows = []
    for v in variants:
        pop = ' <span class="material-tag" data-i18n="popular">Popular</span>' if v['popular'] else ''
        rows.append(f'''      <tr>
        <td>{v['code']}</td>
        <td>{v['mat_en']}{pop}</td>
        <td><span class="price-aed">{v['price']}</span></td>
        <td><span data-i18n="prod_time">Approx. 5.5 months</span></td>
      </tr>''')
    return '\n'.join(rows)

def build_related(related):
    cards = []
    for r in related:
        cards.append(f'''    <a href="{r['slug']}.html" class="related-card">
      <img src="images/{r['img']}" alt="{r['sname']}" loading="lazy">
      <div class="related-card-info">
        <p class="related-series">{r['sname']}</p>
        <p class="related-name">{r['rname']}</p>
        <p class="related-price">From {r['price']}</p>
        <span class="related-arrow" data-i18n="view_series">View Series →</span>
      </div>
    </a>''')
    return '\n'.join(cards)

def build_mat_tabs(variants):
    tabs = []
    for v in variants:
        tabs.append(f'      <button class="mat-tab" onclick="selectMat(\'{v["key"]}\')" data-i18n="mat_{v["key"]}">{v["mat_en"]}</button>')
    return '\n'.join(tabs)

def build_i18n_mats(variants, lang_key):
    pairs = []
    for v in variants:
        val = v[f'mat_{lang_key}']
        pairs.append(f"    mat_{v['key']}:'{val}'")
    return ',\n'.join(pairs)

TEMPLATE = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Series {LETTER} — {NAME_EN_PLAIN} | Rion Memorial Jewellery</title>
<meta name="description" content="Series {LETTER} — {NAME_EN_PLAIN}. Handcrafted memorial jewellery in Japan. K18 Gold &amp; Platinum. From {PRICE_FROM} DDP to Dubai &amp; UAE.">
<meta name="theme-color" content="#1A1714">
<link rel="canonical" href="https://rion.jewelry/series-{SLUG}.html">
<link rel="icon" type="image/jpeg" href="images/collection/ring.jpg">
<meta property="og:type" content="product">
<meta property="og:title" content="Series {LETTER} — {NAME_EN_PLAIN} | Rion">
<meta property="og:description" content="Handcrafted memorial ring in Japan. From {PRICE_FROM} DDP to Dubai.">
<meta property="og:image" content="images/{DEFAULT_IMG}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@200;300;400;500&family=Noto+Sans+Arabic:wght@300;400&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --gold:#C9A96E;--gold-light:#E8D5B0;--gold-dark:#8B6914;
  --cream:#FAF7F2;--ink:#1A1714;--ink-soft:#4A4540;--ink-muted:#8A8480;
  --border:rgba(201,169,110,0.25);--green:#128C7E;
}}
html{{scroll-behavior:smooth}}
body{{font-family:\'Jost\',sans-serif;background:var(--cream);color:var(--ink);font-weight:300;overflow-x:hidden}}
body.lang-ar{{font-family:\'Noto Sans Arabic\',sans-serif}}
nav{{position:sticky;top:0;z-index:200;display:flex;justify-content:space-between;align-items:center;padding:1.2rem 4rem;background:rgba(250,247,242,0.96);backdrop-filter:blur(12px);border-bottom:0.5px solid var(--border)}}
.nav-logo{{font-family:\'Cormorant Garamond\',serif;font-size:1.6rem;font-weight:300;letter-spacing:0.16em;color:var(--ink);text-decoration:none}}
.nav-right{{display:flex;align-items:center;gap:1.25rem}}
.lang-switcher{{display:flex;gap:2px}}
.lang-btn{{font-size:0.62rem;letter-spacing:0.12em;text-transform:uppercase;padding:4px 9px;border:0.5px solid var(--border);background:none;cursor:pointer;color:var(--ink-muted);font-family:\'Jost\',sans-serif;transition:all .2s}}
.lang-btn:hover{{color:var(--gold);border-color:var(--gold)}}
.lang-btn.active{{background:var(--ink);color:var(--gold);border-color:var(--ink)}}
.nav-cta{{font-size:0.68rem;letter-spacing:0.16em;text-transform:uppercase;background:var(--gold-dark);color:var(--cream);padding:8px 20px;text-decoration:none;transition:background .3s}}
.nav-cta:hover{{background:var(--ink)}}
.hamburger{{display:flex;flex-direction:column;justify-content:space-between;width:26px;height:18px;background:none;border:none;cursor:pointer;padding:0;position:relative;z-index:401;margin-left:0.5rem}}
.hamburger span{{display:block;width:100%;height:1px;background:var(--ink);transition:all .35s ease}}
.hamburger:hover span{{background:var(--gold-dark)}}
.hamburger.active span:nth-child(1){{transform:translateY(8.5px) rotate(45deg)}}
.hamburger.active span:nth-child(2){{opacity:0;transform:translateX(-20px)}}
.hamburger.active span:nth-child(3){{transform:translateY(-8.5px) rotate(-45deg)}}
.menu-overlay{{position:fixed;inset:0;background:var(--cream);z-index:400;opacity:0;visibility:hidden;transition:opacity .45s ease,visibility .45s ease;overflow-y:auto}}
.menu-overlay.active{{opacity:1;visibility:visible}}
.menu-inner{{padding:6rem 4rem 3rem;min-height:100%;display:flex;flex-direction:column;justify-content:space-between;max-width:1200px;margin:0 auto}}
.menu-eyebrow{{font-size:0.62rem;letter-spacing:0.32em;text-transform:uppercase;color:var(--gold-dark);margin-bottom:2.5rem;display:block}}
.menu-links{{display:flex;flex-direction:column;gap:0}}
.menu-links a{{font-family:\'Cormorant Garamond\',serif;font-size:clamp(1.7rem,3.6vw,2.6rem);font-weight:300;color:var(--ink);text-decoration:none;letter-spacing:0.02em;transition:color .3s,padding-left .35s ease,background .3s;line-height:1;padding:1.2rem 0.5rem 1.2rem 0;display:flex;align-items:baseline;gap:1.5rem;border-bottom:0.5px solid rgba(26,23,20,0.12)}}
.menu-links a:first-child{{border-top:0.5px solid rgba(26,23,20,0.12)}}
.menu-links a:hover{{color:var(--gold-dark);padding-left:1.25rem;background:rgba(201,169,110,0.08)}}
.menu-links a em{{font-style:italic;color:inherit}}
.menu-links a .menu-num{{font-family:\'Jost\',sans-serif;font-size:0.7rem;letter-spacing:0.22em;color:var(--ink-muted);font-style:normal;font-weight:400;flex-shrink:0;min-width:2.5rem}}
.menu-links a.menu-active{{color:var(--gold-dark)}}
.menu-footer{{margin-top:3rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1.5rem;padding-top:2rem;border-top:0.5px solid rgba(26,23,20,0.15)}}
.menu-lang{{display:flex;gap:0.4rem}}
.menu-lang button{{font-size:0.7rem;letter-spacing:0.14em;text-transform:uppercase;padding:8px 16px;border:0.5px solid rgba(26,23,20,0.3);background:transparent;cursor:pointer;color:var(--ink-soft);font-family:\'Jost\',sans-serif;transition:all .2s}}
.menu-lang button:hover,.menu-lang button.active{{background:var(--ink);color:var(--gold);border-color:var(--ink)}}
.menu-cta{{font-size:0.72rem;letter-spacing:0.18em;text-transform:uppercase;background:var(--green);color:#FFF;padding:1rem 2rem;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:background .3s;font-weight:500}}
.menu-cta:hover{{background:#0E7567}}
.menu-close{{position:absolute;top:1.4rem;right:4rem;width:32px;height:32px;background:none;border:none;cursor:pointer;padding:0;z-index:402;display:flex;align-items:center;justify-content:center}}
.menu-close::before,.menu-close::after{{content:\'\';position:absolute;width:24px;height:1px;background:var(--ink)}}
.menu-close::before{{transform:rotate(45deg)}}
.menu-close::after{{transform:rotate(-45deg)}}
.menu-close:hover::before,.menu-close:hover::after{{background:var(--gold-dark)}}
.breadcrumb{{padding:1rem 6rem;font-size:0.68rem;letter-spacing:0.12em;color:var(--ink-muted);text-transform:uppercase;border-bottom:0.5px solid var(--border);display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap}}
.breadcrumb a{{color:var(--ink-muted);text-decoration:none;transition:color .2s}}
.breadcrumb a:hover{{color:var(--gold-dark)}}
.breadcrumb-sep{{color:var(--gold);font-style:italic;font-family:\'Cormorant Garamond\',serif}}
.breadcrumb-current{{color:var(--gold-dark)}}
.series-hero{{display:grid;grid-template-columns:1fr 1fr;min-height:70vh;border-bottom:0.5px solid var(--border)}}
.hero-images{{position:relative;background:#F0EBE0;overflow:hidden}}
.hero-main-img{{width:100%;height:100%;object-fit:cover;display:block;min-height:500px}}
.hero-thumbs{{position:absolute;bottom:1.5rem;left:1.5rem;display:flex;gap:8px}}
.hero-thumb{{width:60px;height:60px;object-fit:cover;cursor:pointer;border:2px solid transparent;opacity:.75;transition:opacity .2s,border-color .2s}}
.hero-thumb:hover,.hero-thumb.active{{border-color:var(--gold);opacity:1}}
.hero-info{{padding:4rem 4rem 4rem 5rem;display:flex;flex-direction:column;justify-content:center;background:var(--cream)}}
.series-badge{{display:inline-flex;align-items:center;gap:8px;font-size:0.6rem;letter-spacing:0.28em;text-transform:uppercase;color:var(--gold-dark);margin-bottom:1.25rem}}
.series-badge::before{{content:\'✦\';color:var(--gold)}}
.series-name{{font-family:\'Cormorant Garamond\',serif;font-size:clamp(2rem,3.5vw,3rem);font-weight:300;line-height:1.1;margin-bottom:0.75rem}}
.series-name em{{font-style:italic;color:var(--gold-dark)}}
.series-type-tag{{display:inline-block;font-size:0.62rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--ink-muted);border:0.5px solid var(--border);padding:4px 12px;margin-bottom:1.5rem}}
.series-desc{{font-size:0.92rem;line-height:1.9;color:var(--ink-soft);margin-bottom:2rem;max-width:480px}}
.material-tabs{{display:flex;gap:6px;margin-bottom:1.5rem;flex-wrap:wrap}}
.mat-tab{{font-size:0.68rem;letter-spacing:0.12em;text-transform:uppercase;padding:8px 16px;border:0.5px solid var(--border);background:transparent;cursor:pointer;color:var(--ink-muted);font-family:\'Jost\',sans-serif;transition:all .2s}}
.mat-tab:hover{{border-color:var(--gold);color:var(--gold-dark)}}
.mat-tab.active{{background:var(--ink);color:var(--gold);border-color:var(--ink)}}
.price-display{{display:flex;align-items:baseline;gap:0.75rem;margin-bottom:0.5rem}}
.price-big{{font-family:\'Cormorant Garamond\',serif;font-size:2.2rem;color:var(--gold-dark);font-style:italic;line-height:1}}
.price-ddp{{font-size:0.65rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink-muted)}}
.price-note{{font-size:0.75rem;color:var(--ink-muted);margin-bottom:1.5rem}}
.code-display{{font-size:0.72rem;letter-spacing:0.18em;color:var(--ink-muted);text-transform:uppercase;margin-top:0.75rem}}
.code-display strong{{color:var(--gold-dark)}}
.hero-ctas{{display:flex;flex-direction:column;gap:0.75rem;margin-top:0.5rem}}
.btn-wa-hero{{display:flex;align-items:center;justify-content:center;gap:10px;background:var(--green);color:#FFF;font-size:0.76rem;letter-spacing:0.16em;text-transform:uppercase;padding:1.1rem 2rem;text-decoration:none;font-weight:500;transition:background .3s}}
.btn-wa-hero:hover{{background:#0E7567}}
.btn-outline-hero{{display:flex;align-items:center;justify-content:center;gap:8px;background:transparent;color:var(--ink);font-size:0.7rem;letter-spacing:0.16em;text-transform:uppercase;padding:0.9rem 2rem;text-decoration:none;border:0.5px solid var(--ink);transition:all .3s}}
.btn-outline-hero:hover{{background:var(--ink);color:var(--cream)}}
.variants-section{{padding:5rem 6rem;background:#F7F3EC;border-bottom:0.5px solid var(--border)}}
.section-eyebrow{{font-size:0.6rem;letter-spacing:0.28em;text-transform:uppercase;color:var(--gold-dark);margin-bottom:0.5rem;display:block}}
.section-title{{font-family:\'Cormorant Garamond\',serif;font-size:clamp(1.6rem,2.5vw,2rem);font-weight:300;margin-bottom:2rem}}
.section-title em{{font-style:italic;color:var(--gold-dark)}}
.variants-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--border)}}
.variant-card{{background:var(--cream);text-decoration:none;color:inherit;cursor:pointer;transition:background .25s}}
.variant-card:hover{{background:#FBF9F4}}
.variant-card img{{width:100%;aspect-ratio:1;object-fit:cover;display:block;transition:transform .4s}}
.variant-card:hover img{{transform:scale(1.04)}}
.variant-info{{padding:1.25rem 1rem}}
.variant-code{{font-size:0.6rem;letter-spacing:0.22em;text-transform:uppercase;color:var(--ink-muted);margin-bottom:4px}}
.variant-material{{font-size:0.82rem;color:var(--ink-soft);margin-bottom:4px}}
.variant-price{{font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;color:var(--gold-dark);font-style:italic}}
.variant-cta{{font-size:0.62rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold-dark);margin-top:6px;opacity:0;transition:opacity .2s;display:block}}
.variant-card:hover .variant-cta{{opacity:1}}
.material-tag{{display:inline-block;font-size:0.58rem;letter-spacing:0.14em;text-transform:uppercase;background:var(--gold-light);color:var(--gold-dark);padding:2px 8px;margin-left:6px}}
.price-table-section{{padding:4rem 6rem;border-bottom:0.5px solid var(--border)}}
.price-table{{width:100%;border-collapse:collapse;font-size:0.85rem}}
.price-table th{{font-size:0.6rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold-dark);padding:0.75rem 1rem;border-bottom:0.5px solid var(--border);text-align:left;font-weight:400}}
.price-table td{{padding:1rem 1rem;border-bottom:0.5px solid var(--border);color:var(--ink-soft)}}
.price-table tr:last-child td{{border-bottom:none}}
.price-table tr:hover td{{background:rgba(201,169,110,0.05)}}
.price-aed{{font-family:\'Cormorant Garamond\',serif;font-size:1rem;color:var(--gold-dark);font-style:italic}}
.special-note{{margin-top:1.5rem;padding:1rem 1.25rem;background:#F7F3EC;border:0.5px solid var(--border);font-size:0.82rem;color:var(--ink-soft);line-height:1.75}}
.special-note::before{{content:\'✦ \';color:var(--gold)}}
.specs-section{{padding:4rem 6rem;background:#F7F3EC;border-bottom:0.5px solid var(--border)}}
.specs-grid{{display:grid;grid-template-columns:1fr 1fr;gap:4rem;max-width:1000px}}
.spec-group h3{{font-size:0.6rem;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold-dark);margin-bottom:1.25rem}}
.spec-row{{display:grid;grid-template-columns:130px 1fr;gap:0.75rem;padding:0.75rem 0;border-bottom:0.5px solid var(--border);font-size:0.84rem}}
.spec-label{{color:var(--ink-muted);font-size:0.68rem;letter-spacing:0.1em;text-transform:uppercase}}
.spec-value{{color:var(--ink)}}
.craft-section{{padding:5rem 6rem;background:var(--ink);color:var(--cream)}}
.craft-inner{{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}}
.craft-text h2{{font-family:\'Cormorant Garamond\',serif;font-size:clamp(1.8rem,3vw,2.4rem);font-weight:300;color:var(--gold-light);margin-bottom:1rem}}
.craft-text h2 em{{font-style:italic;color:var(--gold)}}
.craft-text p{{font-size:0.88rem;line-height:1.9;color:rgba(250,247,242,0.6)}}
.craft-points{{display:flex;flex-direction:column;gap:1rem}}
.craft-point{{display:flex;gap:1rem;align-items:flex-start}}
.craft-point-num{{font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;color:var(--gold);font-style:italic;flex-shrink:0;line-height:1.4}}
.craft-point-text{{font-size:0.82rem;line-height:1.75;color:rgba(250,247,242,0.6)}}
.craft-point-text strong{{color:var(--gold-light);display:block;font-weight:400;font-size:0.7rem;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:2px}}
.enquire-section{{padding:6rem 6rem;text-align:center}}
.enquire-section h2{{font-family:\'Cormorant Garamond\',serif;font-size:clamp(1.8rem,3vw,2.6rem);font-weight:300;margin-bottom:0.75rem}}
.enquire-section h2 em{{font-style:italic;color:var(--gold-dark)}}
.enquire-section p{{font-size:0.9rem;color:var(--ink-muted);line-height:1.8;max-width:500px;margin:0 auto 2rem}}
.enquire-btns{{display:flex;justify-content:center;gap:1rem;flex-wrap:wrap}}
.btn-enquire-main{{display:inline-flex;align-items:center;gap:10px;background:var(--green);color:#FFF;font-size:0.78rem;letter-spacing:0.16em;text-transform:uppercase;padding:1.2rem 2.5rem;text-decoration:none;font-weight:500;transition:background .3s}}
.btn-enquire-main:hover{{background:#0E7567}}
.btn-view-all{{display:inline-flex;align-items:center;gap:8px;background:transparent;color:var(--ink);font-size:0.72rem;letter-spacing:0.16em;text-transform:uppercase;padding:1.1rem 2.2rem;text-decoration:none;border:0.5px solid var(--ink);transition:all .3s}}
.btn-view-all:hover{{background:var(--ink);color:var(--cream)}}
.related-section{{padding:4rem 6rem;border-top:0.5px solid var(--border);background:#F7F3EC}}
.related-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:2rem}}
.related-card{{text-decoration:none;color:inherit;display:block;background:var(--cream);border:0.5px solid var(--border);transition:border-color .25s}}
.related-card:hover{{border-color:var(--gold)}}
.related-card img{{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}}
.related-card-info{{padding:1.25rem}}
.related-series{{font-size:0.6rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold-dark);margin-bottom:4px}}
.related-name{{font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;font-weight:300;margin-bottom:4px}}
.related-name em{{font-style:italic}}
.related-price{{font-size:0.78rem;color:var(--ink-muted)}}
.related-arrow{{font-size:0.68rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--gold-dark);margin-top:8px;display:block;opacity:0;transition:opacity .2s}}
.related-card:hover .related-arrow{{opacity:1}}
footer{{background:var(--ink);padding:5rem 6rem 2rem;border-top:0.5px solid rgba(201,169,110,0.15)}}
.footer-grid{{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:4rem;margin-bottom:3.5rem}}
.footer-col h5{{font-size:0.62rem;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold);margin-bottom:1.25rem;font-weight:400}}
.footer-brand .footer-logo{{font-family:\'Cormorant Garamond\',serif;font-size:2rem;font-weight:300;color:var(--gold);letter-spacing:0.16em;text-decoration:none;display:block;margin-bottom:1rem}}
.footer-brand p{{font-size:0.78rem;line-height:1.85;color:rgba(250,247,242,0.55);margin-bottom:1.25rem;max-width:280px}}
.footer-brand .footer-est{{font-size:0.65rem;letter-spacing:0.18em;color:rgba(201,169,110,0.5);text-transform:uppercase}}
.footer-col ul{{list-style:none}}
.footer-col ul li{{margin-bottom:0.6rem}}
.footer-col ul a{{font-size:0.8rem;color:rgba(250,247,242,0.55);text-decoration:none;transition:color .25s}}
.footer-col ul a:hover{{color:var(--gold-light)}}
.footer-social{{display:flex;flex-direction:column;gap:0.6rem}}
.footer-social a{{display:inline-flex;align-items:center;gap:8px;font-size:0.78rem;color:rgba(250,247,242,0.55);text-decoration:none;transition:color .25s}}
.footer-social a:hover{{color:var(--gold-light)}}
.footer-social-ico{{color:var(--gold)}}
.footer-bottom{{display:flex;justify-content:space-between;align-items:center;padding-top:2rem;border-top:0.5px solid rgba(201,169,110,0.15);flex-wrap:wrap;gap:1rem}}
.footer-copy{{font-size:0.65rem;color:rgba(250,247,242,0.3)}}
.footer-right{{font-size:0.65rem;color:rgba(201,169,110,0.35);letter-spacing:0.1em;text-transform:uppercase}}
.scroll-top{{position:fixed;bottom:2rem;right:2rem;width:46px;height:46px;border-radius:50%;background:var(--ink);color:var(--gold);border:0.5px solid var(--gold);cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:250;opacity:0;visibility:hidden;transform:translateY(10px);transition:all .3s;font-size:1rem}}
.scroll-top:hover{{background:var(--gold-dark);color:var(--cream)}}
.scroll-top.visible{{opacity:1;visibility:visible;transform:translateY(0)}}
.scroll-top::before{{content:\'↑\'}}
@media(max-width:1024px){{
  nav{{padding:1.2rem 2rem}}.breadcrumb{{padding:0.75rem 2rem}}
  .series-hero{{grid-template-columns:1fr;min-height:auto}}.hero-info{{padding:2.5rem 2rem}}
  .variants-section,.price-table-section,.specs-section,.craft-section,.enquire-section,.related-section{{padding:3rem 2rem}}
  .variants-grid{{grid-template-columns:repeat(2,1fr)}}.specs-grid{{grid-template-columns:1fr;gap:2rem}}
  .craft-inner{{grid-template-columns:1fr}}.related-grid{{grid-template-columns:1fr 1fr}}
  footer{{padding:3rem 1.5rem 1.5rem}}.footer-grid{{grid-template-columns:1fr;gap:2.5rem;margin-bottom:2rem}}
  .footer-bottom{{flex-direction:column;align-items:flex-start;gap:0.5rem}}
}}
@media(max-width:480px){{.variants-grid{{grid-template-columns:1fr 1fr}}.related-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body class="lang-en">
<nav>
  <a href="rion-rings.html" class="nav-logo">Rion</a>
  <div class="nav-right">
    <div class="lang-switcher">
      <button class="lang-btn active" onclick="setLang(\'en\')">EN</button>
      <button class="lang-btn" onclick="setLang(\'ar\')">AR</button>
      <button class="lang-btn" onclick="setLang(\'ja\')">JA</button>
    </div>
    <a href="#enquire" class="nav-cta" data-i18n="nav_cta">Order Now</a>
    <button class="hamburger" aria-label="Open menu" onclick="toggleMenu()">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<div class="menu-overlay" id="menuOverlay" aria-hidden="true">
  <button class="menu-close" aria-label="Close menu" onclick="closeMenu()"></button>
  <div class="menu-inner">
    <div>
      <span class="menu-eyebrow">Navigation · القائمة · メニュー</span>
      <nav class="menu-links">
        <a href="rion-rings.html" onclick="closeMenu()"><span class="menu-num">01</span><span>Home</span></a>
        <a href="collection.html" class="menu-active" onclick="closeMenu()"><span class="menu-num">02</span><span>Collection</span></a>
        <a href="about.html" onclick="closeMenu()"><span class="menu-num">03</span><span>About <em>Rion</em></span></a>
        <a href="order.html" onclick="closeMenu()"><span class="menu-num">04</span><span>How to <em>Order</em></span></a>
        <a href="faq.html" onclick="closeMenu()"><span class="menu-num">05</span><span>FAQ</span></a>
        <a href="shipping.html" onclick="closeMenu()"><span class="menu-num">06</span><span>Shipping &amp; <em>Returns</em></span></a>
        <a href="care.html" onclick="closeMenu()"><span class="menu-num">07</span><span>Care <em>Guide</em></span></a>
        <a href="rion-rings.html#contact" onclick="closeMenu()"><span class="menu-num">08</span><span>Contact</span></a>
      </nav>
    </div>
    <div class="menu-footer">
      <div class="menu-lang">
        <button onclick="setLang(\'en\');closeMenu()">EN</button>
        <button onclick="setLang(\'ar\');closeMenu()">AR</button>
        <button onclick="setLang(\'ja\');closeMenu()">JA</button>
      </div>
      <a href="#" class="menu-cta" id="menuWa" target="_blank">💬 <span data-i18n="menu_wa">Message Us on WhatsApp</span></a>
    </div>
  </div>
</div>
<div class="breadcrumb">
  <a href="rion-rings.html" data-i18n="bc_home">Home</a>
  <span class="breadcrumb-sep">·</span>
  <a href="collection.html" data-i18n="bc_coll">Collection</a>
  <span class="breadcrumb-sep">·</span>
  <span class="breadcrumb-current" data-i18n="bc_cur">Series {LETTER}</span>
</div>
<section class="series-hero">
  <div class="hero-images">
    <img class="hero-main-img" id="mainImg" src="images/{DEFAULT_IMG}" alt="Series {LETTER}">
    <div class="hero-thumbs">
{THUMB_IMGS}
    </div>
  </div>
  <div class="hero-info">
    <span class="series-badge" data-i18n="badge">{BADGE_EN}</span>
    <h1 class="series-name" data-i18n="series_name">{NAME_EN}</h1>
    <span class="series-type-tag" data-i18n="type_tag">{TYPE_TAG_EN}</span>
    <p class="series-desc" data-i18n="series_desc">{DESC_EN}</p>
    <div class="material-tabs">
{MAT_TABS}
    </div>
    <div class="price-display">
      <span class="price-big" id="priceDisplay">{DEFAULT_PRICE}</span>
      <span class="price-ddp" data-i18n="ddp">DDP · all taxes incl.</span>
    </div>
    <p class="price-note" data-i18n="delivery_note">Approx. 5.5 months · Made to order in Japan</p>
    <p class="code-display" data-i18n="code_label">Code: <strong id="codeDisplay">{DEFAULT_CODE}</strong></p>
    <div class="hero-ctas">
      <a href="#" class="btn-wa-hero" id="heroWa" target="_blank">💬 <span data-i18n="cta_wa">Order via WhatsApp</span></a>
      <a href="collection.html" class="btn-outline-hero" data-i18n="cta_back">← Back to Collection</a>
    </div>
  </div>
</section>
<section class="variants-section">
  <span class="section-eyebrow" data-i18n="var_ey">{VAR_EY_EN}</span>
  <h2 class="section-title" data-i18n="var_title">Choose your <em>material</em></h2>
  <div class="variants-grid">
{VARIANT_CARDS}
  </div>
</section>
<section class="price-table-section">
  <span class="section-eyebrow" data-i18n="pt_ey">Series {LETTER} — Pricing</span>
  <h2 class="section-title" data-i18n="pt_title">All prices <em>DDP</em></h2>
  <table class="price-table">
    <thead>
      <tr>
        <th data-i18n="th_code">Code</th>
        <th data-i18n="th_mat">Material</th>
        <th data-i18n="th_price">Price (AED) · DDP incl. all UAE taxes</th>
        <th data-i18n="th_del">Production</th>
      </tr>
    </thead>
    <tbody>
{PRICE_ROWS}
    </tbody>
  </table>
{SPECIAL_NOTE_HTML}
  <p style="font-size:0.75rem;color:var(--ink-muted);margin-top:1rem;line-height:1.7" data-i18n="price_foot">All prices DDP — UAE import duty and 5% VAT prepaid by Rion. No charges on delivery.</p>
</section>
<section class="specs-section">
  <span class="section-eyebrow" data-i18n="spec_ey">Specifications</span>
  <h2 class="section-title" data-i18n="spec_title">Crafted to <em>last forever</em></h2>
  <div class="specs-grid">
    <div class="spec-group">
      <h3 data-i18n="sg1">Product</h3>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_type">Type</span><span class="spec-value" data-i18n="sv_type">{SV_TYPE_EN}</span></div>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_mat">Materials</span><span class="spec-value" data-i18n="sv_mat">K18 Yellow / White / Pink Gold · Platinum Pt900</span></div>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_seal">Hair Chamber</span><span class="spec-value" data-i18n="sv_seal">Hermetically sealed, handcrafted in Japan</span></div>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_eng">Engraving</span><span class="spec-value" data-i18n="sv_eng">Optional, up to 15 characters · + AED 250</span></div>
    </div>
    <div class="spec-group">
      <h3 data-i18n="sg2">Production &amp; Delivery</h3>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_prod">Production</span><span class="spec-value" data-i18n="sv_prod">Approx. 5.5 months from hair receipt</span></div>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_origin">Origin</span><span class="spec-value" data-i18n="sv_origin">100% handcrafted in Japan</span></div>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_ship">Shipping</span><span class="spec-value" data-i18n="sv_ship">DHL Express · Insured · DDP to UAE</span></div>
      <div class="spec-row"><span class="spec-label" data-i18n="sl_polish">Aftercare</span><span class="spec-value" data-i18n="sv_polish">Lifetime polishing in Japan, complimentary</span></div>
    </div>
  </div>
</section>
<section class="craft-section">
  <div class="craft-inner">
    <div class="craft-text">
      <h2 data-i18n="craft_h">Made entirely<br>by hand — <em>in Japan.</em></h2>
      <p data-i18n="craft_p">{CRAFT_P_EN}</p>
    </div>
    <div class="craft-points">
      <div class="craft-point"><span class="craft-point-num">i</span><div class="craft-point-text"><strong data-i18n="cp1_t">Hand Sealed</strong><span data-i18n="cp1_b">Every hair strand placed and sealed by a master artisan, documented with photographs.</span></div></div>
      <div class="craft-point"><span class="craft-point-num">ii</span><div class="craft-point-text"><strong data-i18n="cp2_t">Hermetic Chamber</strong><span data-i18n="cp2_b">Completely airtight and watertight — hair protected from moisture, air, and time.</span></div></div>
      <div class="craft-point"><span class="craft-point-num">iii</span><div class="craft-point-text"><strong data-i18n="cp3_t">Photo Report</strong><span data-i18n="cp3_b">We photograph the sealing process and send to you via WhatsApp.</span></div></div>
      <div class="craft-point"><span class="craft-point-num">iv</span><div class="craft-point-text"><strong data-i18n="cp4_t">Lifetime Polishing</strong><span data-i18n="cp4_b">Complimentary polishing in Japan, for as long as you own your piece.</span></div></div>
    </div>
  </div>
</section>
<section class="enquire-section" id="enquire">
  <h2 data-i18n="enq_h">Ready to begin?<br>We are <em>here.</em></h2>
  <p data-i18n="enq_p">Send us a message on WhatsApp to enquire about Series {LETTER}. No commitment required.</p>
  <div class="enquire-btns">
    <a href="#" class="btn-enquire-main" id="enquireWa" target="_blank">💬 <span data-i18n="enq_wa">Enquire via WhatsApp</span></a>
    <a href="order.html" class="btn-view-all" data-i18n="enq_order">How to Order →</a>
  </div>
</section>
<section class="related-section">
  <span class="section-eyebrow" data-i18n="rel_ey">You may also like</span>
  <h2 class="section-title" data-i18n="rel_title">More from the <em>Collection</em></h2>
  <div class="related-grid">
{RELATED_CARDS}
  </div>
</section>
<footer>
  <div class="footer-grid">
    <div class="footer-col footer-brand">
      <a href="rion-rings.html" class="footer-logo">Rion</a>
      <p>Bespoke memorial jewellery, handcrafted entirely in Japan. One hair. One jewel. One love.</p>
      <p class="footer-est">Est. 2018 · Japan</p>
    </div>
    <div class="footer-col"><h5>Explore</h5><ul>
      <li><a href="rion-rings.html">Home</a></li><li><a href="collection.html">Collection</a></li>
      <li><a href="about.html">About Rion</a></li><li><a href="order.html">How to Order</a></li>
    </ul></div>
    <div class="footer-col"><h5>Help</h5><ul>
      <li><a href="faq.html">FAQ</a></li><li><a href="care.html">Care Guide</a></li>
      <li><a href="shipping.html">Shipping &amp; Returns</a></li><li><a href="legal.html">Legal &amp; Privacy</a></li>
    </ul></div>
    <div class="footer-col"><h5>Connect</h5><div class="footer-social">
      <a href="#" id="footerWa" target="_blank"><span class="footer-social-ico">💬</span>WhatsApp</a>
      <a href="https://instagram.com/rion.rings_official" target="_blank"><span class="footer-social-ico">◈</span>Instagram</a>
    </div></div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">© 2026 Rion™ · My Art Inc. · 100% Made in Japan · DDP</div>
    <div class="footer-right">Est. 2018 · Japan · UAE &amp; Gulf</div>
  </div>
</footer>
<button class="scroll-top" id="scrollTop" onclick="window.scrollTo({{top:0,behavior:\'smooth\'}})"></button>
<script>
const WA=\'\';
const SERIES_LABEL=\'Series {LETTER}\';
const SERIES_NAME_FULL=\'Series {LETTER} — {NAME_EN_PLAIN}\';
const MATERIALS={{
{MATERIALS_JS}
}};
let cur=\'{DEFAULT_MAT_KEY}\';
function buildWa(msg){{return\'https://wa.me/\'+WA+(msg?\'?text=\'+encodeURIComponent(msg):\'\');}}
function updateWa(){{
  const m=MATERIALS[cur];
  const msg=\'Hello Rion, I\\\'d like to enquire about \'+m.code+\' — \'+SERIES_NAME_FULL+\' in \'+m.label+\'. Could you guide me?\';
  document.getElementById(\'heroWa\').href=buildWa(msg);
  document.getElementById(\'enquireWa\').href=buildWa(msg);
  document.getElementById(\'menuWa\').href=buildWa(\'\');
  document.getElementById(\'footerWa\').href=buildWa(\'\');
}}
function selectMat(mat){{
  cur=mat;const m=MATERIALS[mat];
  document.getElementById(\'priceDisplay\').textContent=m.price;
  document.getElementById(\'codeDisplay\').textContent=m.code;
  document.getElementById(\'mainImg\').src=m.img;
  document.querySelectorAll(\'.mat-tab\').forEach(b=>b.classList.remove(\'active\'));
  event.target.classList.add(\'active\');
  document.querySelectorAll(\'.hero-thumb\').forEach(t=>{{
    t.classList.toggle(\'active\',t.getAttribute(\'data-img\')===m.img);
  }});
  updateWa();
}}
function switchImg(el,src){{
  document.getElementById(\'mainImg\').src=src;
  document.querySelectorAll(\'.hero-thumb\').forEach(t=>t.classList.remove(\'active\'));
  el.classList.add(\'active\');
}}
function toggleMenu(){{
  const o=document.getElementById(\'menuOverlay\'),b=document.querySelector(\'.hamburger\');
  const a=o.classList.toggle(\'active\');b.classList.toggle(\'active\',a);
  o.setAttribute(\'aria-hidden\',a?\'false\':\'true\');document.body.style.overflow=a?\'hidden\':\'\';
}}
function closeMenu(){{
  const o=document.getElementById(\'menuOverlay\'),b=document.querySelector(\'.hamburger\');
  o.classList.remove(\'active\');b.classList.remove(\'active\');
  o.setAttribute(\'aria-hidden\',\'true\');document.body.style.overflow=\'\';
}}
document.addEventListener(\'keydown\',e=>{{if(e.key===\'Escape\')closeMenu();}});
window.addEventListener(\'scroll\',()=>{{
  window.scrollY>500?document.getElementById(\'scrollTop\').classList.add(\'visible\'):document.getElementById(\'scrollTop\').classList.remove(\'visible\');
}});
updateWa();
const T={{
  en:{{nav_cta:\'Order Now\',menu_wa:\'Message Us on WhatsApp\',
    bc_home:\'Home\',bc_coll:\'Collection\',bc_cur:\'Series {LETTER}\',
    badge:\'{BADGE_EN}\',series_name:\'{NAME_EN}\',type_tag:\'{TYPE_TAG_EN}\',series_desc:\'{DESC_EN_JS}\',
{I18N_MATS_EN},
    ddp:\'DDP · all taxes incl.\',delivery_note:\'Approx. 5.5 months · Made to order in Japan\',
    code_label:\'Code: \',cta_wa:\'Order via WhatsApp\',cta_back:\'← Back to Collection\',
    var_ey:\'{VAR_EY_EN}\',var_title:\'Choose your <em>material</em>\',
    popular:\'Popular\',view_detail:\'View Details →\',
    pt_ey:\'Series {LETTER} — Pricing\',pt_title:\'All prices <em>DDP</em>\',
    th_code:\'Code\',th_mat:\'Material\',th_price:\'Price (AED) · DDP incl. all UAE taxes\',th_del:\'Production\',
    prod_time:\'Approx. 5.5 months\',price_foot:\'All prices DDP — UAE import duty and 5% VAT prepaid by Rion.\',
    spec_ey:\'Specifications\',spec_title:\'Crafted to <em>last forever</em>\',
    sg1:\'Product\',sg2:\'Production & Delivery\',
    sl_type:\'Type\',sv_type:\'{SV_TYPE_EN}\',sl_mat:\'Materials\',sv_mat:\'K18 Yellow / White / Pink Gold · Platinum Pt900\',
    sl_seal:\'Hair Chamber\',sv_seal:\'Hermetically sealed, handcrafted in Japan\',
    sl_eng:\'Engraving\',sv_eng:\'Optional, up to 15 characters · + AED 250\',
    sl_prod:\'Production\',sv_prod:\'Approx. 5.5 months from hair receipt\',
    sl_origin:\'Origin\',sv_origin:\'100% handcrafted in Japan\',
    sl_ship:\'Shipping\',sv_ship:\'DHL Express · Insured · DDP to UAE\',
    sl_polish:\'Aftercare\',sv_polish:\'Lifetime polishing in Japan, complimentary\',
    craft_h:\'Made entirely<br>by hand — <em>in Japan.</em>\',craft_p:\'{CRAFT_P_EN_JS}\',
    cp1_t:\'Hand Sealed\',cp1_b:\'Every hair strand placed and sealed by a master artisan.\',
    cp2_t:\'Hermetic Chamber\',cp2_b:\'Completely airtight and watertight — hair protected from moisture, air, and time.\',
    cp3_t:\'Photo Report\',cp3_b:\'We photograph the sealing process and send to you via WhatsApp.\',
    cp4_t:\'Lifetime Polishing\',cp4_b:\'Complimentary polishing in Japan, for as long as you own your piece.\',
    enq_h:\'Ready to begin?<br>We are <em>here.</em>\',
    enq_p:\'Send us a message on WhatsApp to enquire about Series {LETTER}. No commitment required.\',
    enq_wa:\'Enquire via WhatsApp\',enq_order:\'How to Order →\',
    rel_ey:\'You may also like\',rel_title:\'More from the <em>Collection</em>\',view_series:\'View Series →\'
  }},
  ar:{{nav_cta:\'اطلب الآن\',menu_wa:\'راسلنا عبر واتساب\',
    bc_home:\'الرئيسية\',bc_coll:\'المجموعة\',bc_cur:\'السلسلة {LETTER}\',
    badge:\'{BADGE_AR}\',series_name:\'{NAME_AR}\',type_tag:\'{TYPE_AR}\',series_desc:\'{DESC_AR_JS}\',
{I18N_MATS_AR},
    ddp:\'DDP · جميع الضرائب مضمّنة\',delivery_note:\'حوالي 5.5 أشهر · مصنوع حسب الطلب في اليابان\',
    code_label:\'الرمز: \',cta_wa:\'اطلبي عبر واتساب\',cta_back:\'← العودة للمجموعة\',
    var_ey:\'أربع مواد · تصميم واحد\',var_title:\'اختاري <em>المادة</em>\',
    popular:\'الأكثر شيوعاً\',view_detail:\'عرض التفاصيل →\',
    pt_ey:\'السلسلة {LETTER} — الأسعار\',pt_title:\'جميع الأسعار <em>DDP</em>\',
    th_code:\'الرمز\',th_mat:\'المادة\',th_price:\'السعر (درهم) · DDP شامل الضرائب\',th_del:\'الإنتاج\',
    prod_time:\'حوالي 5.5 أشهر\',price_foot:\'جميع الأسعار DDP — رسوم الاستيراد وضريبة القيمة المضافة مدفوعة من Rion.\',
    spec_ey:\'المواصفات\',spec_title:\'مصنوعة لتدوم <em>للأبد</em>\',
    sg1:\'المنتج\',sg2:\'الإنتاج والتسليم\',
    sl_type:\'النوع\',sv_type:\'{SV_TYPE_AR}\',sl_mat:\'المواد\',sv_mat:\'ذهب K18 أصفر / أبيض / زهري · بلاتين Pt900\',
    sl_seal:\'غرفة الشعر\',sv_seal:\'مختومة بإحكام، مصنوعة يدوياً في اليابان\',
    sl_eng:\'النقش\',sv_eng:\'اختياري، حتى 15 حرفاً · + 250 درهم\',
    sl_prod:\'الإنتاج\',sv_prod:\'حوالي 5.5 أشهر من استلام الشعر\',
    sl_origin:\'المصدر\',sv_origin:\'مصنوع يدوياً بالكامل في اليابان\',
    sl_ship:\'الشحن\',sv_ship:\'DHL Express · مؤمّن · DDP للإمارات\',
    sl_polish:\'الرعاية\',sv_polish:\'تلميع مجاني مدى الحياة في اليابان\',
    craft_h:\'مصنوع بالكامل<br>يدوياً — <em>في اليابان.</em>\',craft_p:\'{CRAFT_P_AR_JS}\',
    cp1_t:\'ختم يدوي\',cp1_b:\'كل خصلة شعر توضع وتُختم بواسطة حرفي متخصص.\',
    cp2_t:\'غرفة محكمة\',cp2_b:\'محكمة الإغلاق ومقاومة للماء — الشعر محمي من الرطوبة والهواء والزمن.\',
    cp3_t:\'تقرير الصور\',cp3_b:\'نصوّر عملية الختم ونرسلها إليك عبر واتساب.\',
    cp4_t:\'تلميع مدى الحياة\',cp4_b:\'تلميع مجاني في اليابان طالما تملكين القطعة.\',
    enq_h:\'جاهزة للبدء؟<br>نحن <em>هنا.</em>\',
    enq_p:\'أرسلي لنا رسالة على واتساب للاستفسار عن السلسلة {LETTER}. لا التزام مطلوب.\',
    enq_wa:\'استفسري عبر واتساب\',enq_order:\'كيفية الطلب →\',
    rel_ey:\'قد يعجبك أيضاً\',rel_title:\'المزيد من <em>المجموعة</em>\',view_series:\'عرض السلسلة →\'
  }},
  ja:{{nav_cta:\'ご注文\',menu_wa:\'WhatsAppでメッセージ\',
    bc_home:\'ホーム\',bc_coll:\'コレクション\',bc_cur:\'シリーズ{LETTER}\',
    badge:\'{BADGE_JA}\',series_name:\'{NAME_JA}\',type_tag:\'{TYPE_JA}\',series_desc:\'{DESC_JA_JS}\',
{I18N_MATS_JA},
    ddp:\'DDP · 全税込み\',delivery_note:\'約5.5ヶ月 · 日本でオーダーメイド\',
    code_label:\'コード：\',cta_wa:\'WhatsAppで注文する\',cta_back:\'← コレクションへ戻る\',
    var_ey:\'4つの素材 · 1つのデザイン\',var_title:\'<em>素材</em>をお選びください\',
    popular:\'人気\',view_detail:\'詳細を見る →\',
    pt_ey:\'シリーズ{LETTER} — 価格\',pt_title:\'全価格<em>DDP</em>\',
    th_code:\'コード\',th_mat:\'素材\',th_price:\'価格（AED）· UAE全税込みDDP\',th_del:\'制作\',
    prod_time:\'約5.5ヶ月\',price_foot:\'全価格DDP——UAE輸入関税・5%VAT はRionが前払い。\',
    spec_ey:\'仕様\',spec_title:\'永遠に続く<em>クラフト</em>\',
    sg1:\'製品\',sg2:\'制作・配送\',
    sl_type:\'タイプ\',sv_type:\'{SV_TYPE_JA}\',sl_mat:\'素材\',sv_mat:\'K18イエロー/ホワイト/ピンクゴールド · プラチナPt900\',
    sl_seal:\'毛髪チャンバー\',sv_seal:\'日本で手作りされた気密封印チャンバー\',
    sl_eng:\'彫刻\',sv_eng:\'任意、最大15文字 · + AED 250\',
    sl_prod:\'制作\',sv_prod:\'毛髪受け取りから約5.5ヶ月\',
    sl_origin:\'産地\',sv_origin:\'日本で100%手作り\',
    sl_ship:\'配送\',sv_ship:\'DHL Express · 保険付き · UAEへDDP\',
    sl_polish:\'アフターケア\',sv_polish:\'日本での生涯無料ポリッシュサービス\',
    craft_h:\'すべて手作業——<br><em>日本で。</em>\',craft_p:\'{CRAFT_P_JA_JS}\',
    cp1_t:\'手作業封印\',cp1_b:\'すべての毛髪をアーティザンが手で封入し、写真で記録します。\',
    cp2_t:\'気密チャンバー\',cp2_b:\'完全密封——毛髪は水分・空気・時間から守られます。\',
    cp3_t:\'写真レポート\',cp3_b:\'封印工程を撮影しWhatsApp経由でお送りします。\',
    cp4_t:\'生涯ポリッシュ\',cp4_b:\'日本での無料ポリッシュサービス付き。\',
    enq_h:\'ご準備はよろしいですか？<br>私たちが<em>お手伝いします。</em>\',
    enq_p:\'WhatsAppでメッセージをお送りください。ご注文の義務はありません。\',
    enq_wa:\'WhatsAppでお問い合わせ\',enq_order:\'ご注文の流れ →\',
    rel_ey:\'こちらもおすすめ\',rel_title:\'コレクションの<em>他のシリーズ</em>\',view_series:\'シリーズを見る →\'
  }}
}};
function setLang(lang){{
  document.querySelectorAll(\'.lang-btn\').forEach(b=>b.classList.remove(\'active\'));
  document.querySelector(\`.lang-btn[onclick="setLang(\'${{lang}}\')"]\`).classList.add(\'active\');
  document.body.className=\'lang-\'+lang;document.documentElement.lang=lang;
  document.documentElement.dir=lang===\'ar\'?\'rtl\':\'ltr\';
  const t=T[lang];if(!t)return;
  document.querySelectorAll(\'[data-i18n]\').forEach(el=>{{
    const k=el.getAttribute(\'data-i18n\');if(t[k]!==undefined)el.innerHTML=t[k];
  }});
}}
</script>
</body>
</html>'''

def js_escape(s):
    return s.replace("'", "\\'").replace('\n', ' ')

def build_thumbs(variants, default_idx):
    lines = []
    for i, v in enumerate(variants):
        active = ' active' if i == default_idx else ''
        img_path = v["img"]
        lines.append(f'      <img class="hero-thumb{active}" src="images/{img_path}" data-img="images/{img_path}" alt="{v["code"]}" onclick="switchImg(this,\'images/{img_path}\')">')
    return '\n'.join(lines)

def build_mat_tabs_html(variants, default_idx):
    lines = []
    for i, v in enumerate(variants):
        active = ' active' if i == default_idx else ''
        lines.append(f'      <button class="mat-tab{active}" onclick="selectMat(\'{v["key"]}\')" data-i18n="mat_{v["key"]}">{v["mat_en"]}</button>')
    return '\n'.join(lines)

def build_i18n_mats_js(variants, lang):
    pairs = []
    for v in variants:
        key = f'mat_{v["key"]}'
        val = v[f'mat_{lang}']
        pairs.append(f"    {key}:'{val}'")
    return ',\n'.join(pairs)

def build_materials_js(variants):
    lines = []
    for v in variants:
        vimg = v['img']
        vmat = v['mat_en']
        vpop = str(v['popular']).lower()
        lines.append(f"  {v['key']}:{{code:'{v['code']}',price:'{v['price']}',img:'images/{vimg}',label:'{vmat}',popular:{vpop}}}")
    return ',\n'.join(lines)

def strip_html(s):
    return re.sub('<[^>]+>', '', s)

def make_special_note(note):
    if not note:
        return ''
    return f'  <p class="special-note">{note}</p>\n'

OUT = '/Users/aoyamayuma/rion-rings-website'
for slug, s in SERIES.items():
    dv = s['default_variant']
    defv = s['variants'][dv]
    var_ey_en = f"{len(s['variants'])} Materials · One Design"

    html = TEMPLATE.format(
        SLUG=s['slug'],
        LETTER=s['letter'],
        NAME_EN=s['name_en'],
        NAME_EN_PLAIN=strip_html(s['name_en']),
        TYPE_TAG_EN=s['type_en'],
        BADGE_EN=s['badge_en'],
        BADGE_AR=s['badge_ar'],
        BADGE_JA=s['badge_ja'],
        NAME_AR=s['name_ar'],
        NAME_JA=s['name_ja'],
        TYPE_AR=s['type_ar'],
        TYPE_JA=s['type_ja'],
        DESC_EN=s['desc_en'],
        DESC_EN_JS=js_escape(s['desc_en']),
        DESC_AR_JS=js_escape(s['desc_ar']),
        DESC_JA_JS=js_escape(s['desc_ja']),
        DEFAULT_IMG=defv['img'],
        DEFAULT_PRICE=defv['price'],
        DEFAULT_CODE=defv['code'],
        DEFAULT_MAT_KEY=defv['key'],
        PRICE_FROM=s['variants'][-1]['price'] if s['variants'][-1]['key']=='pt' else s['variants'][0]['price'],
        THUMB_IMGS=build_thumbs(s['variants'], dv),
        MAT_TABS=build_mat_tabs_html(s['variants'], dv),
        VARIANT_CARDS=build_variant_cards(s['variants']),
        PRICE_ROWS=build_price_table_rows(s['variants']),
        RELATED_CARDS=build_related(s['related']),
        MATERIALS_JS=build_materials_js(s['variants']),
        I18N_MATS_EN=build_i18n_mats_js(s['variants'], 'en'),
        I18N_MATS_AR=build_i18n_mats_js(s['variants'], 'ar'),
        I18N_MATS_JA=build_i18n_mats_js(s['variants'], 'ja'),
        SV_TYPE_EN=s['sv_type_en'],
        SV_TYPE_AR=s['sv_type_ar'],
        SV_TYPE_JA=s['sv_type_ja'],
        CRAFT_P_EN=s['craft_p_en'],
        CRAFT_P_EN_JS=js_escape(s['craft_p_en']),
        CRAFT_P_AR_JS=js_escape(s['craft_p_ar']),
        CRAFT_P_JA_JS=js_escape(s['craft_p_ja']),
        VAR_EY_EN=var_ey_en,
        SPECIAL_NOTE_HTML=make_special_note(s['special_note']),
    )
    path = f"{OUT}/series-{slug}.html"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: series-{slug}.html")

print("Done!")
