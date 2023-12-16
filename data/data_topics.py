#!/usr/bin/python
# -*- coding: utf8 -*-

# Здесь хранятся топики с вопросами.

from data_library.question import Question
from data_library.topic import Topic
from data_library.sub_topic import SubTopic
from data_library.message import Message

topics_name = ["Культура СССР", "Правление Романовых", "Древняя Русь"]
sub_topics_name = [["Фильмы", "Плакаты", "Песни", "Архитектура"],
                   ["Персоналии", "События", "Портреты", "Разное"],
                   ["Князья", "Даты", "Термины", "Разное"]]

questions = [[['''Из какого фильма кадр? (10)
1) Самогонщики 
2) Кавказская пленница 
3) Бриллиантовая рука 
4) Операция «Ы» и другие приключения Шурика''',
               '''Как зовут актрису? (20) 
1) Людмила Гурченко 
2) Надежда Румянцева 
3) Лариса Гузеева 
4) Барбара Брыльск''',
               '''Из какого фильма кадр? (30)
1) Максим Перепелица
2) В бой идут одни «старики»
3) Судбьа человека
4) На войне как на войне''',
               '''Из какого фильма кадр? (40)
1) А зори здесь тихие
2) Летят журавли
3) Офицеры
4) Они сражались за родину'''],
              ['''Что написано на плакате? (10)
1) Бдительность - наше оружие!
2) Американскому доллару - нет!
3) Останови врага-империалиста!
4) Зарубежной интервенции - нет''',
               '''Что написано на плакате? (20)
1) Вставай, страна, огромная!
2) Родина - мать зовёт!
3) Все на борьбу с окупантом!
4) Вставай на зашиту Родины!''',
               '''Что написано на плакате? (30)
1) Красной армии - слава!
2) Русской армии - слава!
3) Нашей армии - слава!
4) Великой армии - слава!''',
               '''Что написано на плакате? (40)
1) Беспощадно убьем врага!
2) Беспощадно пронзим оружием врага!
3) Беспощадно разгромим и уничтожим врага!
4) Беспощадно сокрушим врага!'''],
              ['''Что это за песня? (10)
1) Катюша 
2) Огонек
3) Смуглянка
4) Синий платочек''',
               '''Что это за песня? (20)
1) В землянке
2) Журавли
3) Казаки
4) Давно мы дома не были''',
               '''Что это за песня? (30)
1) Три танкиста
2) На поле танки грохотали
3) Эх, дороги
4) Священная война''',
               '''Что это за песня? (40)
1) Пора в путь-дорогу
2) Мы друзья, перелетные птицы
3) Несокрушимая и легендарная
4) Прощайте, скалистые горы?'''],
              ['''Что изображено на Картинке? (10)
1) Санаторий «Курпаты»
2) Екатеринбургский цирк
3) Гостиница «Аманауз»
4) Гостиница «Тарелка»''',
               '''Что изображено на картинке? (20)
1) Гелиокомплекс «Солнце»
2) Здание Президиума Российской академии наук
3) Музей «Сулайман-Тоо»
4) Жилой дом «Ромашка»''',
               '''Что изображено на картинке? (30)
1) Главное здание МГУ
2) Гостиница «Ленинградская»
3) Гостиница «Украина»
4) Жилой дом на Кудринской площади''',
               '''Как называется проект, изображенный на картинке? (40)
1) Башня Ленина
2) Башня Татлина
3) Дворец Советов
4) Здание Министерства иностранных дел''']],
             [['''Укажите первого царя из династии Романовых. (10)
1) Фёдор Никитич 
2) Михаил Фёдорович
3) Михаил Александрович
4) Алексей Михайлович''',
               '''Во время правления этого императора было отменено крепостное право. (20)
1) Павел I
2) Николай I
3) Александр II
4) Александр III''',
               '''Прозвище этого царя - «Кровавый». (30)
1) Петр I
2) Николай II
3) Александр II
4) Петр III''',
               '''У этой императрицы была страсть к украшениям — она славилась тем, что никогда не надевала один и тот же наряд дважды. (40)
1) Елизавета Петровна
2) Анна Иоанновна
3) Софья Алексеевна
4) Екатерина II'''],
              ['''В каком году был подписан указ о престолонаследии? (10)
1) 1720 год
2) 1722 год
3) 1723 год
4) 1725 год''',
               '''Укажите даты Русско-Японской войны. (20)
1) 1904-1905 года
2) 1902-1905 года
3) 1905-1907 года
4) 1910-1912 года''',
               '''Выберите событие, названное «кровавым воскресеньем». (30)
1) День шествия рабочих к Зимнему дворцу с обращением к императору ( 9 января 1905 года) 
2) День коронации императора Николая Второго (14 мая 1896 года ) 
3) День бракосочетания Николая Второго и Александры Федоровны (14 ноября 1894 года) 
4) Давка на Ходынском поле (30 мая 1896 года)''',
               '''В каком году произошло первое Стрелецкое восстание? (40)
1) 1680
2) 1681
3) 1682
4) 1684'''],
              ['''Чей портрет изображен на картинке? (10)
1) Николай I
2) Александр II
3) Александр III
4) Павел I''',
               '''Чей портрет изображен на картинке? (20)
1) Федор III
2) Михаил Федорович 
3) Алексей Михайлович  
4) Иван V''',
               '''Чей портрет изображен на картинке? (30)
1) Екатерина I
2) Екатерина II 
3) Елизавета Петровна
4) Анна Иоанновна ''',
               '''Чей портрет изображен на картинке? (40)
1) Михаил Федорович 
2) Алексей Михайлович 
3) Иван V 
4) Федор III'''
               ],
              ['''В каком году был принят Свод законов Российской империи? (10)
1) 1804 
2) 1833 
3) 1866 
4) 1909''',
               '''В каком году был принят Гражданский кодекс Российской империи? (20)
1) 1850 
2) 1852 
3) 1864 
4) 1872''',
               '''Какая императрица основала Эрмитаж в Санкт-Петербурге? (30)
1) Анна Иоанновна 
2) Екатерина II 
3) Елизавета Петровна
4) Александра Федоровна''',
               '''Какая жена императора Павла I Романова утонула в Дворцовом пруду в Санкт-Петербурге? (40)
1) Екатерина II 
2) Мария Федоровна 
3) Елизавета Алексеевна 
4) Александра Федоровна''']],
             [['''Кто был первым князем, объединившим Киевскую Русь? (10)
1) Олег Вещий
2) Владимир Святой
3) Игорь Рюрикович
4) Ярослав Мудрый''',
               '''Какой князь провел крещение Руси и принял христианство? (20)
1) Олег Вещий
2) Святослав Вечевой
3) Владимир Святославич
4) Ярослав Мудрый''',
               '''Кто из князей Древней Руси провел реформы, направленные на сближение с Западной Европой? (30)
1) Олег Вещий
2) Владимир Святославич
3) Игорь Рюрикович
4) Ярослав Мудрый''',
               '''Какой князь считается основателем Москвы и началом формирования Московского государства? (40)
1) Дмитрий Донской
2) Игорь Рюрикович
3) Юрий Долгорукий
4) Василий III'''],
              ['''В каком году состоялось Крещение Руси? (10)
1) 988 год
2) 1066 год
3) 1037 год
4) 1015 год''',
               '''Когда произошла Битва на Неве? (20)
1) 1169 год
2) 1240 год
3) 1380 год
4) 1223 год''',
               '''Когда произошло падение Киева под власть Золотой Орды? (30)
1) 1125 год
2) 1169 год
3) 1240 год
4) 1380 год''',
               '''Когда состоялось объединение Московского княжества и Киевской Руси? (40)
1) 1169 год
2) 1283 год
3) 1480 год
4) 1380 год'''],
              ['''Что означает термин "дружина" в Древней Руси? (10)
1) Земельное владение князя
2) Армия или отряд вооруженных людей, служащих при князе
3) Первобытная община, совместно владеющая землей
4) Торговый союз между городами''',
               '''Что означает термин "поместное право" в Древней Руси? (20)
1) Правила, регулирующие местные торговые отношения
2) Кодекс законов, устанавливающий права и обязанности крестьян
3) Привилегия, предоставляемая местным князьям
4) Правила, определяющие владение и передачу земельного имущества''',
               '''Что означает термин "вече" в Древней Руси? (30)
1) Общественное собрание, на котором принимались важные решения
2) Территория вокруг княжеского города, населённая свободными крестьянами
3) Главное правительственное учреждение в Киевской Руси
4) Торговый центр на Древней Руси''',
               '''Что означает термин "печенеги" в Древней Руси? (40)
1) Племена, живущие на северо-востоке Руси
2) Народ, проживающий на кавказских землях
3) Восточные славяне, населявшие Украину и Белоруссию
4) Кочевой народ, постоянно враждовавший с Русью'''],
              ['''Какое событие стало причиной конца существования Киевской Руси? (10)
1) Разделение Киевской Руси на отдельные княжества
2) Монгольское нашествие на Русь
3) Завоевание Константинополя крестоносцами
4) Расширение власти Литвы на русские земли''',
               '''В Древней Руси за убийство свободного человека платился денежный штраф в пользу князя, называвшийся вирой. А за увечье платилось именно оно. (20)
1) Полувечье
2) Око
3) Зуб
4) Полувирье''',
               '''Павел Флоренский писал: "Древняя Русь возжигает пламя своей культуры непосредственно от священного огня Византии", таким образом, продолжая эстафету. А кто эту эстафету начал? (30)
1) Олимп
2) Прометей
3) Зевс
4) Иерусалим''',
               '''Историк архитектуры Николай Малинин назвал древнюю Русь ЕЮ. (40)
1) Государством Варяг
2) Мордором
3) Деревянной державой
4) Империей Перуна''']]]

