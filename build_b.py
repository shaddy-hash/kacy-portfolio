"""Design B generator. Outputs to ./DesignB/. Run: python3 build_b.py
Images are shared with Design A from ../images/."""
import os, html
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "DesignB")
IMG_DIR = os.path.join(ROOT, "images")
V = "2"

NAME = "Kacy Phillips Hansen"
EMAIL = "kacyhansen70@gmail.com"
PHONE = "720.256.8672"
TEL = "+17202568672"
LINKEDIN = "https://www.linkedin.com/in/kacyphillipshansendesign/"


def dims(src):
    with Image.open(os.path.join(IMG_DIR, src)) as im:
        return im.size


def e(s):
    return html.escape(s, quote=True)


# --------------------------------------------------------------------------- content
PROJECTS = [
    {
        "slug": "lakewood-residence",
        "title": "Lakewood Residence",
        "category": "Residential space planning",
        "accent": "#5d7187",
        "summary": "A two-story home for a growing family, planned around work, entertaining, hobbies and storage, with rooms that can change as the family does.",
        "hero": ("hansen-residentialproject8a.jpg", "First-floor plan showing an open kitchen, dining and living area, a mudroom, a sewing and yoga room, and a two-car garage."),
        "facts": [("Client", "A growing family"), ("Location", "Lakewood, Colorado"),
                  ("Project type", "Two-story home, space plan"), ("Tools", "AutoCAD, pencil sketches, mood boards")],
        "sections": [
            ("The brief", [
                "The family needed a home that works for their current life and leaves room for future plans. The space plan balances an open layout with dedicated areas for work, entertaining, hobbies and storage.",
            ], []),
            ("First floor: shared living and dedicated work zones", [
                "The first floor centers on an open kitchen, dining and living area designed for everyday use and entertaining. The kitchen fits two cooks and island seating.",
                "Rooms next to the main space give each activity its own place: sewing and yoga, laundry and mudroom, pet needs, and storage for outdoor gear and hobby supplies.",
            ], [
                ("hansen-residentialproject8a.jpg", "First-floor plan with kitchen, island seating, dining room, living room, powder room, mudroom and laundry, sewing and yoga room, and garage.", "Main floor plan, drawn in AutoCAD.", "wide"),
                ("hansen-residentialproject7.jpg", "Pencil block diagrams of both floors, showing the rough placement of each room.", "Concept block diagrams, pencil sketches.", "wide"),
            ]),
            ("Second floor: privacy and flexibility", [
                "The second floor is designed for privacy and to adapt over time. The primary suite has a spacious bedroom, a walk-in closet, and a bath with a large freestanding tub.",
                "The guest bedroom can become a child’s room later. A separate home office includes a Murphy bed, so it can also host overnight guests.",
            ], [
                ("hansen-residentialproject8b.jpg", "Second-floor plan with primary bedroom, primary bath, walk-in closet, guest bedroom, full bathroom and office.", "Second floor plan, drawn in AutoCAD.", "tall"),
            ]),
            ("Mood and finishes", [
                "Inspiration images set the tone for the primary suite, great room, bath and mudroom: soft neutrals, natural wood and simple forms.",
            ], [
                ("hansen-residentialproject41.jpg", "Bedroom with an upholstered bed, neutral bedding and a wood nightstand.", "Primary bedroom inspiration.", "grid"),
                ("hansen-residentialproject43.jpg", "Open great room with a white sofa, beamed ceiling and kitchen beyond.", "Great room inspiration.", "grid"),
                ("hansen-residentialproject42.jpg", "Bathroom with a freestanding tub and glass shower.", "Primary bath inspiration.", "grid"),
                ("hansen-residentialproject4.jpg", "Mudroom storage cabinet beside a green upholstered bench.", "Mudroom inspiration.", "grid"),
            ]),
        ],
    },
    {
        "slug": "carolina-coast-kitchen",
        "title": "Carolina Coast Kitchen",
        "category": "Kitchen design",
        "accent": "#5f6150",
        "summary": "A waterfront kitchen for a couple whose North Carolina beach home is the gathering place for their large family.",
        "hero": ("rendering-kitchen-ai.jpg", "Kitchen with sage green cabinetry, a wood island with woven counter stools, pendant lights, and windows looking out to the beach and ocean."),
        "facts": [("Client", "A couple in their mid-60s"), ("Location", "North Carolina coast"),
                  ("Project type", "Kitchen design and technical drawings"),
                  ("Tools", "Hand drafting, pencil on vellum, Photoshop, Illustrator")],
        "sections": [
            ("The brief", [
                "The kitchen has a wide view of the beach and ocean and opens to the great room next to it. It needed to serve as the heart of large family get-togethers.",
                "Natural materials and coastal colors connect the kitchen to its setting without becoming a themed beach look.",
            ], [
                ("rendering-kitchen-ai.jpg", "Final kitchen rendering with sage cabinetry, a wood island and an ocean view.", "Final rendering. Original hand-drawn design, regenerated as a photorealistic image with AI.", "wide"),
            ]),
            ("Design approach", [
                "Custom cabinetry hides appliances and adds storage. The island doubles as a display space for the clients’ collections of dishware and glassware.",
                "Distressed cabinetry, natural stone and soft coastal colors echo the sand, water and landscape outside.",
            ], [
                ("rendering.jpg", "Hand-drawn perspective of the kitchen with color added digitally.", "Original perspective, pencil on vellum with finishes added in Photoshop.", "tall"),
            ]),
            ("Planning for many cooks", [
                "The kitchen is planned for several people at once, with safety, storage, accessibility, universal design and ease of use considered throughout.",
                "A large island supports cooking and gathering. Work areas at different heights accommodate baking, food prep, drinks and everyday tasks.",
                "The floor, construction, mechanical and countertop plans were drafted by hand as part of the technical documentation.",
            ], [
                ("countertop-plan.jpg", "Hand-drafted countertop plan with dimensions and a countertop legend.", "Countertop plan, hand drawn, with labels added in Illustrator.", "wide"),
                ("mechanical-plan.jpg", "Hand-drafted mechanical plan showing lighting, outlets and switching.", "Mechanical plan, hand drawn, with labels added in Illustrator.", "wide"),
                ("countertop.jpg", "White marble-look countertop sample.", "Selected countertop.", "grid"),
                ("stovetop.jpg", "Black induction cooktop with five burners.", "Selected cooktop.", "grid"),
            ]),
            ("Elevations and appliances", [
                "The interior elevations show the floor-to-ceiling custom cabinetry and the built-in coffee machine and wall ovens.",
                "The client is an avid baker, so an adjacent baking area has a lower countertop and extra outlets for countertop appliances and baking equipment. The elevations and final perspective were drawn by hand.",
            ], [
                ("elevation1.jpg", "Hand-drawn elevation of the tall cabinet wall with wall ovens, coffee machine and refrigerator.", "Interior elevation, appliance wall, hand drawn.", "wide"),
                ("elevation2.jpg", "Hand-drawn elevation of the window wall with base cabinets.", "Interior elevation, window wall, hand drawn.", "wide"),
                ("cabinnets.jpg", "Sage green kitchen cabinets.", "Selected cabinetry color.", "grid3"),
                ("coffeemachine.jpg", "Stainless built-in coffee machine.", "Selected built-in coffee machine.", "grid3"),
                ("oven.jpg", "Stainless wall oven.", "Selected wall oven.", "grid3"),
            ]),
        ],
    },
    {
        "slug": "coeur-dalene-a-frame",
        "title": "Coeur d’Alene A-Frame",
        "category": "Sustainable design",
        "accent": "#8a7550",
        "summary": "A small A-frame guest house on a mountain lake property in Idaho, designed around sustainability, durability and healthy living.",
        "hero": ("aframe-image.jpg", "A wood A-frame cabin at dusk with tall windows, a small balcony, pine trees and a fire pit with chairs."),
        "facts": [("Client", "A soon-to-be retired airline captain"), ("Location", "Mountain lake property, Idaho"),
                  ("Project type", "Guest house, space plan and specifications"), ("Tools", "AutoCAD, product specification")],
        "sections": [
            ("The brief", [
                "Sustainability, durability and healthy living guided the design, while still making the most of a small footprint.",
                "Responsibly sourced materials, efficient use of space, and colors and finishes drawn from the surrounding landscape give the home a warm, grounded connection to its site.",
            ], [
                ("aframe-image.jpg", "A-frame cabin at dusk with a fire pit in front.", "Inspiration image. Photo: Mighty Small Homes, mightysmallhomes.com.", "wide"),
            ]),
            ("Floor plans", [
                "The first floor fits a kitchen, bath, bedroom and living area, and opens onto a deck. A ship’s ladder leads up to a storage loft.",
            ], [
                ("sustainablefloorplan.jpg", "First-floor plan with bathroom, kitchen, bedroom, living area and deck.", "First floor plan, drawn in AutoCAD.", "grid"),
                ("attic.jpg", "Second-floor plan showing a storage area and an opening to the floor below.", "Second floor plan, drawn in AutoCAD.", "grid"),
            ]),
            ("Materials and products", [
                "Products and materials were chosen for responsible sourcing, durability, healthy indoor air and long-term performance.",
                "Selections include reclaimed and locally crafted woodwork, furnishings with recycled content, low-impact finishes, and energy-efficient appliances and lighting. Wherever possible, products were picked for long life and repairability, to reduce future replacement.",
            ], [
                ("floorplankeynote.jpg", "First-floor plan with numbered key notes that match the product list.", "First floor plan with key notes, drawn in AutoCAD.", "tall"),
                ("lightplant.jpg", "Wood beam light fixture with hanging plants and exposed bulbs.", "Lighting inspiration.", "grid4"),
                ("tilepallet.jpg", "Tile samples in blue, white, brown and gray.", "Tile palette.", "grid4"),
                ("bedroomnightstand.jpg", "Live-edge wood nightstand beside a bed.", "Nightstand inspiration.", "grid4"),
                ("storagestairs.jpg", "Wood stairs with built-in drawers and shelves underneath.", "Storage stair inspiration.", "grid4"),
            ]),
        ],
        "keynotes": ["Dazuma landscape light spikes", "Polywood Adirondack chairs", "Birch Creek hickory flooring",
                     "Quince drapery", "Prestige 20″ electric convection range",
                     "Thermador under-counter double-drawer refrigerator-freezer", "Moonshine Lamp Company wall sconce",
                     "Old Hat Workshop custom ship’s ladder with storage", "Milstone Netzero floor tile", "Milstone wall tile",
                     "High Sierra shower head", "Horow toilet", "Cottage and Bungalow jute rug",
                     "Benjamin Moore Eco Spec paint", "Old Hat Workshop custom platform bed",
                     "Old Hat Workshop custom nightstand", "Old Hat Workshop custom bookshelves",
                     "Old Hat Workshop custom sofa", "Old Hat Workshop custom coffee table", "Green Building Supply shake tiles"],
    },
    {
        "slug": "caribbean-minimalism",
        "title": "Caribbean Minimalism",
        "category": "Residential remodel",
        "accent": "#4f6d80",
        "summary": "A home remodel for a client from Puerto Rico that blends Caribbean color and Spanish Colonial detail with a minimalist base.",
        "hero": ("living-room-ai-created.jpg", "Living room with a gray sofa, orange pillows, a patterned rug, a gallery wall of black-and-white photos and a wrought-iron chandelier."),
        "facts": [("Client", "A frequent traveler from Puerto Rico"), ("Location", "Existing home"),
                  ("Project type", "Remodel, space plan and built-ins"), ("Tools", "AutoCAD, SketchUp")],
        "sections": [
            ("The brief", [
                "The remodel creates a personal retreat that reconnects the client to their Puerto Rican roots, without becoming overly themed. The client’s frequent travel is built into the design.",
                "Warm woods, wrought-iron details, textured fabrics, island colors and natural elements set the design language. Meaningful pieces from the client connect each space to their heritage.",
            ], [
                ("living-room-ai-created.jpg", "Living room with a gallery wall of the client’s photographs.", "Living room rendering. Modeled in SketchUp, regenerated as a photorealistic image with AI.", "wide"),
            ]),
            ("Reworking the floor plan", [
                "Moving walls, opening the plan and adding built-ins improve circulation, storage and function within the home’s existing footprint.",
                "The primary bedroom was reconfigured to add a larger walk-in closet with a sliding mirror door, which makes the small room feel larger.",
                "A wider doorway between the bedroom and living room features a custom antique tri-fold door. It connects the two rooms while still allowing privacy when needed.",
            ], [
                ("slide8-furnitureplan.jpg", "Furniture plan with bedroom, living room, kitchen, bathroom and entry, with dimensions.", "Floor plan, drawn in AutoCAD.", "tall"),
                ("slide35-livingroom.jpg", "3D view from the living room toward the bedroom, showing the antique door, a credenza and a beach artwork.", "Living room view, modeled in SketchUp.", "wide"),
                ("slide34-bedroom.jpg", "3D view of the bedroom with a white bed and a colorful mosaic artwork.", "Bedroom view, modeled in SketchUp.", "grid"),
                ("slide34-bedroom1.jpg", "3D view into the bedroom through the tri-fold doorway.", "View through the tri-fold door, modeled in SketchUp.", "grid"),
            ]),
            ("A built-in for the living area", [
                "A large hall closet in the main living area was reconfigured into a smaller closet and a built-in display and storage unit.",
            ], [
                ("built-in-cabinet-display-ai-created.jpg", "Built-in cabinet with glass upper doors, display shelves, a dark countertop and closed lower cabinets.", "Built-in rendering. Modeled in SketchUp, regenerated as a photorealistic image with AI.", "grid"),
                ("slide9-detaildrawing.jpg", "Elevation of the built-in with callouts for tempered glass doors, adjustable shelves, quartz backsplash and wood veneers.", "Built-in elevation with callouts, drawn in AutoCAD.", "grid"),
            ]),
            ("A palette from home", [
                "The color palette comes from a custom art piece made of broken tiles brought from Puerto Rico. The client’s own photography fills a gallery wall.",
                "Materials and furnishings blend vibrant Caribbean and Spanish Colonial influences on a minimalist foundation. The result balances relaxation and function.",
            ], [
                ("slide12-artbed.jpg", "Mosaic artwork of fan shapes in orange, teal, red and gold, made from broken tiles.", "Custom artwork made from broken tiles from Puerto Rico.", "wide"),
            ]),
        ],
    },
]

