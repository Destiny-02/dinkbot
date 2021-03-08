# Works with Python 3.9
import discord
import emoji
import random
import os
from keep_alive import keep_alive

TOKEN = os.getenv("TOKEN")
PREFIX = 'd!'

# dink dictionary
dictionary = [["destiny", "destiny", "destiny", "destiny", "destiny", "destiny", "dabbler", "dad", "daddy", "daggerman", "dairy", "dam", "damage", "dame", "damn", "damnation", "damsel", "dance", "dancer", "dancing", "dandelion", "danger", "danseur", "darbuka", "daring", "dark", "darling", "darn", "dash", "dashboard", "data", "date", "datum", "daughter", "dauphin", "davenport", "dawn", "day", "daybed", "daybreak", "daydreaming", "daylight", "daytime", "dazzler", "deacon", "deactivation", "dead", "deadline", "deadlock", "deadweight", "deae", "deal", "dealer", "dean", "dear", "dearth", "death", "deathbed", "debacle", "debate", "debating", "debauchery", "debility", "debt", "debunking", "debut", "debutante", "decade", "decadence", "decay", "deceased", "decedent", "deceit", "deceleration", "decency", "decentralization", "deception", "decimal", "decision", "deck", "decking", "declaration", "declarative", "decline", "declivity", "decolletage", "decomposition", "decompression", "decor", "decoration", "decorator", "decorum", "decrease", "decree", "decrement", "dedication", "deductibility", "deduction", "deed", "deepening", "deer", "defacing", "default", "defeat", "defeatism", "defect", "defection", "defence", "defendant", "defender", "defense", "deference", "deferent", "deferment", "defiance", "deficiency", "deficit", "definition", "deformation", "deformity", "degeneration", "degradation", "degree", "dehydration", "deification", "deity", "dejection", "delay", "delectation", "delegate", "delegation", "deliberation", "delicacy", "delight", "delineation", "delinquency", "delinquent", "delirium", "deliverance", "delivery", "dell", "deltoid", "deluge", "delusion", "deluxer", "demage", "demagnification", "demand", "demander", "demanding", "demarcation", "demeanor", "demineralization", "demise", "democracy", "democratization", "demography", "demolition", "demon", "demonstration", "demoralization", "demurrer", "demythologization", "den", "denial", "denomination", "denouement", "densitometry", "density", "dent", "dentist", "dentistry", "denunciation", "denying", "department", "departure", "dependence", "dependency", "dependent", "depersonalization", "depiction", "depletion", "deployment", "deposit", "deposition", "depot", "depravity", "depreciation", "depression", "deprivation", "depth", "deputy", "derangement", "derby", "derelict", "dereliction", "derision", "derivation", "derivative", "derrick", "derriere", "descendant", "descent", "description", "desecration", "desegregation", "desert", "desertion", "design", "designate", "designation", "designer", "designing", "desirability", "desire", "desk", "desolation", "despair", "despairing", "desperation", "despondency", "despot", "despotism", "dessert", "destination", "destiny", "destroyer", "destruction", "desuetude", "detachment", "detail", "detection", "detective", "detector", "detente", "detention", "detergency", "detergent", "deterioration", "determinability", "determinant", "determination", "determinism", "deterrence", "deterrent", "detestation", "detonation", "detractor", "detriment", "devastation", "developer", "development", "deviance", "deviation", "device", "devil", "devisee", "devotion", "dew", "dexamethasone", "dexterity", "diagnometer", "diagnosing", "diagnostic", "diagram", "dial", "dialect", "dialectic", "dialogue", "diam", "diameter", "diamond", "diaphragm", "diarrhea", "diarrhoea", "diary", "diathermy", "dice", "dichondra", "dichotomy", "dictator", "dictatorship", "diction", "dictionary", "dictum", "die", "diem", "diesel", "diet", "diethylaminoethyl", "diethylstilbestrol", "diety", "difference", "differentiability", "differential", "differentiation", "difficulty", "diffidence", "diffraction", "diffrunce", "diffusion", "dig", "digest", "digit", "digitalization", "dignity", "diisocyanate", "dilatation", "dilation", "dilemma", "dilettante", "diligence", "dill", "dilution", "dime", "dimension", "dimensioning", "dimethylglyoxime", "diminution", "din", "dinghy", "dingo", "dining", "dinner", "dinnertime", "dinnerware", "dinosaur", "diocese", "diorah", "dioxalate", "dioxide", "dip", "diphosphopyridine", "diplomacy", "diplomat", "dipper", "direction", "directionality", "directive", "directivity", "director", "directorate", "directorship", "directory", "dirge", "dirt", "disability", "disadvantage", "disaffection", "disagreement", "disappearance", "disappointment", "disapprobation", "disapproval", "disarmament", "disarray", "disassembly", "disaster", "disbelief", "disbursement", "disc", "discernment", "discharge", "disciple", "discipleship", "discipline", "disclaimer", "disclosure", "discomfort", "discontent", "discontinuance", "discontinuity", "discord", "discount", "discouragement", "discourse", "discoverer", "discovery", "discredit", "discrepancy", "discretion", "discrimination", "discussant", "discussion", "disdain", "disease", "disenfranchisement", "disengagement", "disfavor", "disgrace", "disguise", "disgust", "dish", "disharmony", "dishonesty", "dishonor", "dishwater", "disillusionment", "disinclination", "disintegration", "disinterest", "disk", "dislike", "dislocation", "disloyalty", "dismay", "dismemberment", "dismissal", "disobedience", "disorder", "disorganization", "disparagement", "disparity", "dispatch", "dispensary", "dispensation", "dispenser", "dispersal", "dispersement", "dispersion", "displacement", "display", "displeasure", "disposal", "disposition", "dispossession", "dispute", "disquiet", "disquietude", "disregard", "disrepair", "disrepute", "disrespect", "disruption", "dissatisfaction", "dissection", "dissemination", "dissension", "dissent", "dissenter", "disservice", "dissimulation", "dissociation", "dissolution", "dissolve", "distance", "distaste", "distension", "distillation", "distiller", "distinction", "distortion", "distraction", "distribution", "distributor", "distributorship", "district", "distrust", "disturbance", "disturber", "disunion", "disunity", "ditch", "ditcher", "ditty", "diva", "divan", "dive", "diver", "divergence", "diversification", "diversion", "diversity", "divertimento", "divestiture", "dividend", "divider", "divination", "divine", "diving", "divinity", "division", "divorce", "divorcee", "dline", "dock", "dockside", "doctor", "doctorate", "doctrinaire", "doctrine", "document", "documentary", "documentation", "dodge", "dog", "doghouse", "dogleg", "dogma", "dogmatism", "dogtrot", "dogwood", "doing", "doll", "dollar", "dollarette", "dolphin", "domain", "dome", "domestic", "domesticity", "domicile", "dominance", "domination", "dominion", "don", "donation", "donkey", "donor", "doom", "doomsday", "door", "doorbell", "doorkeeper", "doorknob", "doorman", "doormen", "doorstep", "doorway", "dope", "dormitory", "dosage", "dose", "dot", "dotting", "double", "doubleheader", "doubloon", "doubt", "doubte", "dough", "dove", "dowel", "dower", "down", "downfall", "downpayment", "downpour", "downtrend", "downturn", "dowry", "dozen", "draft", "draftee", "drafting", "drag", "dragger", "dragnet", "dragon", "drain", "drainage", "draining", "dram", "drama", "dramatist", "dramatization", "draper", "drapery", "draught", "draw", "drawback", "drawbridge", "drawer", "drawing", "drawl", "dread", "dream", "dreamer", "dresser", "dressing", "drier", "drift", "drill", "drilling", "drink", "drinker", "drinking", "drip", "drive", "driver", "driveway", "driving", "drizzle", "dromozoa", "drone", "drop", "drought", "drouth", "drove", "drudgery", "drug", "drugstore", "drum", "drumlin", "drummer", "drunk", "drunkard", "dryer", "drying", "drywall", "dualism", "duck", "duct", "ductwork", "dud", "due", "duel", "duet", "duf", "duffel", "duffer", "dugout", "duke", "dumbbell", "dump", "dumping", "dun", "dune", "dung", "dungeon", "duplicate", "duplication", "durability", "duration", "dusk", "dust", "dustbin", "dusting", "duty", "dwarf", "dweller", "dwelling", "dyerear", "dying", "dynamic", "dynamite", "dynamo", "dynasty", "dysentery", "dysplasia", "dystopia", "dystrophy"], 
					["ice", "icebox", "icicle", "icing", "iconoclasm", "idea", "ideal", "idealism", "idealist", "idealization", "identification", "identity", "ideologist", "ideology", "idiom", "idiot", "idler", "idol", "idolatry", "idyll", "ignition", "ileum", "ill", "illegitimacy", "illumination", "illusion", "illustration", "illustrator", "image", "imagery", "imagination", "imaging", "imagnation", "imbalance", "imbecile", "imbroglio", "imitation", "immaturity", "immediacy", "immensity", "immersion", "immigrant", "immigration", "imminence", "immobility", "immodesty", "immorality", "immortality", "immunity", "immunization", "impact", "impairment", "impartiality", "impasse", "impatience", "impediment", "imperative", "imperfectability", "imperfection", "imperialism", "imperialist", "impersonation", "impiety", "implant", "implement", "implementation", "implication", "import", "importance", "importation", "imposition", "impossibility", "impotence", "impotency", "impresario", "impresser", "impression", "impressionist", "imprimatur", "imprisonment", "impromptu", "impropriety", "improvement", "improvisation", "improviser", "improvising", "impudence", "impulse", "impunity", "impurity", "imputation", "inability", "inaccuracy", "inaction", "inactivation", "inactivity", "inadequacy", "inadvertence", "inaugural", "inauguration", "incantation", "incapacity", "incarnation", "incense", "incentive", "inception", "inceptor", "inch", "incidence", "incident", "incinerator", "incipience", "incipiency", "incitement", "inclination", "incline", "inclusion", "income", "incompatibility", "incompetence", "incomprehension", "incongruity", "inconsistency", "inconvenience", "incorporation", "incorruptibility", "increase", "incredulity", "incubation", "incubi", "inculcation", "incursion", "ind", "indecision", "indefinite", "indefinity", "indemnity", "indenture", "independence", "index", "indexing", "indication", "indicator", "indictment", "indifference", "indigation", "indigestion", "indignation", "indirection", "indisposition", "indium", "individual", "individualism", "individualist", "individuality", "individuation", "indivisibility", "indoctrinating", "indoctrination", "indolence", "inducement", "induction", "indulgence", "industralization", "industrialism", "industrialist", "industrialization", "industry", "inefficiency", "inequality", "inertia", "inevitability", "inexperience", "infamy", "infancy", "infant", "infantry", "infantryman", "infantrymen", "infarct", "infarction", "infatuation", "infection", "inference", "inferiority", "inferno", "infestation", "infidelity", "infield", "infighting", "infiltration", "infinite", "infinitive", "infinity", "infirmary", "infirmity", "inflammation", "inflation", "inflection", "infliction", "inflow", "influence", "influent", "influenza", "influx", "informality", "informant", "information", "infraction", "infrared", "infringement", "infuriation", "infusion", "ingenuity", "ingestion", "ingratitoode", "ingratitude", "ingredient", "inhabitation", "inhalation", "inheritance", "inhibition", "inhibitor", "initiation", "initiative", "initiator", "injection", "injunction", "injury", "injustice", "ink", "inkling", "inlet", "inmate", "inn", "inning", "innocence", "innovation", "innuendo", "inoculation", "inpost", "input", "inquest", "inquiry", "inquisitor", "insanity", "inscription", "inscrutability", "insect", "insecticide", "insecurity", "insemination", "insert", "insertion", "inset", "inside", "insight", "insignificance", "insinuation", "insistence", "insolence", "insomnia", "insouciance", "inspection", "inspector", "inspiration", "instability", "installation", "installment", "instance", "instancy", "instant", "instigation", "instigator", "instillation", "instinct", "institute", "institution", "institutionalization", "instruction", "instructor", "instrument", "instrumentation", "insubordination", "insularity", "insulation", "insulator", "insulin", "insult", "insurance", "insurgence", "insurrection", "intake", "integer", "integration", "integrity", "intellect", "intellectual", "intellectuality", "intelligence", "intelligentsia", "intemperance", "intendant", "intensification", "intensifier", "intensity", "intent", "intention", "interaction", "intercept", "interceptor", "interchange", "intercourse", "interdependence", "intereference", "interest", "interface", "interference", "interferometer", "interim", "interior", "interlining", "interlocutor", "interlude", "intermarriage", "interment", "intermission", "intern", "international", "interne", "interplay", "interpolation", "interposition", "interpretation", "interpreter", "interpretor", "interregnum", "interrelation", "interrelationship", "interrogation", "interrogator", "interruption", "intersection", "interval", "intervention", "interview", "interviewee", "interviewer", "interviewing", "intestine", "intima", "intimacy", "intimate", "intimidation", "intolerance", "intonation", "intransigence", "intrigue", "introduction", "introject", "introspection", "intruder", "intrusion", "intuition", "invader", "invalid", "invalidism", "invasion", "invention", "inventor", "inventory", "inverse", "inversion", "investigation", "investigator", "investment", "investor", "invigoration", "inviolability", "invitation", "invite", "invocation", "involution", "involvement", "invulnerability", "iodide", "iodination", "iodine", "iodoamino", "iodoprotein", "ion", "ionosphere", "iota", "ire", "iridium", "iron", "irony", "irradiation", "irrationality", "irredentism", "irregularity", "irreproducibility", "irresolution", "irresponsibility", "irreverence", "irrigation", "irritability", "irritant", "irritation", "irsac", "island", "isle", "isocyanate", "isolation", "isolationism", "issuance", "issue", "itch", "item", "itemization", "itinerary", "ity", "ivory", "ivy"], 
					["no", "nab", "nadir", "naebm", "nagging", "nahb", "nail", "nair", "nairo", "naivete", "name", "namesake", "naming", "nap", "napkin", "narcotic", "nareb", "narration", "narrative", "narrator", "narrowing", "nation", "national", "nationalism", "nationalist", "nationality", "nationhood", "native", "nato", "naturalism", "naturalist", "nature", "naturopath", "nausea", "navel", "navigation", "navigator", "navy", "nebula", "necessity", "neck", "necklace", "neckline", "necktie", "necropsy", "nectar", "need", "needle", "negation", "negative", "negativism", "neglect", "negligence", "negotiation", "neighbor", "neighborhood", "neighbourhood", "neocortex", "neon", "nephew", "nerve", "nest", "nester", "nestling", "net", "network", "neuralgia", "neurasthenic", "neurologist", "neuron", "neuropathology", "neurotic", "neutralism", "neutralist", "neutrality", "neutralization", "neutron", "newcomer", "newel", "newlywed", "newsboy", "newsletter", "newsman", "newsmen", "newspaper", "newspaperman", "newspapermen", "newsreel", "newsstand", "newt", "niche", "nickel", "nickname", "niece", "night", "nightclub", "nightfall", "nightingale", "nightmare", "nightshirt", "nihilism", "nihilist", "nil", "nip", "nirvana", "nitrate", "nitrogen", "nitroglycerine", "nobility", "nobleman", "noblesse", "nod", "noise", "nomenclature", "nomination", "nominee", "nonce", "noncompliance", "nonconformist", "nondefeatist", "nondriver", "nonequivalence", "nonfiction", "nonfood", "nonism", "nonoccurrence", "nonogenarian", "nonpayment", "nonreactivity", "nonsense", "nonstop", "noon", "noontime", "noose", "nop", "norad", "noradrenalin", "norethandrolone", "norm", "normalcy", "north", "northerner", "nose", "nosebag", "nosebleed", "nostalgia", "nostril", "notation", "notch", "note", "notebook", "notice", "notification", "notion", "notoriety", "noun", "nourishment", "novel", "novelist", "novelty", "novice", "novitiate", "nowhere", "nozzle", "nuance", "nuclei", "nucleoli", "nucleotide", "nuclide", "nudge", "nudism", "nudist", "nudity", "nugget", "nuisance", "null", "nullity", "number", "numbering", "numerology", "nun", "nurse", "nursery", "nurture", "nut", "nutmeg", "nutrition", "nutshell", "nux", "nylon", "nymph", "nymphomaniac"], 
					["kids", "kale", "kangaroo", "koala", "kaleidescope", "kaleidoscope", "karl", "kava", "kazoo", "kebob", "kedgeree", "keel", "keelson", "keening", "keep", "keeper", "keeping", "keg", "kegful", "kelp", "ken", "kenning", "keno", "kerchief", "kernel", "kerosene", "kerygma", "ketchup", "kettle", "key", "keyboard", "keyboarding", "keyhole", "keynote", "khan", "kibbutzim", "kick", "kicking", "kickoff", "kid", "kidding", "kidnaper", "kidnapper", "kidney", "kill", "killer", "killing", "kilometer", "kiloton", "kilowatt", "kimono", "kin", "kind", "kindergarten", "kindred", "king", "kingdom", "kingpin", "kinship", "kiosk", "kit", "kitchen", "kitchenette", "kite", "kitten", "klaxon", "knack", "knackwurst", "knee", "kneecap", "knife", "knight", "knob", "knock", "knockdown", "knocking", "knoll", "knot", "knott", "know", "knowledge", "knuckle", "knuckleball", "kob", "kola", "konga", "kqed", "kraft", "kraut"]]