information = [[[
    '''«Самого́нщики» — советский комедийно-приключенческий короткометражный художественный фильм, снятый в 1961 году на киностудии «Мосфильм» режиссёром Леонидом Гайдаем. Вместе с фильмом «Пёс Барбос и необычный кросс» это первое произведение о трио антигероев-жуликов Труса, Балбеса и Бывалого. ''',
    '''Кадр из фильма “Девчата”. Надежда Румянцева – советская актриса, народная артистка РСФСР, известная зрителям по роли "Тоси" из фильма "Девчата". Благодаря этой картине о ней узнал не только весь Советский Союз, но и Голливуд. Правда, в иностранных фильмах Надежда Васильевна так и не снималась, так как Госкино было против этого.''',
    '''«В бой иду́т одни́ „старики́“»  - советский чёрно-белый художественный фильм 1973 года режиссёра Леонида Быкова, повествующий о буднях лётчиков-истребителей в годы Великой Отечественной войны. Действие фильма начинается в конце лета 1943 года, во время битвы за Днепр.''',
    '''«Офице́ры» — советский художественный полнометражный фильм, поставленный на Киностудии имени М. Горького в 1971 году режиссёром Владимиром Роговы́м. Сюжет фильма основан на пьесе «Танкисты» советского писателя Бориса Васильева. Премьера кинокартины в СССР состоялась 26 июля 1971 года. Фильм был снят на чёрно-белую плёнку. В 2010 году был колоризован компанией «Формула цвета».'''
],
    [
        '''''',
        '''''',
        '''''',
        ''''''
    ],
    [
        '''Песня «Катюша». Композитор - Матвей Блантер, автор слов - Михаил Исаковский. В селе Всходы Угранского района (недалеко от  деревни Глотовка - родины М. Исаковского), в Доме культуры, расположен музей песни «Катюша».''',
        '''Песня «Журавли» композитора Яна Френкеля на стихи Расула  Гамзатова в переводе на русский язык Наума  Гребнева. Песня посвящена солдатам, погибшим  во время военных действий.''',
        '''Советская пенся «Эх, дороги», написанная Анатолием Новиковым на стихи Льва Ошанина вскоре после окончания Великой Отечественной войны, осенью 1945 года, для театрализованной программы "Весна победная", которую задумал и осуществил к празднику 7 ноября режиссёр Ансамбля песни и пляски войск НКВД Сергей Юткевич.''',
        '''Песня «Мы друзья, перелетные птицы» из кинофильма «Небесный тихоход», поставленного в 1945 году  режиссёром Семёном Тимошенко. Песня встречается также под другими заглавиями: "Пилоты", "Перелетные птицы", "Потому что мы пилоты" и т. д. и звучит как клятвы героев в момент, когда друзья приходят проведать  сослуживца в госпитале. В фильме песню исполняют  Николай Крючков и Василий Меркурьев.'''
    ],
    [
        '''Санаторий «Курпаты» Где находится: Крым, Ялта. Годы строительства: 1980—1985 Архитектор: Игорь Василевский Инженер: Нодар Канчели. У санатория «Курпаты» два комплекса — «Пальмиро Тольятти» и «Дружба». Последний построили в форме летающей тарелки. Этот основной корпус — совместный проект профсоюзов СССР и Чехословакии.''',
        '''Здание Президиума РАН начали проектировать в 1960-х годах. Архитекторы: А. Батырева, Л. Барщ, С. Захаров, А. Звездин. К строительству приступили в 1974 году, закончили в 1990. Вторую очередь комплекса сдали в эксплуатацию еще спустя восемь лет. В основании комплекса располагаются подземные парковки и технические этажи. В низких зданиях — концертный, конференц-залы и зимний сад. В высотной части работают ученые. На башне находится сложная конструкция, которую прозвали золотыми мозгами: она закрывает собой коммуникационные системы, торчащие из крыши.''',
        '''Здание отеля «Украина». Вторая по высоте 206-метровая «высотка» построена в 1953—1957 годах (архитектор А. Г. Мордвинов при участии В. К. Олтаржевского, В. Г. Калиша, инженера П. А. Красильникова), став, таким образом, последней по времени сооружения. Центральный объём включает 34 этажа. Здание открывает Кутузовский проспект — новую московскую магистраль, созданную в послевоенное время. В пристроенных крыльях расположены 257 квартир.''',
        '''Дворе́ц Сове́тов — неосуществлённый проект строительства высотного административного здания в Москве для проведения сессий Верховного Совета СССР и массовых демонстраций. План архитектора Бориса Иофана предполагал, что высота Дворца Советов вместе с венчающей его стометровой статуей Владимира Ленина составит 415 м. Дворец должен был стать центром новой советской Москвы и самым высоким зданием в мире, символизирующим победу социализма. В 1931 году на месте предполагавшегося строительства Дворца Советов был взорван храм Христа Спасителя, подготовительные работы начались уже на следующий год. Фундамент дворца был завершён в 1939-м, но из-за начала Великой Отечественной войны проект заморозили.'''
    ]],
    [[
        '''Михаил Фёдорович - первый русский царь из династии Романовых. Правил с 1613 года по 1645 год. Михаил Федорович Романов стал царем в непростое время. Ему пришлось восстанавливать экономику страны, возвращать потерянные в ходе неудачных войн земли, исправлять все негативные последствия Смутного времени.''',
        '''3 марта (по нов. Стилю) 1861 года Александр II отменил крепостное право в России. Крестьяне получили личную свободу, но были вынуждены отбывать барщину или платить оброк за пользование наделами. Полностью выйти из зависимости удалось не всем. Со временем помещики-крепостники добились некоторых изменений реформы в свою пользу.''',
        '''Николай II был жестоким самодержцем, получившим прозвище Николай Кровавый. Впервые оно стало ассоциироваться с ним из-за несчастного случая – давки во время церемонии его коронации, а позже оно прижилось из-за голода, бесхозяйственности, политических репрессий и войн, которые Россия проиграет.''',
        '''Елизавета Петровна привнесла стремление к роскоши и величию даже в мелочах, она не позволяла приходить в «ношеных» нарядах и своим придворным дамам. Ее гардероб насчитывал 15000 платьев, а во время пожара в Летнем дворце сгорело 4000 платьев!'''
    ],
        [
            '''Указ о престолонаследии Петра 1 утвердил, что Правитель может назначить себе любого преемника, которого он посчитает лучшим кандидатом для дальнейшего развития страны. Указ Петра 1 окончательно сформировал и закрепил самодержавие в России.''',
            '''Русско-японская война произошла в 1904-1905 годах между Российской империей и Японией. Война началась из-за их территориальных и экономических интересов на территории Маньчжурии и Кореи. Япония обладала технологическим превосходством. Это и другие причины привели к поражению России. События войны привели к серии внутренних протестов и напряжения в России, что стало одной из предпосылок для Революции 1905 года.''',
            '''9 января 1905 года  большое количество мирных демонстрантов, протестующих против разгона мирных митингов и низкого уровня жизни, собралось перед Зимним дворцом. Царская гвардия открыла огонь по толпе, убив более 130 человек и ранив более 300. Это событие получило название "Кровавое воскресенье". Кровавое воскресенье стало поводом для протестов и забастовок во многих городах, что в дальнейшем повысило революционное настроение.''',
            '''Стреле́цкий бунт 1682 года — бунт (восстание) московских стрельцов в начале правления 10-летнего Петра I, в результате которого его соправителем стал старший 15-летний брат Иван, а фактической правительницей при них стала старшая сестра 24-летняя Софья Алексеевна. 15 мая 1682 года стрельцы вторгнутся в Кремль, начнется серия кровавых расправ с последующими выдвижениями ультиматумов. Большая часть рода Нарышкиных была убита, а находящиеся у власти Пётр I и регентша Наталья не могли сделать с бунтом ничего.'''
        ],
        [
            '''Алекса́ндр II Николаевич (17 апреля 1818, Москва — 1 марта 1881, Санкт-Петербург) — российский император (1855—1881 гг.) из династии Романовых, проводивший широкомасштабные реформы. Старший сын сначала великокняжеской, а с 1825 года — императорской четы Николая Павловича и Александры Фёдоровны.''',
            '''Фёдор III Алексе́евич (30 мая 1661, Москва — 27 апреля 1682, Москва) — Государь, Царь и Великий Князь всея Руси с 1676 года, из династии Романовых, сын царя Алексея Михайловича и царицы Марии Ильиничны, старший брат царей Ивана V (родной) и Петра I (единокровный) и родной младший брат царевны Софьи.''',
            '''Елизаве́та Петро́вна (18 декабря 1709, Коломенское — 25 декабря 1761, Санкт-Петербург) — императрица и самодержица Всероссийская из династии Романовых с 25 ноября (6 декабря) 1741 года по 25 декабря 1761 (5 января 1762), младшая дочь Петра I и Екатерины I.''',
            '''Алексе́й Миха́йлович Тиша́йший (9 марта 1629, Москва — 29 января 1676, Москва) — второй русский царь из династии Романовых (14 июля 1645 — 29 января 1676), сын Михаила Фёдоровича и его второй жены Евдокии.'''
        ],
        [
            '''Свод законов Российской империи был принят в 1804 году. Он был первым систематизированным сборником правовых норм, который объединял все ранее существовавшие законы и указы. Свод законов стал важным шагом в совершенствовании правовой системы Российской империи. ''',
            '''Гражданский кодекс Российской империи был принят в 1864 году. Он состоял из четырёх частей и был первым кодифицированным законом, регулирующим гражданское право в Российской империи. Кодекс впервые определил правовой статус граждан и регулировал вопросы семейного, наследственного, трудового и торгового права.''',
            '''Екатерина II основала Эрмитаж в Санкт-Петербурге. Она начала собирать коллекцию произведений искусства и антиквариата, которая позднее стала ядром известного музея. Эрмитаж стал одним из крупнейших и наиболее значимых музеев в мире, хранящих богатую коллекцию произведений искусства.''',
            '''Елизавета Алексеевна, принцесса Вюртембергская, была первой женой императора Павла I Романова. Она утонула 5 апреля 1782 года в Дворцовом пруду в Санкт-Петербурге в результате несчастного случая. Елизавета оставила двух дочерей и была разлучена с Павлом I после его восшествия на престол.'''
        ]],
    [[
        '''Олег Вещий был первым князем, который объединил разрозненные владения восточных славян в IX веке и создал Древнюю Русь.''',
        '''Владимир Святославич принял христианство в X веке и провел крещение Руси. Он дал приказ крестить население Киевской Руси, а также основал много христианских церквей и монастырей.''',
        '''Ярослав Мудрый, также известный как Ярослав Мудрый, провел реформы в XI веке, которые направлены на сближение Киевской Руси с Западной Европой. Он создал законы, строил каменные церкви и монастыри, поддерживал образование и культуру.''',
        '''Основание Москвы датируется 1147 годом и приписывается князю Юрию Долгорукому. На момент основания Москвы Юрий был только князем Ростово-Суздальским.'''
    ],
        [
            '''В 988 году князь Владимир Святославович принял христианство и организовал крещение Руси, что стало важным событием в истории Древней Руси и ее принятия православия.''',
            '''Битва на Неве произошла в 1240 году и была частью монгольско-русской войны. В этой битве русские войска под командованием князя Александра Невского отразили нападение шведского флота.''',
            '''В 1240 году монголо-татарская Золотая Орда вторглась в Киевскую Русь и взяла Киев. Это событие стало важным шагом в укреплении власти Золотой Орды над Русью и распаде Киевской Руси.''',
            '''В 1283 году Московское княжество под руководством князя Даниила Александровича объединило силы с Киевской Русью, что стало важным этапом в формировании единого русского государства и укреплении Московского княжества.'''
        ],
        [
            '''В Древней Руси дружина представляла собой вооруженный отряд, состоящий из личных сторонников князя. Они выполняли роль личной охраны князя, а также участвовали в военных походах и защите интересов княжества.''',
            '''Поместное право было системой норм, которые регулировали передачу и владение землей в Древней Руси. Оно определяло правила наследования, продажи и передачи земельного имущества, а также основы гражданского права.''',
            '''Вече представляло собой общественное собрание, на котором принимались важные социальные, политические и правовые решения в Древней Руси. Здесь собирались князья, бояре и свободные люди для обсуждения общих вопросов и принятия решений.''',
            '''Печенеги были кочевым народом, населявшим преимущественно степные районы современной Украины и России. Они постоянно враждовали с русскими княжествами, атакуя их территории и участвуя в древнерусских конфликтах.'''
        ],
        [
            '''Монгольское нашествие на Русь, которое началось в XIII веке, привело к разорению и опустошению многих русских земель, а также к подчинению Киевской Руси монгольскому игу. Это событие существенно повлияло на последующую историю и распад Киевской Руси.''',
            '''Полувирье — штраф за тяжкие увечья свободному человеку''',
            '''От греков, через Византию в Русь пошел Прометеев огонь Эллады.''',
            '''В древней Руси было особенно развито деревянное зодчество.'''
        ]]]

