"""Generates the static HTML pages for the portfolio. Run: python3 build.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
NAME = "Kacy Phillips Hansen"
EMAIL = "kacyhansen70@gmail.com"
PHONE = "720.256.8672"
LINKEDIN = "https://www.linkedin.com/in/kacyphillipshansendesign/"

PROJECTS = [
    ("lakewood-residence.html", "Lakewood Residence", "Space Plan", "--lakewood"),
    ("carolina-coast-kitchen.html", "North Carolina Waterfront Kitchen", "Kitchen", "--carolina"),
    ("coeur-dalene-a-frame.html", "Coeur d’Alene A-Frame", "Sustainability", "--aframe"),
    ("caribbean-minimalism.html", "Caribbean Minimalism", "Space Plan", "--caribbean"),
]


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v=2">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231c1c1a'/%3E%3Ctext x='16' y='24' font-family='Arial' font-size='22' fill='white' text-anchor='middle'%3Ek%3C/text%3E%3C/svg%3E">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current):
    def cur(f):
        return ' aria-current="page"' if f == current else ""
    proj_links = "".join(
        f'<a href="{f}"{cur(f)}><span class="dot" style="background:var({c})"></span>{t}</a>'
        for f, t, _, c in PROJECTS
    )
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{NAME} — home">
      <span class="mark">k</span>
      <span class="brand-name">kacy phillips hansen<small>Interior Design</small></span>
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="index.html#about"{cur('about')}>About</a>
      <div class="dropdown">
        <button aria-haspopup="true">Projects ▾</button>
        <div class="dropdown-menu"><span class="menu-label">Projects</span>{proj_links}</div>
      </div>
      <a href="resume.html"{cur('resume.html')}>Resume</a>
      <a href="mailto:{EMAIL}">Contact</a>
    </nav>
  </div>
</header>
<main id="main">
"""


def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <span>© 2026 {NAME} · Interior Design Portfolio 2022–2026</span>
    <span><a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;·&nbsp; <a href="tel:7202568672">{PHONE}</a> &nbsp;·&nbsp; <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</footer>
<script src="assets/site.js?v=2"></script>
</body>
</html>
"""


def fig(src, alt, cap=None, cls="plate"):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure><div class="{cls}" data-zoom><img src="images/{src}" alt="{alt}" loading="lazy"></div>{c}</figure>'


def tile(src, alt):
    return f'<div class="tile" data-zoom><img src="images/{src}" alt="{alt}" loading="lazy"></div>'


def pager(idx):
    prev_f, prev_t, _, _ = PROJECTS[idx - 1]
    nxt_f, nxt_t, _, _ = PROJECTS[(idx + 1) % len(PROJECTS)]
    return f"""<nav class="pager" aria-label="Project navigation">
  <a href="{prev_f}"><p class="eyebrow">← Previous project</p><span class="t">{prev_t}</span></a>
  <a href="{nxt_f}"><p class="eyebrow">Next project →</p><span class="t">{nxt_t}</span></a>
</nav>"""


def project_page(idx, title_html, intro, tags, body, dark=False):
    f, t, cat, color = PROJECTS[idx]
    band_cls = "band dark" if dark else "band"
    html = head(f"{t} — {NAME}", f"{cat} project by interior design student {NAME}.")
    html += header(f)
    html += f"""<div class="wrap" style="--c:var({color})">
<section class="p-hero">
  <div class="{band_cls}"><p class="eyebrow">ID: Project / {cat}</p><h1>{title_html}</h1></div>
  <div class="p-intro"><p class="lead">{intro}</p><div class="tags">{tags}</div></div>
