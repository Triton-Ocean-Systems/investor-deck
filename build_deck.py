"""Editable source for Triton's 12-page investor deck. Run: python build_deck.py.
Requires reportlab. Original visual assets are cropped from the supplied deck.
"""
from pathlib import Path
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
c=canvas.Canvas(str(ROOT/'Triton_PreSeed_Deck_v4.pdf'),pagesize=(W,H))
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

start(1,'Ocean data / observation infrastructure','Make the ocean observable')
para(54,145,'A distributed observation network.<br/>Persistent, queryable ocean data for the organizations that need it.',width=505,size=25,color=WHITE)
c.drawImage(ImageReader(str(ROOT/'assets/observation-surfaces.png')),620,H-277,width=292,height=174,mask='auto')
text(54,332,'PRE-SEED TARGET',10,MUTED);text(54,356,'$1.2M',32,WHITE,True);text(54,405,'18-month planning horizon',13,MUTED)
text(354,332,'STAGE',10,MUTED);text(354,356,'Pre-revenue',26,WHITE,True);text(354,405,'Prototype / pre-MVP',13,MUTED)
text(650,332,'FIRST PROOF',10,MUTED);text(650,356,'Node 001',26,WHITE,True);text(650,405,'Reliable capture to data access',13,MUTED)
note('Jorge Pimentel | Founder & CTO. Company status from v2; network and depth coverage are planned, not demonstrated.');end()

start(2,'Economic pain / data access','Useful ocean data has to reach the buyer','The proposed gap is dependable local observation with usable provenance, continuity and access.')
row(180,'Data users','Marine operators, environmental consultancies and ocean analytics teams may need observations beyond available coverage. Buyer demand remains unvalidated.')
rule(247)
row(265,'Economic burden','A buyer may commission collection, combine incompatible feeds or operate with uncertainty. Quantify acquisition and integration cost for each actual buyer.')
rule(333)
row(351,'Investment test','Find a missing dataset with a budget owner. Prove that buying Triton data is more useful or less costly than public feeds, existing suppliers or self-collection.')
note('Existing systems already provide persistent observations. No universal coverage gap, customer loss estimate or savings claim is established.');end()

start(3,'The proposed data product','Observation records are the first product','BeachNode, SailNode and third-party vessel integrations feed EdgeCore and a common Triton data platform.')
row(180,'Capture','Node 001 starts with planned onboard NMEA / AIS / GNSS inputs: vessel location and available navigation context. Audit the actual fields and sample rates.')
rule(247)
row(265,'Qualify','Retain time, location, source and quality flags. Environmental variables require suitable instruments, calibration and explicit coverage definitions.')
rule(333)
row(351,'Deliver','Proposed archive and API access by geography, time and measured variable. Offline buffering preserves records; it does not provide live access during an outage.')
note('NMEA is an interface, not a measured variable. AIS / GNSS alone do not measure water quality or sargassum. Platform access is not yet field-proven.');end()

start(4,'Node 001 / proposed acceptance criteria','One node must prove the full data path','The initial dataset proves infrastructure. Its commercial value must be tested separately before multiplying deployments.')
text(54,171,'GATE',10,MUTED,True);text(310,171,'EVIDENCE REQUIRED BEFORE EXPANSION',10,MUTED,True)
row(202,'Bench | months 0-3','72-hour soak; log power and thermals; inject link loss and reboot. Reconcile captured records and buffered recovery.')
rule(269)
row(286,'Field | months 2-5','30-day run; target >=95% scheduled valid records. Report missing data, source quality, latency, servicing hours and installed cost.')
rule(353)
row(369,'Buyer data trial','Publish a documented sample with query access. Compare coverage and usefulness with alternatives; secure collection and reuse permissions.')
note('Targets, not results. v2 lists an EdgeCore ceiling below $2,000, excluding external sensors and major vessel systems; this is not installed network cost.');end()

