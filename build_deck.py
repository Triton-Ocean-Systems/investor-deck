"""Editable source for Triton's 12-page investor deck. Run: python build_deck.py.
Requires reportlab. Original visual assets are cropped from the supplied deck.
"""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

ROOT = Path(__file__).resolve().parent
W,H=960,540
BG='#03111a'; WHITE='#f6f9fa'; CYAN='#00becd'; MUTED='#93aeb8'; LINE='#20404d'
fontdir=Path('C:/Windows/Fonts')
if (fontdir/'arial.ttf').exists():
    pdfmetrics.registerFont(TTFont('Body',str(fontdir/'arial.ttf')))
    pdfmetrics.registerFont(TTFont('Bold',str(fontdir/'arialbd.ttf')))
else:
    pdfmetrics.registerFont(pdfmetrics.Font('Body','Helvetica','WinAnsiEncoding'))
    pdfmetrics.registerFont(pdfmetrics.Font('Bold','Helvetica-Bold','WinAnsiEncoding'))
c=canvas.Canvas(str(ROOT/'Triton_PreSeed_Deck_v3.pdf'),pagesize=(W,H))
c.setTitle('Triton Ocean Systems | Pre-Seed Investment Case')
c.setAuthor('Triton Ocean Systems')
def text(x,y,s,size=16,color=WHITE,bold=False):
    c.setFillColor(HexColor(color)); c.setFont('Bold' if bold else 'Body',size)
    c.drawString(x,H-y-size,s)
def para(x,y,s,width=850,size=17,color=MUTED,bold=False):
    p=Paragraph(s,ParagraphStyle('p',fontName='Bold' if bold else 'Body',fontSize=size,leading=size*1.35,textColor=HexColor(color)))
    _,h=p.wrap(width,1000)
    if y+h>490: raise ValueError(f'Text exceeds content area: {s}')
    p.drawOn(c,x,H-y-h)
    return h
def start(n,label,title,sub=None):
    c.setFillColor(HexColor(BG)); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(HexColor(CYAN)); c.rect(0,0,6,H,fill=1,stroke=0)
    text(54,38,label.upper(),9,CYAN,True)
    text(54,69,title,30,WHITE,True)
    if sub: para(54,118,sub,size=16)
    text(42,514,'TRITON OCEAN SYSTEMS',7,MUTED)
    text(894,514,f'{n:02}',8,MUTED)
def note(s): para(54,468,s,width=850,size=10,color=MUTED)
def rule(y):
    c.setStrokeColor(HexColor(LINE)); c.setLineWidth(.7); c.line(54,H-y,906,H-y)
def row(y,label,body,x=54,bodyx=310,width=595):
    text(x,y,label,16,CYAN,True); para(bodyx,y,body,width=width,size=16)
def end(): c.showPage()

start(1,'Ocean intelligence infrastructure','Make the ocean observable')
para(54,145,'Persistent local observations for coastal operations.<br/>First proposed application: sargassum cleanup planning for South Florida beachfront resorts.',width=505,size=22,color=WHITE)
c.drawImage(ImageReader(str(ROOT/'assets/observation-surfaces.png')),620,H-277,width=292,height=174,mask='auto')
text(54,332,'PRE-SEED TARGET',10,MUTED);text(54,356,'$1.2M',32,WHITE,True);text(54,405,'18-month planning horizon',13,MUTED)
text(354,332,'STAGE',10,MUTED);text(354,356,'Pre-revenue',26,WHITE,True);text(354,405,'Prototype / pre-MVP',13,MUTED)
text(650,332,'FIRST PROOF',10,MUTED);text(650,356,'Node 001',26,WHITE,True);text(650,405,'Field results not yet supplied',13,MUTED)
note('Jorge Pimentel | Founder & CTO     Company status carried forward from v2; not independently audited.');end()

start(2,'Economic pain / proposed beachhead','Cleanup decisions have a cost','Buyer hypothesis: resort operations director with control over beach-cleaning spend in Miami-Dade and Broward.')
para(54,172,'Before the morning crew dispatch, decide where to clean and how much labor and equipment to commit.',width=820,size=25,color=WHITE,bold=True)
row(254,'Operational pain','Late or unnecessary dispatch can create overtime, equipment expense and lost usable beach time. Resort-specific losses remain unmeasured.')
rule(324)
text(54,346,'$3.80M / year',29,CYAN,True)
para(310,341,'Historical annualized Miami-Dade sargassum removal contract value, reported in an October 2025 county memo. Evidence of cleanup spend; not Triton revenue or a resort budget.',width=595,size=16)
note('Source: <a href="https://www.miamidade.gov/govaction/matter.asp?file=true&amp;fileAnalysis=false&amp;matter=252110&amp;yearFolder=Y2025" color="#00becd">Miami-Dade legislative file 252110 (2025)</a>, fiscal impact section. Historical scope; not a software purchase.');end()