</section>
{body}
{pager(idx)}
</div>
"""
    html += footer()
    return html


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
        fh.write(html)


# ---------------------------------------------------------------- home
cards = [
    ("lakewood-residence.html", "hansen-residentialproject8a.jpg", "First-floor plan, Lakewood Residence",
     "Two-story family home in Lakewood, Colorado, planned around work, entertaining, hobbies and storage."),
    ("carolina-coast-kitchen.html", "rendering-kitchen-ai.jpg", "Rendering of the North Carolina waterfront kitchen",
     "A large waterfront kitchen for a couple whose beach home hosts the whole family."),
    ("coeur-dalene-a-frame.html", "aframe-image.jpg", "A-frame guest house at dusk",
     "A small A-frame guest house in Idaho designed around sustainability, durability and healthy living."),
    ("caribbean-minimalism.html", "living-room-ai-created.jpg", "Living room rendering, Caribbean Minimalism",
     "A remodel for a client from Puerto Rico — Caribbean color and Spanish Colonial detail on a minimalist base."),
]
card_html = ""
for (f, t, cat, color), (_, img, alt, blurb) in zip(PROJECTS, cards):
    card_html += f"""<a class="card" href="{f}" style="--c:var({color})">
  <div class="card-img"><img src="images/{img}" alt="{alt}" loading="lazy"></div>
  <div class="card-body"><p class="eyebrow">ID: Project / {cat}</p><h3>{t}</h3><p>{blurb}</p></div>
</a>"""

home = head(f"{NAME} — Interior Design Portfolio",
            f"Selected work 2022–2026 by interior design student {NAME}.")
home += header("index.html")
home += f"""<div class="wrap">
<section class="hero">
  <div class="hero-grid">
    <div class="hero-title">
      <p class="eyebrow">Selected Work · 2022–2026</p>
      <div class="band"><h1><strong>PORTFOLIO</strong></h1></div>
      <div class="hero-meta"><span>{NAME}</span><span>Interior Design</span></div>
    </div>
    <div class="hero-image"><img src="images/rendering-kitchen-ai.jpg" alt="Kitchen rendering with ocean view"></div>
  </div>
</section>

<section class="about" id="about">
  <img src="images/headshot.jpg" alt="Portrait of {NAME}">
  <div>
    <p class="eyebrow">About me</p>
    <p class="lead">I’m an Interior Design student at ACC with more than 20 years of professional experience in art direction, graphic design, and advertising.</p>
    <p>My design background has taught me to consider each project as a whole without losing sight of the details. I approach interior design by bringing together research, spatial thinking, materials, visual communication, and technical requirements to create thoughtful environments for the people who use them.</p>
    <div class="contact-line">
      <a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:7202568672">{PHONE}</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><a href="resume.html">Resume →</a>
    </div>
  </div>
</section>

<section class="projects" id="projects">
  <div class="section-head"><h2>Selected <strong>Projects</strong></h2></div>
  <div class="cards">{card_html}</div>
</section>
</div>
"""
home += footer()
write("index.html", home)

# ---------------------------------------------------------------- Lakewood
body = f"""
<div class="feature">{fig('hansen-residentialproject8a.jpg', 'First-floor plan with kitchen, dining, living room, mudroom and garage', 'Main Story Floor Plan: Created in AutoCAD')}</div>

<section class="chapter">
  <div class="chapter-text">
    <h2>First floor</h2>
    <p>The first floor centers on an open kitchen, dining, and living area designed for everyday use and entertaining. The kitchen accommodates two cooks and island seating, while adjacent spaces provide dedicated areas for sewing and yoga, laundry and mudroom functions, pet needs, and storage for outdoor gear and hobby supplies.</p>
  </div>
  {fig('hansen-residentialproject7.jpg', 'Hand-drawn concept block diagrams for first and second floors', 'Concept Block Diagrams: Pencil Sketches')}
</section>

<section class="chapter flip">
  <div class="chapter-text">
    <h2>Second floor</h2>
    <p>The second floor was designed for privacy and to adapt with the family’s needs over time. The primary suite includes a spacious bedroom, walk-in closet, and bath with a large freestanding tub, while the guest bedroom can transition into a child’s room. A separate home office incorporates a Murphy bed, allowing the space to also accommodate overnight guests.</p>
  </div>
  {fig('hansen-residentialproject8b.jpg', 'Second-floor plan with primary suite, guest bedroom and office', 'Second Story Floor Plan: Created in AutoCAD')}
</section>