start(5,'Customer discovery / deployment selection','Demand determines where the network grows','South Florida is the initial development geography. The first commercial dataset and buyer segment remain to be selected.')
row(180,'Candidate buyers','Test commercial marine operators, environmental consultancies and ocean analytics teams. Public agencies are a possible later channel, not a prerequisite.')
rule(247)
row(265,'Discovery gate','Proposed: 15 interviews. Identify required variables, coverage, freshness, rights and budget. Rank gaps that a small cluster can economically fill.')
rule(333)
row(351,'Commercial gate','Target 3 paid data trials and 2 annual conversions. Add nodes where contracted demand or documented trial demand supports the cost of coverage.')
note('No customers or paid trials claimed. Sargassum, coastal conditions and environmental monitoring are candidate applications, not committed beachheads.');end()

start(6,'Business model / assumptions to test','Recurring access to observation coverage','Proposed offer: annual data subscriptions and API access, with separate fees for dedicated collection or integration.')
text(54,179,'PRICING HYPOTHESIS',10,CYAN,True)
text(54,211,'$24K / account / year',28,WHITE,True)
para(54,260,'Illustrative base package. Price must reflect the measured variables, licensed footprint, freshness and permitted use.',width=405,size=18)
text(540,179,'COVERAGE ECONOMICS',10,CYAN,True)
para(540,211,'4 accounts x $24K = $96K annual revenue for a shared coverage package.<br/><br/>That revenue must cover direct collection, servicing, connectivity, quality control and delivery costs.',width=360,size=20,color=WHITE)
rule(402)
para(54,418,'Shared coverage can serve multiple buyers only when their needs overlap and contracts permit reuse. Dedicated deployments need separate cost recovery.',size=16,color=WHITE)
note('No validated pricing, account demand, margin or break-even claim. Direct deployment capital must be recovered; acquisition cost and overhead also affect cash flow.');end()

start(7,'Bottom-up market / illustrative scenarios','The market is paid demand for specific data','Size the first market from qualified buying accounts for an identified dataset, not global ocean-economy spending.')
para(54,171,'Qualification: a missing observation + a defined use + budget + rights to use the data. Deduplicate buying accounts and test access to free alternatives.',width=850,size=19,color=WHITE)
text(54,247,'ACCOUNTS',11,MUTED,True);text(310,247,'ASSUMED ANNUAL PACKAGE',11,MUTED,True);text(680,247,'RECURRING REVENUE',11,MUTED,True)
for y,n,rev in [(281,'30','$0.72M'),(323,'100','$2.4M'),(365,'500','$12M')]:
    text(54,y,n,23,WHITE,True);text(310,y,'$24,000 / account',21,MUTED);text(680,y,rev,23,CYAN,True)
para(54,416,'Scale depends on more valuable coverage, additional datasets and customer retention. Count qualified buyers before claiming a serviceable market.',size=15,color=WHITE)
note('Account counts are scenarios, not a verified TAM or pipeline. Accounts do not equal nodes; no collection fees or future applications are included.');end()

start(8,'Competition / proposed differentiation','The benchmark is available ocean data','Triton must prove a valuable coverage gap and reliable delivery. A network alone does not establish differentiation.')
text(54,175,'ALTERNATIVE',10,MUTED,True);text(290,175,'EXISTING VALUE / TRITON PROOF REQUIRED',10,MUTED,True)
row(204,'Public observation','NOAA provides real-time observations; USF provides sargassum forecasts. Demonstrate useful incremental coverage, not generic data availability.',bodyx=290,width=610)
rule(265)
row(281,'Commercial networks','Sofar combines sensing with ocean intelligence. Saildrone collects maritime data autonomously. Benchmark the required dataset and delivery terms.',bodyx=290,width=610)
rule(342)
row(358,'Buy or self-collect','Existing sensors, data suppliers and a buyer\'s own assets are substitutes. Compare total cost, provenance and continuity; commodity AIS is not a moat.',bodyx=290,width=610)
note('Sources: <a href="https://tidesandcurrents.noaa.gov/ports_info.html" color="#00becd">NOAA</a>; <a href="https://ocgweb.marine.usf.edu/Models/Sargassum/sargassum.html" color="#00becd">USF</a>; <a href="https://www.sofarocean.com/products/wayfinder" color="#00becd">Sofar</a>; <a href="https://www.saildrone.com/" color="#00becd">Saildrone</a>. No proven price or accuracy advantage; no partnerships implied.');end()