start(3,'Proposed solution','Local evidence inside the cleanup workflow','A daily site brief and threshold alerts, with timestamps, confidence and an audit trail of observed conditions.')
row(176,'Observe','BeachNode: proposed shore camera or suitable sensor, with manual shoreline labels. Sargassum sensing hardware is not yet validated.')
rule(245)
row(263,'Deliver','EdgeCore buffers observations through outages. Triton joins local evidence to licensed regional data and sends a site brief before crew dispatch.')
rule(331)
row(349,'Measure','Operator logs the decision, cleanup effort and actual shoreline condition. Compare the workflow with existing forecasts plus manual inspection.')
note('Designed architecture, not a demonstrated product. SailNode is the mobile test platform; NMEA / AIS / GNSS alone do not detect sargassum.');end()

start(4,'Technical validation / proposed acceptance criteria','Node 001 must prove reliable observation','Infrastructure validation comes first. Sargassum detection and arrival guidance require a separate coastal pilot.')
text(54,171,'GATE',10,MUTED,True);text(310,171,'EVIDENCE REQUIRED BEFORE EXPANSION',10,MUTED,True)
row(202,'Bench | months 0-3','72-hour soak; log power and thermals; inject link loss and reboot. Recover buffered records without unexplained loss.')
rule(269)
row(286,'Field | months 2-5','30-day run; target >=95% scheduled valid records; reconcile sequence IDs after outage; track servicing hours and actual bill of materials.')
rule(353)
row(369,'Coastal application','Time-aligned shoreline labels and held-out event days; report precision, missed events and useful warning time versus the existing workflow.')
note('All durations and thresholds above are proposed targets, not results. v2 lists an EdgeCore ceiling below $2,000, excluding external sensors and major vessel systems.');end()

start(5,'Commercial validation','A paid pilot must change a decision','First offer: one site, 90 days, a daily operations brief and a weekly review against the current cleanup process.')
row(178,'Discover','Proposed: 15 buyer interviews. Verify who pays, who can change dispatch, seasonal costs and whether contracted cleaning spend is avoidable.')
rule(245)
row(263,'Pilot','Proposed: 3 paid sites at $5,000 each, including setup. Record baseline and intervention days; exclude savings caused only by lighter seaweed arrivals.')
rule(332)
row(350,'Convert','Proposed gate: 2 of 3 sites sign annual contracts after measurable workflow benefit and a full service-cost review.')
note('Pilot pricing is a proposed learning subsidy, not margin proof. No customers or signed pilots established. BeachLens is a discussion, not a formal partner.');end()

start(6,'Business model / unvalidated assumptions','Site subscriptions must cover field service','Proposed pricing to test: $5,000 setup, then $1,500 per site per month ($18,000 annual recurring revenue).')
text(54,177,'ILLUSTRATIVE ANNUAL SITE ECONOMICS',10,CYAN,True)
for y,label,amount in [(207,'Subscription revenue','$18,000'),(242,'Direct recurring service cost','$6,000'),(277,'Gross profit / gross margin','$12,000 / 67%')]:
    text(54,y,label,18,WHITE); text(480,y,amount,22,CYAN,True)
para(690,204,'Service cost must include connectivity, field visits, replacement reserve and direct support. Setup fee assumes $5,000 setup cost.',width=215,size=14)
rule(326)
para(54,344,'Customer break-even: $18,000 of incremental annual benefit before setup. Example only: 30 response days x $1,500 avoidable cost x 40% improvement = $18,000.',width=850,size=19,color=WHITE)
note('No validated price, cost, margin, savings or willingness to pay. First-year break-even including setup is $23,000; CAC and R&D are excluded from gross margin.');end()

start(7,'Bottom-up market / scenario arithmetic','The beachhead is a testable market','Count eligible buying accounts and sites in Miami-Dade and Broward before presenting a serviceable market estimate.')
para(54,171,'Eligibility: beachfront access + authority over cleanup + discretionary budget + deployment permission. Deduplicate properties by buying account.',width=850,size=19,color=WHITE)
text(54,247,'SITES',11,MUTED,True);text(310,247,'ASSUMED ANNUAL PRICE',11,MUTED,True);text(680,247,'RECURRING REVENUE',11,MUTED,True)
for y,n,rev in [(281,'50','$0.9M'),(323,'150','$2.7M'),(365,'1,000','$18M')]:
    text(54,y,n,23,WHITE,True);text(310,y,'$18,000 / site',21,MUTED);text(680,y,rev,23,CYAN,True)
para(54,416,'These are site-count scenarios, not a verified TAM or pipeline. Venture scale requires validated expansion into additional coastal workflows and geographies.',size=15,color=WHITE)
note('Count x price; no setup revenue included. Eligible site count, account concentration, adoption, retention and expansion economics remain unknown.');end()

