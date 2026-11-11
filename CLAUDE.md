# ML Interview Prep — how to add a question

Live site: https://sagarika-ramesh.github.io/ml-interview-questions/
Repo: https://github.com/Sagarika-Ramesh/ml-interview-questions (GitHub Pages, `main` branch, root folder)

When Sagarika gives a new ML interview question, **append** it to this site in exactly the
style below. Don't redesign anything; she iterated a long time to land on this look.

## File layout

```
index.html                         home page: hero + list of question cards
assets/style.css                   ALL shared styles (append new rules at the end)
assets/site.js                     code highlighting, copy buttons, flip cards
questions/<slug>/index.html        one page per question
questions/robust-to-outliers/      Question 1 — THE REFERENCE PAGE; copy its structure
tools/figure_helpers.py            SVG helper functions for both figure styles (illustrations + 3b1b graphs)
```

## Steps to add question N

1. `git clone https://github.com/Sagarika-Ramesh/ml-interview-questions.git` (or `git pull`).
2. Copy `questions/robust-to-outliers/index.html` to `questions/<new-slug>/index.html` and
   replace the content, keeping every structural piece listed under "Page structure".
3. On `index.html`, add an `<li>` with an `a.qitem` card to the `ol.qlist`
   (number `0N`, title, one-line teaser, meta tags such as topic, "N diagrams", "N follow-ups"),
   and update the "N so far, more coming" count.
4. Check it locally (`python3 -m http.server`) in light and dark mode, and at phone width
   (375px, no page-level horizontal scroll).
5. Commit and push to `main`; Pages rebuilds in about a minute. Check the live URL.

## Page structure (question page)

- Top bar: breadcrumb `← All questions / Question N` on the left; colour legend on the right
  (`ul.legend`: pink = Code, yellow = Key content, blue = Note).
- `header.qcard` (yellow outline): "Question N" plus topic chips, `h1.qtitle` with one key word
  wrapped in `span.squiggle`, then **"The 30-second answer"** (`.short`), an interview-ready summary.
- `ul.toc toc-q`: pill links to each section.
- The first content section starts with the "Start here" kicker, then `h3#big-picture` "The big picture"
  and the overview **mind map** (`figure.diagram.illus`, centre node plus one branch per area), before
  anything else. Since it comes first, avoid acronyms in it that haven't been spelled out yet.
- Content `section`s, each with a `.kicker` (handwritten label), an `h2`, then prose, tables,
  code, figures and callouts as needed.
  End each content section with its own **decision chart** (`h3` "Decision chart: …" plus a
  `figure.diagram.illus` built with `tools/figure_helpers.py`), placed inside the section it belongs to
  (e.g. "which loss?" in the loss section), never collected at the bottom.
- **Follow-ups interviewers ask** (`#followups`): hint "Try answering out loud, then tap a card
  to check.", then `.flashes.flashes-wide` holding `button.flash.flash-wide` flip cards.
  Front: `<span class="fn">1.</span>` plus the question. Back: `<span class="bq">1. question</span>`
  plus the answer.
- **Cheat sheet** (`#cheatsheet`), no box around it: just `ol.steps.steps-v`: a vertical numbered list of key steps that covers EVERY area
  on the page (e.g. data, loss, model, training/regularisation, evaluation), each with a short, concrete line. No mind map
  and no decision charts here. NO flash cards in the cheat sheet.
- `nav.pager` "← Back to all questions", a `footer`, then `<p class="signature">Sagarika</p>`.

## Visual rules

- Base: dark, refined look (charcoal `#14151b` in dark mode, Source Serif 4 body, Bricolage
  Grotesque headings, Kalam handwriting accents, JetBrains Mono code, purple accent). Light mode
  must work too.
- **Outline boxes, transparent fill:**
  - **Pink** (`.code`): every code block. Code-head tags: `Trap` (red), `Fix`/`Pattern` (green),
    `Note` (purple).
  - **Yellow**: key content, meaning the question card, tables (`.tbl-wrap`) and home list cards.
  - **Blue** (`.callout`): notes, tips, warnings and other asides.
  - Follow-ups and the cheat sheet are NOT boxed in yellow.
- **Concept illustrations** (`figure.diagram.illus` + `svg.il`): explainer style on a slate
  panel `#47577a` with cream `#f3ecdc` cards (3px `#22252e` outline, soft drop shadow), dark
  mono label chips, coral `#ff6b5e` / teal `#4fb3a5` tags, dashed rounded group boxes, tan
  `#c9a063` rope connectors with ink outline, and a bold dark caption box below (`<em>` turns
  part of it coral). Take only the STYLE from reference images, never their subject.
  Sagarika was annoyed when database cylinders from her style example were copied into a diagram.
- **Graphs with axes or curves** (`figure.diagram.graph` + `svg.g3`): 3Blue1Brown style.
  Near-black panel `#0c0c0e`, faint blue grid, arrowed light-grey axes with ticks, 4px curves in
  the 3b1b palette (blue `#58C4DD`, yellow `#F7D96F`, red `#FC6255`, green `#83C167`), and
  STIX Two Text italic math labels. Caption is italic serif below.
  **Every graph is labelled:** a title at the top-left inside the panel (22px, `#f2f2f2`,
  e.g. "Three loss functions compared"; extend the viewBox upward, e.g. `0 -46 740 …`), plus
  descriptive axis titles in `#cfcfcf` ("feature x", a rotated "target y", "residual r = y − ŷ",
  "loss L(r)"), as well as the short math labels at the arrow tips and a legend where needed.
- **Follow-up flip cards**: rectangles (6px radius) stacked one below the other, a see-through
  pastel yellow tint (about 13–20% alpha) with the normal theme text colour. NOT a near-solid
  yellow with dark text; she called that "eww". Numbering is plain bold "1." in yellow with a
  space after. "tap to flip ↻" is a glowing, shimmering yellow gradient.
- Use flip cards only for genuinely tricky ideas, never simple recall facts.
- Signature: "Sagarika" in Great Vibes, right-aligned below the footer, greyish white
  `#e9e9ec` (soft grey `#8a8f99` in light mode).

## Writing rules

- Spell out every acronym on first use with the short form in brackets:
  "Local Outlier Factor (LOF)", "mean squared error (MSE)".
- Plain, clear sentences. Code examples in Python (scikit-learn, PyTorch, LightGBM).
- Each question page: a 30-second answer, sections that go deeper, about 3 figures, tables
  where comparisons help, pink code blocks with Trap/Fix, about 5 follow-ups, and a cheat sheet.
