from textwrap import dedent

html = dedent("""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wind &amp; Water — Interior Visual System</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#f5f0e8;
  --paper-deep:#ece5d8;
  --ink:#2d2b27;
  --ink-soft:#6a655c;
  --cinnabar:#9c3b2e;
  --gold:#b08d4c;
  --card:#fffdf8;
}
*{box-sizing:border-box;}
body{
  font-family:'Cormorant Garamond', Georgia, serif;
  background:
    radial-gradient(circle at 50% 0%, #faf6ee 0%, var(--paper) 60%);
  margin:0;
  padding:48px 24px;
  color:var(--ink);
  -webkit-font-smoothing:antialiased;
}
.container{
  max-width:1180px;
  margin:auto;
}

/* ---- Hero ---- */
.hero{
  text-align:center;
  padding:72px 40px;
  background:var(--paper-deep);
  border:1px solid rgba(156,59,46,.15);
  border-radius:24px;
  margin-bottom:56px;
  position:relative;
}
.hero::before{
  content:"";
  position:absolute;
  inset:14px;
  border:1px solid rgba(176,141,76,.35);
  border-radius:16px;
  pointer-events:none;
}
.eyebrow{
  font-family:'Jost', sans-serif;
  font-size:13px;
  letter-spacing:.42em;
  text-transform:uppercase;
  color:var(--cinnabar);
  margin-bottom:22px;
}
h1{
  font-size:clamp(48px, 8vw, 78px);
  font-weight:500;
  letter-spacing:.04em;
  margin:0 0 6px;
  line-height:1.05;
}
.ampersand{
  color:var(--cinnabar);
  font-style:italic;
  font-weight:400;
}
.subtitle{
  font-size:clamp(20px, 3vw, 26px);
  font-style:italic;
  color:var(--ink-soft);
  margin-bottom:20px;
}
.rule{
  width:64px;
  height:1px;
  background:var(--gold);
  margin:0 auto 18px;
}
.hero-tag{
  font-family:'Jost', sans-serif;
  font-size:12px;
  letter-spacing:.32em;
  text-transform:uppercase;
  color:var(--ink-soft);
  margin:0;
}

/* ---- Grid ---- */
.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit, minmax(300px, 1fr));
  gap:28px;
}
.card{
  background:var(--card);
  padding:26px 26px 30px;
  border-radius:18px;
  border:1px solid rgba(45,43,39,.06);
  box-shadow:0 6px 22px rgba(45,43,39,.07);
  transition:transform .35s ease, box-shadow .35s ease;
}
.card:hover{
  transform:translateY(-6px);
  box-shadow:0 16px 38px rgba(45,43,39,.14);
}
.card-index{
  font-family:'Jost', sans-serif;
  font-size:12px;
  letter-spacing:.2em;
  color:var(--gold);
}
.card h2{
  font-size:25px;
  font-weight:500;
  margin:6px 0 16px;
  line-height:1.2;
}
.mock{
  height:208px;
  border-radius:13px;
  background:linear-gradient(135deg, #d9d1c3 0%, #f9f6ef 100%);
  display:flex;
  align-items:center;
  justify-content:center;
  text-align:center;
  padding:24px;
  font-style:italic;
  font-size:18px;
  color:#555048;
  border:1px solid rgba(176,141,76,.25);
}

/* ---- Footer ---- */
footer{
  margin-top:64px;
  text-align:center;
  font-family:'Jost', sans-serif;
  font-size:12px;
  letter-spacing:.26em;
  text-transform:uppercase;
  color:var(--ink-soft);
}
footer .seal{
  display:block;
  color:var(--cinnabar);
  font-size:20px;
  margin-bottom:10px;
  letter-spacing:0;
}

@media (max-width:520px){
  body{padding:28px 14px;}
  .hero{padding:52px 22px;}
}
</style>
</head>
<body>

<div class="container">

  <header class="hero">
    <p class="eyebrow">The Complete Feng Shui Compendium</p>
    <h1>WIND <span class="ampersand">&amp;</span> WATER</h1>
    <p class="subtitle">Where placement becomes philosophy</p>
    <div class="rule"></div>
    <p class="hero-tag">Luxury Interior Visual System</p>
  </header>

  <main class="grid">

    <article class="card">
      <span class="card-index">01</span>
      <h2>Dedication Page</h2>
      <div class="mock">Minimal bamboo illustration with centered, breathing typography</div>
    </article>

    <article class="card">
      <span class="card-index">02</span>
      <h2>Quote Landscape Spread</h2>
      <div class="mock">Chinese ink-wash mountains framing a single philosophical quote</div>
    </article>

    <article class="card">
      <span class="card-index">03</span>
      <h2>Contents Layout</h2>
      <div class="mock">Elegant chapter hierarchy accented with fine bamboo detailing</div>
    </article>

    <article class="card">
      <span class="card-index">04</span>
      <h2>The Origins of Wind &amp; Water</h2>
      <div class="mock">Historical river landscape paired with a serif editorial layout</div>
    </article>

    <article class="card">
      <span class="card-index">05</span>
      <h2>Qi — The Breath of the World</h2>
      <div class="mock">Flowing line-art visualization of energy in continuous movement</div>
    </article>

    <article class="card">
      <span class="card-index">06</span>
      <h2>Five Elements Diagram</h2>
      <div class="mock">Wood &bull; Fire &bull; Earth &bull; Metal &bull; Water in cyclical balance</div>
    </article>

    <article class="card">
      <span class="card-index">07</span>
      <h2>Bagua Map</h2>
      <div class="mock">Eight directions orbiting a calm Yin-Yang center</div>
    </article>

    <article class="card">
      <span class="card-index">08</span>
      <h2>Bedroom Commanding Position</h2>
      <div class="mock">Spatial room diagram beside a serene luxury bedroom visual</div>
    </article>

    <article class="card">
      <span class="card-index">09</span>
      <h2>Decluttering Ritual</h2>
      <div class="mock">Keep &bull; Release &bull; Uncertain — a quiet three-part rite</div>
    </article>

  </main>

  <footer>
    <span class="seal">&#9670;</span>
    Wind &amp; Water Visual Identity System
    &nbsp;&bull;&nbsp; Cinnabar-Style Editorial Presentation
  </footer>

</div>

</body>
</html>
""")

output_path = "Wind_Water_Visual_System.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"saved -> {output_path}")