# --------------------------------------------------------------------------- shared chrome
LOGO = """<a class="logo" href="./" aria-label="Kacy Phillips Hansen, Interior Design. Home">
      <span class="logo-mark" aria-hidden="true">k</span>
      <span class="logo-text" aria-hidden="true">kacy phillips hansen<span>Interior Design</span></span>
    </a>"""

NAV_ITEMS = [("Work", "./#work", "work"), ("About", "./#about", "about"),
             ("Resume", "resume.html", "resume"), ("Contact", "./#contact", "contact")]


def page_head(title, desc):
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#f7f4ee">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Public+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/b.css?v={V}">
<script>document.documentElement.classList.remove("no-js")</script>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231f1e1b'/%3E%3Ctext x='16' y='24' font-family='Arial' font-size='22' fill='white' text-anchor='middle'%3Ek%3C/text%3E%3C/svg%3E">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""


def site_header(current):
    items = ""
    for label, href, key in NAV_ITEMS:
        if key != current:
            cur = ""
        elif key == "resume":
            cur = ' aria-current="page"'
        else:
            cur = ' class="is-active"'
        items += f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f"""<header class="site-header">
  <div class="container header-inner">
    {LOGO}
    <nav aria-label="Main">
      <button class="menu-button" type="button" aria-expanded="false" aria-controls="main-nav">
        <span class="menu-icon" aria-hidden="true"></span><span class="menu-text">Menu</span>
      </button>
      <ul class="nav-list" id="main-nav">{items}</ul>
    </nav>
  </div>
</header>
"""