correct_answers = [
    [["1", "2", "2", "3"], ["1", "2", "1", "3"], ["1", "2", "3", "2"],
     ["1", "2", "3", "3"]],
    [["2", "3", "2", "1"], ["2", "1", "1", "3"], ["2", "1", "3", "2"],
     ["1", "3", "2", "3"]],
    [["1", "3", "4", "1"], ["1", "2", "3", "2"], ["2", "4", "1", "4"],
     ["2", "4", "2", "3"]]]

first_photos = [[[
    'AgACAgIAAxkDAAMtZX3GycvT6v_m3dGmQbK7NL6wqMUAApnSMRvmOOlLozkxXvj_AAHwAQADAgADeQADMwQ',
    'AgACAgIAAxkDAAMuZX3GyQABxvm0SX7XNWAfKnrVvQiGAAKa0jEb5jjpS1U1vwpKtppiAQADAgADeQADMwQ',
    'AgACAgIAAxkDAAMvZX3GysbCe2c2i9BksRnvE-ntmFEAApvSMRvmOOlLa_H_Eha6UGkBAAMCAAN5AAMzBA',
    'AgACAgIAAxkDAAMwZX3Gykl1hsHlzGLaY017P6J_DHkAApzSMRvmOOlLHexY_7tIe-0BAAMCAAN5AAMzBA'],
    [
        'AgACAgIAAxkDAAMxZX3GysffRYj6RS8tUmGkXXn6IhkAAp3SMRvmOOlL9J_Pn2wx0g0BAAMCAAN4AAMzBA',
        'AgACAgIAAxkDAAMyZX3Gy4QJAyjjibjKNw9t2GtmgQsAAp7SMRvmOOlLjJkuxaEH08gBAAMCAAN5AAMzBA',
        'AgACAgIAAxkDAAMzZX3Gy3vBzr3wliVFay-GUUi6qR8AAp_SMRvmOOlLMpa-xmC8SZMBAAMCAAN4AAMzBA',
        'AgACAgIAAxkDAAM0ZX3Gy1vFUs8DN2NpuagiReXDJWYAAqDSMRvmOOlL9rOw7ZfnUu0BAAMCAAN4AAMzBA'],
    ['', '', '', ''], [
        'AgACAgIAAxkDAAM1ZX3GzP-XM8YH8y1At18nEiP-1UkAAqHSMRvmOOlLJUkTk47fpskBAAMCAAN5AAMzBA',
        'AgACAgIAAxkDAAM2ZX3GzS9cFKAj0j4mr8nyN9rw060AAqLSMRvmOOlLwdTDWL6diJsBAAMCAAN4AAMzBA',
        'AgACAgIAAxkDAAM3ZX3Gzla4xmKzSq7DUQ9ca-eeeFAAAqPSMRvmOOlLv9O3hxL7ky8BAAMCAAN5AAMzBA',
        'AgACAgIAAxkDAAM4ZX3GzjMt8p7LP6aplM0kZvhOW7wAAqTSMRvmOOlLkesUHYBpu2YBAAMCAAN5AAMzBA']],
    [['', '', '', ''], ['', '', '', ''], [
        'AgACAgIAAxkDAAM5ZX3Gz-3K_Hgxg2UynCV_oRFFzE8AAqXSMRvmOOlLrBT44UJPrqcBAAMCAAN5AAMzBA',
        'AgACAgIAAxkDAAM6ZX3G0DjuZUSTHuV2PFdzUquGe24AAqbSMRvmOOlLRp0zeNbi0akBAAMCAAN5AAMzBA',
        'AgACAgIAAxkDAAM7ZX3G0YMpFIPcA9m04PZjQsSEZIgAAqfSMRvmOOlLvyZzA-e36wcBAAMCAAN5AAMzBA',
        'AgACAgIAAxkDAAM8ZX3G0ojQ0I95Ttk0r81PSnP5HHUAAqjSMRvmOOlLzEP9qr3tEvwBAAMCAAN5AAMzBA'],
     ['', '', '', '']],
    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''],
     ['', '', '', '']]]

