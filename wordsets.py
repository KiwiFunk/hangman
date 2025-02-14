"""
A collection of lists containing themed words to load into the hangman game.
"""

def return_wordlist(set):
    """
    Return a specified list of words
    """
    requested_list = wordsets[set]
    return requested_list

wordsets = {
    1: [
        'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 
        'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon', 'xigua', 'yuzu', 'zucchini'
    ],
    2: [
        'argentina', 'australia', 'austria', 'bangladesh', 'belgium', 'brazil', 'canada', 'chile', 'china', 'colombia', 
        'czechia', 'denmark', 'egypt', 'ethiopia', 'finland', 'france', 'germany', 'greece', 'hungary', 'iceland', 
        'india', 'indonesia', 'iran', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kenya', 'luxembourg', 
        'malaysia', 'mexico', 'morocco', 'netherlands', 'new zealand', 'nigeria', 'norway', 'pakistan', 'peru', 'philippines', 
        'poland', 'portugal', 'qatar', 'romania', 'russia', 'saudi arabia', 'south africa', 'south korea', 'spain', 
        'sweden', 'switzerland', 'taiwan', 'thailand', 'turkey', 'ukraine', 'united kingdom', 'united states', 'uruguay', 
        'vietnam', 'zimbabwe'
    ],
    3: [
        'alligator', 'antelope', 'baboon', 'bear', 'bison', 'binturong', 'camel', 'cheetah', 'chimpanzee', 'crocodile', 'deer', 'elephant', 
        'flamingo', 'fox', 'giraffe', 'gorilla', 'hippopotamus', 'hyena', 'kangaroo', 'koala', 'leopard', 'lion', 'meerkat', 
        'monkey', 'ostrich', 'otter', 'panda', 'parrot', 'penguin', 'rhinoceros', 'seal', 'sloth', 'snake', 'tiger', 'tortoise', 
        'vulture', 'walrus', 'wolf', 'wombat', 'zebra', 'porcupine', 'armadillo', 'lemur', 'wallaby', 'anteater'
    ],
    4: [
        'spaghetti', 'pizza', 'sushi', 'tacos', 'hamburger', 'lasagna', 'ramen', 'paella', 'biryani', 'pho', 'poutine', 'falafel', 
        'ceviche', 'dim sum', 'bibimbap', 'pierogi', 'moussaka', 'ratatouille', 'chili', 'gumbo', 'risotto', 'gnocchi', 'samosa', 
        'empanada', 'bruschetta', 'quiche', 'fondue', 'baklava', 'tiramisu', 'croissant', 'macarons', 'pavlova', 'cheesecake', 
        'brownies', 'cupcakes', 'pancakes', 'waffles', 'crepes', 'dumplings', 'spring rolls'
    ],
    5: [
        'abandon', 'ability', 'absence', 'academy', 'account', 'accused', 'achieve', 'acquire', 'address', 'advance', 'adverse', 'advised', 
        'adviser', 'against', 'airline', 'airport', 'alcohol', 'alleged', 'already', 'analyst', 'ancient', 'another', 'anxiety', 'anybody', 
        'applied', 'arrange', 'arrival', 'article', 'assault', 'assumed', 'assured', 'attempt', 'attract', 'auction', 'average', 'backing', 
        'balance', 'banking', 'barrier', 'battery', 'bearing', 'beating', 'because', 'bedroom', 'believe', 'beneath', 'benefit', 'besides', 
        'between', 'billion', 'binding', 'brother', 'brought', 'burning', 'cabinet', 'caliber', 'calling', 'capable', 'capital', 'captain', 
        'caption', 'capture', 'careful', 'carrier', 'caution', 'ceiling', 'central', 'centric', 'century', 'certain', 'chamber', 'channel', 
        'chapter', 'charity', 'charlie', 'charter', 'checked', 'chicken', 'chronic', 'circuit', 'classes', 'classic', 'climate', 'closing', 
        'closure', 'clothes', 'collect', 'college', 'combine', 'comfort', 'command', 'comment', 'compact', 'company', 'compare', 'compete', 
        'complex', 'concept', 'concern', 'concert', 'conduct', 'confirm', 'connect', 'consent', 'consist', 'contact', 'contain', 'content', 
        'contest', 'context', 'control', 'convert', 'correct', 'council', 'counsel', 'counter', 'country', 'crucial', 'crystal', 'culture', 
        'current', 'cutting', 'dealing', 'decided', 'decline', 'default', 'defence', 'deficit', 'deliver', 'density', 'deposit', 'desktop', 
        'despite', 'destroy', 'develop', 'devoted', 'diamond', 'digital', 'discuss', 'disease', 'display', 'dispute', 'distant', 'diverse', 
        'divided', 'drawing', 'driving', 'dynamic', 'eastern', 'economy', 'edition', 'elderly', 'element', 'engaged', 'enhance', 'essence', 
        'evening', 'evident', 'exactly', 'examine', 'example', 'excited', 'exclude', 'exhibit', 'expense', 'explain', 'explore', 'express', 
        'extreme', 'factory', 'faculty', 'failing', 'failure', 'fashion', 'feature', 'federal', 'feeling', 'fiction', 'fifteen', 'filling', 
        'finance', 'finding', 'fishing', 'fitness', 'foreign', 'forever', 'formula', 'fortune', 'forward', 'founder', 'freedom', 'further', 
        'gallery', 'gateway', 'general', 'genetic', 'genuine', 'gigabit', 'greater', 'hanging', 'heading', 'healthy', 'hearing', 'heavily', 
        'helpful', 'helping', 'herself', 'highway', 'himself', 'history', 'holding', 'holiday', 'housing', 'however', 'hundred', 'husband', 
        'illegal', 'illness', 'imagine', 'imaging', 'improve', 'include', 'initial', 'inquiry', 'insight', 'install', 'instant', 'instead', 
        'intense', 'interim', 'involve', 'jointly', 'journal', 'journey', 'justice', 'justify', 'keeping', 'killing', 'kingdom', 'kitchen', 
        'knowing', 'landing', 'largely', 'lasting', 'leading', 'learned', 'leisure', 'liberal', 'liberty', 'library', 'license', 'limited', 
        'listing', 'logical', 'loyalty', 'machine', 'manager', 'mansion', 'married', 'massive', 'maximum', 'meaning', 'measure', 'medical', 
        'meeting', 'mention', 'message', 'million', 'mineral', 'minimal', 'minimum', 'missing', 'mission', 'mistake', 'mixture', 'monitor', 
        'monthly', 'morning', 'musical', 'mystery', 'natural', 'neither', 'nervous', 'network', 'neutral', 'notable', 'nothing', 'nowhere', 
        'nuclear', 'nursing', 'obvious', 'offense', 'officer', 'ongoing', 'opening', 'operate', 'opinion', 'optical', 'organic', 'outcome', 
        'outdoor', 'outlook', 'outside', 'overall', 'pacific', 'package', 'painted', 'parking', 'partial', 'partner', 'passage', 'passing', 
        'passion', 'passive', 'patient', 'pattern', 'payable', 'payment', 'penalty', 'pending', 'pension', 'percent', 'perfect', 'perform', 
        'perhaps', 'phoenix', 'picking', 'picture', 'pioneer', 'plastic', 'pointed', 'popular', 'portion', 'poverty', 'precise', 'predict', 
        'premier', 'premium', 'prepare', 'present', 'prevent', 'primary', 'printer', 'privacy', 'private', 'problem', 'proceed', 'process', 
        'produce', 'product', 'profile', 'program', 'project', 'promise', 'promote', 'protect', 'protein', 'protest', 'provide', 'publish', 
        'purpose', 'pushing', 'qualify', 'quality', 'quarter', 'radical', 'railway', 'readily', 'reading', 'reality', 'realize', 'receipt', 
        'receive', 'recover', 'reflect', 'regular', 'related', 'release', 'remains', 'removal', 'removed', 'replace', 'request', 'require', 
        'reserve', 'resolve', 'respect', 'respond', 'restore', 'retired', 'revenue', 'reverse', 'rollout', 'routine', 'running', 'satisfy', 
        'science', 'section', 'segment', 'serious', 'service', 'serving', 'session', 'setting', 'seventh', 'several', 'shortly', 'showing', 
        'silence', 'silicon', 'similar', 'sitting', 'sixteen', 'skilled', 'smoking', 'society', 'somehow', 'someone', 'speaker', 'special', 
        'species', 'sponsor', 'station', 'storage', 'strange', 'stretch', 'student', 'studied', 'subject', 'succeed', 'success', 'suggest', 
        'summary', 'support', 'suppose', 'supreme', 'surface', 'surgery', 'surplus', 'survive', 'suspect', 'sustain', 'teacher', 'telecom', 
        'telling', 'tension', 'theatre', 'therapy', 'thereby', 'thought', 'through', 'tonight', 'totally', 'tourist', 'towards', 'traffic', 
        'trouble', 'turning', 'typical', 'uniform', 'unknown', 'unusual', 'upgrade', 'upscale', 'utility', 'variety', 'various', 'vehicle', 
        'venture', 'version', 'veteran', 'victory', 'village', 'virtual', 'visible', 'waiting', 'walking', 'wanting', 'warning', 'warrant', 
        'wearing', 'weather', 'webcast', 'website', 'wedding', 'weekend', 'welcome', 'welfare', 'western', 'whereas', 'whereby', 'whether', 
        'willing', 'winning', 'without', 'witness', 'working', 'writing', 'written', 'younger'
    ]
}