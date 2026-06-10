#!/usr/bin/env python3
"""Add French (FR) language to Switzerland CH site as default language."""
import re, glob

# ─── Navigation FR (shared across all pages) ──────────────────────────────────
NAV_FR = """nav_cta:"Commencer votre commande",menu_eyebrow:"Navigation",nav_home:"Accueil",nav_col:"Collection",nav_about:"À propos de <em>Rion</em>",nav_order:"Comment <em>commander</em>",nav_faq:"FAQ",nav_ship:"Livraison &amp; <em>Retours</em>",nav_care:"Guide d'<em>entretien</em>",nav_contact:"Contact",menu_cta:"💬 &nbsp;Contactez-nous sur WhatsApp","""

# ─── Trust strip FR ───────────────────────────────────────────────────────────
TRUST_FR = """tr1:"Livraison gratuite en Suisse",tr2:"Pas de droits de douane · TVA suisse possible",tr3:"Fabriqué à la main au Japon",tr4:"Paiement sécurisé",tr5:"Certificat d'authenticité inclus",trust_shipping:"Livraison gratuite en Suisse",trust_duties:"Pas de droits de douane · TVA suisse possible",trust_made:"Fabriqué à la main au Japon",trust_payment:"Paiement sécurisé",trust_strip:"Livraison gratuite en Suisse &nbsp;·&nbsp; Pas de droits de douane · TVA suisse possible &nbsp;·&nbsp; Fabriqué à la main au Japon &nbsp;·&nbsp; Paiement sécurisé","""

# ─── Footer FR ────────────────────────────────────────────────────────────────
FOOTER_FR = """footer_p:"Bijoux mémoriaux sur mesure, fabriqués entièrement à la main au Japon. Un cheveu. Un bijou. Un amour — le vôtre, pour toujours. La confiance de familles à travers toute la Suisse.",footer_est:"Fondé en 2018 · Japon · Suisse",footer_explore:"Explorer",footer_about:"À propos de Rion",footer_order:"Comment commander",footer_stories:"Témoignages",footer_help:"Assistance",footer_ship:"Livraison &amp; Retours",footer_legal:"Mentions légales",footer_connect:"Nous contacter",footer_email:"Envoyer un message",footer_copy:"© 2026 Rion™ · My Art Inc. · 100% fabriqué au Japon · Livraison assurée gratuite en Suisse · Pas de droits de douane",footer_right:"Fondé en 2018 · Japon · Suisse","""

# ─── Material names FR ────────────────────────────────────────────────────────
MAT_FR = """mat_ygold:"Or jaune K18",mat_wgold:"Or blanc K18",mat_pgold:"Or rose K18",mat_pt:"Platine Pt900",enquire_wa:"Demande via WhatsApp →","""

# ─── Cookies FR ──────────────────────────────────────────────────────────────
COOKIES_FR = """cookie_msg:"Ce site utilise des cookies pour améliorer votre expérience.",cookie_btn:"Accepter","""

# ─── Per-page FR translations ─────────────────────────────────────────────────
PAGE_FR = {}