<section class="chapter">
  <div class="chapter-text"><h2>Mood</h2><p>Inspiration images for the primary suite, great room, bath and mudroom.</p></div>
  <figure>
    <div class="grid-2">
      {tile('hansen-residentialproject41.jpg', 'Bedroom inspiration')}
      {tile('hansen-residentialproject43.jpg', 'Great room inspiration')}
      {tile('hansen-residentialproject42.jpg', 'Bathroom inspiration')}
      {tile('hansen-residentialproject4.jpg', 'Mudroom inspiration')}
    </div>
    <figcaption>Mood Board: Inspirational Images</figcaption>
  </figure>
</section>
"""
write(PROJECTS[0][0], project_page(
    0, "Lakewood, CO<br>Residence",
    "This two-story home was designed for a growing family in Lakewood, Colorado. The space plan balances an open layout with the family’s work, entertaining, hobby, storage needs and future plans in mind. Flexible and functional spaces were incorporated to accommodate both their current lifestyle and changing needs.",
    "Residential space planning<br>AutoCAD floor plans<br>Concept sketches<br>Mood boards", body))

# ---------------------------------------------------------------- Carolina
body = f"""
<div class="feature">{fig('rendering-kitchen-ai.jpg', 'Kitchen with sage cabinetry, wood island and ocean view', 'Rendering: Original Hand-Drawn Design, Photorealistically regenerated in AI', 'plate bare shadow')}</div>

<section class="chapter">
  <div class="chapter-text">
    <h2>Design intent</h2>
    <p>Custom cabinetry integrates appliances and storage while the island provides a display space for the clients’ unique dishware and glassware collections.</p>
    <p>Distressed cabinetry, natural stone, and subdued coastal colors reference the surrounding sand, water, and ocean landscape.</p>
  </div>
  {fig('rendering.jpg', 'Hand-drawn kitchen perspective', 'Rendering: Original Hand-Drawn Pencil on Vellum, finishes created in Photoshop', 'plate bare')}
</section>

<section class="chapter">
  <div class="chapter-text">
    <h2>Technical plans</h2>
    <p>The kitchen was planned for multiple users with safety, storage, accessibility, universal design, and ease of use considered throughout the space. A large island supports cooking and gathering, while varied work areas and heights accommodate baking, food preparation, beverages, and everyday tasks. The floor, construction, mechanical, and countertop plans were drafted by hand as part of the project’s technical documentation.</p>
  </div>
  <div class="stack">
    {fig('countertop-plan.jpg', 'Hand-drafted countertop plan', 'Countertop Plan: Hand Drawn, typography added in Illustrator')}
    {fig('mechanical-plan.jpg', 'Hand-drafted mechanical plan', 'Mechanical Plan: Hand Drawn, typography added in Illustrator')}
    <figure><div class="grid-2">{tile('countertop.jpg', 'Marble countertop sample')}{tile('stovetop.jpg', 'Induction cooktop')}</div><figcaption>Product Images: Updated Selections</figcaption></figure>
  </div>
</section>

<section class="chapter">
  <div class="chapter-text">
    <h2>Elevations</h2>
    <p>The interior elevations illustrate the kitchen’s custom floor-to-ceiling cabinetry and integration of appliances, including the built-in coffee machine and wall ovens. An adjacent baking area features a lower countertop designed for the client, an avid baker, with additional outlets to support countertop appliances and baking equipment. The elevations and final perspective were drawn by hand.</p>
  </div>
  <div class="stack">
    {fig('elevation1.jpg', 'Hand-drawn cabinetry elevation with ovens and refrigerator', 'Interior Elevation: Hand Drawn')}
    {fig('elevation2.jpg', 'Hand-drawn window wall elevation', 'Interior Elevation: Hand Drawn')}
    <figure><div class="grid-3">{tile('cabinnets.jpg', 'Sage green cabinetry')}{tile('coffeemachine.jpg', 'Built-in coffee machine')}{tile('oven.jpg', 'Wall oven')}</div><figcaption>Product Images: Updated Selections</figcaption></figure>
  </div>