first_photos_test = [[[
    "AgACAgIAAxkBAAIR1WV8qrmnmuJYeOvdKw56E_SZOZvzAAIK1jEbDlLpSwABTbyq5UGjgwEAAwIAA3MAAzME",
    "AgACAgIAAxkBAAIR12V8qwIGx0u0rmlAAYp1dbha1fpnAAIV1jEbDlLpS1QkkiNkCltEAQADAgADcwADMwQ",
    "AgACAgIAAxkBAAIR2WV8qzMjINpRm_Pb7DL-PnLdL-iJAAIc1jEbDlLpS8D1arbJxWpvAQADAgADcwADMwQ",
    "AgACAgIAAxkBAAIR22V8q05wA4Pmq3u_0qg3OmfPlCHnAAIg1jEbDlLpSzakHFKXx_yEAQADAgADcwADMwQ"],
    [
        "AgACAgIAAxkBAAIR3WV8rClpTiRh8RXC4M3x4GhiguG-AAJE1jEbDlLpS7CdhcaEzFQ8AQADAgADcwADMwQ",
        "AgACAgIAAxkBAAIR32V8rDzcWvdAN2HqgpAZirt4naDuAAJF1jEbDlLpSxcgr4M2dhezAQADAgADcwADMwQ",
        "AgACAgIAAxkBAAIR4WV8rFEX-Evj6RZjSWFp4mftFCjYAAJG1jEbDlLpS7RLICaSqv8oAQADAgADcwADMwQ",
        "AgACAgIAAxkBAAIR42V8rGP0pbAxt5fNoSLUnV9rysA5AAJI1jEbDlLpS-B_icQ92I3SAQADAgADcwADMwQ"],
    ["", "", "", ""],
    [
        "AgACAgIAAxkBAAIR5WV8rKZiG71lY8tKnGEcEsET5iV5AAJL1jEbDlLpS9XRVfUTShgFAQADAgADcwADMwQ",
        "AgACAgIAAxkBAAIR52V8rLUOxEaN-hNgT9ev9Qez6NsKAAJM1jEbDlLpS6-P0KJutcxTAQADAgADcwADMwQ",
        "AgACAgIAAxkBAAIR6WV8rNq8rz9N26wIoFrnENaFYIiJAAJN1jEbDlLpS-XpLpbVagXoAQADAgADcwADMwQ",
        "AgACAgIAAxkBAAIR62V8rQlCw8O8NqPJKceTVmv9j5ffAAJP1jEbDlLpS2RSgPeWeRn4AQADAgADcwADMwQ"]],
    [["", "", "", ""], ["", "", "", ""],
     [
         "AgACAgIAAxkBAAIR7WV8rY4YGFRQZnY4HsGy0hE9_6LyAAJf1jEbDlLpSzQdtWhwEonKAQADAgADcwADMwQ",
         "AgACAgIAAxkBAAIR72V8ra67NvH85JBjSCnIb1kyMrreAAJh1jEbDlLpSwaGCpDXUMaeAQADAgADcwADMwQ",
         "AgACAgIAAxkBAAIR8WV8rcFCnZiDjvKJkt6qt013bGFNAAJj1jEbDlLpS7MJdpiUMZk0AQADAgADcwADMwQ",
         "AgACAgIAAxkBAAIR82V8rdIZcSasuMYs_RD5NmPQ4qRZAAJk1jEbDlLpS33YGCAObWpUAQADAgADcwADMwQ"],
     ["", "", "", ""]],
    [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
     ["", "", "", ""]]]