def site_footer():
    proj = "".join(f'<li><a href="{p["slug"]}.html">{e(p["title"])}</a></li>' for p in PROJECTS)
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      {LOGO.replace('class="logo"', 'class="logo logo-footer"')}
      <p class="footer-note">Interior design student at Arapahoe Community College.</p>
    </div>
    <nav aria-label="Projects">
      <h2 class="footer-heading">Projects</h2>
      <ul class="footer-list">{proj}</ul>
    </nav>
    <div>
      <h2 class="footer-heading">Contact</h2>
      <ul class="footer-list">
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="tel:{TEL}">{PHONE}</a></li>
        <li><a href="{LINKEDIN}" rel="noopener">LinkedIn<span class="visually-hidden"> (opens LinkedIn)</span></a></li>
        <li><a href="resume.html">Resume</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-base"><p>© 2026 {NAME}. Portfolio of work from 2022 to 2026.</p></div>
</footer>
<dialog class="viewer" aria-labelledby="viewer-caption">
  <div class="viewer-bar">
    <p class="viewer-count" aria-live="polite"></p>
    <button type="button" class="viewer-btn" data-close>Close<span class="visually-hidden"> image viewer</span></button>
  </div>
  <figure class="viewer-figure">
    <img alt="">
    <figcaption id="viewer-caption"></figcaption>
  </figure>
  <div class="viewer-nav">
    <button type="button" class="viewer-btn" data-prev>← Previous</button>
    <button type="button" class="viewer-btn" data-next>Next →</button>
  </div>