</section>
"""
write(PROJECTS[1][0], project_page(
    1, "Carolina<br>Coast",
    "This waterfront kitchen was designed for a couple in their mid-60s whose North Carolina beach home serves as a main place for their large family get togethers. The large kitchen design has a prime view over the sweeping beach and ocean, and has an open connection to the adjacent great room. Natural materials and coastal-inspired colors connect the kitchen to its surroundings without creating an overly themed beach aesthetic.",
    "Kitchen design · NKBA guidelines<br>Hand-drafted plans &amp; elevations<br>Hand rendering · Photoshop<br>Universal design", body))

# ---------------------------------------------------------------- A-frame
keynotes = ["Dazuma Landscape Light Spikes", "Polywood Adirondack Chairs", "Birch Creek Hickory Flooring",
            "Quince Drapery", "Prestige 20” Electric Convection Range",
            "Therador Under-Counter Double Drawer Refrigerator-Freezer", "Moonshine Lamp Company Wall Sconce",
            "Old Hat Workshop Custom Ships Ladder/Storage", "Milstone Netzero Floor Tile", "Milstone Wall Tile",
            "High Sierra Shower Head", "Horow Toilet", "Cottage and Bungalow Jute Rug",
            "Benjamin Moore Eco Spec Paint", "Old Hat Workshop Custom Platform Bed",
            "Old Hat Workshop Custom Nightstand", "Old Hat Workshop Custom Bookshelves",
            "Old Hat Workshop Custom Sofa", "Old Hat Workshop Custom Coffee Table", "Green Building Supply Shake Tiles"]
kn = "".join(f"<li>{k}</li>" for k in keynotes)
body = f"""
<section class="chapter">
  <div class="chapter-text"><h2>Plan</h2><p>A compact first floor holds the kitchen, bath, bedroom and living area, opening onto a deck. A ship’s ladder leads to storage above.</p></div>
  <div class="grid-2" style="align-items:start">
    {fig('sustainablefloorplan.jpg', 'First-story floor plan of the A-frame', 'First Story Floor Plan: Created in AutoCAD')}
    {fig('attic.jpg', 'Second-story storage plan', 'Second Story Plan: Created in AutoCAD')}
  </div>
</section>

<section class="chapter flip">
  <div class="chapter-text"><h2>Inspiration</h2><p>Colors and finishes inspired by the surrounding landscape create a warm, grounded connection to the home’s location.</p></div>
  {fig('aframe-image.jpg', 'A-frame cabin at dusk with fire pit', 'Mighty Small Home: www.mightysmallhomes.com', 'plate bare shadow')}
</section>

<section class="chapter">
  <div class="chapter-text">
    <h2>Materials &amp; products</h2>
    <p>Product and material selections focused on responsible sourcing, durability, a healthy indoor environment, and long-term performance. Selections include reclaimed and locally crafted woodwork, recycled-content furnishings, low-impact finishes, energy-efficient appliances and lighting, and materials chosen for reduced environmental impact. Whenever possible, products were selected for longevity, repairability, and their ability to reduce the need for future replacement.</p>
  </div>
  <div class="stack">
    {fig('floorplankeynote.jpg', 'Floor plan with numbered key notes', 'First Story Floor Plan: Created in AutoCAD with Key Notes')}
    <div><h3 style="margin-bottom:14px">Key notes</h3><ol class="keynotes">{kn}</ol></div>
    <figure><div class="grid-4">{tile('lightplant.jpg', 'Hanging plant light fixture')}{tile('tilepallet.jpg', 'Tile palette')}{tile('bedroomnightstand.jpg', 'Live-edge wood nightstand')}{tile('storagestairs.jpg', 'Storage stairs')}</div><figcaption>Mood Board: Inspiration Images</figcaption></figure>
  </div>
