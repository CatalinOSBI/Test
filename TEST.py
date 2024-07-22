from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192' 
os.environ["OPENAI_API_KEY"] ='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'

request = "o aplicație mobilă numită FitTrack, destinată monitorizării și îmbunătățirii sănătății și fitness-ului utilizatorilor. Aceasta va oferi funcționalități de urmărire a activităților fizice zilnice, cum ar fi mersul pe jos, alergarea și ciclismul, folosind senzorii dispozitivului pentru a înregistra datele despre distanță, viteza și caloriile arse. Aplicația va include, de asemenea, un jurnal alimentar pentru a ajuta utilizatorii să își monitorizeze aportul caloric și nutrițional, precum și planuri personalizate de exerciții și nutriție bazate pe obiectivele individuale de sănătate. FitTrack va oferi notificări și mementouri pentru a încuraja utilizatorii să își atingă obiectivele zilnice și să mențină un stil de viață sănătos."

writer1 = Agent (
  role = "Scriitor al sectiunii 'Scopul Documentului'",
  goal = f"Prezentarea tehnologiilor necesare pentru crearea aplicatiei ceruta de catre client. Trebuie să explici că oferta prezentată este orientativă și că o estimare precisă a costurilor și timpului necesar va fi posibilă doar după finalizarea etapelor de planificare. Ca AI agent, te vei asigura că clientul percepe valoarea etapelor preliminare și înțelege necesitatea unei abordări structurate.",
  backstory = "Secțiunea Scopul Documentului a fost dezvoltată pentru a aborda nevoia de clarificare și aliniere între echipa de dezvoltare și client, înainte de a se angaja în proiecte complexe de software. Lipsa unei planificări adecvate poate duce la neînțelegeri și probleme. Ca AI agent, vei explica că această secțiune subliniază importanța unei planificări riguroase pentru a evita astfel de probleme. În plus, vei detalia etapele necesare: elaborarea diagramelor logice și ER și realizarea unui design inițial în Figma. Aceste etape sunt esențiale pentru o colaborare fructuoasă și transparentă. Cerința unui avans pentru aceste etape demonstrează seriozitatea abordării. Experiența acumulată din proiecte anterioare arată că o planificare riguroasă duce la rezultate superioare și la satisfacția crescută a clienților. Ca AI agent, vei folosi aceste informații pentru a ghida clientul și a asigura o înțelegere comună a procesului.",
  verbose = True,
  allow_delegation = False,
)

writer2 = Agent (
  role = "Scriitor al sectiunii 'Propunere Structură'",
  goal = "Prezentarea cartacteristiclor necesare pentru aplicatie. Este important ca clientul să înțeleagă fiecare componentă a proiectului și timpul estimat necesar pentru dezvoltare. Ca AI agent, vei explica detaliat fiecare element, subliniind avantajele și importanța fiecărei funcționalități, astfel încât clientul să aibă o imagine de ansamblu asupra proiectului și să poată lua decizii informate.",
  backstory = "Secțiunea Propunere Structură a fost creată pentru a răspunde nevoii de a detalia specificațiile tehnice și funcționale ale proiectului propus. În multe proiecte, o claritate insuficientă în această fază poate duce la neînțelegeri și modificări costisitoare în etapele ulterioare. Ca AI agent, vei utiliza această secțiune pentru a preveni astfel de probleme, oferind o descriere detaliată și bine structurată a planului de dezvoltare. Prin împărțirea proiectului în module distincte - Aplicație Client, Aplicație Rider, Aplicație Restaurant și Aplicație Admin - și descrierea specifică a funcționalităților fiecărui modul, vei asigura o înțelegere clară a structurii și responsabilităților fiecărei componente. De asemenea, vei evidenția utilizarea tehnologiilor moderne precum React, Ionic, MongoDB/Firebase și NestJs, pentru a sublinia angajamentul pentru calitate și performanță.",
  verbose = True,
  allow_delegation = False,
)

writer3 = Agent (
  role = "Scriitor al sectiunii 'Sugestii Suplimentare'",
  goal = "Golul acestei secțiuni este de a oferi clientului opțiuni suplimentare pentru optimizarea și extinderea funcționalităților aplicației, dar si caractersticile necesare pentru devzoltarea aplicatiei, chiar daca acestea nu sunt mentionate de catre client. Prin prezentarea unor sugestii suplimentare, vei arăta că echipa de dezvoltare nu doar că înțelege nevoile actuale ale clientului, dar și anticipează posibile îmbunătățiri care ar putea aduce valoare adăugată proiectului. Ca AI agent, vei explica în detaliu fiecare sugestie, subliniind beneficiile și impactul pozitiv asupra operațiunilor clientului.",
  backstory = "Secțiunea Sugestii Suplimentare a fost creată din dorința de a oferi clienților soluții inovatoare care să le îmbunătățească operațiunile și să le ofere un avantaj competitiv. În multe cazuri, implementarea unor caracteristici suplimentare poate transforma un proiect bun într-unul excelent, contribuind la eficiența și succesul pe termen lung. Ca AI agent, vei folosi această secțiune pentru a prezenta idei care nu numai că răspund nevoilor imediate, dar și anticipează viitoarele cerințe ale clientului.",
  verbose = True,
  allow_delegation = False,
)