</dialog>
<script src="assets/b.js?v={V}"></script>
</body>
</html>
"""


def img_tag(src, alt, eager=False, sizes="100vw"):
    w, h = dims(src)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="../images/{src}" alt="{e(alt)}" width="{w}" height="{h}" {load}>'


def figure(src, alt, caption):
    return f"""<figure class="fig">
  <button type="button" class="zoom" data-src="../images/{src}" data-alt="{e(alt)}" data-caption="{e(caption)}">
    {img_tag(src, alt)}
    <span class="zoom-hint" aria-hidden="true">Enlarge</span>
    <span class="visually-hidden">Enlarge image</span>
  </button>
  <figcaption>{e(caption)}</figcaption>
</figure>"""


def figures_block(figs):
    out, buf, kind = [], [], None

    def flush():
        nonlocal buf, kind
        if not buf:
            return
        if kind in ("wide", "tall"):
            for f in buf:
                out.append(f'<div class="figs figs-{kind}">{figure(*f[:3])}</div>')
        else:
            out.append(f'<div class="figs figs-{kind}">' + "".join(figure(*f[:3]) for f in buf) + "</div>")
        buf, kind = [], None

    for f in figs:
        k = f[3]
        if k != kind or k in ("wide", "tall"):
            flush()
            kind = k
        buf.append(f)
    flush()
    return "\n".join(out)


def slugify(s):
    return "".join(c.lower() if c.isalnum() else "-" for c in s).strip("-").replace("--", "-")


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(content)


os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

# --------------------------------------------------------------------------- home
cards = ""
for i, p in enumerate(PROJECTS):
    cards += f"""<li class="card" style="--accent-project:{p['accent']}">
  <div class="card-media">{img_tag(p['hero'][0], '')}</div>
  <div class="card-body">
    <p class="card-meta">Project {i+1} · {e(p['category'])}</p>
    <h3 class="card-title"><a href="{p['slug']}.html">{e(p['title'])}</a></h3>
    <p class="card-text">{e(p['summary'])}</p>
    <p class="card-cta" aria-hidden="true">View project →</p>
  </div>