</section>
"""
write(PROJECTS[2][0], project_page(
    2, "Coeur d’Alene<br>A-Frame",
    "This A-frame guest house was spaceplanned for a soon-to-be retired airline captain on his mountain lake property in Idaho. Primary consideration on sustainability, durability, and healthy living guided the design, while still maximizing the home’s small footprint. Responsibly sourced materials, efficient use of space, and colors and finishes inspired by the surrounding landscape create a warm, grounded connection to the home’s location.",
    "Sustainable design<br>Small-footprint space planning<br>Product specification<br>AutoCAD", body, dark=True))

# ---------------------------------------------------------------- Caribbean
body = f"""
<section class="chapter">
  <div class="chapter-text">
    <h2>Design language</h2>
    <p>Warm woods, wrought-iron details, textured fabrics, island-inspired colors, and natural elements establish the design language, while meaningful client-provided pieces connect the spaces to the client’s heritage.</p>
    <p>Broken tiles brought from Puerto Rico were repurposed into custom artwork, while the client’s photography was incorporated into a gallery wall. Overall, design balances relaxation and function while creating a home that reconnects the client to their Puerto Rico roots.</p>
  </div>
  <div class="stack">
    {fig('living-room-ai-created.jpg', 'Living room with gallery wall and patterned rug', 'Rendering: Created in SketchUp, Photorealistically regenerated in AI', 'plate bare shadow')}
    {fig('slide8-furnitureplan.jpg', 'Furniture floor plan with bedroom, living room, kitchen and bath', 'Floor Plan: Created in AutoCAD')}
  </div>
</section>

<section class="chapter flip">
  <div class="chapter-text">
    <h2>Opening the plan</h2>
    <p>Moving walls, opening the floor plan and built-ins improves circulation, storage, and functionality within the home’s existing footprint. Reconfiguring the primary bedroom to include a larger walk-in closet with a sliding mirror door provides the small room more space.</p>
    <p>A larger doorway between the bedroom and living room showcases a bespoke tri-fold antique door and allows for a larger connection between the bedroom and living room, while still creating privacy when needed.</p>
  </div>
  <div class="stack">
    {fig('slide35-livingroom.jpg', 'SketchUp living room view toward the bedroom', 'Rendering: Created in SketchUp')}
    <div class="grid-2">{fig('slide34-bedroom.jpg', 'SketchUp bedroom view', 'Rendering: Created in SketchUp')}{fig('slide34-bedroom1.jpg', 'Bedroom view through tri-fold door', 'Rendering: Created in SketchUp')}</div>
  </div>
</section>

<section class="chapter">
  <div class="chapter-text">
    <h2>Built-in &amp; palette</h2>
    <p>In the main living area, a former large hall closet was reconfigured into a smaller closet and a built-in storage area. The color palette for the residence was inspired from a custom art piece made of broken tiles from Puerto Rico.</p>
    <p>Overall, materials and furnishings are a blend of vibrant Caribbean and Spanish Colonial influences but with a minimalist foundation.</p>
  </div>
  <div class="stack">
    {fig('slide12-artbed.jpg', 'Mosaic artwork made from broken Puerto Rican tiles', 'Custom artwork: broken tiles from Puerto Rico', 'plate bare')}
    <div class="grid-2" style="align-items:start">
      {fig('built-in-cabinet-display-ai-created.jpg', 'Built-in display cabinet', 'Rendering: Created in SketchUp, Photorealistically regenerated in AI')}
      {fig('slide9-detaildrawing.jpg', 'Detail elevation of the built-in cabinet with callouts', 'Elevation: Created in AutoCAD')}
    </div>
  </div>
</section>
"""
write(PROJECTS[3][0], project_page(
    3, "Caribbean<br>Minimalism",
    "This home remodel was tailored for a client from Puerto Rico and frequent travel is integrated into the design. Caribbean color, Spanish Colonial details, natural materials, and a minimalist influence create a personal retreat without becoming overly themed.",
    "Residential remodel<br>AutoCAD · SketchUp<br>Built-in millwork detailing<br>Client heritage pieces", body))

# ---------------------------------------------------------------- Resume
res = head(f"Resume — {NAME}", f"Resume of interior design student {NAME}.")
res += header("resume.html")
res += f"""<div class="wrap" style="--c:var(--stone)">
<section class="p-hero">
  <div class="band"><p class="eyebrow">Kacy Phillips Hansen</p><h1><strong>RESUME</strong></h1></div>