output_photos = [[['', '', '', ''], [
    'AgACAgIAAxkDAANDZX3JcN8Xr03hj15Pi3K6Wtd-H7EAArbSMRvmOOlL1japbEwWySsBAAMCAAN4AAMzBA',
    'AgACAgIAAxkDAANEZX3JcRDLMbkfhgJqYqos2CHxenAAArfSMRvmOOlLuBbL0Hd_0DIBAAMCAAN5AAMzBA',
    'AgACAgIAAxkDAANFZX3JcXUXyYOkQb4trG1kgbly5J0AArjSMRvmOOlLHGfsXcphHHgBAAMCAAN4AAMzBA',
    'AgACAgIAAxkDAANGZX3JccNOEx1Kc2z-otY47eBPynIAArnSMRvmOOlLg_WrHSfrio4BAAMCAAN4AAMzBA'],
                  ['', '', '', ''], ['', '', '', '']],
                 [['', '', '', ''], ['', '', '', ''], ['', '', '', ''],
                  ['', '', '', '']],
                 [['', '', '', ''], ['', '', '', ''], ['', '', '', ''],
                  ['', '', '', '']]]

output_photos_test = [[["", "", "", ""],
                       [
                           "AgACAgIAAxkBAAIR9WV8rq8jz6uHFwABH-bPOR5AeKzTVwACcNYxGw5S6UtB0vpBIV7seQEAAwIAA3MAAzME",
                           "AgACAgIAAxkBAAIR92V8rshV2oLou3T2lk5uIv0iEf1BAAJx1jEbDlLpS1nCtdRk2Gw7AQADAgADcwADMwQ",
                           "AgACAgIAAxkBAAIR-WV8rtvip-cDx8FfBaXjtN8qOkg1AAJz1jEbDlLpSyR6Wp7ldvM6AQADAgADcwADMwQ",
                           "AgACAgIAAxkBAAIR-2V8rvMkjV4jJery_tYEnUcQyNrVAAJ01jEbDlLpS-bYUBWGDitiAQADAgADcwADMwQ"],
                       ["", "", "", ""], ["", "", "", ""]],
                      [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                       ["", "", "", ""]],
                      [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                       ["", "", "", ""]]]