start(9,'Compounding network / conditional advantage','Useful coverage and history can compound','The potential asset is a permissioned, quality-controlled record of conditions at specific places and times.')
row(180,'Coverage density','Adjacent nodes may resolve local variation. Measure added unique coverage and whether another buyer or model benefits from each deployment.')
rule(247)
row(265,'Longitudinal record','Consistent variables and calibration make history comparable. Test whether longer records improve a buyer\'s work beyond existing datasets.')
rule(333)
row(351,'Shared acquisition','Serve overlapping data needs from the same observations. Measure revenue per coverage cluster, direct cost and retention before claiming leverage.')
note('No network effect demonstrated. Public AIS redistribution alone is not proprietary ground truth. Data rights, quality and incremental utility are prerequisites.');end()

start(10,'Founder-market fit / current evidence','Jorge Pimentel | Founder & CTO','Founder-led integration of hardware, communications, field operations and software is the current execution thesis.')
text(54,177,'COMPANY-REPORTED FOUNDATION',10,CYAN,True)
para(54,206,'Approximately $48K founder funded.<br/>SEAVANT software foundation and ocean intelligence prototypes.<br/>Founder leads architecture, product and field validation.',width=410,size=21,color=WHITE)
text(540,177,'EVIDENCE STILL NEEDED',10,CYAN,True)
para(540,206,'A dated prototype demonstration.<br/>Relevant prior engineering and marine operating work.<br/>Access to data buyers and deployment assets.<br/>Named field and commercial support.',width=365,size=19,color=MUTED)
rule(393)
para(54,411,'Current disclosed stage: pre-MVP, no paying customers, no institutional capital. No prior exits, credentials or field performance are claimed.',size=16,color=WHITE)
note('Source: original v2 deck. Founder spend, software maturity and current status require confirmation; founder-market fit remains only partially substantiated.');end()

start(11,'18-month plan / proposed spending gates','Funding proves supply, demand and repeatability','Milestones start at funding. Customer discovery runs alongside Node 001 validation; expansion follows measured demand.')
row(180,'0-5 months | $300K','Pass capture and recovery gates. Complete 15 buyer interviews; identify a differentiated dataset, rights and installed cost.')
rule(247)
row(263,'5-12 months | $450K','Target 3 paid data trials and 2 annual conversions. Agree coverage and quality terms; measure direct delivery and collection costs.')
rule(331)
row(347,'12-18 months | $300K','Replicate demand-backed deployments. Test reuse across buyers, recurring coverage economics and renewal evidence where timing permits.')
note('$150K reserve is outside stage envelopes. Proposed management gates, not investor tranches. Hold expansion if data utility or economics fail validation.');end()

start(12,'The ask','A $1.2M raise to prove the first network','Approximately 18 months. The objective is dependable observations with repeatable demand and measured coverage economics.')
alloc=[('Hardware + deployments','$360K','30%'),('Engineering + platform','$300K','25%'),('Ocean ops + SailNode','$150K','12.5%'),('Customer data trials + BD','$150K','12.5%'),('Regulatory + legal','$90K','7.5%'),('Reserve','$150K','12.5%')]
for i,(label,amount,pct) in enumerate(alloc):
    y=176+i*37
    text(54,y,label,17,WHITE);text(485,y,amount,20,CYAN,True);text(645,y,pct,16,MUTED)
para(750,175,'Average gross budget:<br/>~$66.7K / month.<br/><br/>Excluding reserve:<br/>~$58.3K / month.',width=155,size=16)
rule(414)
para(54,429,'Seed evidence: reliable data, paying buyers, repeatable deployments and useful shared coverage.',size=17,color=WHITE,bold=True)
note('Allocation amounts retained from v2. No financing terms supplied. Staffing, licensing, cash flow and buyer requirements remain to be validated.');end()
c.save()
print('Created 12-page Triton_PreSeed_Deck_v4.pdf')
