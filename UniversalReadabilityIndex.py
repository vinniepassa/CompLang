import spacy

# Select language
language = 'en'  # Change to 'it' for Italian

# Load appropriate spaCy model
if language == 'en':
    nlp = spacy.load("en_core_web_sm")
    k = 1.06
    Cp = 4.24
elif language == 'it':
    nlp = spacy.load("it_core_news_sm")
    k = 1.00
    Cp = 4.48
else:
    raise ValueError("Unsupported language")

# Input text
text = "The interminable reiteration of an onto-theological bifurcation—characterized by the obdurate division between the ostensibly autonomous domains of substance and intellection, noumenal alterity and phenomenal immediacy, Being-in-itself and thought-in-relation—constitutes not merely a residual metaphysical scaffolding but a structurally inherited myopia whose conceptual viability has been surreptitiously undermined by the transcendental pivot inaugurated in the Kantian analytic of apperceptive unity, wherein the synthetic activity of the transcendental subject is posited as the precondition for any epistemic comportment toward the world whatsoever, thereby rendering obsolete any naïve presumption of an ontological chasm between knower and known, perceiver and perceived, subject and object. This conceptual obsolescence is not merely an incidental implication of Kant’s critique but rather its central, though often obfuscated, telos, for the very assertion that all representations must be unifiable under the a priori rubric of the “transcendental unity of apperception” implies the radical subsumption of objectivity itself under the synthetically operative horizon of subjectivity—not the empirical ego, to be sure, with its spatiotemporal individuation and contingent predilections, but the formal, self-positing, irreducibly spontaneous condition of possibility for any representational coherence, any horizon of givenness, any manifold of intuition rendered thinkable under the categories legislated by the understanding. Thus, what appears prima facie as a dyadic transaction between a passive receptivity and an active alterity is, under closer scrutiny, nothing more than a phenomenologically disguised unicity, a monism of intelligibility masquerading as a relational duality, for the object qua object, once stripped of its metaphysical pretensions, reveals itself to be but a retrojected artifact of the subject’s legislative function, a residue of reason’s auto-positing activity displaced into an illusory exteriority that no longer withstands critical interrogation. To the extent that this Kantian reframing unseats the ontological priority of object over subject, inaugurating a Copernican inversion in which the world conforms to cognition and not vice versa, it nonetheless leaves room for further radicalization, as manifest in the trajectory of post-Kantian idealisms, wherein Fichte’s Wissenschaftslehre posits the pure I as that which, in positing itself, simultaneously posits its non-I, thereby deriving alterity not as an ontic given but as a moment within the self-articulation of subjectivity—a move which, despite its boldness, arguably collapses into an egoic absolutism insufficiently nuanced to distinguish between transcendental genesis and empirical selfhood, thereby necessitating Schelling’s appeal to a philosophy of identity in which subject and object are no longer opposing poles but moments within an undifferentiated absolute, itself knowable only through intellectual intuition, a position subsequently systematized by Hegel’s speculative dialectic, wherein the identity of identity and difference is realized in the self-mediation of the Concept (Begriff), culminating in an absolute knowing wherein the subject-object dichotomy is aufgehoben not by synthesis but through the immanent auto-development of logical structure itself. However, even this German Idealist culmination, which arguably recapitulates the transcendental insight at an ontologically exhaustive level, may be said to obscure the pre-conceptual horizon of understanding within which such dialectical elaborations become intelligible, a concern articulated with unparalleled hermeneutic subtlety by Heidegger, who, despite his occasional polemics against transcendental subjectivity, in fact retrieves and radicalizes its core insight by disclosing that Dasein, the being for whom Being is an issue, is always already situated in an understanding-of-Being (Seinsverständnis) that precedes all thematic articulation, all theoretical comportment, all subject-object bifurcation, and thus reorients the entire problematic of metaphysics from the question of what is to the question of how Being gives itself to be understood within the finitude of existence, within the thrown-openness of a clearing (Lichtung) that eludes ontic determination yet makes such determination possible. Accordingly, the continued employment of dualistic metaphysical paradigms—whether in the guise of Cartesian internalism, empiricist representationalism, or contemporary neuro-reductionist eliminativism—can be seen as symptomatic of a deeper conceptual inertia, a reluctance to confront the full implications of the transcendental shift, which not only collapses the division between world and mind but also compels a revaluation of what it means for anything to appear, to manifest, to be intelligible in the first place, and it is only by relinquishing this residual dualism that philosophy can begin to address the conditions under which such distinctions emerge, stabilize, and ultimately dissolve within the unfolding horizon of phenomenality itself. Hence, unless philosophical inquiry is willing to reconstitute itself not as the pursuit of a reality presumed to lie beyond appearance but as a genealogical excavation of the very categories through which the distinction between appearance and reality is drawn, it will remain ensnared in the self-generated aporias of its own discursive architecture, forever mistaking the shadows it projects onto the cave wall for the structure of the cave itself, and thereby perpetuating a mythologized account of Being that cannot but falter under the weight of its own unexamined presuppositions."
#text = "È verosimile ritenere che l’uomo, sin dal palesarsi dei primi barlumi di quella autocoscienza che lo contraddistingue nel regno animale, si trovi in uno stato di ricerca perenne di significato nell’apparire del mondo ai sensi. L’autocoscienza di cui l’uomo è dotato implica, con il riconoscimento di altro da sé, anche una naturale tendenza a riconciliarvisi, ossia la volontà di annullare la partizione operata da lui stesso su ciò che ai sensi appare essenzialmente unitario. Questo si traduce nella ricerca dell’uomo del proprio posto nel mondo, una ricerca che conduce l’uomo alla terribile realizzazione di essere limitato dalla morte. La morte, conseguenza necessaria dell’incarnazione, pone apparentemente un limite all’infinita potenzialità dell’essere, e uno degli strumenti di cui l’uomo si è dotato per rifuggire dalla propria limitatezza è l’atto del filosofare. Il passo di Rosenzweig implica che la relazione tra paura della morte e filosofia è il rapporto paradossale di una entità generata (la filosofia) che nega la matrice dalla quale è stata generata (la paura della morte). Attraverso l’esercizio della facoltà di astrazione tipica del filosofare, però, l’uomo non fa altro che esacerbare una già notevole alienazione da se stesso. Nei secoli si sono succeduti filosofi che hanno sostenuto le tesi più disparate: dall’empirismo al razionalismo, dall’idealismo al materialismo, passando per naturalismo, dualismo, monismo. Ciò che accomuna la quasi totalità di questi approcci sono l’elevato livello di astrazione e assunti spesso ingiustificati, persino dogmatici. Operando in questo modo si genera uno strato sempre più denso di concetti senza referenti tangibili, e questo processo induce l’uomo a confondere le proprie astrazioni con ciò che invece gli appare chiaramente ai sensi nel momento presente. Non è possibile rinvenire “io”, “morte”, “realtà”, “sapere” nel dato dell’esperienza, ma certamente non è possibile nemmeno scorgere “scrivania”, “mosca”, “albero”. Il problema da risolvere, infatti, non è la sola assenza di referenti dei concetti filosofici, ma i referenti stessi. Se ci si interfaccia con l’esperienza scevri di qualsivoglia pregiudizio, prima dell’intervento aberrante del pensiero, e della parola sua estensione, appare ovvio che l’esperienza sia integrata, unificata. In quanto integrata e unificata, l’esperienza non concede significato alle proprie parti, l’affermazione dell’esistenza delle quali è un atto di fede. La morte, dunque, collassa in un punto a causa del presentismo integrato sintetizzato dall’esperienza. Ciò rappresenta l’escatologia non solo della morte, ma anche di tutto ciò che fa parte del dominio del discorso, ossia la filosofia e tutti i concetti da essa implicati.In conclusione, il meromorfismo operato dall’uomo sull’uomo come evidenziazione di parti non integrabili cessa di esistere nel momento in cui egli si rende conto che l’esperienza, con la quale egli cerca di riconciliarsi e dalla quale al contempo si separa tramite l’astrazione, non è mai stata in primo luogo null’altro che unificata. La morte in quanto limite dell’uomo, dunque, perde di significato assieme all’uomo stesso, il quale si “ricongiunge” con l’esperienza pur non essendosene mai separato in realtà."