letter_emojis = [":regional_indicator_d:", ":regional_indicator_i:", ":regional_indicator_n:", ":regional_indicator_k:"]

# generates dink string
def find_dink(dictionary, letter_emojis):
    dink_string = ""
    for i in range(0, 4): 
        line = letter_emojis[i]
        # finds random word in dictionary
        line += dictionary[i][random.randrange(0, len(dictionary[i]))]
        line += "\n"
        dink_string += line
    return dink_string

# so bot can see all members 
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):

    
    # we do not want the bot to reply to itself and other bots
    if message.author.bot: 
        return

    # dinkbot is playing ... 
    await client.change_presence(activity=discord.Game(name='d!info'))

    ################# COMMAND BASED FEATURES START HERE #################

    if message.content.startswith(PREFIX):
        command = message.content[len(PREFIX):].split()[0]

        try: 
          command_2 = message.content[len(PREFIX):].split()[1]
        except: 
          command_2 = ""

        # help
        if command == 'info' or command == 'help' or command == 'commands':
            msg = 'd!hello \nd!info \nd!random \nd!dink <user> (use exact discord name, not nickname)\nd!doink <user>\nd!special <user>\nd!big \nd!face\nd!face2\nd!nsfw\n\n made by Destiny \nhttps://destiny-02.github.io/index.html'
            embed_msg = discord.Embed(title="List of commands", description=msg, color=0x852d49)
            await message.channel.send(embed = embed_msg)

        # big
        if command == 'big':
            msg = ':regional_indicator_d::regional_indicator_i::regional_indicator_n::regional_indicator_k:'
            await message.channel.send(msg)

        # face
        if command == 'face':
            msg = ':eyes:'
            bot_msg = await message.channel.send(msg)
            await bot_msg.add_reaction('\U0001f445')

        # face2
        if command == 'face2':
            msg = ':eyes:'
            bot_msg = await message.channel.send(msg)
            await bot_msg.add_reaction('\U0001f444')

        # nsfw >:3
        if command == 'nsfw':
            msg = ':eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n:eyes:\n:tongue:\n'
            await message.channel.send(msg)

        # hello
        if command == 'hello':
            msg = 'Hello {0.author.mention}'.format(message)
            await message.channel.send(msg)

        # dink @user
        if command == 'dink':
            try:
                user = discord.utils.get(client.get_all_members(), name=command_2).id
            except AttributeError:
                return 
            msg = 'You dinked <@!{}>'.format(user)
            await message.channel.send(msg)

        # doink @user
        if command == 'doink':
            try:
                user = discord.utils.get(client.get_all_members(), name=command_2).id
            except AttributeError:
                return
            msg = 'You doinked <@!{}>'.format(user)
            await message.channel.send(msg)

        # special dink @user
        if command == 'special':
            try:
                user = discord.utils.get(client.get_all_members(), name=command_2).id
            except AttributeError:
                return
            msg = 'You :sparkles: special dinked :sparkles: <@!{}>'.format(user)
            await message.channel.send(msg)

        # random dink
        if command == 'random':
            msg = find_dink(dictionary, letter_emojis)
            embed_msg = discord.Embed(title="dink stands for...", description=msg, color=0x852d49)
            await message.channel.send(embed = embed_msg)

    
    #################### NON-COMMAND FEATURES START HERE #######################
    
    # tongue react on any eyes
    if message.content.startswith(emoji.emojize(':eyes:')):
        await message.add_reaction('\U0001f445')

    # i'm
    if message.content.lower().startswith('im '): 
        msg = "Hi {} I'm dinkbot!".format(message.content[3:])
        await message.channel.send(msg)

    if message.content.lower().startswith('i am '): 
        msg = "Hi {} I'm dinkbot!".format(message.content[5:])
        await message.channel.send(msg)

    if message.content.lower().startswith('i\'m '): 
        msg = "Hi {} I'm dinkbot!".format(message.content[4:])
        await message.channel.send(msg)

    # hello / hi
    if message.content.lower().startswith('hello'):
        msg = "hello"
        await message.channel.send(msg)

    if message.content.lower().startswith('hi'):
        msg = "hi"
        await message.channel.send(msg)

    # dink
    if message.content.lower() == "dink":
        await message.channel.send(":tongue:***__DINK__***:tongue:")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


keep_alive()
client.run(TOKEN)
