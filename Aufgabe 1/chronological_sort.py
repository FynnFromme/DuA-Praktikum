from sys import argv

#? Usage: python sort.py < -heap / -quick > (--test) <filename>


class Entry:
    """Eintrag der zu sortierenden Liste"""

    def __init__(self, line: str):
        # Ursprüngliche Eingabe
        self.line = line

        # Zum Vergleich zweier Einträge
        date, text = line.split(maxsplit=1)
        self.key = ''.join(date.split('.')[::-1]) + text
    
    def __le__(self, other):
        return self.key <= other.key

    def __str__(self):
        return self.line


def get_file_entries(filename: str) -> list:
    # Zeilen aus Datei lesen
    with open(filename, 'r') as f:
        # Zeilen zu Einträgen machen, sofern sie nicht leer sind
        entries = [Entry(line) for line in f if line not in {'', ' ', '\n'}]

    # Zu der letzten Zeile ggf. ein '\n' hinzufügen
    if entries:
        if not entries[-1].line.endswith('\n'):
            entries[-1].line = entries[-1].line + '\n'

    return entries


def ouput_entries(entries: list) -> None:
    # Ausgabe Text erstellen
    output = ''.join(list(map(lambda entry: str(entry), entries)))

    # ggf. \n vom ende entfernen
    if output.endswith('\n'):
        output = output[:-1]
    
    if argv[2] == '--test':
        # Gebe Liste in einer Datei aus
        with open('./tmp.txt', 'w') as f:
            f.write(output)
    else:
        # Gebe Liste in der Konsole aus
        print(output)
        
if __name__=='__main__':
    if len(argv) < 3:
        print('\033[31mUsage: python sort.py < -heap / -quick > (--test) <filename>\033[0m')
        exit()
        
    entries = get_file_entries(argv[-1])

    # Liste sortieren
    if argv[1] == '-heap':
        # Mit heapsort
        from sort.heapsort import heapsort
        heapsort(entries)
    else:
        # Mit quicksort
        from sort.quicksort import randomized_quicksort
        randomized_quicksort(entries, 0, len(entries)-1)

    # Sortierte Einträge ausgeben
    ouput_entries(entries)