from pdfminer.high_level import extract_text  
#text = extract_text(r"C:\Users\123456789\Desktop\BookRepo\CogSci\The Logical Foundations of Cognition.pdf")

# Process text with spaCy
doc = nlp(text)

# Extract sentences and tokens
sentences = list(doc.sents)
num_sentences = len(sentences)
words = [token.text for token in doc if token.is_alpha]
num_words = len(words)

# Punctuation of interest
target_punct = {".", ",", ";", ":", "!", "?"}
punctuation_count = sum(1 for token in doc if token.text in target_punct)

# Compute metrics
Pf = num_words / num_sentences if num_sentences else 1
Ip = num_words / punctuation_count if punctuation_count else num_words  # Avoid division by 0

# Readability formulas
G = 89 - 10 * k * Cp + (300 / Pf)
Gu = G - (6 * (Ip - 6))

# Convert Gu to FSIQ
mean_Gu = 54.92
std_Gu = 10.01
FSIQ = 100 - 15 * ((Gu - mean_Gu) / std_Gu)

# Output
print(f"Number of words: {num_words}")
print(f"Number of sentences: {num_sentences}")
print(f"Number of interpunction marks: {punctuation_count}")
print(f"Pf (avg words per sentence): {Pf:.2f}")
print(f"Ip (avg words per punctuation): {Ip:.2f}")
print(f"G readability: {G:.2f}")
print(f"Gu adjusted readability: {Gu:.2f}")
print(f"Estimated FSIQ: {FSIQ:.2f}")
