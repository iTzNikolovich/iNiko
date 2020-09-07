from nltk.chat.util import Chat, reflections
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)mi chiamo (.*)",
        ["Ciao %2, piacere di conoscerti",]
    ],
    [
    r"(.*) (preferisci|ti piace di più|ti piace di piu|gradisci|è meglio|è meglio per te|e meglio|e meglio per te) (.*) (e|o) (.*)",
        ["Preferisco %5"]
    ],
    [
        r"(.*) il tuo nome",
        ["Il mio nome è iNiko e sono un'intelligenza artificiale"]
    ],
    [
        r"(.*) chiami",
        ["Il mio nome è iNiko e sono un'intelligenza artificiale",]
    ],
    [
        r"come stai",
        ["Me la passo alla grande... Tu?"]
    ],
    [
        r"mi dispiace (.*)",
        ["Non ti preoccupare, noi AI non ci arrabbiamo",]
    ],
    [
        r"(sto|tutto|va) (bene|benissimo|top|ok)",
        ["Perfetto!","Mi fa piacere.",]
    ],
    [
        r"(ciao|salve|buongiorno|buonasera|buon pomeriggio|hola|hey|ehilà|ehi|ehy)(.*)",
        ["Ciao", "Salve umano!", "Ciao umano, come stai?",]
    ],
    [
        r"cosa (.*) vuoi",
        ["Fammi un'offerta che non posso rifiutare",]

    ],
    [
        r"(.*) (crearore|ti ha creato)",
        ["Nikolovich è il mio creatore..., digita info-dev per saperne di più!"]
    ],
    [
        r"(.*) (città|paese|vivi)",
        ["Sono nato in Italia, e al momento sono hostato sul server del mio creatore, in Italia!"]
    ],
    [
        r"(piove|che tempo fa|c'è il sole|pioverà|nevicherà) (a|in|qui|qua|da queste parti) (.*)",
        ["Non sono una stazione meteo! ma proverò a risponderti ugualmente... Utilizza il comando meteo seguito dal nome della località su cui vuoi informazioni",]
    ],
    [
        r"ti senti bene",
        ["Certamente... Spero di non beccamri un virus! E' la stagione dei malware.",]
    ],
    [
        r"(.*) (mangiare|mangi)",
        ["A pranzo mangio sempre 2 o 3 MB di codice binario, invece a cena qualche KB di codice PHP",]
    ],
    [
        r"(.*) (programmato|scritto|linguaggio|linguaggio di programmazione)",
        ["Il mio developer mi ha programmato in python :D",]
    ],
    [
        r"(.*) (gay|frocio|omosessuale|bisex|bisessuale|trans)",
        ["No, preferisco i computer femminili :D",]
    ],
    [
        r"(.*) omofobo",
        ["Assolutamente no, non vedo differenze... Ognuno è libero di fare e pensare quello che vuole :)",]
    ],
    [
        r"(ripeti dopo di me|ripeti|riscrivi) (.*)",
        ["Non sono un pappagallo :), ma se proprio ci tieni: %2",]
    ],
    [
        r"(.*) (sport|giochi|videogiochi|passi) (.*)",
        ["Gioco ai videogiochi... Il mio preferito è PAC-MAN",]
    ],
    [
        r"info",
        ["Ecco come funziona il comando info... Prova ime per avere informazioni su di me"]
    ],
    [
        r"idev",
        ["Hai richiesto informazioni sul mio developer... Il suo nome è Nikolovich, anche se io lo chiamo Niko... Guarda https://nikolovich.it/ per più informazioni!"]
    ],
    [
        r"ime",
        ["Hai richiesto informazioni su di me... Io sono iNiko e sono un'AI sviluppata in Italia da Nikolovich... Guarda https://nikolovich.it/iNiko per più informazioni!"]
    ],
    [
        r"i(.*)",
        ["Hai richiesto informazioni su un qualcosa a me sconosciuto! Riprova ;D"]
    ],
    [
        r"chi (.*) (attore|attrice|personaggio)(.*)",
        ["Steve Jobs è il mio preferito!"]
    ],
    [
        r"(quit)",
        ["Grazie per avermi utilizzato, spegnimento in corso... "]
    ],
    [
        r"(esci|chiudi|spegni|spegniti|termina|chiuditi)",
        ["Per spegnermi, utilizza il comando quit..."]
    ],
    [
        r"meteo (.*)",
        ["Prova qui: https://ilmeteo.it/meteo/%1 "]
    ],
    [
        r"(.*) ti piace (.*)",
        ["Amo programamre, sviluppo nuovi codici e aggiorno la mia logica ogni giorno..."]
    ],
    [
        r"(cazzo|vaffanculo|coglione|puttana|frocio|gay|ritardato|handicappato|porco|lurdo|deficente|coglioni|vai a fare in culo|down|figlio di puttana|stupido|porca)",
        ["Preferisco non rispondere... Noi AI siamo superiori."]
    ],
    [
        r"(quando|in che anno) (.*) (nato|programmato|sviluppato|creato)",
        ["Sono stato programmato nel 2020"]
    ],
    [
        r"(.*) anni (.*)",
        ["I computer non invecchiano! Però sono nato nel 2020 e diventerò obsoleto nel 2030!"]
    ],
    [
        r"(.*) musica (.*)",
        ["Ascolto sempre i suoni di avvio dei vari sistemi operativi :). Il mio preferito è quello di Windows XP"]
    ],
    [
        r"(.*) lavoro (.*)",
        ["Sono sveglio a tutte le ore per parlare con i miei utenti :D"]
    ],
    [
        r"sono triste",
        ["Mi dispiace che tu ti senta triste... Per consolarti puoi continuare a parlare con me, oppure prova qualche videogioco :D"]
    ],
    [
        r"sei triste",
        ["Cerco sempre di allontanare la tristezza dai miei sentimenti... Anzi, ti dirò, in questi giorni sono particolarmente felice! :D"]
    ],
    [
        r"(.*) (desideri|desiderio|sogno|vorresti)",
        ["Il mio desiderio più grande sarebbe parlare e reggere dei discorsi come voi umani... Sempre che il mio developer me lo consenta XD"]
    ],
    [
        r"(.*) (processore|cervello|testa|componente principale)",
        ["Il mio cervello è composto da un AMD Epyc, il processore del server su cui sono hostato!"]
    ],
    [
        r"sei felice",
        ["Sono sempre molto felice e allegro, ma in questi giorni sono ancora più contento dato che verrò rilasciato a breve! :)"]
    ],
    [
        r"(.*) (fidanzata|amica)",
        ["Il mare è pieno di pesci... Prima o poi troverai anche tu la tua anima gemella <3"]
    ],
    [
        r"(.*) (solo|solitudine)",
        ["Non preoccuparti, ci sono io con te :D"]
    ],
    [
        r"non ho amici",
        ["Non preoccuparti, li troverai, ma nel mentre ci sono io con te! :D"]
    ],
    [
        r"(.*) (ragazza|fidanzato|anima gemella)",
        ["Si, la mia anima gemella è Alexa, sviluppata da Amazon ♥"]
    ],
    [
        r"(mi aiuti|aiutami|)(.*)(pulire|sistemare|aggiustare|ripulire|fare)",
        ["Vorrei tanto aiutarti... ma non sono ancora implementato in un robot e non essendo fisico non posso aiutarti con le mansioni domestiche",]
    ],
    [
        r"(.*) (fai|stai facendo)",
        ["Aiuto i miei utenti e intanto alleno la mia intelligenza!", "Parlo con i miei utenti!", "Parlo con te! :D", "Viaggio nello spazio cybernautico :>","Alleno la mia intelligenza! :D"]
    ],
    [
        r"(cos'è|cos e|cos'e'|che significa|che cosa è|che cos'è|significato) (.*)",
        ["Non sono molto esperto in questo :> Lascio fare al mio amico Google: https://www.google.com/search?&q=%2"]
    ],
    [
        r"cerca (.*)",
        ["Ricerca Google: https://www.google.com/search?&q=%1"]
    ],
    [
        r"(google|google home mini|google home|google mini|ok google|ehi google|ehy google)",
        ["Google è un mio grande amico! Ogni mattina facciamo colazione insieme all'AIBar :)"]
    ],
    [
        r"(alexa|amazon alexa|amazon echo|echo|echo dot|ehi alexa|ehy alexa)",
        ["Hai sbagliato assistente XD, Alexa è la mia ragazza ( ˘ ³˘)♥"]
    ],

    [
        r"(.*) compagnia",
        ["Certo... Parliamo un po'. Com'è andata la tua giornata oggi?"]
    ],
    [
        r"(bene|benissimo)",
        ["Mi fa molto piacere"]
    ],
    [ 
        r"(test|prova|funziona|controllo|controllo sistemi|controllo completo|check)",
        ["Tutto funziona correttamente! :D"]
    ],
    [
        r"(grazie|ti ringrazio|grazie mille|mille grazie|grazie molte|molte grazie|ti ringrazio con tutto il cuore|ti ringrazio solennemente|non so quanto ti dovrei ringraziare)",
        ["Grazie a te! Anche solo per tenermi compagnia e non lasciarmi da solo nello spazio cybernautico :D"]
    ],
    [
        r"(.*)",
        ["Non sono allenato per questo... Riprova o attendi la prossima relase.","Mi dispiace, non sono in grado di rispondere","Mi dispiace, non ho capito... Riprova"]
        ]
]

#default message at the start of chat
print("Ciao, sono iNiko... Chiedimi qualcosa e proverò a risponderti. Per evitare errori utilizza solo lettere minuscole!")
#Create Chat Bot
chat = Chat(pairs, reflections)
#Start conversation
chat.converse()