start(8,'Competitive differentiation','Triton must beat the existing workflow','The proposed edge is persistent site evidence tied to a cleanup decision. Price or accuracy superiority has not been established.')
text(54,175,'ALTERNATIVE',10,MUTED,True);text(290,175,'EXISTING VALUE / TRITON PROOF REQUIRED',10,MUTED,True)
row(204,'USF forecasting','Satellite and model trajectories, including a 3.5-day forecast. Show incremental value from local observations.',bodyx=290,width=610)
rule(265)
row(281,'Crews / cameras','Direct local inspection and operating experience. Show a brief improves dispatch enough to justify a paid service.',bodyx=290,width=610)
rule(342)
row(358,'Ocean platforms','NOAA: real-time observations; Sofar: sensing and voyage optimization; Saildrone: autonomous data collection. Test the proposed site-service niche.',bodyx=290,width=610)
note('Sources: <a href="https://ocgweb.marine.usf.edu/Models/Sargassum/sargassum.html" color="#00becd">USF</a>; <a href="https://tidesandcurrents.noaa.gov/ports_info.html" color="#00becd">NOAA PORTS</a>; <a href="https://www.sofarocean.com/products/wayfinder" color="#00becd">Sofar</a>; <a href="https://www.saildrone.com/" color="#00becd">Saildrone</a>. Potential substitutes or inputs; no partnerships implied.');end()

start(9,'Compounding data advantage / hypothesis','Useful coverage can compound','The potential asset is a permissioned record of local conditions, operator decisions and observed outcomes.')
row(180,'More nearby sites','Capture spatial variation and shared events. New observations add value only if they improve predictions or decisions at another site.')
rule(247)
row(265,'More event history','Label arrivals and false alarms across seasons. Compare models on held-out sites and events, rather than training-set performance.')
rule(333)
row(351,'More workflow use','Track dispatch changes and outcomes. Test retention, service cost per site and revenue per shared observation footprint.')
note('No network effect demonstrated. Data reuse rights, quality control and cross-site improvement are prerequisites; seasonal gaps and incumbent replication are risks.');end()

start(10,'Founder-market fit / current evidence','Jorge Pimentel | Founder & CTO','Founder-led integration of hardware, communications, field operations and software is the current execution thesis.')
text(54,177,'COMPANY-REPORTED FOUNDATION',10,CYAN,True)
para(54,206,'Approximately $48K founder funded.<br/>SEAVANT software foundation and ocean intelligence prototypes.<br/>Founder leads architecture, product and field validation.',width=410,size=21,color=WHITE)
text(540,177,'EVIDENCE STILL NEEDED',10,CYAN,True)
para(540,206,'A dated prototype demonstration.<br/>Relevant prior engineering and marine operating work.<br/>Access to buyer workflows and deployment sites.<br/>Named field and commercial support.',width=365,size=19,color=MUTED)
rule(393)
para(54,411,'Current disclosed stage: pre-MVP, no paying customers, no institutional capital. No prior exits, credentials or field performance are claimed.',size=16,color=WHITE)
note('Source: original v2 deck. Founder spend, software maturity and current status require confirmation; founder-market fit remains only partially substantiated.');end()

start(11,'18-month plan / proposed spending gates','Capital follows technical and commercial proof','Milestones start at funding; calendar ranges are planning assumptions, not completed work or guaranteed dates.')
row(180,'0-5 months | $300K','Bench and field gates pass. Show valid data, outage recovery, deployment permissions and actual installed cost.')
rule(247)
row(263,'5-12 months | $450K','3 paid pilots; prospective baseline comparison; 2 annual conversions targeted. Stop scaling if buyers cannot change spend or see useful benefit.')
rule(331)
row(347,'12-18 months | $300K','Replicate deployment, measure service cost and seek renewal evidence where contract timing permits. Seed case needs repeatable demand and data value.')
note('$150K reserve remains outside stage envelopes. Proposed management gates, not investor tranches. No pass/fail outcome has yet been demonstrated.');end()

start(12,'The ask','A $1.2M raise to prove the first network','Approximately 18 months. The investment thesis depends on reliable observation, paid adoption and useful data reuse.')
alloc=[('Hardware + deployments','$360K','30%'),('Engineering + platform','$300K','25%'),('Ocean ops + SailNode','$150K','12.5%'),('Customer pilots + BD','$150K','12.5%'),('Regulatory + legal','$90K','7.5%'),('Reserve','$150K','12.5%')]
for i,(label,amount,pct) in enumerate(alloc):
    y=176+i*37
    text(54,y,label,17,WHITE);text(485,y,amount,20,CYAN,True);text(645,y,pct,16,MUTED)
para(750,175,'Average gross budget:<br/>~$66.7K / month.<br/><br/>Excluding reserve:<br/>~$58.3K / month.',width=155,size=16)
rule(414)
para(54,429,'Seed evidence: reliable nodes, paying sites, measured service economics and useful data reuse.',size=17,color=WHITE,bold=True)
note('Allocation retained from v2. No valuation or financing terms supplied. Detailed staffing, cash-flow and seasonal pilot schedule remain to be validated.');end()
c.save()
print('Created 12-page Triton_PreSeed_Deck_v3.pdf')
