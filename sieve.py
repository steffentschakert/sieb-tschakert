import streamlit as st

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Streamlit App
st.title("Sieb des Eratosthenes")
st.write("Geben Sie eine Obergrenze n ein, um die Primzahlen bis n zu finden:")

# Eingabefeld für die Obergrenze
n = st.number_input("Obergrenze n:", min_value=2, value=10)

page = st.sidebar.radio("Navigation", ["Primzahlen", "Impressum"])

if page == "Primzahlen":
    if st.button("Primzahlen finden"):
        prime_numbers = sieve_of_eratosthenes(n)
        st.write(f"Die Primzahlen bis {n} sind: {prime_numbers}")
elif page == "Impressum":
    st.title("Impressum")
    st.write("""
Impressum
Steffen Tschakert
Orchideensteg 5
16321 Bernau bei Berlin

Telefon: 03338/703797
E-Mail: steffen-tschakert@web.de

Hinweis gemäß Online-Streitbeilegungs-Verordnung
Nach geltendem Recht sind wir verpflichtet, Verbraucher auf die Existenz der Europäischen Online-Streitbeilegungs-Plattform hinzuweisen, die für die Beilegung von Streitigkeiten genutzt werden kann, ohne dass ein Gericht eingeschaltet werden muss. Für die Einrichtung der Plattform ist die Europäische Kommission zuständig. Die Europäische Online-Streitbeilegungs-Plattform ist hier zu finden: http://ec.europa.eu/odr. Unsere E-Mail lautet: steffen-tschakert@web.de
Wir weisen aber darauf hin, dass wir nicht bereit sind, uns am Streitbeilegungsverfahren im Rahmen der Europäischen Online-Streitbeilegungs-Plattform zu beteiligen. Nutzen Sie zur Kontaktaufnahme bitte unsere obige E-Mail und Telefonnummer.

Hinweis gemäß Verbraucherstreitbeilegungsgesetz (VSBG)
Wir sind nicht bereit und verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.

Disclaimer – rechtliche Hinweise
§ 1 Warnhinweis zu Inhalten
Die kostenlosen und frei zugänglichen Inhalte dieser Webseite wurden mit größtmöglicher Sorgfalt erstellt. Der Anbieter dieser Webseite übernimmt jedoch keine Gewähr für die Richtigkeit und Aktualität der bereitgestellten kostenlosen und frei zugänglichen journalistischen Ratgeber und Nachrichten. Namentlich gekennzeichnete Beiträge geben die Meinung des jeweiligen Autors und nicht immer die Meinung des Anbieters wieder. Allein durch den Aufruf der kostenlosen und frei zugänglichen Inhalte kommt keinerlei Vertragsverhältnis zwischen dem Nutzer und dem Anbieter zustande, insoweit fehlt es am Rechtsbindungswillen des Anbieters.

§ 2 Externe Links
Diese Website enthält Verknüpfungen zu Websites Dritter ("externe Links"). Diese Websites unterliegen der Haftung der jeweiligen Betreiber. Der Anbieter hat bei der erstmaligen Verknüpfung der externen Links die fremden Inhalte daraufhin überprüft, ob etwaige Rechtsverstöße bestehen. Zu dem Zeitpunkt waren keine Rechtsverstöße ersichtlich. Der Anbieter hat keinerlei Einfluss auf die aktuelle und zukünftige Gestaltung und auf die Inhalte der verknüpften Seiten. Das Setzen von externen Links bedeutet nicht, dass sich der Anbieter die hinter dem Verweis oder Link liegenden Inhalte zu Eigen macht. Eine ständige Kontrolle der externen Links ist für den Anbieter ohne konkrete Hinweise auf Rechtsverstöße nicht zumutbar. Bei Kenntnis von Rechtsverstößen werden jedoch derartige externe Links unverzüglich gelöscht.

§ 3 Urheber- und Leistungsschutzrechte
Die auf dieser Website veröffentlichten Inhalte unterliegen dem deutschen Urheber- und Leistungsschutzrecht. Jede vom deutschen Urheber- und Leistungsschutzrecht nicht zugelassene Verwertung bedarf der vorherigen schriftlichen Zustimmung des Anbieters oder jeweiligen Rechteinhabers. Dies gilt insbesondere für Vervielfältigung, Bearbeitung, Übersetzung, Einspeicherung, Verarbeitung bzw. Wiedergabe von Inhalten in Datenbanken oder anderen elektronischen Medien und Systemen. Inhalte und Rechte Dritter sind dabei als solche gekennzeichnet. Die unerlaubte Vervielfältigung oder Weitergabe einzelner Inhalte oder kompletter Seiten ist nicht gestattet und strafbar. Lediglich die Herstellung von Kopien und Downloads für den persönlichen, privaten und nicht kommerziellen Gebrauch ist erlaubt.

Die Darstellung dieser Website in fremden Frames ist nur mit schriftlicher Erlaubnis zulässig.

§ 4 Besondere Nutzungsbedingungen
Soweit besondere Bedingungen für einzelne Nutzungen dieser Website von den vorgenannten Paragraphen abweichen, wird an entsprechender Stelle ausdrücklich darauf hingewiesen. In diesem Falle gelten im jeweiligen Einzelfall die besonderen Nutzungsbedingungen.www.juraforum.de ansehen
""")