</section>
<div class="resume">
  <div>
    <div class="r-block">
      <h3>Contact Info + Profile</h3>
      <ul class="r-contact">
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/kacyphillipshansendesign</a></li>
        <li><a href="tel:7202568672">{PHONE}</a></li>
      </ul>
      <p class="r-body">Interior design student with over 20 years of experience in art direction, graphic design, and advertising, bringing a professional perspective to the residential and commercial interiors. Combines research, spatial thinking, materials, visual communication, and technical design skills to develop thoughtful, functional solutions.</p>
      <p class="r-body">Student Member: ASID · NKBA · NEWH · IDS</p>
    </div>
    <div class="r-block">
      <h3>Education</h3>
      <div class="r-item"><b>Arapahoe Community College</b> – Littleton, Colorado<br>Expected Graduation: Spring 2027<br>Associate of Applied Science – Interior Design<br>Residential Kitchen Bath Design Certificate<br>President’s List, 2022–2026</div>
      <div class="r-item"><b>The Art Institute of Colorado</b> – Denver, Colorado<br>2007–2009<br>Interior Design, Kitchen &amp; Bath Studies</div>
      <div class="r-item"><b>University of Nebraska, Lincoln</b> – Nebraska<br>Bachelor of Journalism 1988–1992<br>Major: Advertising · Minors: Art, English, History</div>
    </div>
    <div class="r-block">
      <h3>Community + Industry Involvement</h3>
      <div class="r-item"><ul>
        <li>Douglas County School District: District Accountability Committee, Alternate 2026.</li>
        <li>ASID Colorado Home Show Volunteer, 2025.</li>
        <li>ASID Crystal Awards Volunteer, 2024.</li>
        <li>SkyView Academy K–12: Board Secretary, maintained board records, reviewed policies, advised leadership on policy updates, 2019–2022.</li>
      </ul></div>
    </div>
  </div>
  <div class="r-right">
    <div class="r-block">
      <h3>Design + Technical Skills</h3>
      <div class="r-item"><b>Interior Design</b> – Space planning, FF&amp;E and material selection, specifications, lighting, and NKBA planning guidelines.</div>
      <div class="r-item"><b>AutoCAD</b> – Floor plans, furniture plans, reflected ceiling plans, interior elevations, and construction documentation.</div>
      <div class="r-item"><b>SketchUp</b> – 2D/3D modeling, spatial visualization, and rendering.</div>
      <div class="r-item"><b>Adobe Creative Suite</b> – InDesign: mood boards and client presentations; Photoshop: rendering enhancements and image editing; Illustrator: vector graphics and presentation assets.</div>
    </div>
    <div class="r-block">
      <h3>Work Experience</h3>
      <div class="r-item"><b>TAB Interior Design</b> | Internship | Dec 2024 – Feb 2025<ul>
        <li>Conducted field measurements during site visits to support residential design projects.</li>
        <li>Researched products and furnishings and assisted in developing client presentation materials.</li>
        <li>Organized and maintained the studio’s FF&amp;E library and front-of-house showroom, and checked in client product for storage.</li></ul></div>
      <div class="r-item"><b>Imagine Kitchen &amp; Bath</b> | Internship | Dec 2008 – Feb 2009<ul>
        <li>Assisted with kitchen and bath space planning, design development, and materials and finish selections.</li>
        <li>Produced AutoCAD drawings and hand-rendered plans.</li>
        <li>Participated in client meetings, site visits, and field measurements.</li></ul></div>
      <div class="r-item"><b>Kacy Designs, LLC</b> | Freelance Graphic Designer | 2006 – Current<ul>
        <li>Designed two-page ad for the 2024 ASID Colorado Crystal Awards; published in the Colorado Real Estate Journal.</li>
        <li>Manage independent graphic design projects from concept to final production, coordinating with clients and vendors while managing schedules, creative development, and final deliverables.</li></ul></div>
      <div class="r-item"><b>Art Director, Graphic Designer, Design Manager</b> | 1994 – 2006<ul>
        <li>Managed creative projects across branding, advertising, catalogs, packaging, trade shows, and environmental graphics; collaborated with internal teams, vendors, and production partners.</li>
        <li>Supervised a five-person design team and presented concepts and business initiatives to corporate board members, and executive leadership.</li></ul></div>
    </div>
  </div>
  <p class="thanks">Thank you for exploring my work and my process. Let’s connect! — Kacy</p>
</div>
</div>
"""
res += footer()
write("resume.html", res)
print("built")