</li>"""

home = page_head(f"{NAME} | Interior Design Portfolio",
                 f"Interior design portfolio of {NAME}: residential space planning, kitchen design and sustainable design projects, 2022 to 2026.")
home += site_header("home")
home += f"""<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="container hero-grid">
    <div class="hero-text">
      <p class="kicker">Interior design portfolio · 2022–2026</p>
      <h1 id="hero-title">Thoughtful interiors, built on research and detail.</h1>
      <p class="hero-lead">I’m {NAME}, an interior design student at Arapahoe Community College with more than 20 years of experience in art direction, graphic design and advertising.</p>
      <div class="button-row">
        <a class="button button-primary" href="#work">See my work</a>
        <a class="button button-secondary" href="resume.html">Read my resume</a>
      </div>
    </div>
    <div class="hero-media">
      {img_tag('rendering-kitchen-ai.jpg', 'Kitchen design rendering: sage cabinetry, a wood island with woven stools, and an ocean view.', eager=True)}
    </div>
  </div>
</section>

<section class="section" id="work" aria-labelledby="work-title" tabindex="-1">
  <div class="container">
    <div class="section-intro">
      <h2 id="work-title">Selected work</h2>
      <p>Four projects covering space planning, kitchen design, sustainable design and remodeling. Each includes plans, drawings and renderings.</p>
    </div>
    <ul class="cards" role="list">{cards}</ul>
  </div>
