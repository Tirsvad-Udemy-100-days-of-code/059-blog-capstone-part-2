[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

## Krav

- Python 3.13 eller nyere
- Git
- Doxygen (valgfrit, kun til API-dokumentationen)

## Opret og brug et lokalt virtuelt miljø

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

På Linux og macOS bruges `python3 -m venv .venv` og `source .venv/bin/activate`. Forlad miljøet med `deactivate`.

## Kør sitet

```bash
python -m blog.main
```

Åbn <http://127.0.0.1:5000>. Indlæggene kommer fra endpointet i `src/blog/constants.py`; kan det ikke nås, bruges den kopi, der følger med pakken.

## Kør testene

```bash
python -m pytest
```

Testene bruger aldrig netværket. Byg kodedokumentationen med `doxygen Doxyfile`.

## Hvad vi har lært

- En gentagelig opsætning: et virtuelt miljø, `pip` opdateret og projektet installeret i redigerbar tilstand.
- Én kommando til at køre sitet og én til at køre testene, begge beskrevet i README.
