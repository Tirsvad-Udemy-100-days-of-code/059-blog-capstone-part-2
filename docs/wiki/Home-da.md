[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Blog Capstone Part 2 (dag 59)

Denne wiki forklarer projektet fra dag 59 i Udemys "100 Days of Code: The Complete Python Pro Bootcamp": en Flask-blog opgraderet med Start Bootstraps skabelon "Clean Blog". Hvert trin i forelæsningen har en side med et skærmbillede, den vigtigste kode og et afsnit "Hvad vi har lært".

## Hvad du bygger

- Et site med flere sider og en navigationslinje, der tilpasser sig små skærme.
- En header og en footer, der er skrevet én gang og deles med Jinja `include`.
- Blogindlæg hentet fra et JSON-API og vist på forsiden.
- Én side pr. indlæg med et titelbillede i fuld bredde.

## De syv trin

| Trin | Side | Du lærer |
| --- | --- | --- |
| 1 | [Step-1-Template-and-Folders](Step-1-Template-and-Folders-da) | Hvordan et Flask-projekt adskiller `templates` og `static` |
| 2 | [Step-2-Home-Page](Step-2-Home-Page-da) | At levere en side fra en route |
| 3 | [Step-3-Static-Files](Step-3-Static-Files-da) | `url_for('static', ...)` til CSS, JavaScript og billeder |
| 4 | [Step-4-Jinja-Include](Step-4-Jinja-Include-da) | At dele en header og en footer med `include` |
| 5 | [Step-5-About-and-Contact](Step-5-About-and-Contact-da) | Flere routes og links bygget med `url_for` |
| 6 | [Step-6-Posts-from-API](Step-6-Posts-from-API-da) | At læse JSON fra et API og løbe igennem det i Jinja |
| 7 | [Step-7-Single-Post](Step-7-Single-Post-da) | En route med en variabel del og en 404 |

Start med [Getting-Started](Getting-Started-da) for selv at køre sitet.

## Projektet i overblik

Koden følger en let Clean Architecture: `domain` (`Post`), `application` (use cases `get_posts` og `get_post`), `infrastructure` (læsning af API'et) og `presentation` (Flask-routes, templates og statiske filer). Alle konstanter ligger i `src/blog/constants.py`. Flask er den eneste afhængighed ved kørsel.

[Repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2) · [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/issues)