PAGE_FR['index'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Bijoux mémoriaux sur mesure · Fabriqués à la main au Japon",hero_title:"Gardez-les proches.<br><em>Pour toujours.</em>",hero_body:"Une simple mèche de cheveux — seulement 1cm — scellée à jamais dans de l'or ou du platine japonais. Chaque pièce est unique au monde, entièrement faite à la main au Japon, rien que pour vous. Quand les mots ne suffisent plus, l'or perdure.",hero_badge:"✦ &nbsp;Le bijou unique au monde",hero_cta1:"Commencer votre commande",hero_cta2:"💬 &nbsp;WhatsApp",hero_proof:"La confiance de familles à travers toute la Suisse",
sc1:"Cheveux précieux scellés · Une pièce unique, faite uniquement pour vous",sc2:"Seulement 1cm de cheveux suffit",sc3:"Livraison assurée gratuite en Suisse",sc4:"Certificat d'authenticité et rapport photo inclus",
tb1_h:"Unique au monde",tb1_p:"Chaque pièce renferme vos précieux cheveux — un bijou unique créé rien que pour vous.",tb2_h:"100% fabriqué au Japon",tb2_p:"Or, platine, diamants — sourcés et façonnés entièrement au Japon par des maîtres artisans.",tb3_h:"Documentation photo",tb3_p:"Nous photographions chaque étape et vous envoyons les photos avant la livraison.",tb4_h:"Votre approbation d'abord",tb4_p:"Design et matériaux sont confirmés par écrit avant le début du travail. Rien n'avance sans votre accord.",
story_label:"Notre histoire",story_title:"Né du <em>deuil.</em><br>Fait d'amour.",story_p1:"En 2011, notre fondateur a tenu son fils nouveau-né pendant trois jours — puis a dit au revoir. Dans ce deuil, une question est née : comment porter les êtres aimés quand ils ne peuvent plus marcher à nos côtés ?",story_p2:"Il a découvert les bijoux mémoriaux — une bague qui pouvait garder un fragment de son fils près de son cœur pour toujours. En 2018, il a fondé Rion — du nom de cet enfant. Chaque pièce commence par une histoire. La vôtre.",story_quote:"\"L'amour éternel. Un lien qui dure — pour toujours.\"",story_p3:"Une mèche de cheveux d'un être cher devient un bijou que vous portez chaque jour. Seulement 1cm. Une mèche. C'est tout ce qu'il nous faut.",
proc_title:"De leurs <em>cheveux</em><br>à votre cœur.",proc_sub:"Six étapes — du choix de votre design à la livraison gratuite à votre porte, n'importe où en Suisse.",ps1_t:"Parcourir la collection",ps1_b:"Choisissez votre série et métal — Or jaune K18, Or blanc, Or rose ou Platine Pt900.",ps2_t:"Contactez-nous",ps2_b:"Envoyez-nous un message via WhatsApp ou <a href='mailto:info@art-rings.com' style='color:var(--gold)'>email</a>. Sans engagement. Nous répondons sous 24h.",ps3_t:"Confirmer &amp; Payer",ps3_b:"Nous confirmons votre design, gravure, taille et le prix final tout inclus en CHF. Paiement intégral avant production.",ps4_t:"Recevoir votre kit",ps4_b:"Un kit stérile et un calibre de taille sont envoyés à votre adresse suisse. Placez quelques mèches et renvoyez-le au Japon.",ps5_t:"Fabriqué au Japon",ps5_b:"Nos maîtres artisans façonnent votre bijou. Environ 5,5 mois, avec des mises à jour photo.",ps6_t:"Livré à votre porte",ps6_b:"DHL Express, entièrement assuré, gratuit en Suisse. Pas de droits de douane.",proc_cta:"Guide de commande complet — étape par étape →",
col_title:"La<br><em>Collection</em>",col_sub:"Chaque pièce renferme vos précieux cheveux — une création unique rien que pour vous. Tous les prix en CHF, livraison gratuite incluse. Pas de droits de douane.",badge1:"Le plus choisi",badge3:"Premium",p1_name:"La bague classique",p1_sub:"Bague mémoriale · Série A",p1_body:"Un anneau intemporel avec chambre intérieure scellée. Percé dans l'or K18 ou platine, vos cheveux scellés hermétiquement. Le design le plus choisi.",p_ddp:"Livraison gratuite · Pas de droits",p1_cta:"Explorer la Série A →",p2_name:"Le pendentif barre",p2_sub:"Collier mémoriel · Série B",p2_body:"Une fine barre en or massif suspendue à une chaîne élégante. La mèche est scellée dans la barre, près de votre cœur.",p2_cta:"Explorer la Série B →",p3_name:"Commission sur mesure",p3_sub:"Entièrement personnalisé · Votre vision",p3_body:"Un design sur mesure créé avec nos artisans. Diamants, rubis, saphirs — toute combinaison. Le bijou ultime unique.",p3_cta:"Commencer votre voyage sur mesure →",unique_stmt:"<strong>Un bijou unique avec vos précieux cheveux — fait uniquement pour vous.</strong> Votre amour, scellé dans l'or, à porter pour toujours.",
gallery_label:"Notre travail",ps1_title:"Or K18, Platine<br>&amp; <em>Pierres précieuses</em>",ps1_body:"Chaque matériau est sourcé et façonné entièrement au Japon. Or jaune K18, or blanc, or rose et platine disponibles. Diamants, rubis et saphirs sur n'importe quel design.",ps2_title:"Fait avec soin,<br><em>livré avec amour.</em>",ps2_body:"Chaque pièce arrive dans un coffret en bois de paulownia exclusif Rion. À l'intérieur : votre bijou unique, votre Certificat d'authenticité et les cheveux restants. Livré via DHL Express, assuré, à votre porte en Suisse. Aucun frais surprise.",
test_title:"Portez vos proches<br><em>près de votre cœur</em>",test_sub:"Des témoignages réels de toute la Suisse",t1_text:"\"J'ai perdu ma mère d'un cancer l'année dernière. J'ai porté cette bague à la remise des diplômes de ma fille — sa présence était constante. Je ne peux pas exprimer ce que cette pièce signifie. La maîtrise japonaise est bouleversante.\"",t1_tag:"Sa mère · Bague classique",t2_text:"\"Mon mari est décédé subitement à 41 ans. Depuis le premier WhatsApp jusqu'à la réception, chaque interaction était exceptionnellement attentionnée. Je serre cette bague quand il me manque le plus.\"",t2_tag:"Son mari · Anneau milgrain",t3_text:"\"J'avais Charlie, mon golden retriever, pendant 14 ans. L'équipe Rion m'a traité avec le même respect qu'un être humain. Je le porte tous les jours.\"",t3_tag:"Son chien · Anneau fleuri",
cta_title:"Commencez votre <em>parcours</em> aujourd'hui",cta_body:"Chaque bijou Rion commence par une simple conversation. Sans engagement — contactez-nous et nous vous guiderons à chaque étape. Livraison gratuite en Suisse, pas de droits de douane, tarification tout inclus en CHF.",cta_btn1:"Parcourir la collection",cta_btn2:"💬 &nbsp;Contactez-nous via WhatsApp",
faq_title:"Vos questions, <em>répondues</em>",fq1:"De combien de cheveux avez-vous besoin ?",fa1:"Seulement 1cm de long, une mèche. Encore moins, c'est parfait. Pour les poils d'animaux, pareil. Vous en avez presque certainement suffisamment.",fq2:"Comment connaître ma taille de bague ?",fa2:"Un calibre de taille (tailles 1–12, demi-tailles incluses) est inclus dans votre kit. Essayez chaque bague et dites-nous laquelle convient. Si vous connaissez déjà votre taille, faites-le nous savoir.",fq3:"Comment fonctionne la livraison en Suisse ?",fa3:"Nous livrons en Suisse — totalement gratuitement, entièrement assuré, sans droits de douane. Nous envoyons un kit stérile à votre adresse suisse. Glissez les cheveux, scellez et déposez — nous gérons les douanes. Aucun frais surprise.",fq4:"Puis-je voir les cheveux être scellés ?",fa4:"Oui. Nous photographions avant, pendant et après le scellement, et vous envoyons les photos via WhatsApp ou <a href='mailto:info@art-rings.com'>email</a> avant l'expédition.",fq5:"Combien de temps cela prend-il ?",fa5:"Environ 5,5 mois au total — depuis la réception de vos cheveux au Japon jusqu'à l'arrivée en Suisse. Nous envoyons des mises à jour régulières. Les bonnes choses prennent du temps.",fq6:"Y a-t-il des droits de douane ou des frais supplémentaires ?",fa6:"Aucun. Nous livrons en Suisse en DDP — tous les droits de douane sont couverts par Rion et inclus dans le prix. Le prix indiqué est le prix payé.",fq7:"Puis-je mettre les cheveux de plusieurs proches dans une pièce ?",fa7:"Oui, sur certains designs. Demandez-nous lesquels lors de votre prise de contact.",fq8:"Puis-je commander pour un animal ?",fa8:"Absolument. De nombreux clients commandent pour leurs animaux adorés. Le kit et le processus sont identiques. 1cm suffit.",fq9:"Quelle est votre politique de retour ?",fa9:"Chaque pièce est entièrement faite sur commande personnelle — nous n'acceptons pas d'annulations, retours ou remboursements une fois la production commencée. En cas de défaut de fabrication, nous refaisons la pièce sans frais.",fq10:"Que devient le reste des cheveux ?",fa10:"Tout cheveu restant vous est retourné dans un contenant dédié, avec votre bijou. Rien de précieux n'est jamais jeté.",fq11:"Comment entretenir mon bijou Rion ?",fa11:"Votre pièce est en or K18 massif ou platine Pt900 — extrêmement durable. Essuyez avec un chiffon doux. Évitez le chlore et les parfums. Polissage à vie gratuit au Japon sur demande.",
vip_eyebrow:"Service VIP",vip_title:"Nous venons<br>en <em style='font-style:italic;color:var(--gold)'>Suisse.</em>",vip_body1:"Pour les clients souhaitant une expérience véritablement personnelle, notre fondateur voyage du Japon en Suisse pour vous rencontrer en personne.",vip_body2:"Ce n'est pas qu'une livraison. C'est la rencontre de deux personnes qui comprennent ce que renferme ce bijou.",vip_quote:"\"Ce bijou a été fait avec amour — il doit être remis de main en main.\"",vip_f1t:"Présentation directe",vip_f1b:"Notre fondateur vous remet lui-même votre bijou.",vip_f2t:"À l'endroit de votre choix",vip_f2b:"Votre domicile, une suite d'hôtel ou un lieu de votre préférence en Suisse.",vip_f3t:"Nouvelles commandes acceptées",vip_f3b:"Vous pouvez passer commande directement lors de la visite.",vip_f4t:"Frais supplémentaires",vip_f4b:"Des frais de voyage s'appliquent. Contactez-nous via WhatsApp.",vip_cta:"&#128172; &nbsp;Renseignez-vous sur le service VIP",vip_tag:"Japon → Suisse · Remise personnelle · Sur demande · Frais de voyage supplémentaires",
con_title:"Votre<br><em>histoire commence ici.</em>",con_body:"Chaque bijou Rion commence par une simple conversation. Contactez-nous via WhatsApp ou email. Nous répondons en français, anglais et japonais.",con_sub:"Livraison assurée gratuite en Suisse · Pas de droits de douane · Tarification tout inclus en CHF · Design approuvé avant production · 100% fabriqué au Japon",mij_label:"100% fabriqué au Japon — notre engagement",mij_body:"De l'or au platine — tous les matériaux sont sourcés et façonnés au Japon. Fabriqué au Japon n'est pas un argument de vente. C'est notre façon de travailler.",wa_sub:"Réponse la plus rapide · Français, anglais et japonais · Sous 24h",email_label:"Email",ship_label:"Livraison DHL assurée gratuite",ship_sub:"Suisse · Pas de droits de douane",hours_label:"Heures",hours_val:"9h00–19h00 JST · WhatsApp disponible hors heures",
legal_title:"Mentions légales &amp; <em>conformité</em>",leg1_h:"Informations pour les clients suisses",leg1_p:"Tous les prix en CHF. Livraison DDP — droits de douane couverts par Rion. Aucun frais supplémentaire. Chaque pièce est sur mesure. Approbation écrite du design avant production. Défauts : refabrication gratuite.",leg2_h:"Produit &amp; Livraison",leg2_1:"Toutes les pièces fabriquées à la main au Japon",leg2_2:"Certificat d'authenticité avec chaque commande",leg2_3:"Rapport photo du scellement inclus",leg2_4:"Livré via DHL Express (entièrement assuré)",leg2_5:"Cheveux : non biologique, conforme aux douanes",leg2_6:"Aucun frais supplémentaire à la livraison",leg2_7:"Cheveux restants retournés avec votre bijou",leg3_h:"Informations sur l'entreprise",leg3_p:"Rion · My Art Inc. · Fondé en 2018, Japon · Tous les prix en CHF. Conformité aux lois suisses de protection des consommateurs. Contact via WhatsApp ou email.",
""" + FOOTER_FR + """
sticky_text:"<strong>Un cheveu. Un bijou. Un amour.</strong> &nbsp;Dès CHF4,600 · Livraison gratuite en Suisse · Pas de droits de douane · Fabriqué au Japon.",sticky_wa:"💬 WhatsApp",sticky_order:"Commencer →"
"""

PAGE_FR['collection'] = NAV_FR + TRUST_FR + """
page_note:"✦ Tous les prix en CHF · Livraison assurée gratuite · Pas de droits de douane",hero_eyebrow:"Bijoux mémoriaux sur mesure · Fabriqués à la main au Japon",page_title:"La<br><em>Collection</em>",page_sub:"Chaque pièce renferme vos précieux cheveux — une création unique rien que pour vous. Tous les prix en CHF, livraison gratuite incluse en Suisse. Pas de droits de douane.",
bespoke_title:"Au-delà<br>de la <em>collection</em>",bespoke_sub:"Commission entièrement sur mesure",bespoke_p:"Aucun de nos designs standards ne vous convient ? Nous créons des commissions entièrement sur mesure — conçues de zéro avec notre équipe. Aucun modèle, aucune limite : toute forme, tout matériau, toute combinaison de pierres. Les commissions sur mesure commencent à CHF18,000 et prennent environ 6 mois. Contactez-nous via WhatsApp.",bespoke_cta:"Commencer votre parcours sur mesure →",
""" + MAT_FR + FOOTER_FR

PAGE_FR['product'] = NAV_FR + TRUST_FR + """
spec_series:"Série",spec_mat:"Matériau",spec_size:"Taille de bague",spec_sizing:"Calibre",spec_time:"Délai de production",spec_ship:"Livraison",spec_price:"Prix",
price_note:"Livraison gratuite en Suisse · Pas de droits de douane · TVA suisse possible",
engrave_label:"Gravure personnalisée (optionnel)",engrave_desc:"Ajoutez un texte gravé à l'intérieur de la bague — jusqu'à 10 caractères inclus.",
birthstone_label:"Pierres de naissance (optionnel)",birthstone_desc:"Ajoutez 1 à 4 pierres à votre design.",
order_cta:"Commencer via WhatsApp →",order_sub:"Sans engagement · Nous répondons sous 24h",
related_title:"Vous pourriez aussi aimer",
""" + MAT_FR + FOOTER_FR

PAGE_FR['about'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Notre Histoire",hero_title:"Né du <em>deuil.</em><br>Fait d'amour.",
story_p1:"En 2011, notre fondateur a tenu son fils nouveau-né pendant trois jours — puis a dit au revoir. Ce deuil a soulevé une question : comment porter les êtres aimés quand ils ne peuvent plus marcher à nos côtés ?",story_p2:"Il a découvert les bijoux mémoriaux. Sept ans plus tard, en 2018, il a fondé Rion — du nom de cet enfant. Chaque pièce commence par une histoire. La vôtre.",story_quote:"\"L'amour éternel. Un lien qui dure — pour toujours.\"",
craft_title:"L'<em>artisanat</em>",craft_p:"Chaque bijou Rion est fabriqué entièrement à la main par des maîtres artisans au Japon. De l'or au platine, des diamants aux rubis — tous les matériaux sont sourcés au Japon.",mij_stmt:"100% fabriqué au Japon — notre engagement",
""" + FOOTER_FR

PAGE_FR['care'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Guide d'entretien",hero_title:"Prenez <em>soin</em><br>de votre bijou.",page_lead:"Votre bijou Rion est en or K18 ou platine Pt900 massif — extrêmement durable. Avec des soins appropriés, il durera toute une vie et au-delà.",
care1_title:"Nettoyage quotidien",care1_body:"Essuyez votre bijou avec un chiffon en microfibre doux après chaque port. Pour un nettoyage plus en profondeur, trempez-le brièvement dans de l'eau tiède savonneuse, frottez doucement et rincez.",care2_title:"À éviter",care2_body:"Évitez l'exposition au chlore (piscines, spas), les parfums et lotions en contact direct, et les chocs violents contre des surfaces dures.",care3_title:"Polissage à vie",care3_body:"Nous offrons un service de polissage à vie gratuit au Japon. Contactez-nous pour organiser le retour — nous couvrons les frais d'expédition.",
""" + FOOTER_FR

PAGE_FR['faq'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"FAQ",hero_title:"Vos questions,<br><em>répondues</em>",hero_lead:"Tout ce que vous devez savoir sur les bijoux mémoriaux Rion.",
tab_all:"Toutes les questions",tab_process:"Processus",tab_product:"Le bijou",tab_shipping:"Livraison",tab_payment:"Paiement",tab_usa:"Suisse spécifique",
fq1:"De combien de cheveux avez-vous besoin ?",fa1:"Seulement 1cm de long, une mèche. Encore moins fonctionne parfaitement. Pour les poils d'animaux, pareil. Vous en avez presque certainement suffisamment.",fq2:"Comment connaître ma taille de bague ?",fa2:"Un calibre de taille est inclus dans votre kit de collecte. Essayez chaque bague et dites-nous laquelle convient. Si vous connaissez déjà votre taille, faites-le nous savoir.",fq3:"Comment fonctionne la livraison en Suisse ?",fa3:"Livraison totalement gratuite, entièrement assurée, sans droits de douane. Nous envoyons un kit stérile à votre adresse suisse. Glissez les cheveux, scellez et déposez — nous gérons les douanes.",fq4:"Puis-je voir les cheveux être scellés ?",fa4:"Oui. Nous photographions avant, pendant et après le scellement, et vous envoyons les photos avant l'expédition.",fq5:"Combien de temps cela prend-il ?",fa5:"Environ 5,5 mois au total depuis la réception de vos cheveux au Japon jusqu'à la livraison en Suisse. Mises à jour régulières incluses.",fq6:"Y a-t-il des droits de douane ou des frais supplémentaires ?",fa6:"Aucun. Livraison DDP — tous les droits de douane couverts par Rion. Le prix indiqué est le prix payé.",fq7:"Puis-je mettre les cheveux de plusieurs proches dans une pièce ?",fa7:"Oui, sur certains designs. Demandez-nous lesquels lors de votre contact.",fq8:"Puis-je commander pour un animal ?",fa8:"Absolument. De nombreux clients commandent pour leurs animaux. 1cm suffit.",fq9:"Quelle est votre politique de retour ?",fa9:"Chaque pièce est faite sur commande personnelle — pas d'annulations ou remboursements une fois commencée. Défauts : refabrication gratuite.",fq10:"Que devient le reste des cheveux ?",fa10:"Les cheveux restants vous sont retournés dans un contenant dédié avec votre bijou.",fq11:"Comment entretenir mon bijou Rion ?",fa11:"Or K18 ou platine Pt900 — durable pour port quotidien. Chiffon doux, évitez chlore et parfums. Polissage à vie gratuit au Japon.",
""" + FOOTER_FR

PAGE_FR['heritage'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Notre Héritage",hero_title:"L'art de <em>l'orfèvrerie</em><br>japonaise.",page_lead:"Rion est enraciné dans des siècles d'artisanat japonais. Chaque bijou incarne une tradition transmise de maître à apprenti, façonnée à la main au cœur du Japon.",
craft_title:"Tradition &amp; <em>Innovation</em>",craft_body:"Nos artisans combinent des décennies de techniques orfèvrières traditionnelles avec un design contemporain. Chaque bijou Rion est une fusion d'héritage et d'amour moderne.",
""" + FOOTER_FR

PAGE_FR['legal'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Mentions légales",hero_title:"Mentions légales &amp;<br><em>confidentialité</em>",hero_lead:"Transparence et conformité dans chaque aspect de notre activité.",
s1_eyebrow:"Section 1",s1_title:"Informations sur l'<em>entreprise</em>",s2_eyebrow:"Section 2",s2_title:"Divulgation <em>commerciale</em>",s2_intro:"Divulgation requise selon la loi japonaise sur les transactions commerciales spécifiées. En tant que vendeur japonais livrant à l'international, cette divulgation s'applique à toutes les commandes. Les clients conservent les droits de protection des consommateurs applicables.",s3_eyebrow:"Section 3",s3_title:"Conditions <em>générales</em>",s4_eyebrow:"Section 4",s4_title:"Politique de <em>confidentialité</em>",
th_item:"Article",th_detail:"Détail",th_tax:"Taxe",
priv7_h:"7. Transfert international de données (Suisse → Japon)",
""" + FOOTER_FR

PAGE_FR['order'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Comment commander",hero_title:"Six étapes.<br><em>Un bijou à vie.</em>",hero_lead:"De la première conversation à la livraison à votre porte — chaque étape est conçue pour être simple, transparente et personnelle.",
s1_eyebrow:"Étape 1",s1_title:"Parcourez la <em>collection</em>",s1_body:"Explorez nos séries et choisissez le design qui vous parle. Chaque série est disponible en Or jaune K18, Or blanc, Or rose et Platine Pt900.",s1_note:"Temps estimé : 5–15 minutes",
s2_eyebrow:"Étape 2",s2_title:"<em>Contactez-nous</em>",s2_body:"Envoyez-nous un message via WhatsApp ou email avec la série qui vous intéresse. Sans engagement — juste une conversation. Nous répondons sous 24 heures.",s2_note:"Sous 24 heures",
s3_eyebrow:"Étape 3",s3_title:"Confirmer le design &amp; <em>payer</em>",s3_body:"Nous confirmons votre design, gravure, taille de bague et prix final tout inclus en CHF. Paiement par carte (Visa, Mastercard, Amex via Stripe) ou virement bancaire.",s3_note:"Paiement intégral avant production",
s4_eyebrow:"Étape 4",s4_title:"Recevoir votre <em>kit de cheveux</em>",s4_body:"Un kit de collecte stérile et un calibre de taille sont envoyés à votre adresse suisse via DHL Express — gratuitement. Placez quelques mèches et renvoyez-le au Japon avec l'étiquette prépayée.",s4_note:"Japon → Votre adresse suisse · DHL Express · Gratuit",
s5_eyebrow:"Étape 5",s5_title:"Fabriqué à la <em>main au Japon</em>",s5_body:"Nos maîtres artisans façonnent votre bijou au Japon. Environ 5,5 mois, avec des rapports photo de chaque étape envoyés via WhatsApp ou email.",s5_note:"Environ 5,5 mois · Mises à jour incluses",
s6_eyebrow:"Étape 6",s6_title:"Livré à <em>votre porte</em>",s6_body:"Une fois votre bijou prêt, nous l'expédions via DHL Express — entièrement assuré, gratuit, partout en Suisse. Pas de droits de douane.",s6_note:"DHL Express · Entièrement assuré · Pas de droits de douane",
sizing_title:"Taille de bague",sizing_body:"Un calibre de taille est inclus dans votre kit — confirmez votre taille avant la production. Demi-tailles disponibles (tailles 1–12).",
payment_title:"Paiement",payment_stripe:"Carte de crédit via Stripe — Visa, Mastercard, Amex, Diners, JCB",payment_bank:"Virement bancaire (CHF ou JPY acceptés)",
fee_title:"Récapitulatif des frais",fee1:"Kit de collecte de cheveux",fee2:"Retour des cheveux",fee3:"Fabrication artisanale",fee4:"Droits de douane et taxes",fee5:"Livraison du bijou final",fee_all:"Rion",
""" + FOOTER_FR

PAGE_FR['sealing'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Le processus de scellement",hero_title:"Comment vos <em>cheveux</em><br>sont scellés.",hero_lead:"Chaque mèche est scellée à la main dans l'or ou le platine par nos maîtres artisans au Japon. Voici exactement comment cela se passe.",
step1_title:"Réception &amp; <em>vérification</em>",step1_body:"À l'arrivée au Japon, vos cheveux sont réceptionnés et soigneusement vérifiés par notre équipe.",step2_title:"Préparation du <em>bijou</em>",step2_body:"La cavité de la bague ou du pendentif est préparée par nos artisans avec précision.",step3_title:"<em>Scellement</em> des cheveux",step3_body:"Vos cheveux sont placés dans la cavité et scellés avec le même métal — or ou platine. Entièrement hermétique.",step4_title:"Documentation <em>photo</em>",step4_body:"Nous photographions chaque étape et vous envoyons les photos via WhatsApp ou email avant l'expédition.",
""" + FOOTER_FR

PAGE_FR['shipping'] = NAV_FR + TRUST_FR + """
hero_eyebrow:"Livraison &amp; Retours",hero_title:"Gratuit, assuré,<br><em>de porte à porte.</em>",hero_lead:"Chaque bijou Rion est expédié du Japon via DHL Express en conditions DDP. Tous les droits de douane sont prépayés — vous ne payez rien à la livraison. Gratuit en Suisse.",
step1_title:"Kit de collecte <em>envoyé à votre adresse suisse</em>",step1_body:"Après confirmation de votre commande, nous expédions un kit Rion directement à votre adresse suisse via DHL Express — gratuitement. Le kit comprend : une enveloppe stérile scellée, un calibre de taille de bague, des instructions claires et une étiquette de retour DHL prépayée.",step1_meta:"Japon → Votre adresse suisse · DHL Express · Gratuit",step2_title:"Vous <em>renvoyez</em> les cheveux",step2_body:"Placez quelques mèches dans l'enveloppe scellée, puis déposez-la dans un point de collecte DHL ou programmez un enlèvement gratuit.",step2_meta:"Votre adresse suisse → Japon · DHL Express · Gratuit · Étiquette prépayée",step3_title:"<em>Fabriqué</em> au Japon",step3_body:"Environ 5,5 mois de fabrication artisanale avec mises à jour photo.",step3_meta:"Environ 5,5 mois · Mises à jour incluses",step4_title:"Votre bijou terminé <em>arrive chez vous</em>",step4_body:"Expédié via DHL Express, entièrement assuré. Tous les droits de douane suisses sont prépayés. Délai typique : 3–5 jours ouvrables depuis le Japon.",step4_meta:"Japon → Suisse · DHL Express · Entièrement assuré · 3–5 jours ouvrables",
coverage_title:"Où nous <em>livrons.</em>",coverage_lead:"Livraison DDP gratuite partout en Suisse — sans exception ni supplément.",cov1_title:"Suisse",cov1_body:"Toutes les régions · Allemand, français, italien, romanche",cov1_meta:"DDP · Pas de droits · DHL Express gratuit",cov2_title:"Principauté de Liechtenstein",cov2_body:"Livraison disponible · Pas de droits de douane",cov2_meta:"DDP · Pas de droits · DHL Express",cov3_title:"Couverture Suisse",cov3_body:"DHL Express · Entièrement assuré",cov3_meta:"DDP · Pas de droits · DHL Express gratuit",
returns_title:"Politique de <em>retour</em>",returns_p1:"Chaque pièce est entièrement faite sur commande personnelle — incorporant vos cheveux, votre design choisi et votre approbation écrite. Pour cette raison, nous n'acceptons pas les annulations, retours ou remboursements une fois la production commencée.",returns_p2:"En cas de défaut de fabrication, veuillez nous notifier dans les 3 jours suivant la réception — nous referons la pièce sans frais.",
trust_shipping:"Livraison gratuite en Suisse",trust_duties:"Pas de droits de douane · TVA suisse possible",trust_made:"Fabriqué à la main au Japon",trust_payment:"Paiement sécurisé",
fee1_item:"Kit de collecte (Japon → votre adresse suisse)",fee1_note:"DHL Express, livré à votre porte. Gratuit.",fee2_item:"Retour des cheveux (votre adresse → Japon)",fee2_note:"Étiquette DHL prépayée incluse.",fee3_item:"Fabrication artisanale",fee3_note:"Environ 5,5 mois.",fee4_item:"Droits de douane suisses &amp; frais de douane",fee4_note:"DDP — 100% couverts par Rion.",fee5_item:"Expédition du bijou final (Japon → Suisse)",fee5_note:"DHL Express · Entièrement assuré · Gratuit.",
""" + FOOTER_FR

# Series pages — common FR content
SERIES_FR_COMMON = NAV_FR + TRUST_FR + MAT_FR + FOOTER_FR + """
price_ddp:"Livraison gratuite en Suisse · Pas de droits de douane",
"""

PAGE_FR['series-a'] = SERIES_FR_COMMON + """
hero_title:"Série A — <em>La Bague Classique</em>",hero_sub:"La bague mémoriale la plus choisie au monde.",hero_eyebrow:"Bijoux mémoriaux · Série A",spec_title:"Spécifications",
"""
PAGE_FR['series-b'] = SERIES_FR_COMMON + """hero_title:"Série B — <em>Le Pendentif Barre</em>",hero_sub:"Un collier mémoriel élégant en or massif.",hero_eyebrow:"Bijoux mémoriaux · Série B",spec_title:"Spécifications","""
PAGE_FR['series-c'] = SERIES_FR_COMMON + """hero_title:"Série C — <em>Le Pendentif Pierre de Naissance</em>",hero_sub:"Votre bijou mémoriel avec vos pierres de naissance.",hero_eyebrow:"Bijoux mémoriaux · Série C",spec_title:"Spécifications","""
PAGE_FR['series-d'] = SERIES_FR_COMMON + """hero_title:"Série D — <em>La Bague Chevalière</em>",hero_sub:"Une déclaration élégante en or massif.",hero_eyebrow:"Bijoux mémoriaux · Série D",spec_title:"Spécifications","""
PAGE_FR['series-f'] = SERIES_FR_COMMON + """hero_title:"Série F — <em>L'Anneau Fleuri</em>",hero_sub:"Un anneau éternel orné de fleurs et de cheveux.",hero_eyebrow:"Bijoux mémoriaux · Série F",spec_title:"Spécifications","""
PAGE_FR['series-g'] = SERIES_FR_COMMON + """hero_title:"Série G — <em>Le Pendentif Goutte</em>",hero_sub:"Un pendentif en forme de goutte, intemporel.",hero_eyebrow:"Bijoux mémoriaux · Série G",spec_title:"Spécifications","""
PAGE_FR['series-h'] = SERIES_FR_COMMON + """hero_title:"Série H — <em>Le Pendentif Cœur</em>",hero_sub:"Un cœur en or, une histoire d'amour.",hero_eyebrow:"Bijoux mémoriaux · Série H",spec_title:"Spécifications","""
PAGE_FR['series-j'] = SERIES_FR_COMMON + """hero_title:"Série J — <em>La Bague Solitaire</em>",hero_sub:"Un design élégant avec pierre centrale.",hero_eyebrow:"Bijoux mémoriaux · Série J",spec_title:"Spécifications","""


def get_page_key(filename):
    """Map filename to page key."""
    name = filename.replace('.html', '')
    if name in PAGE_FR:
        return name
    # Check for series pages
    if name.startswith('series-'):
        return name
    return None


def add_fr_to_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = path.replace('.html', '')
    fr_content = PAGE_FR.get(filename, '')
    if not fr_content:
        # For pages without specific FR content, use nav + trust + footer
        fr_content = NAV_FR + TRUST_FR + MAT_FR + FOOTER_FR

    # 1. Add FR to T object (before en:{ or en: {)
    if 'fr:{' in content:
        pass  # already done
    else:
        fr_block = f"\n fr:{{\n {fr_content.strip()}\n }},\n"
        if ' en:{' in content:
            content = content.replace(' en:{', fr_block + ' en:{', 1)
        elif ' en: {' in content:
            content = content.replace(' en: {', fr_block + ' en: {', 1)

    # 2. Add FR language button (before EN button)
    content = content.replace(
        '<button class="lang-btn active" data-lang="en" onclick="setLang(\'en\')">EN</button>',
        '<button class="lang-btn active" data-lang="fr" onclick="setLang(\'fr\')">FR</button>\n  <button class="lang-btn" data-lang="en" onclick="setLang(\'en\')">EN</button>'
    )

    # 3. Set FR as default language (change 'en' fallback to 'fr')
    content = content.replace(
        "const saved=localStorage.getItem('rion_ch_lang')||'en'",
        "const saved=localStorage.getItem('rion_ch_lang')||'fr'"
    )

    # 4. Update setLang to handle 3 languages
    # The existing setLang should already work since it uses T[l] lookup

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    html_files = glob.glob('*.html')
    count = 0
    for path in html_files:
        if add_fr_to_file(path):
            print(f'  Updated: {path}')
            count += 1
    print(f'French added to {count} files.')


if __name__ == '__main__':
    main()