audios = [[['', '', '', ''], ['', '', '', ''], ['AwACAgIAAxkDAANNZX3KvU__QHLMem1BXEyaehJDapkAAkhAAALmOOlLGbAjnbmtXckzBA', 'AwACAgIAAxkDAANOZX3Kvtwan2MkAjsgSHRsUvU1g6gAAklAAALmOOlLnw-pLezKt_gzBA', 'AwACAgIAAxkDAANPZX3KviKQuD80o2yg6-oXjEPiI-kAAkpAAALmOOlLEYMDlkP3oj8zBA', 'AwACAgIAAxkDAANQZX3KvrxXLyMdn-lHqeKmiRtK7sgAAktAAALmOOlLuILcl0VnuU0zBA'], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]]

audios_test = [[["", "", "", ""], ["", "", "", ""],
           [
               "AwACAgQAAxkBAAISFmV8tUeRVDnlZX0TSKBryRlkP-ZBAAJuUQAC3X_hU5wXHHMP-HnKMwQ",
               "AwACAgQAAxkBAAISImV8tizBq6QOPLVXZ0B6vCcx2v7PAAK4UQAC3X_hU8YEelWUB5v3MwQ",
               "AwACAgQAAxkBAAISJWV8tmSRhZ4REOfzsXi6ViuIroJ9AALHUQAC3X_hU0ARZi2Ky162MwQ",
               "AwACAgQAAxkBAAISKGV8t1Qf9CwzfwFhOeO6glhWUk_ZAAIVUgAC3X_hU7zaz9GgGyP-MwQ"],
           ["", "", "", ""]],
          [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
           ["", "", "", ""]],
          [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
           ["", "", "", ""]]]

topics = [
    Topic(topic, "", [SubTopic(stn, [Question(correct_answers[i][j][k], 4,
                                              Message(questions[i][j][k],
                                                      first_photos[i][j][k],
                                                      audio=audios[i][j][k]),
                                              Message(information[i][j][k],
                                                      output_photos[i][j][k]))
                                     for k in range(4)]) for j, stn in
                      enumerate(sub_topics_name[i])])
    for i, topic in enumerate(topics_name)]