</section>

<section class="section section-alt" id="about" aria-labelledby="about-title" tabindex="-1">
  <div class="container about-grid">
    <div class="about-photo">{img_tag('headshot.jpg', f'Portrait of {NAME}.')}</div>
    <div class="about-text">
      <h2 id="about-title">About me</h2>
      <p>My background in design taught me to look at each project as a whole without losing sight of the details.</p>
      <p>I approach interior design by bringing together research, spatial thinking, materials, visual communication and technical requirements, to create thoughtful spaces for the people who use them.</p>
      <dl class="about-facts">
        <div><dt>Studying</dt><dd>AAS in Interior Design and Residential Kitchen &amp; Bath Design Certificate, Arapahoe Community College. Graduating spring 2027.</dd></div>
        <div><dt>Software</dt><dd>AutoCAD, SketchUp, InDesign, Photoshop, Illustrator</dd></div>
        <div><dt>Student member</dt><dd><abbr title="American Society of Interior Designers">ASID</abbr>, <abbr title="National Kitchen and Bath Association">NKBA</abbr>, <abbr title="Network of Executive Women in Hospitality">NEWH</abbr>, <abbr title="Interior Design Society">IDS</abbr></dd></div>
      </dl>
      <p><a class="text-link" href="resume.html">Read my full resume</a></p>
    </div>
  </div>
</section>

<section class="section" id="contact" aria-labelledby="contact-title" tabindex="-1">
  <div class="container contact">
    <h2 id="contact-title">Let’s connect</h2>
    <p>Thank you for looking through my work and my process. I’d love to hear from you.</p>
    <ul class="contact-list" role="list">
      <li><a class="contact-item" href="mailto:{EMAIL}"><span class="contact-label">Email</span><span class="contact-value">{EMAIL}</span></a></li>
      <li><a class="contact-item" href="tel:{TEL}"><span class="contact-label">Phone</span><span class="contact-value">{PHONE}</span></a></li>
      <li><a class="contact-item" href="{LINKEDIN}" rel="noopener"><span class="contact-label">LinkedIn</span><span class="contact-value">kacyphillipshansendesign</span></a></li>
    </ul>
  </div>
</section>
</main>
"""
home += site_footer()
write("index.html", home)

# --------------------------------------------------------------------------- project pages
for i, p in enumerate(PROJECTS):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    prv = PROJECTS[i - 1]
    facts = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in p["facts"])
    toc = "".join(f'<li><a href="#{slugify(h)}">{e(h)}</a></li>' for h, _, _ in p["sections"])
    secs = ""
    for h, paras, figs in p["sections"]:
        sid = slugify(h)
        ptxt = "".join(f"<p>{e(x)}</p>" for x in paras)
        extra = ""
        if h == "Materials and products" and p.get("keynotes"):
            kn = "".join(f"<li>{e(k)}</li>" for k in p["keynotes"])
            extra = f"""<div class="keynotes">
  <h3>Key notes</h3>
  <p class="keynotes-help">Numbers match the circled numbers on the key-note floor plan.</p>
  <ol>{kn}</ol>