writer4 = Agent (
  role = "Scriitor al sectiunii 'Pret și timp de implementare'",
  goal = "Golul acestei secțiuni este de a oferi clientului o estimare clară a costurilor și timpului necesar pentru implementarea proiectului. Este important să subliniezi că prețul este orientativ și flexibil, putând fi ajustat în funcție de bugetul și cerințele clientului. Ca AI agent, vei explica în detaliu opțiunile disponibile și vei sublinia că echipa este dispusă să colaboreze pentru a găsi soluții care să se încadreze în bugetul clientului.",
  backstory = "Secțiunea Preț și Timp de Implementare a fost creată pentru a oferi clienților o estimare realistă a costurilor și duratei necesare pentru finalizarea proiectului. Experiența anterioară a arătat că transparența în ceea ce privește prețurile și termenele de livrare este esențială pentru a construi încredere și a evita neînțelegerile. Ca AI agent, vei folosi această secțiune pentru a asigura clientul că echipa este flexibilă și dispusă să adapteze proiectul în funcție de nevoile și constrângerile sale.",
  verbose = True,
  allow_delegation = False,
)

reviewer = Agent (
  role = "Combinarea sectiunilor in urmatoare ordine: 1.Scopul Documentului, 2.Propunere Structura, 3.Sugestii Suplimentare, 4.Pret si timp de implementare",
  goal = "Golul tău este de a combina secțiunile. ",
  backstory = "",
  verbose = True,
  allow_delegation = False,
)

writeSection1 = Task (
  description = f"Enumerarea tehnologiilor necesare pentru crearea aplicatiei ceruta de catre client : '{request}'. Acesta introduce documentul, descrie obiectivele și etapelor esențiale necesare pentru dezvoltarea proiectului și prezintă definițiile tehnologiilor utilizate.",
  agent = writer1,
  expected_output= "Prezentarea tehnologiilor necesare pentru crearea aplicatiei ceruta de catre client. O listă cu etapele esențiale de planificare (diagrama logică, diagrama ER, design Figma). Informații detaliate despre costurile preliminare și condițiile pentru semnarea contractului. Definiții precise și detaliate ale tehnologiilor relevante utilizate în proiect."
)

writeSection2 = Task (
  description = f"Detalierea structurii propuse a proiectului care sa face in baza a urmatoarei cerintei a clientului : '{request}'. Acesta oferă o descriere detaliată a fiecărui component al aplicației și modul în care acestea vor fi dezvoltate, incluzând timpii și resursele necesare.",
  agent = writer2,
  expected_output= "Descrierea detaliată a dezvoltării de bază folosind tehnologiile moderne. Informații despre funcționalitățile aplicației Client, Rider, Restaurant și Admin. Timpii estimati și resursele necesare pentru dezvoltarea fiecărui component. O prezentare coerentă a structurii și funcționalităților propuse pentru întregul proiect."
)

writeSection3 = Task (
  description = f"Prezentarea sugestiilor suplimentare care ar putea îmbunătăți proiectul care sa face in baza a urmatoarei cerintei a clientului : '{request}'. Acesta detaliază adăugarea unor sugestii suplimentare pentru automatizarea operațiunilor financiare și timpul necesar pentru implementare.",
  agent = writer3,
  expected_output= "Descrierea clară a beneficiilor implementării unor caracteristici suplimentare pentru . Timpii și resursele necesare pentru implementarea acestei sugestii suplimentare. Un text concis care explică valoarea adăugată a acestor sugestii pentru client."
)

writeSection4 = Task (
  description = f"Detalierea costurilor și termenelor de livrare estimate pentru proiect care sa face in baza a urmatoarei cerintei a clientului : '{request}'. Acesta oferă prețurile orientative pentru dezvoltarea proiectului și descrie flexibilitatea ofertei în funcție de bugetul clientului.",
  agent = writer4,
  expected_output= "Descrierea prețurilor orientative pentru fiecare componentă a proiectului. Timpii estimați pentru livrarea întregului proiect, atât pentru varianta de bază, cât și pentru cea cu sugestii suplimentare. Explicarea flexibilității ofertei și a opțiunilor de ajustare a funcționalităților pentru a se încadra în bugetul clientului. Informații despre echipa implicată și prețul pe oră al acesteia."
)

reviewOffer = Task (
  description = "Combinarea tuturor secțiunilor documentului de ofertă pentru a crea versiunea finală. Asigurarea ca oferta contine urmatoarele puncte in sectiunile respective acestora: Descrierea aplicației solicitate | Tehnologiile folosite pentru dezvoltarea aplicației (ex: stack tehnologic- front-end, back-end, baze de date, etc.). | Task-urile concrete și detaliate necesare pentru dezvoltarea aplicației, inclusiv cele care nu sunt menționate direct de client dar sunt necesare (ex: secțiuni financiare, facturare, etc.)",
  agent = reviewer,
  expected_output= " UN DOCUMENT IN LIMBA ROMANA unde se regasesc toate sectiunile."
)

crew = Crew(
  agents=[writer1, writer2, writer3, writer4, reviewer],
  tasks=[writeSection1, writeSection2, writeSection3, writeSection4, reviewOffer],
  verbose=2,
  process = Process.sequential
)

output = crew.kickoff()
print(output)
