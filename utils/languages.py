"""
This file contains all translates the names of the languages.
The list will be updated in the features.
"""

languages = [
    "English",
    "Русский",
]

all_lang = [
    "Русский",
    "English",
    "中文",       # Китайский (Мандарин)
    "Español",    # Испанский
    "Français",   # Французский
    "Português",  # Португальский
    "Deutsch",    # Немецкий
    "日本語",      # Японский
    "한국어",      # Корейский
    "हिन्दी",     # Хинди
    "العربية",    # Арабский
    "বাংলা",     # Бенгальский
    "Italiano",   # Итальянский
    "Türkçe",     # Турецкий
    "Nederlands", # Голландский / Нидерландский
    "Polski",     # Польский
    "Українська", # Украинский
    "فارسی",      # Персидский
    "ไทย",        # Тайский
    "Việt",       # Вьетнамский
    "Bahasa Indonesia", # Индонезийский
    "עברית",      # Иврит
    "Română",     # Румынский
    "Ελληνικά",   # Греческий
    "Magyar",     # Венгерский
    "Čeština",    # Чешский
    "Svenska",    # Шведский
    "Norsk",      # Норвежский
    "Suomi",      # Финский
    "Dansk"       # Датский
]

countries_native = [
    "افغانستان (Afghanistan)",  # Афганистан - персидский/паштунский
    "Shqipëria",                # Албания - албанский
    "الجزائر (Al-Jazāʼir)",     # Алжир - арабский
    "Andorra",                  # Андорра - каталанский
    "Angola",                   # Ангола - португальский
    "Antigua and Barbuda",     # Антигуа и Барбуда - английский
    "Argentina",               # Аргентина - испанский
    "Հայաստան (Hayastan)",     # Армения - армянский
    "Australia",               # Австралия - английский
    "Österreich",              # Австрия - немецкий
    "Azərbaycan",              # Азербайджан - азербайджанский
    "Bahamas",                 # Багамы - английский
    "البحرين (Al-Baḥrayn)",    # Бахрейн - арабский
    "বাংলাদেশ (Bangladesh)", # Бангладеш - бенгальский
    "Barbados",                # Барбадос - английский
    "Беларусь",                # Беларусь - белорусский/русский
    "België / Belgique / Belgien", # Бельгия - фламандский/французский/немецкий
    "Belize",                  # Белиз - английский
    "Bénin",                   # Бенин - французский
    "འབྲུག (Druk Yul)",       # Бутан - дзонг-кэ
    "Bolivia",                 # Боливия - испанский/кечуа/аймара
    "Bosna i Hercegovina",     # Босния и Герцеговина - боснийский/хорватский/сербский
    "Botswana",                # Ботсвана - сетсвана/английский
    "Brasil",                  # Бразилия - португальский
    "بروناي (Brunei)",         # Бруней - малайский
    "България",                # Болгария - болгарский
    "Burkina Faso",            # Буркина-Фасо - французский
    "Burundi",                 # Бурунди - кирунди/французский/английский
    "Cabo Verde",              # Кабо-Верде - португальский
    "កម្ពុជា (Kampuchea)",    # Камбоджа - кхмерский
    "Cameroun",                # Камерун - французский/английский
    "Canada",                  # Канада - английский/французский
    "République Centrafricaine", # Центральноафриканская Республика - французский/санго
    "Tchad / تشاد (Tshadd)",   # Чад - французский/арабский
    "Chile",                   # Чили - испанский
    "中国 (Zhōngguó)",         # Китай - китайский
    "Colombia",                # Колумбия - испанский
    "Komori",                  # Коморы - коморский/арабский/французский
    "Congo-Brazzaville",       # Конго - французский
    "Costa Rica",              # Коста-Рика - испанский
    "Hrvatska",                # Хорватия - хорватский
    "Cuba",                    # Куба - испанский
    "Κύπρος / Kıbrıs",         # Кипр - греческий/турецкий
    "Česko",                   # Чехия - чешский
    "République démocratique du Congo", # Демократическая Республика Конго - французский
    "Danmark",                 # Дания - датский
    "Djibouti / جيبوتي",       # Джибути - французский/арабский
    "Dominica",                # Доминика - английский
    "República Dominicana",    # Доминиканская Республика - испанский
    "Timor-Leste",             # Восточный Тимор - тетум/португальский
    "Ecuador",                 # Эквадор - испанский/кечуа/шуар
    "مصر (Miṣr)",              # Египет - арабский
    "El Salvador",             # Сальвадор - испанский
    "Guinea Ekuatorial",       # Экваториальная Гвинея - испанский/французский/португальский
    "ኤርትራ (Ertra)",          # Эритрея - тигринья/арабский
    "Eesti",                   # Эстония - эстонский
    "Eswatini",                # Эсватини - суази/английский
    "ኢትዮጵያ (Ītyōṗṗyā)",      # Эфиопия - амхарский
    "Fiji",                    # Фиджи - английский/фиджийский/хинди
    "Suomi / Finland",         # Финляндия - финский/шведский
    "France",                  # Франция - французский
    "Gabon",                   # Габон - французский
    "The Gambia",              # Гамбия - английский
    "საქართველო (Sakartvelo)", # Грузия - грузинский
    "Deutschland",             # Германия - немецкий
    "Ghana",                   # Гана - английский
    "Ελλάδα",                  # Греция - греческий
    "Grenada",                 # Гренада - английский
    "Guatemala",               # Гватемала - испанский
    "Guinée",                  # Гвинея - французский
    "Guiné-Bissau",            # Гвинея-Бисау - португальский
    "Guyana",                  # Гайана - английский
    "Haïti",                   # Гаити - французский/креольский
    "Honduras",                # Гондурас - испанский
    "Magyarország",            # Венгрия - венгерский
    "Ísland",                  # Исландия - исландский
    "भारत (Bhārata)",         # Индия - хинди/английский
    "Indonesia",               # Индонезия - индонезийский
    "ایران (Īrān)",            # Иран - персидский
    "العراق (Al-ʻIrāq)",       # Ирак - арабский/курдский
    "Éire / Ireland",          # Ирландия - ирландский/английский
    "ישראל (Yisra'el)",        # Израиль - иврит/арабский
    "Italia",                  # Италия - итальянский
    "Côte d'Ivoire",           # Кот-д’Ивуар - французский
    "Jamaica",                 # Ямайка - английский
    "日本 (Nihon / Nippon)",    # Япония - японский
    "الأردن (Al-Urdunn)",      # Иордания - арабский
    "Қазақстан",               # Казахстан - казахский/русский
    "Kenya",                   # Кения - суахили/английский
    "Kiribati",                # Кирибати - кирибати/английский
    "Косово",                  # Косово - албанский/сербский
    "الكويت (Al-Kuwayt)",      # Кувейт - арабский
    "Кыргызстан",              # Киргизия - киргизский/русский
    "ລາວ (Lao)",              # Лаос - лаосский
    "Latvija",                 # Латвия - латышский
    "لبنان (Libnān)",          # Ливан - арабский
    "Lesotho",                 # Лесото - сетсуру/английский
    "Liberia",                 # Либерия - английский
    "ليبيا (Libyā)",           # Ливия - арабский
    "Liechtenstein",           # Лихтенштейн - немецкий
    "Lietuva",                 # Литва - литовский
    "Luxembourg",              # Люксембург - люксембургский/немецкий/французский
    "Madagascar",              # Мадагаскар - малагасийский/французский
    "Malawi",                  # Малави - чичева/английский
    "Malaysia",                # Малайзия - малайский
    "Maldives",                # Мальдивы - дивехи
    "Mali",                    # Мали - французский
    "Malta",                   # Мальта - мальтийский/английский
    " Marshall Islands",       # Маршалловы Острова - маршалльский/английский
    "Mauritanie / موريتانيا", # Мавритания - арабский/французский
    "Maurice",                 # Маврикий - французский/английский
    "México",                  # Мексика - испанский
    "Micronesia",              # Федеративные Штаты Микронезии - английский
    "Moldova",                 # Молдова - румынский
    "Liechtenstein",           # Монако - французский
    "Монгол улс",              # Монголия - монгольский
    "Crna Gora",               # Черногория - черногорский
    "Maroc",                   # Марокко - арабский/амазигский
    "Moçambique",              # Мозамбик - португальский
    "Myanmar",                 # Мьянма - бирманский
    "Namibia",                 # Намибия - английский
    "Nauru",                   # Науру - науру/английский
    "नेपाल (Nepāl)",          # Непал - непальский
    "Nederland",               # Нидерланды - голландский
    "New Zealand / Aotearoa",  # Новая Зеландия - маори/английский
    "Nicaragua",               # Никарагуа - испанский
    "Niger",                   # Нигер - французский
    "Nigeria",                 # Нигерия - английский
    "북한 (Pukhan)",           # Северная Корея - корейский
    "Северна Македонија",      # Северная Македония - македонский
    "Norway / Norge",          # Норвегия - норвежский
    "عُمان (ʻUmān)",           # Оман - арабский
    "پاکستان (Pākistān)",      # Пакистан - урду
    "Palau",                   # Палау - английский/палаванский
    "فلسطين (Filasṭīn)",       # Палестина - арабский
    "Panamá",                  # Панама - испанский
    "Papua New Guinea",        # Папуа — Новая Гвинея - английский/ток-писин/хيري-моту
    "Paraguay",                # Парагвай - испанский/гуарани
    "Perú",                    # Перу - испанский/кечуа/аймара
    "Pilipinas",               # Филиппины - тагальский
    "Polska",                  # Польша - польский
    "Portugal",                # Португалия - португальский
    "Qatar",                   # Катар - арабский
    "România",                 # Румыния - румынский
    "Россия",                  # Россия - русский
    "Rwanda",                  # Руанда - киньяруанда/английский/французский
    "Saint Kitts and Nevis",   # Сент-Китс и Невис - английский
    "Saint Lucia",             # Сент-Люсия - английский
    "Saint Vincent and the Grenadines", # Сент-Винсент и Гренадины - английский
    "Samoa",                   # Самоа - самоанский/английский
    "San Marino",              # Сан-Марино - итальянский
    "São Tomé e Príncipe",     # Сан-Томе и Принсипи - португальский
    "المملكة العربية السعودية", # Саудовская Аравия - арабский
    "Sénégal",                 # Сенегал - французский
    "Srbija",                  # Сербия - сербский
    "Seychelles",              # Сейшелы - французский/креольский
    "Sierra Leone",            # Сьерра-Леоне - английский
    "Singapura",               # Сингапур - английский/малайский/китайский/тамильский
    "Slovensko",               # Словакия - словацкий
    "Slovenija",               # Словения - словенский
    "Solomon Islands",         # Соломоновы Острова - английский
    "Soomaaliya",              # Сомали - сомалийский/арабский
    "South Africa",            # ЮАР - зулу/коса/африкаанс/английский и другие
    "대한민국 (Daehan Minguk)",# Южная Корея - корейский
    "South Sudan",             # Южный Судан - английский
    "España",                  # Испания - испанский
    "Sri Lanka",               # Шри-Ланка - сингальский/тамильский
    "السودان (As-Sūdān)",      # Судан - арабский/английский
    "Suriname",                # Суринам - нидерландский
    "Sverige",                 # Швеция - шведский
    "Schweiz / Suisse / Svizzera", # Швейцария - немецкий/французский/итальянский
    "سوريا (Sūryā)",           # Сирия - арабский
    "Тоҷикистон",              # Таджикистан - таджикский
    "Tanzania",                # Танзания - суахили/английский
    "ไทย (Prathet Thai)",      # Таиланд - тайский
    "Togo",                    # Того - французский
    "Tonga",                   # Тонга - тонганский/английский
    "Trinidad and Tobago",     # Тринидад и Тобаго - английский
    "تونس (Tūnis)",            # Тунис - арабский
    "Türkiye",                 # Турция - турецкий
    "Türkmenistan",            # Туркменистан - туркменский
    "Tuvalu",                  # Тувалу - тувалуанский/английский
    "Uganda",                  # Уганда - английский
    "Україна",                 # Украина - украинский
    "الإمارات العربية المتحدة", # Объединённые Арабские Эмираты - арабский
    "United Kingdom",          # Соединённое Королевство - английский
    "United States of America",# США - английский
    "Uruguay",                 # Уругвай - испанский
    "Oʻzbekiston",             # Узбекистан - узбекский
    "Vanuatu",                 # Вануату - бислама/французский/английский
    "Vaticano",                # Ватикан - итальянский
    "Venezuela",               # Венесуэла - испанский
    "Việt Nam",                # Вьетнам - вьетнамский
    "اليمن (Al-Yaman)",        # Йемен - арабский
    "Zambia",                  # Замбия - английский
    "Zimbabwe"                 # Зимбабве - английский/шиньяса/нде́бе́ле
]