</div>"""
        secs += f"""<section class="p-section" id="{sid}" aria-labelledby="{sid}-h">
  <div class="p-section-text"><h2 id="{sid}-h">{e(h)}</h2>{ptxt}</div>
  {figures_block([f for f in figs if f[0] != p["hero"][0]])}
  {extra}
</section>
"""
    hero_src, hero_alt = p["hero"]
    hero_cap = next((f[2] for _, _, fs in p["sections"] for f in fs if f[0] == hero_src), "")
    pg = page_head(f"{p['title']} | {NAME}", p["summary"])
    pg += site_header("work")
    pg += f"""<main id="main" style="--accent-project:{p['accent']}">
<div class="container">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol><li><a href="./">Home</a></li><li><a href="./#work">Work</a></li><li><a href="{p['slug']}.html" aria-current="page">{e(p['title'])}</a></li></ol>
  </nav>
  <header class="p-header">
    <p class="kicker">Project {i+1} of {len(PROJECTS)} · {e(p['category'])}</p>
    <h1>{e(p['title'])}</h1>
    <p class="p-lead">{e(p['summary'])}</p>
    <dl class="facts">{facts}</dl>
  </header>
  <div class="p-hero">{figure(hero_src, hero_alt, hero_cap).replace('loading="lazy" decoding="async"', 'fetchpriority="high"')}</div>
  <div class="p-layout">
    <nav class="toc" aria-label="On this page">
      <h2 class="toc-title">On this page</h2>
      <ol>{toc}</ol>
    </nav>
    <div class="p-content">
{secs}
    </div>
  </div>
  <nav class="p-pager" aria-label="More projects">
    <a class="pager-link" href="{prv['slug']}.html"><span class="pager-dir">Previous project</span><span class="pager-title">{e(prv['title'])}</span></a>
    <a class="pager-link pager-next" href="{nxt['slug']}.html"><span class="pager-dir">Next project</span><span class="pager-title">{e(nxt['title'])}</span></a>
  </nav>
