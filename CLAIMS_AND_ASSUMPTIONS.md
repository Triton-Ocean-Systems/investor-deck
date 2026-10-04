# Triton v4: claims, assumptions and remaining evidence

Prepared October 4, 2026. Companion to the network-first 12-page deck. Ocean data and the observation network are the focus; buyer discovery determines which datasets and deployments deserve investment. Sargassum is one candidate application. County procurement is not a prerequisite.

## The Temptation of Done

A finished PDF and working data pipe do not validate demand. Separate company reports, external evidence, proposed targets and arithmetic. Ask what would disprove the thesis. v4 supersedes the resort cleanup framing and removes its $18K site subscription, $6K service-cost assumption and savings example.

## Sources

- Original [v2 deck](https://triton-ocean-systems.github.io/investor-deck/Triton_PreSeed_Deck_v2.pdf): company-reported prototype stage, approximately $48K founder funding, no paying customers or institutional capital, software foundation, intended NMEA / AIS / GNSS inputs and EdgeCore ceiling. These disclosures are not independently audited or updated accounts.
- [NOAA PORTS](https://tidesandcurrents.noaa.gov/ports_info.html): existing real-time oceanographic observations. Persistent observation already exists; Triton must prove an incremental coverage or access advantage.
- [USF sargassum trajectory system](https://ocgweb.marine.usf.edu/Models/Sargassum/sargassum.html): an established alternative for one possible application. No affiliation, commercial license or data agreement established.
- [Sofar Wayfinder](https://www.sofarocean.com/products/wayfinder): ocean intelligence and voyage guidance. [Saildrone](https://www.saildrone.com/): autonomous maritime observation and data delivery. No inferred Triton superiority or partnership.

## Slide evidence register

| Slide | Status and evidence needed |
|---|---|
| 1 | Network positioning; company-reported stage; proposed raise. No field-proven network or water-column/seafloor coverage. Cover graphic represents intended surfaces. |
| 2 | Hypothesized data-user pain. Verify actual data gaps, acquisition/integration costs, budget and value beyond available feeds. No quantified customer loss or savings claimed. |
| 3 | Proposed architecture and record product. Audit actual fields, sensors, rates, calibration and rights. Query access, provenance and quality controls remain requirements, not demonstrated capabilities. |
| 4 | Proposed 72-hour bench, 30-day field and >=95% valid-record targets. Need raw logs and fixed schedule/validity definitions. No pass result supplied. |
| 5 | Candidate buyers; 15 interviews, 3 paid trials and 2 annual conversions are targets. No established customer segment or signed trial. |
| 6 | $24K annual account price and four-account package are illustrative. No validated demand, margin, direct network cost or break-even point. |
| 7 | 30, 100 and 500 accounts are scenarios, not TAM, SAM or pipeline. Build a named, deduplicated inventory for a selected dataset. |
| 8 | Primary-source descriptions of alternatives. Compare a specific dataset's coverage, continuity, provenance, delivery, cost and license terms. |
| 9 | Conditional compounding advantage. Prove unique coverage, comparable history and multiple buyers benefiting from shared acquisition; establish lawful reuse. |
| 10 | Original founder disclosures. Confirm spend, prototype maturity and stage. Prior credentials, engineering/marine experience and buyer access remain unsupplied. |
| 11 | Proposed spending gates. Cost staffing, deployments and discovery. Renewals may occur after month 18; no guaranteed seed-readiness date. |
| 12 | Original allocation amounts, now applied to data/network validation. Detailed cash flow, licensing costs and financing terms remain absent. |

## Dataset critique

The first engineering baseline is planned vessel position and available navigation context from NMEA / AIS / GNSS inputs. NMEA is an interface, not a scientific variable. Inventory actual fields and rates on Node 001.

This can validate capture, provenance, outage recovery and delivery, but may offer weak standalone commercial differentiation. AIS/GNSS do not establish proprietary oceanographic ground truth, water-quality measurement, sargassum detection or seabed observation. Environmental variables require specified sensors, calibration, measurement context and maintenance. The first commercial dataset remains unselected: discover demand alongside Node 001 validation, then instrument the necessary variables where economics support it.

Offline buffering preserves records for later recovery; it does not provide live access during outages. Completeness, timeliness and measurement accuracy require separate tests. BeachLens remains an exploratory discussion per v2, not a customer or formal partner.

## Commercial assumptions and arithmetic

- Proposed annual subscriptions/API access cover a defined dataset. Dedicated collection and integration require separate pricing. Specify footprint, variables, freshness, quality, permitted use and support before quoting.
- $24,000/account/year is a proposed price test, not a current price, quote or validated willingness to pay. Four accounts sharing a package produce $96,000 annual revenue. This is not a profitability or four-account break-even claim.
- Direct cost must include collection, recovery of deployment capital, licensing, servicing, replacements, connectivity, quality control, hosting and direct support. Sales acquisition, engineering and overhead also affect cash flow. No gross-margin figure is asserted.
- Reuse requires overlapping buyer needs and contractual permission. Dedicated contracts may prohibit resale. Shared acquisition does not mean cost-free revenue expansion.
- Scenarios: 30 x $24K = $720K; 100 x $24K = $2.4M; 500 x $24K = $12M recurring revenue. These do not establish that those buyers exist. Accounts and nodes differ: one buyer may require many nodes; one node may serve multiple buyers. Dedicated-collection fees are excluded.
- A bottom-up market needs a selected dataset, named eligible organizations, budget authority, free-alternative analysis and tested pricing. The $12M scenario does not alone demonstrate venture scale. New datasets and territories need their own evidence.
- Raise amounts: $360K + $300K + $150K + $150K + $90K + $150K = $1.2M. Percentages total 100%. The $150K customer-pilot category is now customer data trials + BD; its amount is unchanged.
- Average gross 18-month budget: $66,666.67/month; excluding $150K reserve: $58,333.33/month. Phase envelopes: $300K + $450K + $300K + $150K reserve = $1.2M. Phases and functional categories describe the same capital, not additive budgets or investor tranches.

## Falsification tests

1. Buyers already get adequate observations free or from existing suppliers. Generic feed aggregation may have no paid advantage.
2. Node 001 reliably transports records but its variables do not answer a valuable question. Infrastructure success is not product-market fit.
3. Interviewees like the concept but lack budget or a purchase path. Interest is not paid demand.
4. Required instruments and coverage cost more than buyers will pay. Measure installed and recurring costs, not just compute hardware.
5. Buyers require incompatible variables, freshness or footprints. A single network cannot automatically support every application.
6. Providers, hosts or customers restrict collection and reuse. No commercial data asset compounds without rights.
7. Added nodes produce redundancy or maintenance expense. Measure unique coverage, revenue and direct cost by cluster.
8. Historical measurements drift or lack calibration. An archive can accumulate error instead of value.

## Evidence before circulation

Confirm company/founder disclosures. Provide dated demonstrations, Node 001 logs and an inventory of fields, instruments, provenance, coverage and rights. Document buyer discovery and price tests; select a differentiated commercial dataset. Agree trial success criteria, count eligible accounts, and prepare staffing/monthly cash flow. Present these as missing evidence until they exist.

## Source

`build_deck.py` generates `Triton_PreSeed_Deck_v4.pdf` with Python 3 and ReportLab. Original observation-surface artwork and earlier PDFs are retained. The review branch selects v4; live Pages changes only when merged and deployed.