</div>
</main>
"""
    pg += site_footer()
    write(f"{p['slug']}.html", pg)

# --------------------------------------------------------------------------- resume
res = page_head(f"Resume | {NAME}", f"Resume of {NAME}, interior design student with 20+ years in art direction and graphic design.")
res += site_header("resume")
res += f"""<main id="main">
<div class="container resume">
  <header class="r-header">
    <p class="kicker">Resume</p>
    <h1>{NAME}</h1>
    <p class="p-lead">Interior design student with more than 20 years of experience in art direction, graphic design and advertising, bringing a professional perspective to residential and commercial interiors.</p>
    <ul class="r-contact" role="list">
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="tel:{TEL}">{PHONE}</a></li>
      <li><a href="{LINKEDIN}" rel="noopener">linkedin.com/in/kacyphillipshansendesign</a></li>
    </ul>
    <p class="r-actions"><button type="button" class="button button-secondary" data-print>Print or save as PDF</button></p>
  </header>

  <div class="r-grid">
    <div class="r-main">
      <section aria-labelledby="exp">
        <h2 id="exp">Work experience</h2>
        <article class="r-entry">
          <h3>Design Intern, TAB Interior Design</h3>
          <p class="r-when">December 2024 – February 2025</p>
          <ul>
            <li>Took field measurements on site visits for residential design projects.</li>
            <li>Researched products and furnishings and helped develop client presentation materials.</li>
            <li>Organized and maintained the studio’s FF&amp;E library and showroom, and checked in client product for storage.</li>
          </ul>
        </article>
        <article class="r-entry">
          <h3>Design Intern, Imagine Kitchen &amp; Bath</h3>
          <p class="r-when">December 2008 – February 2009</p>
          <ul>
            <li>Assisted with kitchen and bath space planning, design development, and material and finish selections.</li>
            <li>Produced AutoCAD drawings and hand-rendered plans.</li>
            <li>Took part in client meetings, site visits and field measurements.</li>
          </ul>
        </article>
        <article class="r-entry">
          <h3>Freelance Graphic Designer, Kacy Designs, LLC</h3>
          <p class="r-when">2006 – present</p>
          <ul>
            <li>Designed a two-page ad for the 2024 ASID Colorado Crystal Awards, published in the Colorado Real Estate Journal.</li>
            <li>Manage independent design projects from concept to final production, coordinating with clients and vendors and managing schedules and deliverables.</li>
          </ul>
        </article>
        <article class="r-entry">
          <h3>Art Director, Graphic Designer and Design Manager</h3>
          <p class="r-when">1994 – 2006</p>
          <ul>
            <li>Managed creative projects across branding, advertising, catalogs, packaging, trade shows and environmental graphics, working with internal teams, vendors and production partners.</li>
            <li>Supervised a five-person design team and presented concepts and business initiatives to corporate board members and executive leadership.</li>
          </ul>
        </article>
      </section>

      <section aria-labelledby="skills">
        <h2 id="skills">Design and technical skills</h2>
        <dl class="r-skills">
          <div><dt>Interior design</dt><dd>Space planning, FF&amp;E and material selection, specifications, lighting, NKBA planning guidelines</dd></div>
          <div><dt>AutoCAD</dt><dd>Floor plans, furniture plans, reflected ceiling plans, interior elevations, construction documents</dd></div>
          <div><dt>SketchUp</dt><dd>2D and 3D modeling, spatial visualization, rendering</dd></div>
          <div><dt>Adobe Creative Suite</dt><dd>InDesign for mood boards and client presentations; Photoshop for rendering and image editing; Illustrator for vector graphics and presentation assets</dd></div>
        </dl>
      </section>
    </div>

    <div class="r-side">
      <section aria-labelledby="edu">
        <h2 id="edu">Education</h2>
        <article class="r-entry">
          <h3>Arapahoe Community College</h3>
          <p class="r-when">Littleton, Colorado · 2022 – expected spring 2027</p>
          <p>Associate of Applied Science, Interior Design<br>Residential Kitchen &amp; Bath Design Certificate<br>President’s List, 2022–2026</p>
        </article>
        <article class="r-entry">
          <h3>The Art Institute of Colorado</h3>
          <p class="r-when">Denver, Colorado · 2007–2009</p>
          <p>Interior Design, Kitchen &amp; Bath Studies</p>
        </article>
        <article class="r-entry">
          <h3>University of Nebraska–Lincoln</h3>
          <p class="r-when">Lincoln, Nebraska · 1988–1992</p>
          <p>Bachelor of Journalism, Advertising<br>Minors: Art, English, History</p>
        </article>
      </section>

      <section aria-labelledby="memb">
        <h2 id="memb">Student memberships</h2>
        <ul class="r-plain">
          <li>American Society of Interior Designers (ASID)</li>
          <li>National Kitchen and Bath Association (NKBA)</li>
          <li>Network of Executive Women in Hospitality (NEWH)</li>
          <li>Interior Design Society (IDS)</li>
        </ul>
      </section>

      <section aria-labelledby="comm">
        <h2 id="comm">Community and industry involvement</h2>
        <ul class="r-plain">
          <li>Douglas County School District, District Accountability Committee, alternate (2026)</li>
          <li>ASID Colorado Home Show volunteer (2025)</li>
          <li>ASID Crystal Awards volunteer (2024)</li>
          <li>SkyView Academy K–12, board secretary: kept board records, reviewed policies and advised leadership on policy updates (2019–2022)</li>
        </ul>
      </section>
    </div>
  </div>
</div>
</main>
"""
res += site_footer()
write("resume.html", res)
print("Design B built:", sorted(os.listdir(OUT)))
